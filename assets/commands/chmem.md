# TAGLINE

配置内存热插拔状态

# TLDR

**将内存块置于离线**

```sudo chmem -b -d [block_number]```

**将内存块置于在线**

```sudo chmem -b -e [block_number]```

**将内存范围置于离线**

```sudo chmem -d 0x[start_address]-0x[end_address]```

**将内存范围置于在线**

```sudo chmem -e 0x[start_address]-0x[end_address]```

**将内存置入特定 zone 并上线**

```sudo chmem -e 0x[start_address] -z [Movable]```

# SYNOPSIS

**chmem** [_options_] _size_|_range_|_block_

# DESCRIPTION

**chmem** 修改 Linux 系统中内存块的状态，将其置于在线或离线。这主要用于虚拟化环境中的内存热插拔操作。

内存块是可单独管理的物理内存片段。该工具无需重启即可实现动态内存管理。

# PARAMETERS

**-b, --block**
> 按块编号操作内存块

**-d, --disable**
> 将内存置于离线

**-e, --enable**
> 将内存置于在线

**-z, --zone** _zone_
> 将内存分配到特定的 zone（DMA、DMA32、Normal、Movable）

**-h, --help**
> 显示帮助

# CAVEATS

需要 root 权限。并非所有系统都支持内存热插拔。包含内核数据或正在使用的页面的内存无法离线。虚拟机可能需要特定配置才能支持内存热插拔。

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

[lsmem](/man/lsmem)(1), [free](/man/free)(1)
