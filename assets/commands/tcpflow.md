# TAGLINE

TCP 流量记录器

# TLDR

在接口和端口上捕获并显示**流量**

```tcpflow -c -i [eth0] port [80]```

从 **pcap 文件**读取流

```tcpflow -r [path/to/capture.pcap] -o [output_dir]```

以**彩色**控制台输出捕获（蓝色=客户端，红色=服务器）

```tcpflow -c -g -i [eth0]```

限制每条流最多捕获的**字节数**

```tcpflow -b [10000] -i [eth0] port [443]```

在控制台输出去除**不可打印**字符

```tcpflow -c -s -i [eth0]```

# SYNOPSIS

**tcpflow** [_OPTIONS_] [_EXPRESSION_]

# PARAMETERS

**-c**
> 带源/目标头部打印到控制台（不创建文件）

**-C**
> 不带头部打印到控制台（不创建文件）

**-i** _INTERFACE_
> 在指定网络接口上捕获

**-r** _FILE_
> 从 pcap 文件读取而非实时捕获

**-o** _DIR_
> 流文件的输出目录

**-b** _MAX_BYTES_
> 每条流最多捕获 max_bytes 字节

**-e** _SCANNER_
> 启用指定的扫描器

**-s**
> 去除不可打印字符（替换为 '.'）

**-g**
> 彩色控制台输出（蓝色=客户端，红色=服务器）

**-D**
> 以十六进制输出到控制台

**-d** _LEVEL_
> 调试级别（0=静默，1=默认）

**-f** _MAX_FDS_
> 可使用的最大文件描述符数量

**-p**
> 不将接口置于混杂模式

**-q**
> 安静模式，抑制警告

**-P**
> 不从哈希表中清除已关闭的连接

# DESCRIPTION

**tcpflow** 捕获 TCP 流量并重建数据流，用于调试和分析。与逐个显示数据包的嗅探器不同，tcpflow 会将 TCP 连接重组为完整的数据流。

每条 TCP 流保存为一个单独的文件，文件名由源和目标的地址/端口组成，便于分析单个连接。

# CAVEATS

需要 root 权限或相应的能力。使用 libpcap 过滤表达式。只捕获 TCP 流量，不捕获 UDP 或其他协议。大规模捕获会占用大量磁盘空间。

# HISTORY

**tcpflow** 由 **Jeremy Elson** 创建，通过重建 TCP 会话实现网络应用的取证分析与调试。

# INSTALL

```apt: sudo apt install tcpflow```

```dnf: sudo dnf install tcpflow```

```pacman: sudo pacman -S tcpflow```

```apk: sudo apk add tcpflow```

```zypper: sudo zypper install tcpflow```

```brew: brew install tcpflow```

```nix: nix profile install nixpkgs#tcpflow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(8), [wireshark](/man/wireshark)(1), [tcpick](/man/tcpick)(8), [nmap](/man/nmap)(1)
