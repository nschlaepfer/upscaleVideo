
# Video Upscaling with ESRGAN

This project is a video upscaling application that uses the Enhanced Super-Resolution Generative Adversarial Network (ESRGAN) to upscale videos to a higher resolution.

## Requirements

- Python 3.7 or higher
- OpenCV
- PyTorch
- Torchvision

You can install the required Python libraries using pip:

```bash
pip install opencv-python-headless torch torchvision
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/nschlaepfer/upscaleVideo.git
cd upscaleVideo
```

2. Download the pre-trained ESRGAN model:

```bash
wget https://www.dropbox.com/s/vouc15j8jjp2o5n/RRDB_ESRGAN_x4_old_arch.pth?dl=0 -O models/RRDB_ESRGAN_x4_old_arch.pth
```

3. Run the `main.py` script with the necessary arguments:

```bash
python main.py -i input.mp4 -o output.mp4
```

Replace `input.mp4` with the path to your input video file, and `output.mp4` with the path where you want to save the upscaled video.

## Arguments

- `-i`, `--input`: The path of the input video file. (required)
- `-o`, `--output`: The path of the output video file. (required)
- `-m`, `--model`: The path of the ESRGAN model file. (default: `./models/RRDB_ESRGAN_x4_old_arch.pth`)
- `-r`, `--resolution`: The factor by which to increase the resolution of the video. (default: `2`)
- `-c`, `--codec`: The four-character code of the video codec to use for the output video. (default: `mp4v`)

## License

This project is licensed under the terms of the MIT license.
