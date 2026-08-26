# TAGLINE

创建压缩文件系统树

# TLDR

**压缩目录树**

```mkzftree [input/] [output/]```

**设置压缩级别**（1-9，默认 9）

```mkzftree -z [6] [input/] [output/]```

**强制**压缩每个文件（即使压缩后更大）

```mkzftree -f [input/] [output/]```

**详细输出**

```mkzftree -v [input/] [output/]```

用 N 个线程**并行**压缩

```mkzftree -p [4] [input/] [output/]```

将 zisofs 树**解压**回普通文件

```mkzftree -u [input/] [output/]```

# SYNOPSIS

**mkzftree** [_options_] _input_ _output_

# PARAMETERS

_INPUT_
> 源目录（使用 **-F** 时可以是单个文件）。

_OUTPUT_
> 目标目录/文件。

**-z**, **--level** _LEVEL_
> 压缩级别 1-9（默认：9）。越低越快，越高压缩率越大。

**-f**, **--force**
> 总是压缩，即使结果比原始文件更大。

**-u**, **--uncompress**
> 解压先前已压缩的树。

**-p**, **--parallelism** _N_
> 并行压缩线程数。

**-F**, **--file**
> 将 INPUT 视为单个文件而不是目录树。

**-x**, **--one-filesystem**
> 不跨越文件系统边界；在挂载点创建目录占位。

**-X**, **--strict-one-filesystem**
> 不跨越文件系统边界且不创建占位目录。

**-l**, **--local**
> 不递归进入子目录（仍会创建这些目录）。

**-s**, **--sloppy**
> 放宽对文件模式、时间和所有权的保留要求。

**-v**, **--verbose**
> 增加输出详细程度。

**-q**, **--quiet**
> 抑制包括错误在内的所有消息。

**-h**, **--help**
> 显示帮助信息。

**-w**, **--version**
> 显示版本信息。

# DESCRIPTION

**mkzftree** 创建适合在 ISO 9660（zisofs）文件系统上进行透明解压的压缩目录树。输出树中的文件逐个用 zlib 压缩，并保留目录结构。

这些压缩树设计为配合带 `-z` 选项的 **mkisofs**（或 **genisoimage**）使用，以创建这样的 ISO 镜像：在支持 zisofs 的 Linux 系统上读取时文件会被透明解压。

# CAVEATS

属于 **zisofs-tools** 的一部分。透明解压需要 Linux 内核支持 zisofs。只对创建 ISO 9660 文件系统有用；不是通用压缩工具。

# HISTORY

mkzftree 是 **zisofs-tools** 的一部分，用于在 ISO9660 文件系统上实现透明压缩。

# INSTALL

```apt: sudo apt install genisoimage```

```dnf: sudo dnf install genisoimage```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkisofs](/man/mkisofs)(1), [genisoimage](/man/genisoimage)(1)
