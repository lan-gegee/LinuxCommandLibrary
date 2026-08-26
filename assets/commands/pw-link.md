# TAGLINE

创建和管理 PipeWire 端口连接

# TLDR

列出带 ID 的**输入和输出**端口

```pw-link -oiI```

在端口之间**创建**链接

```pw-link [output_port] [input_port]```

**断开**两个端口的连接

```pw-link -d [output_port] [input_port]```

列出带 ID 的所有**链接**

```pw-link -lI```

显示**帮助**

```pw-link -h```

# SYNOPSIS

**pw-link** [**-o**] [**-i**] [**-l**] [**-I**] [**-d**] [_output_port_ _input_port_]

# PARAMETERS

**-o, --output**
> 列出输出端口

**-i, --input**
> 列出输入端口

**-l, --links**
> 列出现有链接

**-I, --id**
> 显示对象 ID

**-d, --disconnect**
> 断开端口连接而非建立连接

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**pw-link** 管理 PipeWire 端口之间的连接。它可以列出可用端口、在音频源和输出设备之间创建新链接，以及移除现有连接。

该工具支持在应用与设备之间路由音频，可用于构建复杂的音频配置，例如虚拟连线或录制应用输出。

# CAVEATS

端口名称可能很长且复杂。会话管理器可能会重建链接。编写脚本时使用 ID 更稳定。某些链接由 WirePlumber 管理。

# HISTORY

**pw-link** 是 **PipeWire** 的一部分，提供类似于 JACK 的 jack_connect 的端口连接管理。它支持对音频路由图进行手动控制。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cli](/man/pw-cli)(1), [wpctl](/man/wpctl)(1), [jack_connect](/man/jack_connect)(1)
