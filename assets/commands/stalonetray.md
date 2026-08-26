# TAGLINE

独立的 X11 系统托盘

# TLDR

**以默认设置启动 stalonetray**

```stalonetray```

**以自定义背景色启动**

```stalonetray --background "[#2e3440]"```

**以自定义图标大小启动**

```stalonetray --icon-size [32]```

**以窗口 strut 启动**以预留屏幕空间

```stalonetray --window-strut [auto]```

**以 dockapp 模式启动**（面向 WindowMaker）

```stalonetray --dockapp-mode [wmaker]```

**以图标从右下角生长的方式启动**

```stalonetray --icon-gravity [SE]```

**使用自定义配置文件**

```stalonetray --config [~/.config/stalonetray/stalonetrayrc]```

# SYNOPSIS

**stalonetray** [_options_]

# PARAMETERS

**-bg**, **--background** _color_
> 托盘背景色（十六进制三元组或 X11 颜色名）。

**-i**, **--icon-size** _n_
> 默认图标大小（像素）。默认：24，最小：16。

**--icon-gravity** _gravity_
> 图标定位的重力方向：**NW**、**NE**、**SW** 或 **SE**。默认：NW。

**--grow-gravity** _gravity_
> 托盘生长方向：**NW**、**NE**、**SW**、**SE**、**N**、**S**、**E** 或 **W**。

**--geometry** _geometry_
> 托盘初始窗口几何尺寸（WIDTHxHEIGHT+X+Y）。

**--max-geometry** _geometry_
> 托盘的最大尺寸。

**--window-type** _type_
> EWMH 窗口类型：**desktop**、**dock**、**normal**、**toolbar**、**utility**。默认：dock。

**--window-strut** _mode_
> 预留屏幕空间：**auto**、**top**、**bottom**、**left**、**right** 或 **none**。

**-d**, **--dockapp-mode** _mode_
> Dockapp 模式：**none**、**simple** 或 **wmaker**。

**--slot-size** _size_
> 用于放置图标的网格槽位大小。

**--sticky**
> 让托盘窗口出现在所有桌面上。

**--skip-taskbar**
> 将托盘窗口从任务栏移除。

**--kludges** _list_
> 启用变通方案：fix_window_pos、force_icons_size、use_icons_hints。

**--log-level** _level_
> 日志详细程度：**err**、**info** 或 **trace**。

**-c**, **--config** _file_
> 配置文件路径。

# DESCRIPTION

**stalonetray** 是一个面向 X11 的独立系统托盘（通知区域）实现。它提供一个极简的托盘，可与任何符合 EWMH 标准的窗口管理器配合工作，非常适合轻量级环境或没有内置系统托盘的窗口管理器。

该托盘支持 freedesktop.org 系统托盘协议和用于嵌入应用程序图标的 XEMBED 规范。它可以放置在屏幕上的任意位置，并可配置为预留空间（strut），避免其他窗口与其重叠。

配置可以通过命令行选项或 **~/.stalonetrayrc** 配置文件完成。文件使用"关键字-参数"对的形式，命令行选项的优先级更高。

# CONFIGURATION

**~/.stalonetrayrc**
> 默认配置文件，使用与命令行选项名对应的"关键字-参数"对（例如 background #2e3440、icon_size 24）。

# CAVEATS

某些应用程序可能不能正确支持系统托盘协议，需要使用 **--kludges** 选项。窗口类型 **dock** 在不同窗口管理器下的行为可能不同。构建只需要 Xlib，可选 libXinerama。trace 日志级别需要以 --enable-debug 构建。

# HISTORY

**stalonetray** 作为一个极简、无依赖的 X11 系统托盘实现而创建。它填补了那些原生不提供系统托盘的窗口管理器（如 i3、bspwm 或 dwm）的需求空白。该项目遵循 freedesktop.org 的系统托盘互操作性规范。

# INSTALL

```apt: sudo apt install stalonetray```

```dnf: sudo dnf install stalonetray```

```pacman: sudo pacman -S stalonetray```

```apk: sudo apk add stalonetray```

```zypper: sudo zypper install stalonetray```

```nix: nix profile install nixpkgs#stalonetray```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trayer](/man/trayer)(1), [polybar](/man/polybar)(1), [tint](/man/tint)(1)
