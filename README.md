# Fork of [wonbeomjang/mobile-hair-segmentation-pytorch](https://github.com/wonbeomjang/mobile-hair-segmentation-pytorch)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.4. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/mobile-hair-segmentation-pytorch/releases). (🔥)
* Model conversion to ONNX format using the [export.py](export.py) file. (🔥)
* Installation with updated [requirements.txt](requirements.txt) file.
* The following deprecations and errors has been fixed:
  * FutureWarning: You are using 'torch.load' with 'weights_only=False'.
  * TypeError: model got an unexpected keyword argument 'device'.
  * KeyError: 'state_dict' not found.
  * UserWarning: The default value of the antialias parameter of all the resizing transforms will change from None to True.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

* Download links:

| Name            | Model Size (MB) | Link                                                                                                                                                                                                                                           | SHA-256                                                                                                                              |
|-----------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| MobileHairNetV1 | 14.9<br>14.7    | [PyTorch](https://github.com/clibdev/mobile-hair-segmentation-pytorch/releases/latest/download/mobile-hair-net-v1.pth)<br>[ONNX](https://github.com/clibdev/mobile-hair-segmentation-pytorch/releases/latest/download/mobile-hair-net-v1.onnx) | 2cddf210e82ca5d91310374f0ee1605f7d07a02dc3f1ab39628b80bd754816d0<br>6f84c31265b0f168d8192d3e4b04adcd32a86ee5d1050d0eeb83ac3fa2f90085 |
| MobileHairNetV2 | 14.6<br>9.4     | [PyTorch](https://github.com/clibdev/mobile-hair-segmentation-pytorch/releases/latest/download/mobile-hair-net-v2.pth)<br>[ONNX](https://github.com/clibdev/mobile-hair-segmentation-pytorch/releases/latest/download/mobile-hair-net-v2.onnx) | 588ca7a3d29de60f80102d90a26672c0d4a37b11def264e42a5d21bc3b5d240f<br>cdc80e96f1d44e53ef1951714e39bc0cfda607cc82bd981b955704c1020bc26d |

* Evaluation results:

| Name            | IoU (%) |
|-----------------|---------|
| MobileHairNetV1 | 92.48   |
| MobileHairNetV2 | 93.21   |

# Inference

```shell
python predict.py --model_path mobile-hair-net-v1.pth --model_version 1 --image_path image/5930.jpg --result_path image/5930_out.jpg
python predict.py --model_path mobile-hair-net-v2.pth --model_version 2 --image_path image/5930.jpg --result_path image/5930_out.jpg
```

# Export to ONNX format

```shell
pip install onnx onnxruntime
```
```shell
python export.py --model_path mobile-hair-net-v1.pth --model_version 1
python export.py --model_path mobile-hair-net-v2.pth --model_version 2
```
