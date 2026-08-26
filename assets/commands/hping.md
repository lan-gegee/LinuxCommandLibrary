# TAGLINE

老式的 TCP/IP 数据包构造与分析工具，hping3 的前身

# TLDR

**发送 ICMP ping**

```hping -1 [host]```

**向端口发送 TCP SYN**

```hping -S -p [80] [host]```

**向端口发送 UDP 包**

```hping -2 -p [53] [host]```

**traceroute 模式**

```hping --traceroute -1 [host]```

**发送固定数量的数据包**

```hping -c [5] -1 [host]```

**伪造源 IP 地址**

```hping -a [source-ip] -S -p [80] [host]```

**扫描一段端口范围**

```hping -8 [1-100] -S [host]```

# SYNOPSIS

**hping** [_options_] _host_

# PARAMETERS

**-0**, **--rawip**
> Raw IP 模式。

**-1**, **--icmp**
> ICMP 模式。

**-2**, **--udp**
> UDP 模式。

**-8**, **--scan** _range_
> 端口扫描模式。

**-S**, **--syn**
> 设置 TCP SYN 标志。

**-A**, **--ack**
> 设置 TCP ACK 标志。

**-p**, **--destport** _port_
> 目标端口。

**-s**, **--baseport** _port_
> 源端口。

**-c**, **--count** _count_
> 要发送的数据包数量。

**-i**, **--interval** _wait_
> 数据包之间的间隔。

**-a**, **--spoof** _host_
> 伪造源地址。

**-T**, **--traceroute**
> traceroute 模式。

**-C** _type_
> 设置 ICMP 类型。

**-K** _code_
> 设置 ICMP 代码。

# DESCRIPTION

**hping**（也称为 hping2）是一个命令行工具，用于构造并发送自定义的 TCP、UDP、ICMP 或 Raw IP 数据包，并显示目标的回应，类似于 **ping** 显示 ICMP 回显应答。它支持分片和任意数据包载荷，可用于防火墙测试、端口扫描、路径 MTU 发现、基于任意协议的类 traceroute 探测以及 TCP/IP 协议栈审计。

**hping3** 通过增加 Tcl 脚本支持取代了这个版本，但复用了相同的底层数据包生成代码，因此 hping 的命令行标志几乎原样沿用。当前大多数 Linux 发行版只打包 **hping3**；单纯的 **hping** 二进制文件在很大程度上是保留兼容性的遗留名称，默认可能不会安装。

# CAVEATS

构造原始数据包需要 root 权限。**hping** 已无人维护；新的部署应改用仍在（有限地）维护的 **hping3**。未经授权发送伪造数据包或进行激进扫描可能违法，并可能触发防火墙或 IDS 系统。

# HISTORY

**hping** 由 **Salvatore Sanfilippo**（"antirez"，也是 Redis 的作者）于 20 世纪 90 年代末创建，作为 TCP/IP 协议的数据包生成器和分析器。Sanfilippo 用它开发了后来被 Nmap 采用的 idle scan 技术。2005 年发布的 **hping3** 在相同的核心数据包构造代码之上加入了 Tcl 脚本引擎，取代它成为活跃开发的版本。

# INSTALL

```pacman: sudo pacman -S hping```

```nix: nix profile install nixpkgs#hping```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hping3](/man/hping3)(8), [nmap](/man/nmap)(1), [ping](/man/ping)(1), [traceroute](/man/traceroute)(1)

# RESOURCES

```[Source code](https://github.com/antirez/hping)```

<!-- verified: 2026-07-19 -->
