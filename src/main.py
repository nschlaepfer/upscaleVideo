"""A video upscaling application using VS Code, M1 Mac, and Core ML."""

import argparse
import logging
import coremltools as ct
from video_processing import process_video
from model_training import train_model

def main():
    """The main function of the application."""

    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description='A video upscaling application using VS Code, M1 Mac, and Core ML.')
    parser.add_argument('-i', '--input', type=str, required=True, help='The path of the input video file.')
    parser.add_argument('-o', '--output', type=str, required=True, help='The path of the output video file.')
    parser.add_argument('-m', '--model', type=str, default='../models/my_model.mlmodel', help='The path of the Core ML model file.')
    parser.add_argument('-r', '--resolution', type=int, default=2, help='The factor by which to increase the resolution of the video.')
    parser.add_argument('-c', '--codec', type=str, default='mp4v', help='The four-character code of the video codec to use for the output video.')
    arguments = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Train the model (optional; you can skip this step if you already have a pre-trained model)
    logger.info('Training the model...')
    model = train_model()

    # Convert the TensorFlow model to Core ML format (optional; you can skip this step if you already have a Core ML model)
    logger.info('Converting the model to Core ML format...')
    coreml_model = convert_model(model)

    # Save the Core ML model
    logger.info(f'Saving the Core ML model to {arguments.model}...')
    coreml_model.save(arguments.model)

    # Process the video
    logger.info(f'Processing the video from {arguments.input} to {arguments.output}...')
    process_video(arguments.input, arguments.output, arguments.model, arguments.resolution, arguments.codec)

    # Done
    logger.info('Done!')

if __name__ == '__main__':
    main()
