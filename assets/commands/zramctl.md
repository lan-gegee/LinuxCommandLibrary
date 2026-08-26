# TAGLINE

设置和控制 zram 设备

# TLDR

**检查** zram 是否已启用

```lsmod | grep -i zram```

**启用** zram，设备数量动态确定

```sudo modprobe zram```

**启用** zram 并固定为 2 个设备

```sudo modprobe zram num_devices=2```

**查找**并初始化下一个空闲的 zram 设备

```sudo zramctl -f -s 2GB -a lz4```

**列出**当前已初始化的设备

```sudo zramctl```

# SYNOPSIS

**zramctl** [_options_] [_zram-device_]

# PARAMETERS

**-f, --find**
> 查找并初始化下一个空闲的 zram 设备

**-s, --size _size_**
> 设置 zram 设备的大小

**-a, --algorithm _alg_**
> 设置压缩算法（lz4、lzo、zstd 等）

**-t, --streams _number_**
> 设置压缩流的数量

**-r, --reset**
> 重置设备

**-o, --output _list_**
> 定义输出的列

**--raw**
> 原始输出格式

**-n, --no-headings**
> 不打印列标题

# DESCRIPTION

**zramctl** 用于设置和控制 zram 设备，即基于内存的压缩块设备。zram 适合用来创建压缩交换空间或临时文件系统，提高内存使用效率。

用 zramctl 创建 zram 设备后，可以用 **mkswap** 和 **swapon** 将其作为交换空间，或用 **mkfs** 在其上创建文件系统。

# CAVEATS

需要 zram 内核模块。可用的压缩算法因内核版本而异。zram 交换空间能改善内存受限系统的性能，但要用 CPU 进行压缩。属于 util-linux 软件包的一部分。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkswap](/man/mkswap)(8), [swapon](/man/swapon)(8), [free](/man/free)(1), [lsblk](/man/lsblk)(8)
