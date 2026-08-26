# TAGLINE

SSD TRIM 命令发送工具

# TLDR

对**所有**已挂载分区执行 TRIM

```sudo fstrim -a```

对**特定**分区执行 TRIM

```sudo fstrim /```

带**详细输出**执行 TRIM

```sudo fstrim -v /```

# SYNOPSIS

**fstrim** [_OPTIONS_] _mountpoint_

# DESCRIPTION

**fstrim** 丢弃已挂载文件系统上未使用的块，向底层存储设备发送 TRIM 命令。这对 SSD 和闪存设备尤其有用，可以维持性能并延长设备寿命。

# PARAMETERS

**-a, --all**
> 对所有支持 discard 的已挂载文件系统执行 TRIM。

**-v, --verbose**
> 显示丢弃的字节数。

**-n, --dry-run**
> 只打印将执行的操作而不实际执行 TRIM。

**-o, --offset** _offset_
> 文件系统中开始 TRIM 的字节偏移。

**-l, --length** _length_
> 从偏移处起要 TRIM 的字节数。

**-m, --minimum** _size_
> 要 TRIM 的最小连续空闲区间。

# CAVEATS

仅对底层存储支持 discard 的文件系统有效（大多数 SSD、NVMe、精简配置设备）。过于频繁地运行没有收益；通常的做法是通过 **fstrim.timer** systemd 单元安排每周运行。挂载选项中的持续 **discard** 是另一种选择，但通常不如周期性 **fstrim** 高效。

# HISTORY

**fstrim** 是 **util-linux** 软件包的一部分，为 Linux 系统上的 SSD 优化提供 TRIM 支持。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add fstrim```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blkdiscard](/man/blkdiscard)(8), [mount](/man/mount)(8)
