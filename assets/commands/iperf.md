# TAGLINE

测量两个端点之间的网络带宽

# TLDR

**以服务器模式启动**

```iperf -s```

**连接服务器**并运行测试

```iperf -c [server_ip]```

按指定时长**运行测试**

```iperf -c [server_ip] -t [30]```

**改用 UDP 测试**而非 TCP

```iperf -c [server_ip] -u```

**使用多条并行流**进行测试

```iperf -c [server_ip] -P [4]```

**运行双向**测试

```iperf -c [server_ip] -d```

为 UDP **设置目标带宽**

```iperf -c [server_ip] -u -b [100M]```

**指定端口**

```iperf -c [server_ip] -p [5001]```

**定期报告**结果

```iperf -c [server_ip] -i [1]```

# SYNOPSIS

**iperf** **-s** [_OPTIONS_]

**iperf** **-c** _HOST_ [_OPTIONS_]

# PARAMETERS

**-s**
> 以服务器模式运行。

**-c** _HOST_
> 以客户端模式运行，连接到 HOST 上的服务器。

**-p** _PORT_
> 监听或连接的服务器端口（默认：5001）。

**-u**
> 使用 UDP 而非 TCP。

**-b** _BANDWIDTH_
> 目标带宽（如 10M、1G）。限制 UDP 和 TCP 的速率。

**-t** _TIME_
> 测试时长（秒）（默认：10）。

**-n** _BYTES_
> 传输指定的字节数而非按时长测试（如 100M、1G）。

**-i** _INTERVAL_
> 报告间隔（秒）。

**-P** _STREAMS_
> 并行客户端流的数量。

**-d**
> 双向测试，使用独立的单向套接字。

**-r**
> 双向测试（先客户端到服务器，再反向依次进行）。

**--full-duplex**
> 全双工测试，两个方向共用单个套接字。

**-R**
> 反转流量方向（服务器发送，客户端接收）。

**-f** _FORMAT_
> 报告格式：a（自适应）、k/m/g（比特）、K/M/G（字节）。

**-w** _SIZE_
> 套接字缓冲区大小（TCP 窗口大小）。

**-l** _LENGTH_
> 读/写缓冲区长度（TCP 默认 128K，UDP 默认 1470）。

**-M** _MSS_
> 通过 TCP_MAXSEG 设置 TCP 最大报文段大小。

**-N**
> 禁用 Nagle 算法（设置 TCP_NODELAY）。

**-B** _HOST_
> 绑定到特定的主机、接口或多播地址。

**-D**
> 将服务器作为守护进程运行。

**-e**
> 在报告中显示增强的输出。

**-o** _FILE_
> 将报告输出写入指定文件。

# DESCRIPTION

**iperf** 测量两个端点之间的网络带宽。一台主机以服务器模式运行（-s），另一台作为客户端连接（-c）执行测试。默认情况下，iperf 测量 TCP 吞吐量。

UDP 模式（-u）以可配置的目标带宽测试 UDP 性能。这可用于测量特定速率下的丢包和抖动。并行流（-P）可以打满单条流无法填满的高带宽链路。

结果显示达到的带宽，以及取决于协议的其他指标（TCP 显示重传数，UDP 显示丢包率和抖动）。

# CAVEATS

iperf（版本 2）与 iperf3 是相互独立的项目，协议互不兼容。本页面介绍的是 iperf2。防火墙规则可能需要放行 iperf 端口（默认 5001）。测试结果可能受任一端 CPU 性能限制的影响，在高带宽下尤其明显。

# HISTORY

iperf 由 NLANR/DAST 开发，是一款开源的网络测试工具。最初的 iperf（版本 2）被广泛用于网络诊断。**iperf3** 是 ESnet 的完全重写版本，功能有所增强，但使用不兼容的协议，要求两端使用相同的版本。

# INSTALL

```apt: sudo apt install iperf```

```dnf: sudo dnf install iperf```

```pacman: sudo pacman -S iperf```

```apk: sudo apk add iperf```

```zypper: sudo zypper install iperf```

```brew: brew install iperf```

```nix: nix profile install nixpkgs#iperf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iperf3](/man/iperf3)(1), [netcat](/man/netcat)(1), [speedtest-cli](/man/speedtest-cli)(1), [ping](/man/ping)(8)
