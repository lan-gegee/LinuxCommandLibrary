# TAGLINE

显示或设置控制台到帧缓冲的映射

# TLDR

**显示**控制台 1 映射到的帧缓冲设备

```con2fbmap 1```

**将**控制台 1 映射到帧缓冲设备 0

```con2fbmap 1 0```

**将**控制台 3 映射到帧缓冲设备 1

```con2fbmap 3 1```

# SYNOPSIS

**con2fbmap** _console_ [_framebuffer_]

# PARAMETERS

**console**
> 要查询或修改的虚拟控制台编号（必填）。

**framebuffer**
> 控制台要映射到的帧缓冲设备编号。若省略，则显示当前映射。

# DESCRIPTION

**con2fbmap** 用于显示或设置 Linux 虚拟控制台与帧缓冲设备之间的映射。帧缓冲设备为访问图形显示提供统一接口，通过设备节点 **/dev/fb\<n\>** 访问，其中 **n** 是设备编号。

仅传入控制台编号调用时，它会显示该控制台当前的帧缓冲映射。同时传入控制台编号和帧缓冲编号时，它会将该控制台重新分配给指定的帧缓冲设备。

在配备多个图形适配器或显示器的系统上很有用，可以让不同的虚拟控制台渲染到不同的屏幕上。

# CAVEATS

更改映射需要 root 权限。仅适用于使用 Linux 帧缓冲子系统的系统。在使用 KMS/DRM 的现代系统上，帧缓冲设备可能通过 **vesafb**、**simplefb** 或 DRM 帧缓冲模拟层提供。

# HISTORY

**con2fbmap** 是 **fbset** 软件包的一部分，这是一套面向 Linux 的帧缓冲实用工具。帧缓冲子系统于 **1998** 年随 **Linux 2.1.107** 引入，最初从 Amiga 和 Atari 的 Linux 内核移植而来。fbset 软件包由 **Geert Uytterhoeven** 维护，是早期 Linux 帧缓冲基础设施的一部分。

# INSTALL

```apt: sudo apt install fbset```

```pacman: sudo pacman -S fbset```

```nix: nix profile install nixpkgs#fbset```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fbset](/man/fbset)(1)
