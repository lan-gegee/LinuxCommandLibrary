# TAGLINE

在一个窗口中运行多个 GNOME 终端

# TLDR

**启动** terminator 窗口

```terminator```

**以全屏窗口启动**

```terminator -f```

**水平分割**终端

```Ctrl+Shift+O```

**垂直分割**终端

```Ctrl+Shift+E```

**打开**新标签页

```Ctrl+Shift+T```

# SYNOPSIS

**terminator** [_options_]

# PARAMETERS

**-f, --fullscreen**
> 以全屏模式启动

**-m, --maximise**
> 最大化启动

**-b, --borderless**
> 无窗口装饰启动

**-T, --title _title_**
> 设置窗口标题

**-e, --command _command_**
> 在终端中运行命令

**-l, --layout _layout_**
> 加载指定的布局

**-p, --profile _profile_**
> 使用指定的配置档

**-g, --config _file_**
> 使用备用配置文件

# DESCRIPTION

**terminator** 是一个终端模拟器，允许在单个窗口中排列多个 GNOME 终端。终端可以水平和垂直分割、组织为标签页，并可动态调整大小。

快捷键支持快速导航和操作终端网格。布局和配置档可以保存与恢复，以便获得一致的工作区设置。

# CAVEATS

需要图形环境。配置存储在 **~/.config/terminator/**。某些快捷键可能与终端内运行的应用冲突。

# INSTALL

```dnf: sudo dnf install terminator```

```pacman: sudo pacman -S terminator```

```apk: sudo apk add terminator```

```zypper: sudo zypper install terminator```

```brew: brew install terminator```

```nix: nix profile install nixpkgs#terminator```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnome-terminal](/man/gnome-terminal)(1), [tmux](/man/tmux)(1), [screen](/man/screen)(1), [konsole](/man/konsole)(1)
