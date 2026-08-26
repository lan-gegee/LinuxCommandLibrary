# TAGLINE

在 PipeWire 上运行 V4L2 视频应用

# TLDR

在 PipeWire 中运行 **v4l2 程序**

```pw-v4l2 program```

显示**帮助**

```pw-v4l2 -h```

# SYNOPSIS

**pw-v4l2** [_options_] _program_ [_arguments_...]

# PARAMETERS

**-h**
> 显示帮助信息

# DESCRIPTION

**pw-v4l2** 在 PipeWire 中运行 V4L2（Video4Linux2）程序。它提供一个兼容层，使使用 V4L2 API 的应用能够访问由 PipeWire 管理的摄像头设备。

这让视频应用得以受益于 PipeWire 的权限系统和设备共享能力。

# CAVEATS

并非所有 V4L2 特性都能被完全支持。某些应用可能需要原生 PipeWire 支持才能实现完整功能。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。将 PipeWire 的设备抽象扩展到视频采集设备。

# INSTALL

```apt: sudo apt install pipewire-v4l2```

```dnf: sudo dnf install pipewire-v4l2```

```pacman: sudo pacman -S pipewire-v4l2```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1), [v4l2-ctl](/man/v4l2-ctl)(1)
