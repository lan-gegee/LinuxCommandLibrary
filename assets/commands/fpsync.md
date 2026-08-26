# TAGLINE

并行 rsync 同步工具

# TLDR

**同步目录**

```fpsync [source/] [destination/]```

**设置任务数量**

```fpsync -n [4] [source/] [destination/]```

**设置分区大小**

```fpsync -f [1000] [source/] [destination/]```

**详细输出**

```fpsync -v [source/] [destination/]```

**恢复同步**

```fpsync -r [work_dir] [source/] [destination/]```

# SYNOPSIS

**fpsync** [_options_] _source_ _destination_

# PARAMETERS

_SOURCE_
> 源目录。

_DESTINATION_
> 目标目录。

**-n** _JOBS_
> 并发同步任务数（默认为 2）。

**-f** _FILES_
> 每个分区的最大文件数（默认为 2000）。

**-s** _SIZE_
> 分区最大大小（字节，默认为 4096×1024）。

**-v**
> 详细输出（重复使用可输出更多信息）。

**-r** _DIR_
> 从给定的工作目录恢复上一次未完成的运行。

**-w** _DIR_
> 用于存放分区文件和日志文件的工作目录。

**-t** _DIR_
> 临时目录。

**-o** _OPTS_
> 传给底层同步工具（如 rsync）的额外选项。

**-O** _OPTS_
> 传给 **fpart** 的额外选项。

**-m** _TOOL_
> 要使用的同步工具：rsync、cpio 或 tar。

**-d** _DIR_
> 分布式模式（sudo/ssh）使用的共享工作目录。

**-q**
> 队列模式：只生成分区而不执行同步。

**-l**
> 划分分区时使用 **lstat** 而非 **stat**。

**-h**
> 显示帮助信息。

**-V**
> 显示版本信息。

# DESCRIPTION

**fpsync** 通过对源文件划分分区并运行多个 rsync 进程来执行并行 rsync 同步。对于大规模传输，它能获得比单个 rsync 更高的吞吐量。

该工具将源内容切分成多个块，并启动并行 rsync 任务。断点续传能力支持从中断处继续传输。它是 fpart 项目的一部分。

fpsync 通过并行化最大限度地利用带宽，从而优化大文件传输。

# CAVEATS

需要已安装 rsync。并行传输可能使网络或磁盘不堪重负。小文件可能无法从中受益。

# HISTORY

fpsync 是 **fpart** 的一部分，fpart 是一个面向并行操作的文件划分工具。它解决了 rsync 在大规模文件同步中单线程的局限。

# INSTALL

```apt: sudo apt install fpart```

```dnf: sudo dnf install fpart```

```brew: brew install fpart```

```nix: nix profile install nixpkgs#fpart```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [parallel](/man/parallel)(1), [cpio](/man/cpio)(1), [tar](/man/tar)(1)
