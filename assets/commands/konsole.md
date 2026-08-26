# TAGLINE

KDE 的终端模拟器应用

# TLDR

在**指定目录**中打开终端

```konsole --workdir [path/to/directory]```

**执行**命令并保持窗口打开

```konsole --noclose -e [command]```

在已有窗口中打开**新标签页**

```konsole --new-tab```

以**后台模式**启动（按 Ctrl+Shift+F12 显示）

```konsole --background-mode```

使用指定的 **profile**

```konsole --profile [profile_name]```

# SYNOPSIS

**konsole** [_options_]

# PARAMETERS

**--workdir** _DIR_
> 设置初始工作目录

**-e** _COMMAND_
> 在终端中执行命令

**--noclose**
> 命令退出后不关闭窗口

**--new-tab**
> 在已有窗口中打开新标签页

**--background-mode**
> 在后台运行，Ctrl+Shift+F12 可将其调到前台

**--profile** _NAME_
> 使用指定的 profile

**--separate**
> 在单独的进程中运行

**--show-tabbar**
> 显示标签栏

**--hide-tabbar**
> 隐藏标签栏

**--show-menubar**
> 显示菜单栏

**--hide-menubar**
> 隐藏菜单栏

**--fullscreen**
> 以全屏模式启动

# DESCRIPTION

**konsole** 是 KDE 的终端模拟器应用。它提供强大的命令行界面，具备多标签页、分屏视图、profile 和会话管理等功能。

特性包括可自定义的配色方案、字体、键盘快捷键，以及监控终端活动或静默状态的能力。它支持 SSH 书签并与 KDE 桌面集成。

# CAVEATS

某些功能需要 KDE Plasma 桌面。某些情况下 profile 设置会覆盖命令行选项。后台模式要求 KDE 正在运行。

# HISTORY

Konsole 自 KDE 项目早期起就是 KDE 的默认终端模拟器。它为 KDE 4 进行了重写，并随 Plasma 桌面持续演进。

# INSTALL

```apt: sudo apt install konsole```

```dnf: sudo dnf install konsole```

```pacman: sudo pacman -S konsole```

```apk: sudo apk add konsole```

```zypper: sudo zypper install konsole```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yakuake](/man/yakuake)(1), [gnome-terminal](/man/gnome-terminal)(1), [xterm](/man/xterm)(1)
