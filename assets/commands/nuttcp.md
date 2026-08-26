# TAGLINE

网络性能测量工具

# TLDR

**启动服务器**

```nuttcp -S```

**测试到服务器的吞吐量**

```nuttcp [server_ip]```

**测试 UDP 吞吐量**

```nuttcp -u [server_ip]```

**指定带宽限制**

```nuttcp -R [100M] [server_ip]```

**测试特定时长**

```nuttcp -T [30] [server_ip]```

**接收方模式**（反向方向测试）

```nuttcp -r [server_ip]```

**使用多条并行流**

```nuttcp -N [4] [server_ip]```

**测试时每隔一秒输出报告**

```nuttcp -i [1] [server_ip]```

# SYNOPSIS

**nuttcp** [_options_] [_host_]

# PARAMETERS

**-S**
> 服务器模式。

**-u**
> UDP 模式（默认 TCP）。

**-R** _rate_
> 速率限制（K、M、G）。

**-T** _time_
> 测试时长。

**-t**
> 发送方模式。

**-r**
> 接收方模式。

**-p** _port_
> 数据端口。

**-P** _port_
> 控制端口。

**-w** _size_
> 窗口大小（套接字缓冲区大小）。

**-N** _nstream_
> 并行数据流的数量（默认 1，最大 128）。

**-i** _interval_
> 以秒为单位的间隔报告。

**-l** _buflen_
> 网络读/写缓冲区的长度（字节）。

**-s**
> 使用 stdin/stdout 传输数据（支持磁盘到网络的传输）。

**-F**
> 反转数据连接的打开方向（在防火墙/NAT 环境下有用）。

**-b**
> 简洁的单行输出（默认格式）。

# DESCRIPTION

**nuttcp** 是一款网络性能测量工具。它测量系统之间的 TCP 和 UDP 吞吐量，并提供关于网络性能的详细统计信息。

nuttcp 与 iperf 类似，但包含服务器模式、速率限制、多条并行流以及基于计时器的用法等特性。它还支持 IPv6、IPv4 组播以及设置 TOS/DSCP 位。

# EXAMPLE OUTPUT

```
   84.8594 MB /  10.00 sec =   71.1477 Mbps 0 retrans
```

# CAVEATS

远端需要运行服务器。防火墙必须放行相关端口。UDP 测试可能显示丢包。测试结果会受到其他流量的影响。

# HISTORY

nuttcp 由 **Bill Fink** 在 NLANR/DAST 开发，是一款网络测试工具，在更早的 ttcp 基础上构建而成。

# INSTALL

```apt: sudo apt install nuttcp```

```dnf: sudo dnf install nuttcp```

```apk: sudo apk add nuttcp```

```brew: brew install nuttcp```

```nix: nix profile install nixpkgs#nuttcp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iperf3](/man/iperf3)(1), [iperf](/man/iperf)(1), [netperf](/man/netperf)(1), [tc](/man/tc)(8)
