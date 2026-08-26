# TAGLINE

读取 OpenWrt 及类似嵌入式 Linux 系统上 logd 的环形缓冲区日志

# TLDR

**打印**所有日志消息

```logread```

实时**跟踪**日志输出

```logread -f```

打印**最后 N 条**消息

```logread -l [50]```

按模式**过滤**消息

```logread -e [pattern]```

按 syslog 优先级**过滤**

```logread -p [daemon.info]```

打印日志并**跟踪**新消息

```logread -f -e [error]```

# SYNOPSIS

**logread** [_options_]

# DESCRIPTION

**logread** 读取 OpenWrt 及类似嵌入式 Linux 系统上 logd 的环形缓冲区日志，提供对存储在内存中（而非磁盘上）的系统消息的访问。

# PARAMETERS

**-f**
> 实时跟踪日志输出（类似 tail -f）。

**-l** _N_
> 只打印最后 N 条消息。

**-e** _PATTERN_
> 过滤匹配关键字或模式的消息。

**-p** _FACILITY.LEVEL_
> 按 syslog facility 和优先级过滤（如 kern.err、daemon.info）。

**-t**
> 为每条消息附带人类可读的时间戳。

**-h**
> 显示帮助信息。

# CAVEATS

特定于 OpenWrt 和基于 BusyBox 的系统。环形缓冲区容量有限；较旧的消息会被覆盖。

# INSTALL

```apk: sudo apk add logbookd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmesg](/man/dmesg)(1), [journalctl](/man/journalctl)(1), [logger](/man/logger)(1)
