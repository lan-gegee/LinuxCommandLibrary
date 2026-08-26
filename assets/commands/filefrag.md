# TAGLINE

报告文件的碎片化程度

# TLDR

显示文件的**碎片化报告**

```filefrag [path/to/file1] [path/to/file2]```

以 **1024 字节**块大小生成报告

```filefrag -k [path/to/file]```

以**指定**块大小生成报告

```filefrag -b[1024|1K|1M|1G] [path/to/file]```

请求映射前先**同步**文件

```filefrag -s [path/to/file1] [path/to/file2]```

显示带 extent 详情的**详细**报告

```filefrag -v [path/to/file1] [path/to/file2]```

显示**扩展属性**的映射

```filefrag -x [path/to/file1] [path/to/file2]```

以**十六进制**显示 extent 块号

```filefrag -X [path/to/file]```

打印**版本**号

```filefrag -V```

# SYNOPSIS

**filefrag** [**-b** _blocksize_] [**-BeEkPsvVxX**] [_files..._]

# DESCRIPTION

**filefrag** 报告某个文件碎片化的严重程度。它显示每个文件的 extent（连续区块）数量，以此反映碎片化水平：只有 1 个 extent 的文件没有碎片；extent 越多说明碎片越严重。

可用于找出那些做碎片整理会有收益的文件。

# PARAMETERS

**-b** _blocksize_
> 指定输出使用的块大小，单位为字节，也可带 [KMG] 后缀，上限 1GB，用它代替文件系统的块大小。未指定块大小时默认为 1024 字节。必须紧跟在 -b 之后书写，中间不能有空格。

**-B**
> 为便于测试，强制使用较旧的 FIBMAP ioctl 而不是 FIEMAP ioctl。

**-e**
> 即使对按块映射的文件，也以 extent 格式打印输出。

**-E**
> 显示 ext4 extent 状态缓存的内容。仅在 ext4 文件系统上受支持。

**-k**
> 输出时使用 1024 字节的块大小（等同 '-b1024'）。

**-P**
> 预加载该文件的 ext4 extent 状态缓存。仅在 ext4 文件系统上受支持。

**-s**
> 在请求映射之前先同步文件。

**-v**
> 检查文件碎片时输出详细信息。

**-V**
> 打印程序和库的版本号。若给出两次，还会打印当前版本所能理解的 FIEMAP 标志。

**-x**
> 显示扩展属性的映射。

**-X**
> 以十六进制格式显示 extent 块号。

# CAVEATS

属于 e2fsprogs。在 ext2/ext3/ext4 上效果最好，但也能通过 FIEMAP ioctl 支持其他文件系统。-E 和 -P 选项为 ext4 专属，并非所有内核都支持。

# INSTALL

```apt: sudo apt install e2fsprogs```

```dnf: sudo dnf install e2fsprogs```

```pacman: sudo pacman -S e2fsprogs```

```apk: sudo apk add e2fsprogs-extra```

```zypper: sudo zypper install e2fsprogs```

```brew: brew install e2fsprogs```

```nix: nix profile install nixpkgs#e2fsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[e4defrag](/man/e4defrag)(8), [debugfs](/man/debugfs)(8), [fsck](/man/fsck)(8)
