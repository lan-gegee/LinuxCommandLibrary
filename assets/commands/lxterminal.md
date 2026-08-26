# TAGLINE

为 LXDE 桌面环境设计的轻量级终端模拟器

# TLDR

打开**终端**窗口

```lxterminal```

运行**命令**后退出

```lxterminal -e "[command]"```

以**多个标签页**打开

```lxterminal --tabs=[tab1,tab2,tab3]```

以指定**标题**打开

```lxterminal --title=[title]```

设置**工作目录**

```lxterminal --working-directory=[path/to/dir]```

# SYNOPSIS

**lxterminal** [_options_]

# DESCRIPTION

**lxterminal** 是一款为 LXDE 桌面环境设计的轻量级终端模拟器。它支持标签页、可自定义的外观以及命令执行。

# PARAMETERS

**-e, --command COMMAND**
> 在终端中执行命令

**--tabs=TAB1,TAB2,...**
> 以命名的标签页打开

**--title=TITLE**
> 设置窗口标题

**--working-directory=DIR**
> 设置工作目录

**--geometry=WxH**
> 窗口几何尺寸

**-?, --help**
> 显示帮助信息

# CAVEATS

属于 LXDE 桌面的一部分。是 gnome-terminal 或 konsole 的轻量替代品。

# INSTALL

```apt: sudo apt install lxterminal```

```dnf: sudo dnf install lxterminal```

```pacman: sudo pacman -S lxterminal```

```apk: sudo apk add lxterminal```

```zypper: sudo zypper install lxterminal```

```nix: nix profile install nixpkgs#lxterminal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xterm](/man/xterm)(1), [gnome-terminal](/man/gnome-terminal)(1), [konsole](/man/konsole)(1)
