# TAGLINE

系统级事件捕获与分析

# TLDR

从运行中的系统**捕获**所有事件

```sysdig```

将事件**保存**到文件

```sysdig -w [path/to/file].scap```

从文件**读取**事件

```sysdig -r [path/to/file].scap```

按进程和事件类型**过滤**事件

```sysdig proc.name=cat and evt.type=open```

**列出**可用的 chisel

```sysdig -cl```

**使用** chisel 分析流量

```sysdig -c spy_ip [ip_address]```

# SYNOPSIS

**sysdig** [_options_] [_filter_]

# PARAMETERS

**-w, --write _file_**
> 将捕获的事件写入文件

**-r, --read _file_**
> 从文件读取事件

**-c, --chisel _name_**
> 运行指定的 chisel

**-cl, --list-chisels**
> 列出可用的 chisel

**-l, --list**
> 列出可用字段

**-I _source_**
> 使用指定的输入源

**-n _num_**
> 在 num 个事件后停止

**-p _format_**
> 自定义输出格式

**-j, --json**
> 以 JSON 格式输出

**-A, --print-ascii**
> 以 ASCII 打印事件缓冲区（跳过不可打印字节）。

**-X, --print-hex-ascii**
> 以十六进制 + ASCII 打印事件缓冲区。

**-s** _len_, **--snaplen** _len_
> 捕获每个 I/O 缓冲区的前 _len_ 字节（默认 80）。

**-pc**, **-pcontainer**
> 使用容器感知的输出格式（主机 + container.id、container.name）。

**-M** _seconds_
> 在给定秒数后停止捕获。

**--list-fields**
> 列出所有可用的过滤/格式化字段。

# DESCRIPTION

**sysdig** 是一个系统级探索与故障排查工具。它捕获系统调用和事件，提供对系统行为的深入可见性。它支持过滤、chisel（用于分析的 Lua 脚本）以及多种输出格式。

Sysdig 可用于性能分析、安全监控和调试。

# FILTER SYNTAX

过滤器使用 **field=value** 语法，支持 AND、OR 和 NOT 运算符：
- proc.name=nginx
- evt.type=open and fd.name contains /etc
- container.id!=host

# CAVEATS

实时捕获需要 root 权限。某些特性可能需要内核头文件。在繁忙的系统上会产生大量数据。

# INSTALL

```pacman: sudo pacman -S sysdig```

```zypper: sudo zypper install sysdig```

```brew: brew install sysdig```

```nix: nix profile install nixpkgs#sysdig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strace](/man/strace)(1), [tcpdump](/man/tcpdump)(8), [perf](/man/perf)(1)
