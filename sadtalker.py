import os
import shutil
from time import strftime

from src.utils.preprocess import CropAndExtract
from src.test_audio2coeff import Audio2Coeff
from src.facerender.animate import AnimateFromCoeff
from src.generate_batch import get_data
from src.generate_facerender_batch import get_facerender_data
from src.utils.init_path import init_path
from src.utils.device_utils import get_device
from src.utils.constants import DEFAULT_IMAGE_SIZE, DEFAULT_BATCH_SIZE
from src.utils.logger import setup_logger

class SadTalker:
    def __init__(self, checkpoint_dir, config_dir, device='cuda', size=DEFAULT_IMAGE_SIZE, preprocess='crop'):
        self.logger = setup_logger('sadtalker')
        self.device = get_device(device)
        self.logger.info(f"Using device: {self.device}")
        
        self.sadtalker_paths = init_path(checkpoint_dir, config_dir, size, False, preprocess)
        self.logger.info(f"Initialized paths for size {size} and preprocess {preprocess}")

        try:
            self.preprocess_model = CropAndExtract(self.sadtalker_paths, self.device)
            self.audio_to_coeff = Audio2Coeff(self.sadtalker_paths, self.device)
            self.animate_from_coeff = AnimateFromCoeff(self.sadtalker_paths, self.device)
            self.logger.info("Successfully initialized all models")
        except Exception as e:
            self.logger.error(f"Failed to initialize models: {e}")
            raise

    def generate(self, source_image_path, driven_audio_path, output_video_path):
        self.logger.info(f"Starting video generation: {source_image_path} + {driven_audio_path} -> {output_video_path}")
        
        if not os.path.exists(source_image_path):
            raise FileNotFoundError(f"Source image not found: {source_image_path}")
        if not os.path.exists(driven_audio_path):
            raise FileNotFoundError(f"Audio file not found: {driven_audio_path}")
        
        save_dir = os.path.join(os.path.dirname(output_video_path), strftime("%Y_%m_%d_%H.%M.%S"))
        os.makedirs(save_dir, exist_ok=True)
        self.logger.info(f"Created temporary directory: {save_dir}")

        try:
            # Crop image and extract 3DMM from image
            first_frame_dir = os.path.join(save_dir, 'first_frame_dir')
            os.makedirs(first_frame_dir, exist_ok=True)
            self.logger.info("Processing source image...")
            first_coeff_path, crop_pic_path, crop_info = self.preprocess_model.generate(
                source_image_path, first_frame_dir, 'crop', source_image_flag=True, pic_size=DEFAULT_IMAGE_SIZE
            )
            if first_coeff_path is None:
                raise ValueError("Can't get the coeffs of the input image")
            self.logger.info("Image preprocessing completed")

            # Convert audio to coefficients
            self.logger.info("Converting audio to coefficients...")
            ref_eyeblink_coeff_path = None
            batch = get_data(first_coeff_path, driven_audio_path, self.device, ref_eyeblink_coeff_path)
            coeff_path = self.audio_to_coeff.generate(batch, save_dir, pose_style=0)
            self.logger.info("Audio processing completed")

            # Render the face from coefficients
            self.logger.info("Rendering face animation...")
            data = get_facerender_data(coeff_path, crop_pic_path, first_coeff_path, driven_audio_path, batch_size=DEFAULT_BATCH_SIZE)
            result = self.animate_from_coeff.generate(data, save_dir, source_image_path, crop_info)
            self.logger.info("Face rendering completed")

            shutil.move(result, output_video_path)
            self.logger.info(f'The generated video is saved as: {output_video_path}')
            
        except Exception as e:
            self.logger.error(f"Error during video generation: {e}")
            raise
