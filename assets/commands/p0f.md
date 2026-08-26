# TAGLINE

执行被动式操作系统指纹识别

# TLDR

**开始指纹识别**

```p0f -i [eth0]```

**读取 pcap 文件**

```p0f -r [capture.pcap]```

**写入日志文件**

```p0f -i [eth0] -o [log.txt]```

**针对特定端口进行指纹识别**

```p0f -i [eth0] "port 80"```

**在后台运行**

```p0f -i [eth0] -d```

# SYNOPSIS

**p0f** [_options_] [_filter_]

# PARAMETERS

**-i** _INTERFACE_
> 在指定网络接口上监听。

**-r** _FILE_
> 从 pcap 抓包文件而非实时接口读取数据包。

**-o** _FILE_
> 将指纹识别结果追加到 _FILE_（文本日志）。

**-w** _FILE_
> 将捕获的数据包写入新的 pcap 文件（类似 **tcpdump -w**）。

**-s** _PATH_
> 在 _PATH_ 上监听 Unix 域套接字以提供 API 查询。

**-d**
> 作为守护进程在后台运行。需要 **-o** 或 **-s**。

**-u** _USER_
> 打开捕获接口后将权限降为 _USER_。

**-p**
> 将接口置于混杂模式。

**-f** _FILE_
> 使用 _FILE_ 作为指纹数据库（默认：**/etc/p0f/p0f.fp**）。

**-S** _N_
> 设置并发 API 连接的最大数量。

**-c** _DIR_
> 通过 chroot 到 _DIR_ 来限制输出。

**-L**
> 列出可用的捕获接口并退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**p0f** 是一款被动式的操作系统、应用和链路类型指纹识别工具。它监听 TCP/IP 流量而不发送任何数据包，并根据所观察到的 SYN、SYN+ACK 及 HTTP 流量中的特征推断远程操作系统、MTU/上行链路、NAT 存在与否以及大致的开机时长。

由于从不主动探测目标，**p0f** 在网络上是不可见的，非常适合对 pcap 进行取证分析、对面向公众服务的访问者做指纹识别，以及检测策略违规行为（如防火墙后未做 NAT 的设备）。

# CAVEATS

需要原始套接字 / **CAP_NET_RAW** 权限（或 root）。检测质量取决于是否有最新的 **p0f.fp** 签名数据库。**p0f v3** 是一次重写，不读取 v2 的指纹文件；请确保随附的指纹与二进制版本匹配。

# HISTORY

p0f 由 **Michal Zalewski** 创建，用于被动式 TCP/IP 协议栈指纹识别。

# INSTALL

```apt: sudo apt install p0f```

```dnf: sudo dnf install p0f```

```pacman: sudo pacman -S p0f```

```zypper: sudo zypper install p0f```

```brew: brew install p0f```

```nix: nix profile install nixpkgs#p0f```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1)
