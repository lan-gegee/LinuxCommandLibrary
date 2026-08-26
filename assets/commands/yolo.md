# TAGLINE

Ultralytics YOLO 目标检测与计算机视觉 CLI

# TLDR

对图像**运行目标检测**

```yolo detect predict model=[yolo11n.pt] source=[image.jpg]```

在自定义数据集上**训练模型**

```yolo detect train data=[data.yaml] model=[yolo11n.pt] epochs=[100] imgsz=[640]```

**验证模型**准确率

```yolo detect val model=[best.pt] data=[data.yaml]```

将模型**导出**为 ONNX 格式

```yolo export model=[best.pt] format=[onnx]```

在视频中**跟踪目标**

```yolo detect track model=[yolo11n.pt] source=[video.mp4]```

**运行姿态估计**

```yolo pose predict model=[yolo11n-pose.pt] source=[image.jpg]```

跨导出格式对模型性能进行**基准测试**

```yolo benchmark model=[yolo11n.pt] imgsz=[640]```

# SYNOPSIS

**yolo** _TASK_ _MODE_ [_arg=value_...]

# PARAMETERS

## Tasks

**detect**
> 目标检测。

**segment**
> 实例分割。

**classify**
> 图像分类。

**pose**
> 姿态估计。

**obb**
> 旋转边界框检测。

## Modes

**train**
> 在数据集上训练模型。

**val**
> 验证模型准确率。

**predict**
> 对图像、视频或流进行推理。

**export**
> 将模型转换为部署格式（ONNX、TensorRT、CoreML 等）。

**track**
> 在视频上进行多目标跟踪。

**benchmark**
> 跨导出格式测试模型的速度与准确率。

## Common Arguments

**model=**_path_
> 模型文件路径（例如 yolo11n.pt）。

**data=**_path_
> 数据集配置 YAML 文件。

**source=**_path_
> 输入源：图像、视频、目录、URL 或摄像头（0）。

**epochs=**_n_
> 训练轮数。

**imgsz=**_size_
> 输入图像尺寸（默认：640）。

**batch=**_n_
> 批大小。

**device=**_id_
> 设备：GPU id（0、0,1）或 cpu。

**format=**_fmt_
> 导出格式：onnx、engine、coreml、tflite 等。

**conf=**_threshold_
> 预测的置信度阈值。

# DESCRIPTION

**yolo** 是 Ultralytics YOLO 的命令行工具，这是一个先进的计算机视觉框架。它提供从终端执行目标检测、实例分割、图像分类、姿态估计和旋转边界框检测的命令。

该工具支持完整的工作流：**train** 基于数据集构建模型，**val** 评估模型准确率，**predict** 对图像或视频进行推理，**export** 将模型转换为 ONNX 和 TensorRT 等部署格式，**track** 对视频流执行多目标跟踪，**benchmark** 测试模型在各格式下的性能。

每条命令都接受可选的任务类型（detect、segment、classify、pose、obb）和必需的模式。参数以 key=value 键值对的形式传入。预训练模型可以直接用于推理，也可以在自定义数据集上微调。GPU 加速通过 PyTorch 支持。

# CAVEATS

需要 Python 和 PyTorch。训练建议使用 GPU。预训练模型权重会在首次使用时自动下载。使用 `yolo cfg` 可查看所有可用的配置参数。

# SEE ALSO

[python](/man/python)(1), [pip](/man/pip)(1), [nvidia-smi](/man/nvidia-smi)(1)
