# TAGLINE

发送 ARP 请求以发现和测试网络主机

# TLDR

**使用 ARP ping 一台主机**

```sudo arping [192.168.1.1]```

**通过指定接口进行 ping**

```sudo arping -I [eth0] [192.168.1.1]```

**发送指定数量的请求**

```sudo arping -c [5] [192.168.1.1]```

**检测网络中的重复 IP 地址**

```sudo arping -D [192.168.1.1]```

**收到第一个应答后退出**（检查主机是否存活）

```sudo arping -f [192.168.1.1]```

# SYNOPSIS

**arping** [_-c count_] [_-I interface_] [_-D_] _destination_

# DESCRIPTION

**arping** 向目标主机发送 ARP 请求并显示响应。与 ICMP ping 不同，ARP 工作在第 2 层，无法被 IP 防火墙拦截。

该工具可用于验证二层连通性、查找 MAC 地址以及检测网络中的重复 IP 地址。

# PARAMETERS

**-c** _count_
> 在发送 _count_ 个 ARP REQUEST 包后停止。

**-I** _interface_
> 发送 ARP 请求所用的网络接口。

**-D**
> 重复地址检测模式（DAD）。参见 RFC 2131。

**-A**
> ARP 应答模式（免费 ARP 应答）。

**-U**
> 主动 ARP 模式，用于更新邻居的 ARP 缓存。不期待收到应答。

**-b**
> 只发送 MAC 层广播；收到应答后不切换为单播。

**-q**
> 安静模式；不显示任何内容。

**-s** _source_
> ARP 包中使用的源 IP 地址。

**-w** _deadline_
> 超时时间，单位秒，无论已收发多少数据包都会在到期后退出。

**-i** _interval_
> 数据包之间的发送间隔，单位秒。

**-f**
> 收到第一个确认目标存活的应答后退出。

**-V**
> 打印版本信息并退出。

# CAVEATS

需要 root/sudo 权限以访问原始套接字。只能在本网段内工作。无法跨路由器进行 ping。

# HISTORY

**arping** 自 **2000** 年代初以来就以各种形式存在。最常见的实现位于作为 Linux 网络工具一部分维护的 **iputils** 软件包中。Thomas Habets 的另一个独立实现提供了更多功能。

# INSTALL

```apt: sudo apt install arping```

```apk: sudo apk add iputils-arping```

```brew: brew install arping```

```nix: nix profile install nixpkgs#arping```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ping](/man/ping)(8), [arp](/man/arp)(8), [arp-scan](/man/arp-scan)(1), [ip](/man/ip)(8)
