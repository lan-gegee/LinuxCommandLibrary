# TAGLINE

GNOME 桌面终端模拟器

# TLDR

打开一个新的 **GNOME 终端窗口**

```gnome-terminal```

在新终端窗口中运行**特定命令**

```gnome-terminal -- [command]```

在最后打开的窗口中新建一个**标签页**

```gnome-terminal --tab```

设置新标签页的**标题**

```gnome-terminal --tab -t "[title]"```

# SYNOPSIS

**gnome-terminal** [_options_] [**--**] [_command_]

# PARAMETERS

**--tab**
> 在现有窗口中打开新标签页

**--window**
> 打开新窗口

**-t**, **--title** _TITLE_
> 设置终端初始标题

**--working-directory** _DIR_
> 设置工作目录

**--geometry** _GEOMETRY_
> 设置窗口大小和位置（WIDTHxHEIGHT+X+Y）

**--profile** _PROFILE_
> 使用指定的配置文件（profile）

**-e**, **--command** _CMD_
> 执行命令（已弃用，请改用 --）

**--wait**
> 等待终端退出

**--maximize**
> 以最大化方式启动

**--full-screen**
> 以全屏模式启动

# DESCRIPTION

**gnome-terminal** 是 GNOME 桌面环境的默认终端模拟器。它是一个功能丰富的终端，支持多标签页、多种配置文件（profile）和自定义选项。

其特性包括多套不同颜色和字体的 profile、透明背景、自定义快捷键，以及基于 VTE 的终端模拟并支持 Unicode。

# CONFIGURATION

**dconf /org/gnome/terminal/**
> 保存在 dconf 中的终端设置，可通过 gsettings 或首选项对话框修改。

# CAVEATS

在 Wayland 上，某些 X11 特有的功能（如 geometry 定位）可能无法工作。--geometry 选项在现代环境下已弃用。深度自定义需要编辑 dconf 设置。

# HISTORY

gnome-terminal 自 **1999** 年 GNOME 1.0 起就是其组成部分。它使用 VTE（Virtual Terminal Emulator）部件库，Terminator 和 Tilix 等其他终端也使用了该库。随着 GNOME 各个版本的迭代，该应用经历了显著演进。

# INSTALL

```apt: sudo apt install gnome-terminal```

```dnf: sudo dnf install gnome-terminal```

```pacman: sudo pacman -S gnome-terminal```

```apk: sudo apk add gnome-terminal```

```zypper: sudo zypper install gnome-terminal```

```nix: nix profile install nixpkgs#gnome-terminal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [xterm](/man/xterm)(1), [alacritty](/man/alacritty)(1)
