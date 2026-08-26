# TAGLINE

检查或设置 DVD-RAM 盘片的特性

# TLDR

**显示 DVD-RAM 盘片的当前设置**

```dvd-ram-control [/dev/dvd]```

**使盘片变为只读**（持久写保护）

```dvd-ram-control -rdonly [/dev/dvd]```

**重新启用读/写**访问

```dvd-ram-control -rdwr [/dev/dvd]```

**启用自动写重定位**（AWRE）

```dvd-ram-control -awre [/dev/dvd]```

**启用自动读重定位**（ARRE）

```dvd-ram-control -arre [/dev/dvd]```

# SYNOPSIS

**dvd-ram-control** [**-arre**] [**-awre**] [**-rdonly**|**-rdwr**] _/dev/dvd_

# PARAMETERS

_/dev/dvd_
> 要操作的 DVD-RAM 驱动器设备。

**-rdonly**
> 开启持久写保护（只读）。

**-rdwr**
> 关闭持久写保护（读写）。

**-awre**
> 切换自动写重定位启用（AWRE）状态。

**-arre**
> 切换自动读重定位启用（ARRE）状态。

# DESCRIPTION

**dvd-ram-control** 是 **dvd+rw-tools** 工具集的一员，可用于检查或更改 DVD-RAM 盘片的底层特性。不带任何选项标志运行时会打印盘片当前的持久写保护状态和 AWRE/ARRE 标志。添加标志则会切换或设置驱动器缺陷管理数据中的相应特性。

持久写保护（**-rdonly** / **-rdwr**）会将整张盘片变成只读或可读写介质；AWRE 和 ARRE 控制在读或写出错时的扇区自动重分配。

# CAVEATS

仅适用于 DVD-RAM 介质（不适用于 DVD±R、DVD±RW 或蓝光）。需要访问原始设备（通常以 root 身份或作为 `cdrom`/`disk` 组成员）。持久写保护可能在当前会话结束后仍然生效——尝试刻录前请显式重新启用读/写。

# HISTORY

**dvd-ram-control** 由 **Andy Polyakov** 开发，随 **dvd+rw-tools** 一起发布，这是一套用于在 Unix 上处理 DVD±RW、DVD±R 和 DVD-RAM 介质的实用工具。

# INSTALL

```apt: sudo apt install dvd+rw-tools```

```dnf: sudo dnf install dvd+rw-tools```

```pacman: sudo pacman -S dvd+rw-tools```

```apk: sudo apk add dvd+rw-tools```

```zypper: sudo zypper install dvd+rw-tools```

```brew: brew install dvd+rw-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvd+rw-mediainfo](/man/dvd+rw-mediainfo)(1), [growisofs](/man/growisofs)(1)
