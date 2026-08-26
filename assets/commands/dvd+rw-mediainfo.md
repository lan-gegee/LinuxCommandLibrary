# TAGLINE

显示 DVD 盘片信息

# TLDR

**显示盘片信息**

```dvd+rw-mediainfo [/dev/dvd]```

# SYNOPSIS

**dvd+rw-mediainfo** _device_

# PARAMETERS

_DEVICE_
> DVD/BD 驱动器设备路径（例如 /dev/dvd、/dev/sr0）。

# DESCRIPTION

**dvd+rw-mediainfo** 显示当前位于驱动器中的光盘介质（DVD/BD）以及驱动器本身的详细信息。它会报告盘片类型、容量、booktype、写入速度和当前使用状态。

输出包括制造商信息、盘片状态（空白、可追加、已完成）以及双层盘片的层信息。这有助于在刻录前确认盘片兼容性和可用容量。它在调试时尤其有用，报告 dvd+rw-tools 的 bug 时应附上其输出。

此程序不接受设备路径之外的任何命令行选项。

# CAVEATS

大多数信息需要驱动器中装有盘片。某些信息取决于驱动器的能力。访问设备可能需要 root 权限。

# HISTORY

dvd+rw-mediainfo 是 **dvd+rw-tools** 的一部分，提供在 Linux 系统上进行 DVD 制作和刻录所必需的盘片分析能力。

# INSTALL

```apt: sudo apt install dvd+rw-tools```

```dnf: sudo dnf install dvd+rw-tools```

```pacman: sudo pacman -S dvd+rw-tools```

```apk: sudo apk add dvd+rw-tools```

```zypper: sudo zypper install dvd+rw-tools```

```brew: brew install dvd+rw-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvd+rw-booktype](/man/dvd+rw-booktype)(1), [growisofs](/man/growisofs)(1), [cdrecord](/man/cdrecord)(1)
