# TAGLINE

支持 GPU 加速的深度学习框架

# TLDR

**安装 PyTorch**

```pip install torch torchvision```

**检查 CUDA 可用性**

```python -c "import torch; print(torch.cuda.is_available())"```

**检查版本**

```python -c "import torch; print(torch.__version__)"```

**指定 GPU 运行**

```CUDA_VISIBLE_DEVICES=[0] python [script.py]```

# SYNOPSIS

**pytorch** Python library for deep learning

# DESCRIPTION

**PyTorch** 是一个采用动态计算图的开源深度学习框架。它提供 GPU 加速的张量计算以及面向神经网络的自动微分。

# BASIC EXAMPLE

```python
import torch
import torch.nn as nn

# Create tensor
x = torch.tensor([[1., 2.], [3., 4.]])

# GPU transfer
if torch.cuda.is_available():
    x = x.cuda()

# Simple model
model = nn.Sequential(
    nn.Linear(10, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
)

# Training loop
optimizer = torch.optim.Adam(model.parameters())
criterion = nn.MSELoss()

for epoch in range(100):
    output = model(input)
    loss = criterion(output, target)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

# ENVIRONMENT

```bash
# Use specific GPU
CUDA_VISIBLE_DEVICES=0,1 python train.py

# Check GPU memory
python -c "import torch; print(torch.cuda.memory_summary())"
```

# CONFIGURATION

**CUDA_VISIBLE_DEVICES**
> 环境变量，控制哪些 GPU 对 PyTorch 可见，用于把训练限制在特定设备上。

**TORCH_HOME**
> 环境变量，设置缓存模型和数据集的目录（默认 ~/.cache/torch）。

# CAVEATS

GPU 版本需要 CUDA。库体积较大（约 2 GB）。为匹配 CUDA 版本请从 pytorch.org 安装。

# HISTORY

PyTorch 由 **Facebook AI Research**（FAIR）开发，于 2016 年发布，作为 Torch（Lua）的后继者。

# INSTALL

```brew: brew install pytorch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [nvidia-smi](/man/nvidia-smi)(1)
