import cv2
import numpy as np

def process_frame(frame, model):
    tensor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
    tensor = torch.from_numpy(np.transpose(tensor, (2, 0, 1))).unsqueeze(0)

    with torch.no_grad():
        tensor = model(tensor).squeeze().clamp(0, 1)

    frame = cv2.cvtColor(np.transpose(tensor.numpy(), (1, 2, 0)), cv2.COLOR_RGB2BGR)
    return np.array(frame * 255, dtype=np.uint8)

def process_video(input_path, output_path, model, resolution, codec):
    video = cv2.VideoCapture(input_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*codec)
    output = cv2.VideoWriter(output_path, fourcc, fps, (width * resolution, height * resolution))

    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame = process_frame(frame, model)
        output.write(frame)

    video.release()
    output.release()
