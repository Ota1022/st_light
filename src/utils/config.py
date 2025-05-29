"""
Configuration management for SadTalker.
"""
import os
import yaml
from typing import Dict, Any, Optional
from .constants import DEFAULT_IMAGE_SIZE, DEFAULT_DEVICE, DEFAULT_BATCH_SIZE


class SadTalkerConfig:
    """Configuration manager for SadTalker parameters."""
    
    def __init__(self, config_file: Optional[str] = None):
        self.config = self._load_default_config()
        if config_file and os.path.exists(config_file):
            self._load_config_file(config_file)
    
    def _load_default_config(self) -> Dict[str, Any]:
        """Load default configuration values."""
        return {
            'device': DEFAULT_DEVICE,
            'size': DEFAULT_IMAGE_SIZE,
            'batch_size': DEFAULT_BATCH_SIZE,
            'preprocess': 'crop',
            'pose_style': 0,
            'checkpoint_dir': './checkpoints',
            'config_dir': './src/config',
            'output_dir': './output',
            'log_level': 'INFO',
            'use_safetensor': True
        }
    
    def _load_config_file(self, config_file: str) -> None:
        """Load configuration from YAML file."""
        try:
            with open(config_file, 'r') as f:
                file_config = yaml.safe_load(f)
                self.config.update(file_config)
        except Exception as e:
            raise ValueError(f"Failed to load config file {config_file}: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        self.config[key] = value
    
    def update(self, updates: Dict[str, Any]) -> None:
        """Update multiple configuration values."""
        self.config.update(updates)
    
    def save(self, config_file: str) -> None:
        """Save configuration to YAML file."""
        try:
            os.makedirs(os.path.dirname(config_file), exist_ok=True)
            with open(config_file, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
        except Exception as e:
            raise ValueError(f"Failed to save config file {config_file}: {e}")
    
    def validate(self) -> None:
        """Validate configuration values."""
        required_dirs = ['checkpoint_dir', 'config_dir']
        for dir_key in required_dirs:
            dir_path = self.get(dir_key)
            if not os.path.exists(dir_path):
                raise ValueError(f"Required directory does not exist: {dir_path}")
        
        if self.get('size') not in [256, 512]:
            raise ValueError("Size must be 256 or 512")
        
        if self.get('device') not in ['cuda', 'cpu']:
            raise ValueError("Device must be 'cuda' or 'cpu'")
    
    def __str__(self) -> str:
        """String representation of configuration."""
        return f"SadTalkerConfig({self.config})"