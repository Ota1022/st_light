"""
Constants used throughout the SadTalker project.
"""

# Audio/Video processing constants
DEFAULT_FPS = 25
DEFAULT_SAMPLE_RATE = 16000
DEFAULT_IMAGE_SIZE = 256
DEFAULT_BATCH_SIZE = 2

# File extensions
SUPPORTED_IMAGE_EXTENSIONS = ['jpg', 'png', 'jpeg']
SUPPORTED_AUDIO_EXTENSIONS = ['wav', 'mp3', 'm4a']

# Checkpoint file names
CHECKPOINT_FILES = {
    'wav2lip': 'wav2lip.pth',
    'audio2pose': 'auido2pose_00140-model.pth',
    'audio2exp': 'auido2exp_00300-model.pth',
    'free_view': 'facevid2vid_00189-model.pth.tar',
    'net_recon': 'epoch_20.pth',
    'mapping_full': 'mapping_00109-model.pth.tar',
    'mapping_crop': 'mapping_00229-model.pth.tar'
}

# Configuration file names
CONFIG_FILES = {
    'audio2pose': 'auido2pose.yaml',
    'audio2exp': 'auido2exp.yaml',
    'facerender': 'facerender.yaml',
    'facerender_still': 'facerender_still.yaml'
}

# Default device
DEFAULT_DEVICE = 'cuda'
CPU_DEVICE = 'cpu'