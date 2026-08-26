# TAGLINE

为 PulseAudio 包装 OSS 应用程序

# TLDR

**在 PulseAudio 下运行 OSS 应用**

```padsp [oss_application]```

**连接到指定的** PulseAudio 服务器

```padsp -s [server] [application]```

**设置客户端**应用程序名称

```padsp -n [name] [application]```

**禁用 /dev/dsp 模拟**

```padsp -D [application]```

**启用调试**输出

```padsp -d [application]```

# SYNOPSIS

**padsp** [_options_] _program_ [_arguments_...]

# PARAMETERS

_PROGRAM_
> 要运行的 OSS 应用程序。

**-s** _SERVER_
> 要连接的 PulseAudio 服务器。

**-n** _NAME_
> 发送给服务器的客户端应用程序名称。

**-m** _NAME_
> 创建流时传递的流名称。

**-M**
> 禁用 /dev/mixer 设备模拟。

**-S**
> 禁用 /dev/sndstat 设备模拟。

**-D**
> 禁用 /dev/dsp 设备模拟。

**-d**
> 启用调试输出。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**padsp**（PulseAudio OSS 包装器）使用 LD_PRELOAD 库启动程序，将 OSS 音频设备访问（/dev/dsp、/dev/mixer、/dev/sndstat）重定向到 PulseAudio。它为旧式 OSS 应用程序提供兼容层，使其通过 PulseAudio 声音服务器播放声音。

# CAVEATS

依赖 **LD_PRELOAD**，因此只对动态链接的 ELF 二进制文件有效。并非所有 OSS 特性都被模拟；使用 mmap 或特殊 ioctl 的应用程序可能无法工作。属于 PulseAudio 发行版的一部分。

# HISTORY

**padsp** 作为 **PulseAudio** 项目的一部分而开发，用于在 PulseAudio 取代 OSS 成为大多数 Linux 发行版默认声音系统之后继续支持旧式 OSS 应用程序。

# INSTALL

```apt: sudo apt install pulseaudio-utils```

```dnf: sudo dnf install pulseaudio-utils```

```apk: sudo apk add pulseaudio-utils```

```zypper: sudo zypper install pulseaudio-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulseaudio](/man/pulseaudio)(1), [aoss](/man/aoss)(1), [pactl](/man/pactl)(1)
