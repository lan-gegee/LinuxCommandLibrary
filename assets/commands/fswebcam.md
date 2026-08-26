# TAGLINE

命令行网络摄像头图像采集工具

# TLDR

**采集图像**

```fswebcam [image.jpg]```

从指定设备**采集**

```fswebcam -d [/dev/video0] [image.jpg]```

**设置分辨率**

```fswebcam -r [1280x720] [image.jpg]```

**去除横幅**

```fswebcam --no-banner [image.jpg]```

**添加时间戳**

```fswebcam --timestamp "%Y-%m-%d %H:%M" [image.jpg]```

**设置帧数以提高画质**

```fswebcam -F [10] -S [5] [image.jpg]```

# SYNOPSIS

**fswebcam** [_options_] _filename_

# PARAMETERS

**-d**, **--device** _dev_
> 视频设备（默认 /dev/video0）。

**-r**, **--resolution** _WxH_
> 采集分辨率。

**-F**, **--frames** _n_
> 采集 n 帧。

**-S**, **--skip** _n_
> 正式采集前跳过 n 帧。

**--no-banner**
> 去除信息横幅。

**--timestamp** _format_
> 添加时间戳叠加层。

**--title** _text_
> 设置横幅标题。

**--subtitle** _text_
> 设置横幅副标题。

**-q**, **--quiet**
> 抑制输出。

**--png** _level_
> 以 PNG 保存并指定压缩级别（0-9，或 -1 表示自动）。

**--jpeg** _quality_
> JPEG 质量（0-95，或 -1 表示自动）。

**-i**, **--input** _input_
> 设置要使用的输入（编号或名称，默认 "0"）。

**--flip** _direction_
> 翻转图像（h 为水平，v 为垂直）。

**--list-inputs**
> 列出所选源可用的输入。

**--list-controls**
> 列出可用的控制项及其当前值。

# CONFIGURATION

**~/.fswebcam**
> 可选的配置文件，用于保存默认设置。

# DESCRIPTION

**fswebcam** 是一个小巧简洁的命令行网络摄像头采集工具。它从 V4L2（Video4Linux）设备采集图像并保存为 JPEG 或 PNG 文件。源模块包括 V4L2、V4L1、FILE、RAW 和 TEST。

该工具适用于延时摄影、安防摄像头快照和自动化图像采集。它支持叠加层、时间戳、横幅以及各种图像调节功能。

# CAVEATS

需要 V4L2 兼容的网络摄像头。最初几帧可能偏暗（用 -S 跳过）。分辨率必须为摄像头所支持。部分摄像头需要时间调整曝光。

# HISTORY

fswebcam 由 **Philip Heron** 编写，是 Linux 上采集摄像头图像的简单命令行工具。它面向脚本和自动化场景设计，而非交互式使用。

# INSTALL

```apt: sudo apt install fswebcam```

```dnf: sudo dnf install fswebcam```

```zypper: sudo zypper install fswebcam```

```nix: nix profile install nixpkgs#fswebcam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[v4l2-ctl](/man/v4l2-ctl)(1), [ffmpeg](/man/ffmpeg)(1), [motion](/man/motion)(1)
