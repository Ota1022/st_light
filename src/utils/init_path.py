import os
import glob
from .constants import CHECKPOINT_FILES, CONFIG_FILES


def _get_checkpoint_paths(checkpoint_dir):
    """Build checkpoint paths dictionary."""
    return {
        'wav2lip_checkpoint': os.path.join(checkpoint_dir, CHECKPOINT_FILES['wav2lip']),
        'audio2pose_checkpoint': os.path.join(checkpoint_dir, CHECKPOINT_FILES['audio2pose']),
        'audio2exp_checkpoint': os.path.join(checkpoint_dir, CHECKPOINT_FILES['audio2exp']),
        'free_view_checkpoint': os.path.join(checkpoint_dir, CHECKPOINT_FILES['free_view']),
        'path_of_net_recon_model': os.path.join(checkpoint_dir, CHECKPOINT_FILES['net_recon'])
    }


def init_path(checkpoint_dir, config_dir, size=512, old_version=False, preprocess='crop'):

    if old_version:
        sadtalker_paths = _get_checkpoint_paths(checkpoint_dir)
        use_safetensor = False
    elif len(glob.glob(os.path.join(checkpoint_dir, '*.safetensors'))):
        print('using safetensor as default')
        sadtalker_paths = {
            "checkpoint": os.path.join(checkpoint_dir, f'SadTalker_V0.0.2_{size}.safetensors'),
        }
        use_safetensor = True
    else:
        print("WARNING: The new version of the model will be updated by safetensor, you may need to download it manually. We run the old version of the checkpoint this time!")
        use_safetensor = False
        sadtalker_paths = _get_checkpoint_paths(checkpoint_dir)

    sadtalker_paths['dir_of_BFM_fitting'] = os.path.join(config_dir)
    sadtalker_paths['audio2pose_yaml_path'] = os.path.join(config_dir, CONFIG_FILES['audio2pose'])
    sadtalker_paths['audio2exp_yaml_path'] = os.path.join(config_dir, CONFIG_FILES['audio2exp'])
    sadtalker_paths['use_safetensor'] = use_safetensor

    if 'full' in preprocess:
        sadtalker_paths['mappingnet_checkpoint'] = os.path.join(checkpoint_dir, CHECKPOINT_FILES['mapping_full'])
        sadtalker_paths['facerender_yaml'] = os.path.join(config_dir, CONFIG_FILES['facerender_still'])
    else:
        sadtalker_paths['mappingnet_checkpoint'] = os.path.join(checkpoint_dir, CHECKPOINT_FILES['mapping_crop'])
        sadtalker_paths['facerender_yaml'] = os.path.join(config_dir, CONFIG_FILES['facerender'])

    return sadtalker_paths