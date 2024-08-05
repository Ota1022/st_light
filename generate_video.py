from sadtalker import SadTalker

def main():
    checkpoint_dir = './checkpoints'
    config_dir = './src/config'
    source_image_path = './examples/source_image/full_body_1.png'
    driven_audio_path = './examples/driven_audio/bus_chinese.wav'
    output_video_path = './results/generated_video.mp4'

    sadtalker = SadTalker(checkpoint_dir, config_dir)
    sadtalker.generate(source_image_path, driven_audio_path, output_video_path)

if __name__ == '__main__':
    main()
