import torch
import os
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from torchvision.utils import save_image
from utils.custom_transfrom import UnNormalize

class Tester:
    def __init__(self, config, dataloader):
        self.batch_size = config.batch_size
        self.config = config
        self.model_path = config.checkpoint_dir
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.data_loader = dataloader
        self.num_classes = config.num_classes
        self.num_test = config.num_test
        self.sample_dir = config.sample_dir
        self.epoch = config.epoch
        self.checkpoint_dir = config.checkpoint_dir
        self.quantize = config.quantize
        self.load_model()
        
    def load_model(self):
        save_info = torch.load(f'{self.checkpoint_dir}/quantized.pt') if self.quantize else torch.load(f'{self.checkpoint_dir}/last.pt')
        # save_info = {'model': self.net, 'state_dict': self.net.state_dict(), 'optimizer' : self.optimizer.state_dict()}
        
        self.epoch = save_info['epoch']
        self.net = save_info['model']
        self.net.load_state_dict(save_info['state_dict'], map_location=self.device)
        self.optimizer = save_info['optimizer']
        
        print(f"[*] Load Model from {self.model_path}")

    def test(self):
        unnormal = UnNormalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
        for step, (image, mask) in enumerate(self.data_loader):
            image = unnormal(image.to(self.device))
            mask = mask.to(self.device).repeat_interleave(3, 1)
            result = self.net(image)
            argmax = torch.argmax(result, dim=1).unsqueeze(dim=1)
            result = result[:, 1, :, :].unsqueeze(dim=1)
            result = result * argmax
            result = result.repeat_interleave(3, 1)
            torch.cat([image, result, mask])

            save_image(torch.cat([image, result, mask]), os.path.join(self.sample_dir, f"{step}.png"))
            print('[*] Saved sample images')

