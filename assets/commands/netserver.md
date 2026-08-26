# TAGLINE

netperf 测试的服务端

# TLDR

**启动 netserver**

```netserver```

**指定端口**

```netserver -p [12865]```

**调试模式**

```netserver -D```

**绑定到指定地址**

```netserver -L [192.168.1.10]```

**使用 IPv4 模式**

```netserver -4```

**使用 IPv6 模式**

```netserver -6```

# SYNOPSIS

**netserver** [_options_]

# PARAMETERS

**-p** _PORT_
> 监听端口（默认 12865）。

**-D**
> 不守护进程化；在前台运行（调试）。

**-d**
> 增加调试详细程度。

**-L** _ADDR_
> 本地绑定地址。

**-N**
> 无控制连接；独立数据模式。

**-f**
> 不按需派生；保持在前台运行。

**-v** _LEVEL_
> 详细程度。

**-4**
> 仅 IPv4。

**-6**
> 仅 IPv6。

**--help**
> 显示帮助信息。

# DESCRIPTION

**netserver** 是 netperf 测试的服务端。它负责接收网络性能测试。

该工具处理基准测试请求。在目标机器上运行即可进行吞吐量测试。

# CAVEATS

需要 netperf 客户端。会打开网络端口。属于性能测试工具。

# HISTORY

netserver 是 **netperf** 的组成部分，后者由 HP 为网络性能测量而创建。

# INSTALL

```apt: sudo apt install netperf```

```dnf: sudo dnf install netperf```

```pacman: sudo pacman -S netperf```

```nix: nix profile install nixpkgs#netperf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[netperf](/man/netperf)(1), [iperf](/man/iperf)(1), [iperf3](/man/iperf3)(1), [nuttcp](/man/nuttcp)(1)
