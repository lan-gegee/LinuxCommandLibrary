# TAGLINE

创建指定大小的文件

# TLDR

**创建指定大小的文件**

```mkfile [100m] [filename]```

**创建稀疏文件**

```mkfile -n [1g] [filename]```

**以字节为单位创建文件**

```mkfile [1048576] [filename]```

**创建多个文件**

```mkfile [10m] [file1] [file2]```

**详细输出**

```mkfile -v [100m] [filename]```

# SYNOPSIS

**mkfile** [_options_] _size_ _file_

# PARAMETERS

_SIZE_
> 文件大小（后缀 b、k、m、g）。

_FILE_
> 输出文件名。

**-n**
> 创建稀疏文件。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mkfile** 创建指定大小的文件。它可以创建空文件或稀疏文件。

该工具适用于测试和创建磁盘镜像。稀疏文件不分配全部空间。

# CAVEATS

macOS/Solaris 工具。Linux 使用 truncate/fallocate。稀疏文件支持因平台而异。

# HISTORY

mkfile 起源于 **Solaris**，在 macOS 上同样可用，用于创建任意大小的文件。

# SEE ALSO

[truncate](/man/truncate)(1), [fallocate](/man/fallocate)(1), [dd](/man/dd)(1)
