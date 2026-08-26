# TAGLINE

报告 btrfs 文件系统的压缩率

# TLDR

计算文件或目录的**压缩率**

```sudo compsize [path/to/file_or_directory]```

不跨过**文件系统边界**

```sudo compsize -x [path/to/file_or_directory]```

显示**原始字节数**而非人类可读的大小

```sudo compsize -b [path/to/file_or_directory]```

# SYNOPSIS

**compsize** [**-b**] [**-x**] _file-or-dir_ [_file-or-dir_...]

# DESCRIPTION

**compsize** 是一款专为 btrfs 文件系统打造的实用工具，可报告透明文件系统压缩的详细统计信息。Btrfs 支持多种压缩算法（zlib、lzo、zstd），可以对数据进行即时压缩，而 compsize 能揭示相对于表面上的未压缩文件大小，实际节省了多少空间。

该工具通过检查 btrfs extent 元数据来确定逻辑大小（应用程序所看到的）和实际占用的物理磁盘空间。它会按压缩类型细分结果，展示哪种算法达到了怎样的压缩比。这对于评估压缩是否物有所值极为有用，因为某些文件类型（已压缩的图片、视频）可能几乎没有收益，甚至可能浪费 CPU 周期。

运行 compsize 需要 root 权限，因为它需要通过 btrfs ioctl 对文件系统 extent 信息进行底层访问。结果通常显示总字节数、压缩后的字节数以及以百分比表示的压缩率。该工具可以针对单个文件、目录或整个子卷运行，有助于找出文件系统中从压缩中受益最大的部分。

# PARAMETERS

**-x, --one-file-system**
> 不跨越文件系统边界

**-b, --bytes**
> 显示原始字节数

# CAVEATS

仅适用于 btrfs 文件系统。需要 root 权限才能访问 extent 信息。结果取决于文件内容和压缩算法。

# INSTALL

```apt: sudo apt install btrfs-compsize```

```dnf: sudo dnf install compsize```

```pacman: sudo pacman -S compsize```

```apk: sudo apk add btrfs-compsize```

```zypper: sudo zypper install compsize```

```nix: nix profile install nixpkgs#compsize```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-filesystem](/man/btrfs-filesystem)(8), [df](/man/df)(1), [du](/man/du)(1)
