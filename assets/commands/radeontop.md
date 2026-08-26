# TAGLINE

实时监控 AMD Radeon GPU 利用率

# TLDR

显示 **GPU 利用率**

```radeontop```

启用**彩色**输出

```radeontop -c```

按总线号选择特定 **GPU**

```radeontop -b [bus_number]```

设置**采样率**（每秒采样次数）

```radeontop -t [10]```

将输出**转储**到文件

```radeontop -d [output.txt]```

# SYNOPSIS

**radeontop** [_options_]

# PARAMETERS

**-c**, **--color**
> 启用彩色输出。

**-b**, **--bus** _bus_
> 按 PCI 总线号选择 GPU。对于 lspci 输出 `01:00.0`，总线值为 `1`。

**-t**, **--ticks** _ticks_
> 每秒采样次数。默认为 120。值越高精度和开销越大。

**-d**, **--dump** _file_
> 将数据转储到文件而不是显示。使用 `-` 表示标准输出。

**-i**, **--dump-interval** _seconds_
> 转储时每行数据输出之间等待 N 秒。

**-l**, **--limit** _limit_
> 转储指定行数后退出。仅在转储模式下有效。

**-p**, **--path** _device_
> 打开指定的 DRM 设备节点（例如 `/dev/dri/card0`）。

**-m**, **--mem**
> 自动检测失败时强制使用 `/dev/mem` 路径。在使用专有驱动时有用。

**-v**, **--version**
> 显示程序版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**radeontop** 显示 AMD Radeon GPU 的实时利用率统计信息。它展示 GPU 各组件的使用百分比，包括图形管线、着色器、纹理单元以及视频解码/编码引擎。

该工具从内核 debugfs 接口读取数据，并以类似 top 的格式呈现，适合在游戏或计算任务期间监控 GPU 负载。

# CAVEATS

在某些系统上可能需要 root 权限。仅支持使用 radeon 或 amdgpu 驱动的 AMD Radeon GPU。较旧的 GPU 可能不支持全部指标。

# HISTORY

**radeontop** 由 **Chris Blaas** 创建，用于在 Linux 上监控 AMD 显卡，类似于 NVIDIA 卡上的 nvidia-smi。

# INSTALL

```apt: sudo apt install radeontop```

```dnf: sudo dnf install radeontop```

```pacman: sudo pacman -S radeontop```

```apk: sudo apk add radeontop```

```zypper: sudo zypper install radeontop```

```nix: nix profile install nixpkgs#radeontop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[amdgpu_top](/man/amdgpu_top)(1), [nvidia-smi](/man/nvidia-smi)(1), [glxinfo](/man/glxinfo)(1), [lspci](/man/lspci)(8)
