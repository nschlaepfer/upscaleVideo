import torch

def load_model(model_path):
    model = torch.load(model_path)
    model.eval()
    return model
