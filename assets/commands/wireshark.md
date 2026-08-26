# TAGLINE

图形化网络协议分析器

# TLDR

**启动 Wireshark** 图形界面

```wireshark```

**打开捕获文件**

```wireshark [capture.pcapng]```

在指定网卡接口上**开始捕获**

```wireshark -i [eth0] -k```

**使用 BPF 捕获过滤器进行捕获**

```wireshark -i [eth0] -f "port 80" -k```

**打开文件并应用显示过滤器**

```wireshark -Y "http.request" -r [capture.pcapng]```

**捕获到文件**并在指定时长后停止

```wireshark -i [eth0] -w [output.pcapng] -a duration:[60]```

**列出可用的捕获接口**

```wireshark -D```

# SYNOPSIS

**wireshark** [_options_] [_file_]

# DESCRIPTION

**Wireshark** 是一款图形化网络协议分析器，用于捕获并交互式分析网络流量。它能解码数百种协议，并以友好的界面提供详细的数据包信息。

应用程序以三栏窗口显示数据包：数据包列表、数据包详情（协议树）和数据包字节。强大的显示过滤器可以隔离特定的流量模式。捕获过滤器则可减小捕获文件的体积。

Wireshark 是网络排错、安全分析、协议开发和教学领域的行业标准。它支持从多种类型的接口进行实时捕获，并能读取多种捕获文件格式。

# PARAMETERS

**-i** _interface_
> 在指定接口上捕获。

**-f** _filter_
> 捕获过滤器（BPF 语法）。

**-Y** _filter_
> 显示过滤器。

**-w** _file_
> 将捕获写入文件。

**-r** _file_
> 读取捕获文件。

**-a** _condition_
> 自动停止条件（时长、文件大小、数据包数量）。

**-b** _option_
> 环形缓冲区选项。

**-k**
> 立即开始捕获。

**-D**
> 列出可用接口。

**-S**
> 捕获期间实时更新数据包列表。

**-c** _count_
> 收到指定数量的数据包后停止捕获。

**-n**
> 禁用网络名称解析。

**-o** _preference:value_
> 设置偏好项的值（覆盖偏好设置文件）。

**-X** _extension_option_
> 指定扩展选项（如 lua_script:myscript.lua）。

**--fullscreen**
> 以全屏模式启动 Wireshark。

**--list-time-stamp-types**
> 列出接口的时间戳类型。

# DISPLAY FILTERS

**ip.addr == 192.168.1.1**: 按 IP 地址过滤（源或目标）。
**tcp.port == 443**: 按 TCP 端口过滤。
**http.request**: 仅显示 HTTP 请求。
**dns**: 显示 DNS 流量。
**tcp.flags.syn == 1 && tcp.flags.ack == 0**: SYN 数据包（连接发起）。
**frame contains "password"**: 在数据包内容中搜索字符串。
**ip.src == 10.0.0.0/8**: 按源子网过滤。
**tcp.analysis.retransmission**: 显示 TCP 重传。

# CAVEATS

实时捕获需要权限（root 或 cap_net_raw 能力）。大型捕获会占用大量内存。显示过滤器的语法与捕获过滤器不同。某些协议需要额外的解析器插件。

# HISTORY

**Wireshark** 的前身是 **Ethereal**，由 **Gerald Combs** 于 **1998 年**创建。由于商标问题，它于 **2006 年**更名为 Wireshark。如今它已成为使用最广泛的网络协议分析器，由活跃的社区和 Wireshark 基金会提供支持。该项目持续为新协议添加解析支持。

# INSTALL

```apt: sudo apt install wireshark```

```dnf: sudo dnf install wireshark```

```apk: sudo apk add wireshark```

```zypper: sudo zypper install wireshark```

```brew: brew install wireshark```

```nix: nix profile install nixpkgs#wireshark```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tshark](/man/tshark)(1), [tcpdump](/man/tcpdump)(1), [dumpcap](/man/dumpcap)(1), [editcap](/man/editcap)(1), [ngrep](/man/ngrep)(1)
