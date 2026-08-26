# TAGLINE

结合 traceroute 与 ping 的网络诊断工具

# TLDR

**对主机运行 traceroute**

```mtr [hostname]```

**用 TCP 代替 ICMP**

```mtr --tcp [hostname]```

**用 UDP 代替 ICMP**

```mtr --udp [hostname]```

**为 TCP/UDP 指定端口**

```mtr --tcp --port [443] [hostname]```

**生成报告后退出**

```mtr --report [hostname]```

**以 N 个循环生成报告**

```mtr --report --report-cycles [100] [hostname]```

**只显示数字 IP，不做 DNS 解析**

```mtr --no-dns [hostname]```

**以 JSON 输出**

```mtr --json [hostname]```

# SYNOPSIS

**mtr** [_--report_] [_--tcp_|_--udp_] [_--port num_] [_--no-dns_] [_options_] _hostname_

# PARAMETERS

**-r**, **--report**
> 以报告模式生成输出并退出。

**-c** _NUM_, **--report-cycles** _NUM_
> 每一跳的 ping 次数（默认：10）。

**-s** _SIZE_, **--psize** _SIZE_
> 数据包大小（字节）。

**-T**, **--tcp**
> 使用 TCP SYN 包。

**-U**, **--udp**
> 使用 UDP 数据报。

**-P** _PORT_, **--port** _PORT_
> TCP/UDP 的目标端口。

**-n**, **--no-dns**
> 不解析主机名。

**-b**, **--show-ips**
> 同时显示主机名和 IP。

**-w**, **--report-wide**
> 宽幅报告格式（不截断）。

**-j**, **--json**
> 以 JSON 格式输出。

**-x**, **--xml**
> 以 XML 格式输出。

**-C**, **--csv**
> 以 CSV 格式输出。

**-i** _SECONDS_, **--interval** _SECONDS_
> ping 之间的间隔。

**-m** _NUM_, **--max-ttl** _NUM_
> 最大 TTL / 跳数。

**-f** _NUM_, **--first-ttl** _NUM_
> 起始 TTL。

**-4**
> 仅使用 IPv4。

**-6**
> 仅使用 IPv6。

**-a** _ADDRESS_, **--address** _ADDRESS_
> 绑定到指定的源地址。

**-e**, **--mpls**
> 显示来自 ICMP 扩展的 MPLS 信息。

**-o** _FIELDS_, **--order** _FIELDS_
> 指定报告输出的字段及其顺序。

# DESCRIPTION

**mtr**（My TraceRoute）将 traceroute 和 ping 的功能结合到一个网络诊断工具中。它发送故意设置低 TTL 的数据包，持续探测到目标沿途的每一跳，并实时显示丢包率和延迟统计信息。

交互式界面会持续更新，逐跳显示每个路由器的丢包百分比、发送/接收计数以及延迟统计数据（最佳、平均、最差、标准差）。这使定位网络问题的发生位置变得容易。

报告模式（**-r**）运行固定数量的循环（默认 10）后输出汇总统计信息，适合记录日志和编写脚本。宽幅报告模式（**-w**）可避免主机名被截断。输出格式包括纯文本、JSON、XML 和 CSV，便于与监控系统对接。

TCP 和 UDP 模式有助于在 ICMP 被过滤时诊断问题。使用 TCP 端口 443 或 80 往往能到达那些屏蔽 ping 的目标。该工具还能检测非对称路由和路径变化。

MTR 对诊断间歇性网络问题极为有用——你可以持续观察它，捕捉单次 traceroute 可能遗漏的偶发丢包。

# CAVEATS

除非使用 TCP 模式，否则需要 root 权限或相应 capabilities 才能访问原始套接字（ICMP/UDP）。有些路由器不响应 TTL 超限消息，会显示为 "???"。路由器上的速率限制可能造成丢包误读。ICMP 降优先级处理可能导致显示的延迟高于实际数据流量。

# HISTORY

**mtr** 由 **Matt Kimball** 于 **1997 年**编写，是对传统 traceroute 的改进。名字最初代表 "Matt's TraceRoute"。后来 Roger Wolff 接手维护并添加了许多特性。该工具已成为标准的网络诊断工具，包含在大多数 Linux 发行版中，也可用于其他类 Unix 系统和 Windows。

# INSTALL

```apt: sudo apt install mtr```

```dnf: sudo dnf install mtr```

```pacman: sudo pacman -S mtr```

```apk: sudo apk add mtr```

```zypper: sudo zypper install mtr```

```brew: brew install mtr```

```nix: nix profile install nixpkgs#mtr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[traceroute](/man/traceroute)(1), [ping](/man/ping)(1), [tracepath](/man/tracepath)(1), [nmap](/man/nmap)(1), [ss](/man/ss)(1), [netstat](/man/netstat)(1)
