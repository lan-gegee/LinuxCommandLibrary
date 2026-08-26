# TAGLINE

交互式 NVIDIA GPU 进程查看器与监控工具

# TLDR

**启动 GPU 监控器**

```nvitop```

**以监控模式运行**

```nvitop -m```

# SYNOPSIS

**nvitop** [_options_]

# PARAMETERS

**-m**, **--monitor**
> 以持续监控模式运行（类似 htop）。

**-o**, **--only** _VISIBLE_
> 仅显示当前用户拥有的 GPU 进程。

# DESCRIPTION

**nvitop** 是一款交互式 NVIDIA GPU 进程查看器和资源监控工具。它在 TUI 中实时显示 GPU 利用率、显存使用、温度和进程信息。与 nvidia-smi 不同，nvitop 直接使用 NVML Python 绑定查询设备状态，并提供树状视图、环境变量查看、进程过滤等交互功能。

它还附带 **nvisel**，一款面向深度学习研究人员的 CUDA 设备选择工具。

# CAVEATS

仅适用于 NVIDIA GPU。需要支持 NVML 的 NVIDIA 驱动程序。

# HISTORY

**nvitop** 由 **XuehaiPan** 创建，使用 **Python** 编写。可在 Linux 和 Windows 上运行。

# INSTALL

```nix: nix profile install nixpkgs#nvitop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [nvtop](/man/nvtop)(1), [htop](/man/htop)(1)
