# TAGLINE

测量网络吞吐量和延迟

# TLDR

**运行 TCP 吞吐量测试**

```netperf -H [hostname]```

**运行 UDP 测试**

```netperf -H [hostname] -t UDP_STREAM```

**运行延迟测试**

```netperf -H [hostname] -t TCP_RR```

**运行指定时长的测试**

```netperf -H [hostname] -l [30]```

**指定消息大小**

```netperf -H [hostname] -- -m [1024]```

**以多个连接运行**

```netperf -H [hostname] -C -c```

**启动 netserver**（在远程主机上）

```netserver```

# SYNOPSIS

**netperf** [_-H host_] [_-t test_] [_-l duration_] [_options_] [_-- test_options_]

# PARAMETERS

**-H** _HOST_
> 运行 netserver 的远程主机。

**-t** _TEST_
> 测试类型（TCP_STREAM、UDP_STREAM、TCP_RR 等）。

**-l** _SECONDS_
> 测试时长。

**-p** _PORT_
> 控制连接的端口。

**-P** _PORT_
> 数据连接的端口。

**-c**
> 报告本地 CPU 使用率。

**-C**
> 报告远程 CPU 使用率。

**-f** _UNITS_
> 输出格式（K、M、G，针对比特/字节）。

**-v** _LEVEL_
> 详细程度。

**-- -m** _SIZE_
> 测试使用的消息大小。

**-- -s** _SIZE_
> 本地套接字缓冲区大小。

**-- -S** _SIZE_
> 远程套接字缓冲区大小。

# DESCRIPTION

**netperf** 用于测量网络吞吐量和延迟。它由 netperf（客户端）和 netserver（运行在远程主机上的服务端）组成。

TCP_STREAM 测试批量数据传输吞吐量。它测量数据通过 TCP 连接的推送速度，可用于评估网络容量。

UDP_STREAM 测试没有 TCP 开销的 UDP 吞吐量。结果反映原始网络能力，但可能包含丢包影响。

TCP_RR（请求/响应）测量延迟——往返一次需要多长时间。这对交互式应用和数据库至关重要。

CPU 使用率报告有助于判断性能瓶颈在网络还是 CPU。网络测试期间 CPU 占用过高说明端点是瓶颈。

套接字缓冲区大小会影响性能。更大的缓冲区可提升高延迟链路上的吞吐量，但会增加内存占用。

# CAVEATS

远程主机上必须运行 netserver。防火墙可能阻断连接。测试结果受其他网络流量影响。在某些系统上，CPU 测量需要特权。

# HISTORY

**netperf** 由 **Hewlett-Packard** 从 **20 世纪 90 年代**开始开发，是一款网络基准测试工具。它已成为测量网络性能的标准工具，被无数基准测试和学术论文使用。

# INSTALL

```apt: sudo apt install netperf```

```dnf: sudo dnf install netperf```

```pacman: sudo pacman -S netperf```

```nix: nix profile install nixpkgs#netperf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iperf3](/man/iperf3)(1), [nuttcp](/man/nuttcp)(1), [ping](/man/ping)(1), [netcat](/man/netcat)(1)
