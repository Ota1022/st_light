import argparse
import os
from sadtalker import SadTalker

def main():
    parser = argparse.ArgumentParser(description="Generate video from image and audio using SadTalker.")
    parser.add_argument("--driven_audio", required=True, help="Path to driven audio file")
    parser.add_argument("--source_image", required=True, help="Path to source image file")
    parser.add_argument("--result_dir", required=True, help="Directory to save the output video file")

    args = parser.parse_args()

    checkpoint_dir = './checkpoints'
    config_dir = './src/config'

    sadtalker = SadTalker(checkpoint_dir, config_dir)
    output_video_path = os.path.join(args.result_dir, "generated_video.mp4")
    sadtalker.generate(args.source_image, args.driven_audio, output_video_path)

if __name__ == '__main__':
    main()
