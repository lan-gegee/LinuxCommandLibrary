# TAGLINE

基于终端的 Wireshark 界面

# TLDR

监控**默认**网络接口

```sudo termshark```

监控**指定**网络接口

```sudo termshark -i [eth0]```

读取 **pcap** 文件

```termshark -r [path/to/capture.pcap]```

应用**显示过滤器**

```sudo termshark -i [eth0] -Y "[http.request]"```

应用**捕获过滤器**

```sudo termshark -i [eth0] -f "[port 80]"```

# SYNOPSIS

**termshark** [_OPTIONS_] [_INTERFACE_|_FILE_]

# PARAMETERS

**-i** _INTERFACE_
> 在指定接口上捕获

**-r** _FILE_
> 从 pcap 文件读取

**-Y** _FILTER_
> 应用显示过滤器

**-f** _FILTER_
> 应用捕获过滤器

**-d** _layer==selector,protocol_
> 指定某一层的解析方式

**--pass-thru** _[auto|yes|no]_
> 直接运行 tshark 而不启动 UI（auto 表示当 stdout 不是 tty 时）

**--debug**
> 启用调试模式，并在端口 6060 开启性能分析服务器

# DESCRIPTION

**termshark** 是一个基于终端的 tshark 用户界面，可在终端中提供类似 Wireshark 的体验。它提供数据包列表、数据包详情和数据包字节三种视图，并支持交互式导航。

该界面支持键盘导航、显示过滤和流重组，与图形版 Wireshark 类似。

# KEYBOARD SHORTCUTS

**Tab** - 在视图之间切换

**/** - 过滤数据包

**Enter** - 展开/折叠详情

**q** - 退出

# CAVEATS

需要安装 tshark（Wireshark CLI）。实时捕获需要 root 权限。较大的捕获文件加载可能较慢。

# HISTORY

**termshark** 由 **Graham Clark** 创建，旨在把 Wireshark 的界面范式带到终端，使通过 SSH 或在无 GUI 环境中进行数据包分析成为可能。

# INSTALL

```apt: sudo apt install termshark```

```pacman: sudo pacman -S termshark```

```apk: sudo apk add termshark```

```zypper: sudo zypper install termshark```

```brew: brew install termshark```

```nix: nix profile install nixpkgs#termshark```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tshark](/man/tshark)(1), [wireshark](/man/wireshark)(1), [tcpdump](/man/tcpdump)(8)
