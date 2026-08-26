# TAGLINE

显示套接字统计信息与连接

# TLDR

显示所有 **TCP/UDP/RAW/UNIX 套接字**

```ss -a -t```

显示所有处于**监听**状态的套接字

```ss -l```

显示带**进程**信息的所有 TCP 套接字

```ss -tp```

显示连接到本地 **HTTPS 端口**的所有 TCP 套接字

```ss -t src :443```

显示在 8080 端口上**监听**的所有 TCP 套接字

```ss -lt src :8080```

显示已**建立（established）**的 SSH 连接

```ss -o state established '( dport = :ssh or sport = :ssh )'```

**杀死**一个套接字连接

```ss -K dst 192.168.1.1 dport = 22```

打印**汇总**统计信息

```ss -s```

# SYNOPSIS

**ss** [_options_] [_FILTER_]

# DESCRIPTION

**ss** 用于转储套接字统计信息。它显示的信息与 netstat 类似，但能比其他工具呈现更多的 TCP 和状态信息。它直接从内核空间获取套接字信息，因此比 netstat 更快。

# PARAMETERS

**-h, --help**
> 显示选项摘要

**-a, --all**
> 同时显示监听和非监听状态的套接字

**-l, --listening**
> 只显示监听状态的套接字

**-n, --numeric**
> 不解析服务名；以数字形式显示端口

**-r, --resolve**
> 尝试解析数字地址/端口

**-p, --processes**
> 显示使用套接字的进程

**-t, --tcp**
> 显示 TCP 套接字

**-u, --udp**
> 显示 UDP 套接字

**-x, --unix**
> 显示 Unix 域套接字

**-w, --raw**
> 显示原始（raw）套接字

**-4, --ipv4**
> 仅显示 IPv4 套接字

**-6, --ipv6**
> 仅显示 IPv6 套接字

**-o, --options**
> 显示定时器信息

**-e, --extended**
> 显示详细的套接字信息（UID、inode、cookie）

**-m, --memory**
> 显示套接字内存占用

**-i, --info**
> 显示 TCP 内部信息

**-K, --kill**
> 强制关闭套接字

**-s, --summary**
> 打印汇总统计信息

**-E, --events**
> 持续显示正在被销毁的套接字

**-N, --net=NSNAME**
> 切换到指定的网络命名空间

# CAVEATS

状态过滤支持 TCP 状态（established、syn-sent、syn-recv、fin-wait-1、fin-wait-2、time-wait、closed、close-wait、last-ack、listening、closing）和元状态（all、connected、synchronized、bucket）。**-K** 选项需要相应权限。

# HISTORY

**ss** 是 **iproute2** 软件包的一部分，作为 **netstat** 的现代替代品而开发。它直接读取内核 netlink 套接字而非解析 /proc 文件，因而性能更快。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2-ss```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [netstat](/man/netstat)(8), [lsof](/man/lsof)(8)
