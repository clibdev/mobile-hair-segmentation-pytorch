# Fork of [wonbeomjang/mobile-hair-segmentation-pytorch](https://github.com/wonbeomjang/mobile-hair-segmentation-pytorch)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)
* Original pretrained models from GitHub [releases page](https://github.com/clibdev/mobile-hair-segmentation-pytorch/releases). (🔥)
* Installation with updated [requirements.txt](requirements.txt) file.
* The following errors and warnings has been fixed:
  * TypeError: model got an unexpected keyword argument 'device'.
  * KeyError: 'state_dict' not found.
  * UserWarning: The default value of the antialias parameter of all the resizing transforms will change from None to True.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name                          | IoU (%) | Link                                                                                                                |
|-------------------------------|---------|---------------------------------------------------------------------------------------------------------------------|
| MobileHairNetV1 (MobileNetV1) | 92.48   | [PyTorch](https://github.com/clibdev/mobile-hair-segmentation-pytorch/releases/latest/download/hairmattenet_v1.pth) |
| MobileHairNetV2 (MobileNetV2) | 93.21   | [PyTorch](https://github.com/clibdev/mobile-hair-segmentation-pytorch/releases/latest/download/hairmattenet_v2.pth) |

# Inference

```shell
python predict.py --model_path hairmattenet_v1.pth --model_version 1 --image_path image/5930.jpg --result_path image/5930_out.jpg
python predict.py --model_path hairmattenet_v2.pth --model_version 2 --image_path image/5930.jpg --result_path image/5930_out.jpg
```
