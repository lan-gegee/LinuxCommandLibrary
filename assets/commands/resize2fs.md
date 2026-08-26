# TAGLINE

调整 ext2/ext3/ext4 文件系统大小

# TLDR

调整到**最大**可能大小

```sudo resize2fs /dev/sdXN```

以进度显示调整到**指定大小**

```sudo resize2fs -p /dev/sdXN 40G```

**收缩**到最小可能大小

```sudo resize2fs -M /dev/sdXN```

即使检测到错误也**强制**调整大小

```sudo resize2fs -f /dev/sdXN```

# SYNOPSIS

**resize2fs** [_-fFpPMbs_] [_-d debug-flags_] [_-S RAID-stride_] _device_ [_size_]

# DESCRIPTION

**resize2fs** 用于调整 ext2、ext3 或 ext4 文件系统的大小。它可以增长或收缩文件系统。注意它不会调整底层分区；请使用分区工具完成该操作。

# PARAMETERS

**-b**
> 启用 64 位块号

**-d DEBUG-FLAGS**
> 启用调试输出

**-f**
> 即使有错误也强制调整大小

**-F**
> 调整前刷新缓冲区缓存

**-M**
> 收缩到最小大小

**-p**
> 显示进度条

**-P**
> 打印最小大小并退出

**-s**
> 禁用 64 位块号

**-S STRIDE**
> 指定 RAID stride 以优化布局

# SIZE UNITS

大小可以指定为块数，或使用后缀：
**s**：512 字节扇区
**K**：千字节
**M**：兆字节
**G**：吉字节

# CAVEATS

收缩文件系统要求其已卸载。对 ext3/ext4 而言，增长文件系统通常可以在挂载状态下进行（在线调整）。增长前或收缩后务必先调整分区大小。

# HISTORY

**resize2fs** 是 **e2fsprogs** 的一部分。在线调整大小的能力在 ext3 中加入并在 ext4 中得到改进。

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

[e2fsck](/man/e2fsck)(8), [tune2fs](/man/tune2fs)(8), [fdisk](/man/fdisk)(8), [parted](/man/parted)(8)
