"""
Device management utilities for SadTalker.
"""
import torch
from .constants import DEFAULT_DEVICE, CPU_DEVICE


def get_device(preferred_device=DEFAULT_DEVICE):
    """
    Get the appropriate device based on availability and preference.
    
    Args:
        preferred_device (str): Preferred device ('cuda' or 'cpu')
        
    Returns:
        str: The device to use ('cuda' or 'cpu')
    """
    if preferred_device == 'cuda' and torch.cuda.is_available():
        return 'cuda'
    return CPU_DEVICE


def freeze_model_parameters(model):
    """
    Freeze all parameters of a model.
    
    Args:
        model: PyTorch model to freeze
    """
    for param in model.parameters():
        param.requires_grad = False