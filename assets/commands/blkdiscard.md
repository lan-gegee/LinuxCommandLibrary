# TAGLINE

丢弃存储设备上的扇区

# TLDR

**丢弃**全部扇区

```blkdiscard /dev/device```

**安全**丢弃

```blkdiscard -s /dev/device```

丢弃前 **100 MiB**

```blkdiscard -l 100M /dev/device```

以 **512 MiB** 为步长分次丢弃（避免长时间不可中断的操作）

```blkdiscard -p 512M /dev/device```

# SYNOPSIS

**blkdiscard** [_OPTIONS_] _device_

# DESCRIPTION

**blkdiscard** 向块设备发送 TRIM/DISCARD 命令，将扇区标记为未使用。与 **fstrim**(8) 不同，它直接作用于块设备而非已挂载的文件系统。这对 SSD 和精简配置（thinly-provisioned）存储尤其有用。被丢弃区域中的所有数据都会丢失。

# PARAMETERS

**-o, --offset** _offset_
> 开始丢弃的字节偏移量。必须按设备扇区大小对齐。默认为 0。

**-l, --length** _size_
> 从偏移量起要丢弃的字节数。必须按设备扇区大小对齐。

**-p, --step** _size_
> 每次迭代只丢弃这么多字节，而非一次性完成。有助于避免在大设备上出现长时间不可中断的操作。

**-s, --secure**
> 执行安全丢弃。这会让设备同时擦除被弃数据的任何副本（例如垃圾回收中的副本）。需要设备支持。

**-z, --zeroout**
> 将指定区域填零，而不是丢弃。

**-f, --force**
> 禁用独占打开检查，允许对已挂载的设备操作。请谨慎使用。

**-q, --quiet**
> 抑制警告消息。

**-v, --verbose**
> 打印对齐后的偏移量和长度值以及进度信息。

# CAVEATS

此操作会破坏数据且不可逆。被丢弃区域中的所有数据都将丢失。并非所有设备都支持丢弃操作；在不支持的设备上，blkdiscard 以状态码 2 退出（自 util-linux 2.39 起）。安全丢弃需要明确的硬件支持，并且在某些设备上未必比普通丢弃提供更强的保证。

# HISTORY

**blkdiscard** 是 **util-linux** 软件包的一部分，提供 SSD 优化和安全擦除功能。

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

[fstrim](/man/fstrim)(8), [hdparm](/man/hdparm)(8), [wipefs](/man/wipefs)(8), [blkid](/man/blkid)(8)
