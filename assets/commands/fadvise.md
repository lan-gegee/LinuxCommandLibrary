# TAGLINE

文件缓存行为控制工具

# TLDR

**提示**文件即将被使用（预加载进缓存）

```fadvise -a willneed [path/to/file]```

**提示从缓存中丢弃**文件（默认建议）

```fadvise [path/to/file]```

对指定的字节范围**应用建议**

```fadvise -a sequential -o [offset] -l [length] [path/to/file]```

对已打开的文件描述符**应用建议**

```fadvise -a dontneed -d [fd]```

显示**帮助**

```fadvise -h```

# SYNOPSIS

**fadvise** [_options_] _file_

**fadvise** [_options_] **-d** _file-descriptor_

# DESCRIPTION

**fadvise** 是 **posix_fadvise**(2) 系统调用的简单封装。它向内核提供应用程序打算如何访问文件的提示，使内核得以优化 I/O 行为和页缓存的使用。

适用于在大量读取工作之前预加载文件，或在一次性顺序读取之后丢弃页缓存。

# PARAMETERS

**-a, --advice** _advice_
> 缓存建议。可选值：**normal**、**sequential**、**random**、**noreuse**、**willneed**、**dontneed**。默认为 **dontneed**。

**-d, --fd** _fd_
> 对给定的已打开文件描述符而非路径应用建议。

**-o, --offset** _offset_
> 起始字节偏移量（默认 0）。

**-l, --length** _length_
> 应用建议的字节数（0 表示整个文件，为默认值）。

**-h, --help**
> 显示帮助信息。

**-V, --version**
> 显示版本信息。

# CAVEATS

属于 util-linux。建议只是给内核的提示，不是命令。实际行为取决于系统的内存压力。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fincore](/man/fincore)(1), [vmtouch](/man/vmtouch)(1)
