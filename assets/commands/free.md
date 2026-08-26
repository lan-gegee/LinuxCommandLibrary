# TAGLINE

显示内存使用统计

# TLDR

显示**系统内存**

```free```

以**人类可读**的单位显示内存

```free -h```

以**兆字节**为单位显示内存

```free -m```

以**吉字节**为单位显示内存

```free -g```

每 2 秒**刷新**一次输出

```free -s 2```

显示**合计**行

```free -t```

以**宽表**输出并分开显示 buffers 与 cache

```free -hw```

每 2 秒重复输出一次，共 **5 次**

```free -s 2 -c 5```

# SYNOPSIS

**free** [_-b_|_-k_|_-m_|_-g_] [_-h_] [_-s delay_] [_-c count_] [_-t_]

# DESCRIPTION

**free** 显示系统中空闲和已使用的物理内存与交换空间总量，以及内核占用的 buffers 和 cache。这些信息来自 /proc/meminfo。

# PARAMETERS

**-b**
> 以字节为单位显示。

**-k**
> 以千字节为单位显示（默认）。

**-m**
> 以兆字节为单位显示。

**-g**
> 以吉字节为单位显示。

**-h, --human**
> 以人类可读的带单位格式显示。

**-s, --seconds delay**
> 每隔 delay 秒连续显示一次输出。

**-c, --count count**
> 显示 count 次后停止（与 -s 配合使用）。

**-t, --total**
> 显示一行合计信息。

**-w, --wide**
> 宽表输出（将 buffers 与 cache 分开显示）。

**-l, --lohi**
> 显示详细的低位与高位内存统计。

# CAVEATS

"available"（可用）内存列（在 Linux 3.14 中加入）能更准确地估算可用于启动新应用的内存量。"free"（空闲）内存没有把可以释放的 buffers/cache 计算在内。

# HISTORY

属于 **procps**（或 procps-ng）软件包，该包为 Linux 提供进程监控工具。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[top](/man/top)(1), [htop](/man/htop)(1), [vmstat](/man/vmstat)(8), [sar](/man/sar)(1)
