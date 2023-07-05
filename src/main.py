import argparse
import logging
from model_training import load_model
from video_processing import process_video

def main():
    parser = argparse.ArgumentParser(description='A video upscaling application using VS Code, M1 Mac, and ESRGAN.')
    parser.add_argument('-i', '--input', type=str, required=True, help='The path of the input video file.')
    parser.add_argument('-o', '--output', type=str, required=True, help='The path of the output video file.')
    parser.add_argument('-m', '--model', type=str, required=True, help='The path of the ESRGAN model file.')
    parser.add_argument('-r', '--resolution', type=int, default=2, help='The factor by which to increase the resolution of the video.')
    parser.add_argument('-c', '--codec', type=str, default='mp4v', help='The four-character code of the video codec to use for the output video.')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info('Loading the ESRGAN model...')
    model = load_model(args.model)

    logger.info(f'Processing the video from {args.input} to {args.output}...')
    process_video(args.input, args.output, model, args.resolution, args.codec)

    logger.info('Done!')

if __name__ == '__main__':
    main()
