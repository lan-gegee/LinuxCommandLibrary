# TAGLINE

XFCE 终端模拟器

# TLDR

**打开**新终端

```xfce4-terminal```

设置**标题**

```xfce4-terminal --initial-title "[initial_title]"```

打开新**标签页**

```xfce4-terminal --tab```

**执行**命令

```xfce4-terminal --command "[command_with_args]"```

执行并**保持**窗口

```xfce4-terminal --command "[command_with_args]" --hold```

打开**多个**标签页

```xfce4-terminal --tab --command "[command1]" --tab --command "[command2]"```

# SYNOPSIS

**xfce4-terminal** [_OPTIONS_]

# PARAMETERS

**--initial-title** _TITLE_
> 设置初始窗口标题

**--tab**
> 打开新标签页

**--command** _COMMAND_
> 在终端中执行命令

**--hold**
> 命令退出后保持终端打开

**--working-directory** _DIR_
> 设置工作目录

**--geometry** _WxH+X+Y_
> 窗口几何尺寸

**--fullscreen**
> 以全屏模式启动

# DESCRIPTION

**xfce4-terminal** 是 XFCE 桌面环境的终端模拟器。它提供标签页、可定制的外观以及下拉模式支持。

该终端支持多种配置文件（profile），并可在启动时执行命令。

# CAVEATS

为 XFCE 设计，但也可在其他桌面上使用。需要 GTK 和 VTE 库。

# INSTALL

```apt: sudo apt install xfce4-terminal```

```dnf: sudo dnf install xfce4-terminal```

```pacman: sudo pacman -S xfce4-terminal```

```apk: sudo apk add xfce4-terminal```

```zypper: sudo zypper install xfce4-terminal```

```nix: nix profile install nixpkgs#xfce4-terminal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnome-terminal](/man/gnome-terminal)(1), [konsole](/man/konsole)(1), [xterm](/man/xterm)(1)
