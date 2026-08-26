# TAGLINE

PipeWire SPA 设备调试工具

# TLDR

**加载 SPA 插件**并从中实例化一个设备

```spa-monitor [path/to/plugin.so]```

**调试 JACK 兼容插件**

```spa-monitor /usr/lib/x86_64-linux-gnu/spa-0.2/jack/libspa-jack.so```

**调试 ALSA 插件**

```spa-monitor /usr/lib/x86_64-linux-gnu/spa-0.2/alsa/libspa-alsa.so```

**调试蓝牙插件**

```spa-monitor /usr/lib/x86_64-linux-gnu/spa-0.2/bluez5/libspa-bluez5.so```

**调试 V4L2 视频插件**

```spa-monitor /usr/lib/x86_64-linux-gnu/spa-0.2/v4l2/libspa-v4l2.so```

# SYNOPSIS

**spa-monitor** _FILE_

# DESCRIPTION

**spa-monitor** 是 **PipeWire** 附带的一个小型调试工具。它加载一个 **SPA**（Simple Plugin API）共享对象插件，并从中实例化一个设备对象，让开发者可以观察插件如何枚举硬件、通告节点以及发出事件。

该工具并非面向最终用户；它的存在是为了帮助插件作者和 PipeWire 开发者验证 SPA 插件能否正确初始化、暴露预期的接口，并在系统总线上报告设备。对某个插件运行 **spa-monitor** 会打印诊断输出，描述发现的设备以及实例化过程中遇到的任何错误。

典型用法是将其指向 _/usr/lib/<triplet>/spa-0.2/_ 下的某个插件库，以检查该插件在当前机器上的行为。

# PARAMETERS

_FILE_
> SPA 插件共享对象（.so）文件的路径。插件会被 dlopen 加载，并从中实例化一个设备。

# CAVEATS

**spa-monitor** 是一个调试辅助工具：只对从事 PipeWire 设备插件开发的开发者有用。程序不接受任何标志，其输出只有在 SPA 插件 API 的语境下才有意义。它在 Debian/Ubuntu 上随 _pipewire-bin_ 软件包发布，在 Arch 上随 _pipewire_ 发布。

# HISTORY

由 **PipeWire** 项目作为 SPA 插件框架的一部分开发。PipeWire 由 **Red Hat** 的 **Wim Taymans** 自 **2015 年**开始创建，是 Linux 上统一的音视频服务器，旨在最终取代 **PulseAudio** 和 **JACK** 处理媒体。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-spa-tools```

```zypper: sudo zypper install pipewire-spa-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1), [pw-dump](/man/pw-dump)(1), [wpctl](/man/wpctl)(1)
