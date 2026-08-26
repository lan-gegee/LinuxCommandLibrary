# TAGLINE

查看 PipeWire SPA 插件详情

# TLDR

显示某个 **SPA 插件**的信息

```spa-inspect [path/to/plugin.so]```

查看**蓝牙编解码器**插件

```spa-inspect /usr/lib64/spa-0.2/bluez5/libspa-codec-bluez5-sbc.so```

查看**音频转换**插件

```spa-inspect /usr/lib64/spa-0.2/audioconvert/libspa-audioconvert.so```

# SYNOPSIS

**spa-inspect** _FILE_

# PARAMETERS

_FILE_
> SPA 插件共享对象文件（.so）的路径

# DESCRIPTION

**spa-inspect** 显示 PipeWire 所用 SPA（Simple Plugin API）插件的信息。它会列出插件包含的工厂（factory），并尝试实例化它们，从而展示可用的接口和能力。

SPA 插件是 PipeWire 的底层构建模块，负责音频/视频处理、设备访问和格式转换。此工具帮助开发者和管理员了解每个插件提供的功能。

# CAVEATS

插件路径因发行版和架构而异（lib 与 lib64）。某些插件在缺少相应硬件或依赖时可能无法实例化。主要用于调试和开发目的。

# HISTORY

**spa-inspect** 是 **PipeWire** 的一部分，由 Red Hat 的 **Wim Taymans** 开发。PipeWire 自 **2017 年**前后开始创建，是一个统一的 Linux 多媒体框架，结合了 PulseAudio 和 JACK 的能力。SPA 层提供了使 PipeWire 模块化且可扩展的插件架构。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-spa-tools```

```zypper: sudo zypper install pipewire-spa-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [spa-acp-tool](/man/spa-acp-tool)(1), [pw-cli](/man/pw-cli)(1)
