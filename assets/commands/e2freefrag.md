# TAGLINE

分析 ext 文件系统空闲空间碎片

# TLDR

检查**空闲空间碎片**

```e2freefrag [/dev/sdXN]```

以指定**块大小**检查

```e2freefrag -c [chunk_size_in_kb] [/dev/sdXN]```

# SYNOPSIS

**e2freefrag** [_options_] _device_

# DESCRIPTION

**e2freefrag** 打印 ext2/ext3/ext4 文件系统的空闲空间碎片信息。它以直方图形式显示有多少空闲块可作为连续且对齐的空闲空间使用。

该工具分析文件系统的空闲空间分布，报告关于块大小及其出现频率的统计信息。这些信息有助于评估文件系统健康状况，并判断碎片整理是否能提升性能。

可用于识别可能影响顺序 I/O 性能的碎片模式，对于存在大文件或数据库负载的系统尤其有用。

# PARAMETERS

**-c** _chunk_kb_
> 报告给定大小（KB）的空闲块数量。必须是 2 的幂且大于文件系统块大小。

**-h**
> 显示用法信息。

_device_
> 要分析的文件系统设备（例如 **/dev/sda1**）。

# CAVEATS

为获得准确结果，文件系统应处于卸载状态或以只读方式挂载。属于 e2fsprogs 软件包。

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

[e4defrag](/man/e4defrag)(8), [dumpe2fs](/man/dumpe2fs)(8), [e2fsck](/man/e2fsck)(8), [debugfs](/man/debugfs)(8), [tune2fs](/man/tune2fs)(8)
