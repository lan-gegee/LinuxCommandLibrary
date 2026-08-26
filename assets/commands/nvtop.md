# TAGLINE

基于 ncurses 的 GPU 进程监控器，类似 htop 但面向 GPU

# TLDR

**监控所有 GPU**

```nvtop```

**监控特定 GPU**

```nvtop -i [0]```

**监控多个 GPU**

```nvtop -i [0,1,2]```

**设置更新间隔**

```nvtop -d [2]```

**无彩色输出**

```nvtop -C```

# SYNOPSIS

**nvtop** [_options_]

# DESCRIPTION

**nvtop** 是一款基于 ncurses 的 GPU 进程监控器，类似 htop 但面向 GPU。它实时显示 GPU 利用率、显存使用、温度和运行中的进程。

该工具支持多种加速器：NVIDIA（Kepler 及更新架构，专有驱动）、AMD（amdgpu，内核 5.14+）、Intel（i915/Xe，内核 5.19+）、Qualcomm Adreno（msm，内核 6.0+）、Apple Silicon（M1/M2，实验性）、树莓派上的 Broadcom VideoCore、Rockchip NPU、华为昇腾、MetaX 与 Enflame 显卡。

# PARAMETERS

**-i** _ids_
> 要监控的 GPU ID。

**-d** _seconds_
> 更新之间的间隔。

**-s** _sort_
> 排序依据（pid、type、rate、mem 等）。

**-C**
> 不使用颜色。

**-p**
> 仅显示进程。

**-f** _file_
> 记录日志到文件。

**--no-header**
> 隐藏表头。

**-h**, **--help**
> 显示帮助并退出。

**-v**, **--version**
> 输出版本信息并退出。

# KEYBOARD SHORTCUTS

**F1/q**: 退出
**F2**: 设置（交互式选项窗口）
**F3**: 搜索
**F4**: 过滤
**F6**: 排序
**F9**: 终止进程
**F12**: 保存偏好设置供以后会话使用

# CAVEATS

NVIDIA 需要 410 以上版本驱动。AMD 需要 ROCm。Intel 需要 i915 驱动。功能支持因 GPU 厂商而异。

# HISTORY

**nvtop** 由 **Maxime Schmitt** 创建，旨在为 GPU 监控提供类 htop 的体验。它最初仅支持 NVIDIA，后来加入了对 AMD 和 Intel GPU 的支持。

# INSTALL

```apt: sudo apt install nvtop```

```dnf: sudo dnf install nvtop```

```pacman: sudo pacman -S nvtop```

```zypper: sudo zypper install nvtop```

```brew: brew install nvtop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [gpustat](/man/gpustat)(1), [htop](/man/htop)(1), [radeontop](/man/radeontop)(1), [amdgpu_top](/man/amdgpu_top)(1)
