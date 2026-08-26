# TAGLINE

以类似 vmstat/iostat 的格式报告网络接口带宽

# TLDR

显示所有接口的统计信息，每**秒**更新一次

```ifstat```

每**5 秒**显示一次统计信息

```ifstat [5]```

以 **kbits/sec** 而非 kbytes/sec 报告带宽

```ifstat -b```

只监控**指定接口**

```ifstat -i [eth0],[wlan0]```

显示所有接口的**总带宽**

```ifstat -T```

忽略历史记录并显示**绝对计数**

```ifstat -a```

# SYNOPSIS

**ifstat** [_options_] [_delay_[/_delay2_] [_count_]]

# PARAMETERS

**-a**
> 忽略历史文件，显示自启动以来的绝对计数

**-b**
> 以 kbits/sec 而非 kbytes/sec 报告带宽

**-e**
> 显示错误

**-i** _IFACE_
> 只监控指定的接口（逗号分隔）

**-l**
> 启用对环回接口的监控

**-n**
> 关闭周期性显示的表头

**-r**
> 重置历史记录

**-S**
> 统计数据保持在同一行（不滚动）

**-T**
> 显示所有被监控接口的总带宽

**-t**
> 在每行开头添加时间戳

**-w**
> 使用固定宽度的列

**-z**
> 隐藏计数为零的接口

# DESCRIPTION

**ifstat** 报告网络接口的带宽，就像 vmstat/iostat 对其他系统计数器所做的那样。它在多次调用之间保留历史记录，默认显示自上次调用以来的差值。

位置参数 _delay_ 设置更新间隔，单位为秒（默认 1）。可选的 _count_ 限制更新次数。还可以用一个斜杠分隔的第二个延迟值来交替间隔。

注意：有两个不同的工具共用 ifstat 这个名字。这里描述的是最常见的独立版本（section 1）。iproute2 版本（section 8）的选项不同。

# CAVEATS

统计依赖于内核接口计数器。极高的流量速率可能导致旧系统上的 32 位计数器溢出。iproute2 的 ifstat(8) 与独立的 ifstat(1) 标志不同。

# INSTALL

```apt: sudo apt install ifstat```

```dnf: sudo dnf install ifstat```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2```

```zypper: sudo zypper install iproute2```

```brew: brew install ifstat```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [netstat](/man/netstat)(8), [iftop](/man/iftop)(8), [vmstat](/man/vmstat)(8)
