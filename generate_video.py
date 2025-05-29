import argparse
import os
from sadtalker import SadTalker
from src.utils.config import SadTalkerConfig
from src.utils.logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Generate video from image and audio using SadTalker.")
    parser.add_argument("--driven_audio", required=True, help="Path to driven audio file")
    parser.add_argument("--source_image", required=True, help="Path to source image file")
    parser.add_argument("--result_dir", required=True, help="Directory to save the output video file")
    parser.add_argument("--config", help="Path to configuration file")
    parser.add_argument("--device", choices=['cuda', 'cpu'], help="Device to use for inference")
    parser.add_argument("--size", type=int, choices=[256, 512], help="Model size")

    args = parser.parse_args()
    
    logger = setup_logger('main')
    
    try:
        # Load configuration
        config = SadTalkerConfig(args.config)
        
        # Override with command line arguments
        if args.device:
            config.set('device', args.device)
        if args.size:
            config.set('size', args.size)
        
        config.validate()
        logger.info(f"Using configuration: {config}")
        
        # Initialize SadTalker
        sadtalker = SadTalker(
            config.get('checkpoint_dir'), 
            config.get('config_dir'),
            device=config.get('device'),
            size=config.get('size'),
            preprocess=config.get('preprocess')
        )
        
        # Generate video
        os.makedirs(args.result_dir, exist_ok=True)
        output_video_path = os.path.join(args.result_dir, "generated_video.mp4")
        sadtalker.generate(args.source_image, args.driven_audio, output_video_path)
        
        logger.info("Video generation completed successfully")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()
