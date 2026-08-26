# TAGLINE

控制台鼠标支持守护进程

# TLDR

以 **PS/2 鼠标**启动 gpm

```sudo gpm -m /dev/input/mice -t ps2```

以 **Microsoft 串口鼠标**启动 gpm

```sudo gpm -m /dev/ttyS0 -t ms```

以前台模式启动 gpm 进行**调试**

```sudo gpm -m [path/to/mouse_device] -t [mouse_type] -D```

**终止**正在运行的 gpm

```sudo gpm -k```

以**转发器模式**启动 gpm 以兼容 X 服务器

```sudo gpm -m [path/to/mouse_device] -t [mouse_type] -R```

列出可用的**鼠标类型**

```gpm -t help```

# SYNOPSIS

**gpm** [_options_]

# PARAMETERS

**-m** _DEVICE_
> 鼠标设备（例如 /dev/input/mice、/dev/ttyS0）

**-t** _TYPE_
> 鼠标类型（ps2、ms、imps2 等）

**-R** [_TYPE_]
> 用于 X 服务器的转发器模式；可选指定输出类型

**-D**
> 调试模式；前台运行

**-k**
> 终止正在运行的 gpm 守护进程

**-B** _SEQUENCE_
> 按键序列（1、2、3 或其排列）

**-2**
> 强制模拟两键鼠标

**-3**
> 强制模拟三键鼠标

# DESCRIPTION

**gpm**（General Purpose Mouse）为 Linux 虚拟控制台（文本模式）提供鼠标支持。它在控制台应用程序中启用复制/粘贴功能、鼠标光标移动和鼠标按键事件。

文本选择通过按住左键并拖动完成。中键粘贴选中的文本。右键扩展选择范围。这在纯文本模式下提供了类似 X11 的剪贴板功能。

在转发器模式（**-R**）下，gpm 可以将鼠标事件传递给 X 服务器，让控制台和 X 应用程序共享同一个鼠标设备。

# CONFIGURATION

**/etc/gpm.conf**
> 守护进程配置文件，包括鼠标设备、类型和选项。

# CAVEATS

仅在 Linux 虚拟控制台中有效，不适用于终端模拟器或 SSH 会话。需要 root 权限。如果未配置转发器模式，可能与 X 服务器的鼠标处理冲突。现代系统通常使用 systemd 来管理 gpm。

# HISTORY

gpm 由 Alessandro Rubini 于 **1994 年**创建，为 Linux 控制台引入鼠标支持。在图形桌面普及之前，它对文本模式应用程序和系统管理至关重要。该项目至今仍在为基于控制台的系统进行维护。

# INSTALL

```apt: sudo apt install gpm```

```dnf: sudo dnf install gpm```

```pacman: sudo pacman -S gpm```

```apk: sudo apk add gpm```

```zypper: sudo zypper install gpm```

```nix: nix profile install nixpkgs#gpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[Xorg](/man/Xorg)(1)
