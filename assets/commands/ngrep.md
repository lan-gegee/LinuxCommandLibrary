# TAGLINE

网络数据包 grep 工具

# TLDR

**以静默模式在数据包中搜索模式**

```ngrep -q "[pattern]"```

**在指定接口和端口上搜索**

```ngrep -d [eth0] "[pattern]" port [80]```

**以按行输出的方式搜索 HTTP 流量**

```ngrep -q -W byline "[GET|POST]" port [80]```

**搜索来自指定主机的流量**

```ngrep -q "[pattern]" host [192.168.1.1]```

**随匹配的数据包一起显示时间戳**

```ngrep -q -t "[pattern]"```

**从 pcap 抓包文件读取**

```ngrep -I [file.pcap] "[pattern]"```

**不区分大小写搜索并将匹配结果写入 pcap 文件**

```ngrep -qi -O [output.pcap] "[pattern]"```

**只匹配指定数量的数据包**

```ngrep -q -n [10] "[pattern]"```

# SYNOPSIS

**ngrep** [_options_] _pattern_ [_filter_]

# PARAMETERS

_PATTERN_
> 用于匹配数据包载荷的扩展正则表达式。

_FILTER_
> BPF 过滤表达式（语法与 tcpdump 相同）。

**-q**
> 静默模式；只输出包头和载荷。

**-d** _IFACE_
> 要监听的网络接口（默认：自动选择）。

**-W** _MODE_
> 输出模式：normal（默认）、byline（保留换行）、single（每个包一行）、none。

**-i**
> 不区分大小写匹配。

**-I** _FILE_
> 从 pcap 转储文件读取数据包。

**-O** _FILE_
> 将匹配的数据包写入 pcap 转储文件。

**-t**
> 为每个匹配的数据包打印时间戳。

**-n** _NUM_
> 总共只匹配 NUM 个数据包后退出。

**-s** _SNAPLEN_
> 设置 BPF 捕获长度（默认：65536）。

**-X**
> 将匹配表达式当作十六进制字符串处理。

**-w**
> 将正则表达式按整词匹配。

# DESCRIPTION

**ngrep** 是一个基于 pcap 的工具，它把类似 GNU grep 的模式匹配应用到网络数据包的载荷上。它能识别以太网、PPP、SLIP、FDDI 以及 null 接口上的 TCP、UDP 和 ICMP 数据包，并以与 tcpdump 相同的方式理解 BPF 过滤逻辑。匹配到的数据包可以直接显示，也可以写入 pcap 文件以便进一步分析。

# CAVEATS

实时抓包需要 root 权限或相应的能力（capabilities）。只能匹配数据包的载荷数据（对加密流量无效）。BPF 过滤表达式遵循 tcpdump 语法。

# HISTORY

ngrep 的出现是为了给网络数据包检查提供 **类 grep** 的功能。

# INSTALL

```apt: sudo apt install ngrep```

```dnf: sudo dnf install ngrep```

```pacman: sudo pacman -S ngrep```

```apk: sudo apk add ngrep```

```zypper: sudo zypper install ngrep```

```brew: brew install ngrep```

```nix: nix profile install nixpkgs#ngrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [grep](/man/grep)(1), [wireshark](/man/wireshark)(1)
