"""
Logging utilities for SadTalker.
"""
import logging
import os
from datetime import datetime


def setup_logger(name='sadtalker', log_dir='logs', level=logging.INFO):
    """
    Set up a logger with file and console handlers.
    
    Args:
        name (str): Logger name
        log_dir (str): Directory to save log files
        level: Logging level
        
    Returns:
        logging.Logger: Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if logger.handlers:
        return logger
    
    os.makedirs(log_dir, exist_ok=True)
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # File handler
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(log_dir, f'{name}_{timestamp}.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger