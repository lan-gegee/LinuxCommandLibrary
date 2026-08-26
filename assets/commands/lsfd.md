# TAGLINE

列出 Linux 上运行中进程所打开文件的信息

# TLDR

列出**所有打开的文件**

```lsfd```

按**进程 ID** 列出文件

```lsfd -Q 'PID == [pid]'```

查找**打开了某文件**的进程

```lsfd -Q "NAME == '[path/to/file]'"```

列出**特定 PID** 的文件（高效）

```lsfd -p [pid]```

列出 **IPv4 套接字**

```lsfd -i4```

列出 **IPv6 套接字**

```lsfd -i6```

以**指定列**列出

```lsfd -o COMMAND,PID,TYPE,NAME```

# SYNOPSIS

**lsfd** [_options_]

# DESCRIPTION

**lsfd** 列出 Linux 上运行中进程所打开文件描述符的信息。它是 lsof 的现代化替代品，仅面向 Linux，性能更好，并支持用类 SQL 的查询语言进行过滤。属于 util-linux。

# PARAMETERS

**-p, --pid** _PIDS_
> 只收集指定进程的信息（比 -Q 更高效）。

**-Q, --filter** _EXPR_
> 用表达式过滤输出（如 'PID == 1234'、"NAME == '/path'"）。

**-l, --threads**
> 按线程级别列出。

**-i4**
> 仅显示 IPv4 套接字。

**-i6**
> 仅显示 IPv6 套接字。

**-o, --output** _COLUMNS_
> 指定输出的列（用 -H 可列出可用列）。

**-r, --raw**
> 使用原始输出格式。

**-J, --json**
> 以 JSON 格式输出。

**-n, --noheadings**
> 不显示列标题。

**-u, --notruncate**
> 不截断列中的文本。

**-H, --list-columns**
> 列出可用的输出列。

**--summary**[=_WHEN_]
> 打印汇总信息（only、append 或 never）。

# CAVEATS

属于 util-linux 软件包。完整功能需要 Linux 5.12 及以上版本。过滤语法与 lsof 不同。按 PID 过滤时使用 **-p** 比 **-Q** 更高效。列名在未来版本中可能变化。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsof](/man/lsof)(8), [fuser](/man/fuser)(1), [ss](/man/ss)(8)
