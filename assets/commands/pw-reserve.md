# TAGLINE

为独占使用保留音频设备

# TLDR

**保留**设备（仅限音频设备）

```pw-reserve -n audio0```

**监控**设备而非保留它

```pw-reserve -n audio0 -m```

显示**帮助**

```pw-reserve -h```

# SYNOPSIS

**pw-reserve** [_options_]

# PARAMETERS

**-n**, **--name** _device_
> 指定要保留的设备名称（如 audio0、audio1）

**-m**, **--monitor**
> 监控设备而非保留它

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**pw-reserve** 为 PipeWire 独占使用而保留设备。它实现了 D-Bus 设备保留协议，使 PipeWire 能够与其他音频服务器协调设备访问。

目前只支持音频设备。设备保留可防止多个音频系统同时访问同一硬件时发生冲突。

# CAVEATS

目前仅支持音频设备。设备名称遵循 audioN 命名约定。保留操作需要 D-Bus 访问权限。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。实现 org.freedesktop.ReserveDevice 规范以共享音频设备。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1)
