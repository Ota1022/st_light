import os
import shutil
import torch
from time import strftime

from src.utils.preprocess import CropAndExtract
from src.test_audio2coeff import Audio2Coeff
from src.facerender.animate import AnimateFromCoeff
from src.generate_batch import get_data
from src.generate_facerender_batch import get_facerender_data
from src.utils.init_path import init_path

class SadTalker:
    def __init__(self, checkpoint_dir, config_dir, device='cuda', size=256, preprocess='crop'):
        self.device = device if torch.cuda.is_available() and device == 'cuda' else 'cpu'
        self.sadtalker_paths = init_path(checkpoint_dir, config_dir, size, False, preprocess)

        self.preprocess_model = CropAndExtract(self.sadtalker_paths, self.device)
        self.audio_to_coeff = Audio2Coeff(self.sadtalker_paths, self.device)
        self.animate_from_coeff = AnimateFromCoeff(self.sadtalker_paths, self.device)

    def generate(self, source_image_path, driven_audio_path, output_video_path):
        save_dir = os.path.join(os.path.dirname(output_video_path), strftime("%Y_%m_%d_%H.%M.%S"))
        os.makedirs(save_dir, exist_ok=True)

        # Crop image and extract 3DMM from image
        first_frame_dir = os.path.join(save_dir, 'first_frame_dir')
        os.makedirs(first_frame_dir, exist_ok=True)
        first_coeff_path, crop_pic_path, crop_info = self.preprocess_model.generate(source_image_path, first_frame_dir, 'crop', source_image_flag=True, pic_size=256)
        if first_coeff_path is None:
            raise ValueError("Can't get the coeffs of the input image")

        # Convert audio to coefficients
        ref_eyeblink_coeff_path = None
        batch = get_data(first_coeff_path, driven_audio_path, self.device, ref_eyeblink_coeff_path)
        coeff_path = self.audio_to_coeff.generate(batch, save_dir, pose_style=0)

        # Render the face from coefficients
        data = get_facerender_data(coeff_path, crop_pic_path, first_coeff_path, driven_audio_path, batch_size=2)
        result = self.animate_from_coeff.generate(data, save_dir, source_image_path, crop_info)

        shutil.move(result, output_video_path)
        print('The generated video is named:', output_video_path)
