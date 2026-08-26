# TAGLINE

交互式 SIP 流量分析工具

# TLDR

**捕获 SIP 流量**

```sngrep```

**在指定接口上捕获**

```sngrep -d [eth0]```

**从 pcap 读取**

```sngrep -I [capture.pcap]```

**只显示 INVITE 对话**

```sngrep -c```

**捕获到文件**

```sngrep -O [output.pcap]```

**用 BPF 按 IP 过滤**

```sngrep host [192.168.1.100]```

**无界面捕获**（静默模式）

```sngrep -N -q -O [output.pcap]```

# SYNOPSIS

**sngrep** [_-d device_] [_-I file_] [_-O file_] [_options_] [_filter_]

# PARAMETERS

**-d** _DEVICE_
> 捕获设备（或逗号分隔的列表）。

**-I** _FILE_
> 从 pcap 文件读取数据包。

**-O** _FILE_
> 将捕获的数据包保存到 pcap 文件。

**-c**
> 只显示以 INVITE 开始的对话。

**-l** _LIMIT_
> 可捕获的最大对话数。

**-N**
> 无界面模式（仅捕获）。

**-q**
> 静默模式（在无界面模式下抑制输出）。

**-r**
> 捕获 RTP 数据包载荷。

**-R**
> 达到捕获上限时轮转呼叫记录。

**-k** _FILE_
> 用于 TLS 解密的 RSA 私钥。

**-B** _SIZE_
> Pcap 缓冲区大小，单位 MB（默认：2）。

**-H** _URL_
> 将捕获的数据包发送到 Homer sipcapture URL。

**-f** _FILE_
> 加载指定的配置文件。

**-D**
> 打印当前生效的配置并退出。

# DESCRIPTION

**sngrep** 是一个基于终端的工具，用于捕获和分析 VoIP 系统中使用的 SIP（会话发起协议）流量。它提供交互式 ncurses 界面，显示活动的 SIP 对话、带方向箭头的呼叫流程图，以及包含头部和正文的完整消息内容。

该工具可以从网络接口实时捕获 SIP 数据包，也可以读取先前捕获的 pcap 文件进行离线分析。过滤器可按 SIP 方法、源或目标地址以及自定义 BPF 表达式缩小结果范围。捕获的流量可以保存为 pcap 格式，便于日后查看或与其他分析工具共享。

呼叫流程可视化是该工具的突出特色，它显示端点之间 SIP 消息（INVITE、200 OK、ACK、BYE）的先后顺序及时间信息。这使它特别适合诊断 VoIP 呼叫建立失败、注册问题和编解码协商问题。

# INTERFACE CONTROLS

**方向键** - 导航
**Enter** - 显示详情
**F2** - 保存
**F7** - 过滤
**F10/q** - 退出

# CAVEATS

抓包需要 root 权限。TLS 流量需要解密。高流量时可能丢包。

# HISTORY

**sngrep** 由 **Irontec** 为 VoIP 故障排查而创建。它在终端中提供可视化的 SIP 分析。

# INSTALL

```apt: sudo apt install sngrep```

```dnf: sudo dnf install sngrep```

```apk: sudo apk add sngrep```

```zypper: sudo zypper install sngrep```

```brew: brew install sngrep```

```nix: nix profile install nixpkgs#sngrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [tshark](/man/tshark)(1), [wireshark](/man/wireshark)(1)
