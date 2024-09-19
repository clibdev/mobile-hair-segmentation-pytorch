import argparse
import os
from models import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_version', type=int, default=2, help='MobileHairNet version')
    parser.add_argument('--model_path', type=str, default='./hairmattenet_v2.pth')
    parser.add_argument('--device', type=str, default='cpu', help='cuda or cpu')
    parser.add_argument('--dynamic', action='store_true', default=False, help='enable dynamic axis in onnx model')
    args = parser.parse_args()

    device = torch.device(args.device)

    pretrained = False if args.model_path else True
    if args.model_version == 1:
        net = modelv1(pretrained=pretrained).to(device)
    elif args.model_version == 2:
        net = modelv2(pretrained=pretrained).to(device)
    else:
        raise Exception('[!] Unexpected model version')

    if args.model_path:
        net.load_state_dict(torch.load(args.model_path, map_location=device, weights_only=True))

    net.eval()

    model_path = os.path.splitext(args.model_path)[0] + '.onnx'

    dummy_input = torch.randn(1, 3, 224, 224).to(device)
    dynamic_axes = {'input': {2: '?', 3: '?'}, 'output': {2: '?', 3: '?'}} if args.dynamic else None
    torch.onnx.export(
        net,
        dummy_input,
        model_path,
        verbose=False,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes=dynamic_axes,
        opset_version=17
    )
