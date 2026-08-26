# TAGLINE

缩小或扩展文件大小

# TLDR

**将文件设为指定大小**（不存在时创建）

```truncate -s [100M] [file]```

清空文件（大小设为 0）

```truncate -s 0 [file]```

将文件缩小指定数量

```truncate -s -[10K] [file]```

将文件扩大指定数量

```truncate -s +[50M] [file]```

将文件设为与另一文件相同的大小

```truncate -r [reference_file] [target_file]```

创建特定大小的稀疏文件

```truncate -s [1G] [sparse_file]```

# SYNOPSIS

**truncate** [_-c_] [_-o_] **-s** _SIZE_ _FILE..._

**truncate** [_-c_] [_-o_] **-r** _RFILE_ _FILE..._

# PARAMETERS

**-s** _SIZE_, **--size**=_SIZE_
> 将文件大小设置或调整为 SIZE 字节

**-c**, **--no-create**
> 不创建不存在的文件

**-o**, **--io-blocks**
> 将 SIZE 视为 IO 块数而非字节数

**-r** _RFILE_, **--reference**=_RFILE_
> 以 RFILE 的大小作为参考大小

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# SIZE SUFFIXES

SIZE 可以使用以下后缀：

**K** - 千字节 (1024 字节)

**M** - 兆字节 (1024 K)

**G** - 吉字节 (1024 M)

**T** - 太字节 (1024 G)

**KB** - 1000 字节

**MB** - 1000 KB

**GB** - 1000 MB

SIZE 还可以加 **+** 前缀表示增加，或 **-** 前缀表示减少相应数量。

# DESCRIPTION

**truncate** 将每个 FILE 的大小缩小或扩展到指定大小。如果 FILE 不存在，则创建它。如果 FILE 比指定大小大，多余的数据会丢失。如果 FILE 更短，则用零字节扩展（在大多数文件系统上会形成稀疏文件）。

该命令适用于：创建特定大小的测试文件；在不删除日志文件的情况下清空其内容（保留权限和所有者）；以及为磁盘镜像分配或数据库预分配创建稀疏文件。

截断文件时，超出新大小的数据会永久丢失。扩展文件时会形成稀疏文件——扩展部分在被写入数据之前并不实际占用磁盘空间。

# CAVEATS

截断正被其他进程写入的文件可能导致数据损坏或应用错误。在保持所有权和权限的同时清空文件，**-s 0** 操作比先 **rm** 再 **touch** 更快。稀疏文件行为取决于文件系统；并非所有文件系统都支持稀疏文件。扩展区域读取时表现为零，但复制到不支持稀疏文件的系统上可能消耗实际空间。

# HISTORY

**truncate** 命令是 **GNU Coreutils** 的一部分，多年来一直可在 Linux 系统上使用。底层的 **ftruncate()** 系统调用自 POSIX 诞生之初就已存在，但这个命令行工具为该功能提供了便捷的访问方式。BSD 系统上存在语法略有不同的类似 **truncate** 命令。GNU 版本已成为大多数 Linux 发行版的标准。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [fallocate](/man/fallocate)(1), [touch](/man/touch)(1), [stat](/man/stat)(1), [rm](/man/rm)(1)
