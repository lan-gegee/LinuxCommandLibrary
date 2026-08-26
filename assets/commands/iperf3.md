# TAGLINE

测量最大 TCP 和 UDP 带宽的网络吞吐量测试工具

# TLDR

**启动服务器**

```iperf3 -s```

**连接服务器**并运行测试

```iperf3 -c [server_ip]```

按指定时长**运行测试**

```iperf3 -c [server_ip] -t [30]```

**测试上传速度**（反向模式）

```iperf3 -c [server_ip] -R```

**改用 UDP 测试**而非 TCP

```iperf3 -c [server_ip] -u```

**使用多条并行流**

```iperf3 -c [server_ip] -P [4]```

**设置目标带宽**（针对 UDP）

```iperf3 -c [server_ip] -u -b [100M]```

**以 JSON 输出**结果

```iperf3 -c [server_ip] -J```

# SYNOPSIS

**iperf3** [_-s|-c host_] [_-p port_] [_-t time_] [_-P parallel_] [_-u_] [_-b bandwidth_] [_-R_] [_options_]

# PARAMETERS

**-s**, **--server**
> 以服务器模式运行。

**-c**, **--client** _host_
> 作为客户端连接服务器。

**-p**, **--port** _port_
> 服务器端口（默认：5201）。

**-t**, **--time** _n_
> 测试时长（秒）（默认：10）。

**-P**, **--parallel** _n_
> 并行流的数量。

**-u**, **--udp**
> 使用 UDP 而非 TCP。

**-b**, **--bandwidth** _n[KMG]_
> 目标带宽（UDP 默认：1 Mbit/s）。

**-R**, **--reverse**
> 以反向模式运行（服务器发送，客户端接收）。

**--bidir**
> 同时进行双向测试。

**-i**, **--interval** _n_
> 定期报告之间的间隔秒数。

**-n**, **--bytes** _n[KMG]_
> 要传输的字节数。

**-J**, **--json**
> 以 JSON 格式输出。

**-l**, **--length** _n[KMG]_
> 缓冲区/数据包大小。

**-w**, **--window** _n[KMG]_
> 套接字缓冲区大小。

**-B**, **--bind** _addr_
> 绑定到特定地址。

**-4**, **-6**
> 仅使用 IPv4/IPv6。

**-D**, **--daemon**
> 将服务器作为守护进程运行。

**--logfile** _file_
> 将输出写入文件。

# DESCRIPTION

**iperf3** 是一款网络吞吐量测试工具，用于测量最大 TCP 和 UDP 带宽性能。它在服务器和客户端之间创建数据流来测量可达的网络速度，可用于故障排查、基准测试和容量规划。

典型的测试需要在一台机器上以服务器模式运行 iperf3，在另一台上以客户端模式运行。由客户端发起测试，双方都会报告测得的吞吐量。默认情况下，测试以 TCP 运行 10 秒。

TCP 模式测量批量传输速度，受拥塞控制、RTT 和链路容量的限制。配合 -b 的 UDP 模式可设定目标发送速率，适合测试网络能否在不丢包的情况下维持特定带宽。

并行流（-P）可以发现聚合能力的上限，并帮助打满单条流无法占满的高带宽链路。反向模式（-R）让服务器向客户端发送数据，从而测试上传速度。

JSON 输出便于自动化测试和与监控系统集成。服务器可作为守护进程运行，以保持持续可用。

# CAVEATS

与 iperf2 协议不兼容。服务器端口（5201）必须能穿过防火墙访问。测试会消耗大量带宽——不要在生产网络上未经告知就运行。单个服务器一次只能处理一个客户端。结果受 CPU、内存和网络接口能力的影响。

# HISTORY

**iperf3** 由劳伦斯伯克利国家实验室的 ESnet（能源科学网络）开发，约在 **2014 年**发布，是对原版 iperf 的重写。重写改进了代码库，加入了 JSON 输出和双向测试等特性，并修复了协议上的局限。它已成为标准的网络吞吐量测试工具。

# INSTALL

```apt: sudo apt install iperf3```

```dnf: sudo dnf install iperf3```

```pacman: sudo pacman -S iperf3```

```apk: sudo apk add iperf3```

```brew: brew install iperf3```

```nix: nix profile install nixpkgs#iperf3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iperf](/man/iperf)(1), [netperf](/man/netperf)(1), [nuttcp](/man/nuttcp)(8), [speedtest-cli](/man/speedtest-cli)(1)
