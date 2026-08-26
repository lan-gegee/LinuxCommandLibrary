# TAGLINE

面向多主机的并行 ping 工具

# TLDR

**Ping 多个主机**

```fping [host1] [host2] [host3]```

**从文件中读取主机并 Ping**

```fping -f [path/to/hosts.txt]```

**Ping 一段 IP 地址范围**

```fping -g [192.168.1.1] [192.168.1.254]```

**Ping 一个 CIDR 范围**

```fping -g [192.168.1.0/24]```

**仅显示存活主机**

```fping -a [host1] [host2]```

**仅显示不可达主机**

```fping -u [host1] [host2]```

**Ping 并输出统计信息**（类似 ping）

```fping -s [host1] [host2]```

以指定间隔进行**持续 Ping**

```fping -l -p [1000] [host]```

# SYNOPSIS

**fping** [_-aAcdDeglmnqQrstuvV_] [_-b size_] [_-B backoff_] [_-c count_] [_-f file_] [_-g addr/mask_] [_-i interval_] [_-p period_] [_-r retry_] [_-S source_] [_-t timeout_] [_targets_]

# PARAMETERS

**-a**
> 仅显示存活（可达）的主机。

**-u**
> 仅显示不可达的主机。

**-g** _addr/mask_ 或 _start end_
> 从 CIDR 或地址范围生成目标列表。

**-f** _file_
> 从文件读取目标（`-` 表示标准输入）。

**-c** _count_
> 对每个目标发送的 ping 次数。

**-l**
> 循环模式：无限持续 ping。

**-p** _period_
> 对同一目标两次 ping 之间的间隔（毫秒）。

**-i** _interval_
> 对不同目标两次 ping 之间的间隔（毫秒）。

**-t** _timeout_
> 单次 ping 的超时时间（毫秒）。

**-r** _retry_
> 对不可达主机的重试次数。

**-s**
> 在结束时输出累计统计信息。

**-q**
> 安静模式：仅显示摘要。

**-e**
> 显示每次响应的耗时。

**-A**
> 以 IP 地址形式显示目标。

**-D**
> 在每行之前显示时间戳。

**-S** _source_
> 设置源地址。

**-b** _size_
> ping 数据包大小（字节）。

# DESCRIPTION

**fping** 专为脚本和监控场景设计，在检查多个主机方面比标准 ping 命令有显著优势。它可以并行 ping 大量主机，并以适合解析的格式报告结果。

与逐个等待每台主机响应的 ping 不同，fping 以轮询方式向所有目标发送探测包，然后等待响应。这种并行机制使它在检查大量主机时快得多。

该工具常用于网络监控脚本、主机发现和可用性检查。用于生成 IP 范围的 **-g** 选项可以快速扫描子网。退出码表示总体的可达性状态，便于在脚本中使用。

输出模式涵盖从每次 ping 的详细信息到只显示摘要的安静模式。仅显示存活（-a）或仅显示不可达（-u）的模式在你只需要特定结果时可以简化解析工作。

fping 可以从文件或标准输入读取目标，便于与其他工具集成。对于持续监控，循环模式（-l）配合自定义间隔可提供持续的状态更新。

# CAVEATS

在某些系统上需要 root/sudo 权限才能访问原始套接字（或以 setuid 方式安装）。极快的扫描可能被网络安全系统判定为攻击行为。过高的探测频率可能给网络基础设施带来压力。部分主机可能会屏蔽 ICMP。

# HISTORY

**fping** 由 Roland Schemers 于 **1992** 年前后在斯坦福大学编写，目的是弥补标准 ping 在网络监控方面的不足。它已成为网络管理员的标准工具，并被收录进大多数 Linux 发行版的软件仓库。

# INSTALL

```apt: sudo apt install fping```

```dnf: sudo dnf install fping```

```pacman: sudo pacman -S fping```

```apk: sudo apk add fping```

```zypper: sudo zypper install fping```

```brew: brew install fping```

```nix: nix profile install nixpkgs#fping```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ping](/man/ping)(8), [nmap](/man/nmap)(1), [hping3](/man/hping3)(8), [mtr](/man/mtr)(8)

# RESOURCES

```[Source code](https://github.com/schweikert/fping)```

```[Homepage](https://fping.org/)```

<!-- verified: 2026-07-15 -->
