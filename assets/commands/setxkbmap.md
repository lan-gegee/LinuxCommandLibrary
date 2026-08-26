# TAGLINE

配置 X11 键盘布局

# TLDR

将键盘布局设置为**法语 AZERTY**

```setxkbmap fr```

设置**多个布局**及切换选项

```setxkbmap -layout us,de -variant ,qwerty -option 'grp:alt_caps_toggle'```

**查询**当前键盘设置

```setxkbmap -query```

设置键盘**型号**

```setxkbmap -model pc105 -layout us```

**打印**键位映射组件但不应用

```setxkbmap -layout us -print```

为特定**输入设备**设置布局

```setxkbmap -device [device_id] -layout [layout]```

# SYNOPSIS

**setxkbmap** [_args_] [_layout_ [_variant_ [_option_...]]]

# PARAMETERS

**-layout** _name_
> 指定布局名称（多个布局用逗号分隔）

**-variant** _name_
> 指定布局变体（逗号分隔，顺序与布局对应）

**-model** _name_
> 指定键盘型号（例如 pc104、pc105、thinkpad）

**-option** _name_
> 指定 XKB 选项（可多次使用）

**-device** _device_
> 要更新的数字设备 ID（默认：核心键盘）

**-display** _display_
> 要更新的 X 显示器

**-config** _file_
> 描述键盘的 XKB 配置文件

**-rules** _file_
> 用于将布局解析为组件的规则文件

**-query**
> 显示当前的规则、型号、布局、变体和选项

**-print**
> 以 xkbcomp 格式输出组件名后退出

**-I** _directory_
> 将目录加入布局文件的搜索路径

**-v, -verbose** [_level_]
> 设置详细程度（0-10，默认 5）

**-help**
> 显示用法信息

**-version**
> 打印程序版本

# DESCRIPTION

**setxkbmap** 使用 X 键盘扩展（XKB）为 X Window System 配置键盘布局。它根据存储在 **/usr/share/X11/xkb** 中的组件构建键位映射，并将其应用到当前 X 会话。

该命令支持多个键盘布局，可通过可配置的按键组合（选项）进行切换。常用的切换选项包括 **grp:alt_shift_toggle**、**grp:caps_toggle** 和 **grp:win_space_toggle**。

# CONFIGURATION

**/usr/share/X11/xkb/**
> 系统 XKB 数据目录，包含布局定义、规则、符号和键码。

**/etc/X11/xorg.conf.d/**
> 通过 X.Org 持久保存键盘布局设置的即插式配置目录。

# CAVEATS

更改仅在会话内有效，X 重启后不会保留。要永久更改，请通过桌面环境设置、**/etc/X11/xorg.conf.d/** 或 systemd 的 **localectl** 进行配置。在 Wayland 会话中不起作用；请改用合成器自带的工具。布局名称因发行版而异。

# HISTORY

**setxkbmap** 是 X 键盘扩展（XKB）的一部分，XKB 开发于 **20 世纪 90 年代中期**，用于取代较旧的核心 X 键盘协议。XKB 被集成进 XFree86 以及后来的 X.Org，成为 X11 的标准键盘配置机制。该工具作为 **xorg-x11-xkb-utils** 软件包的一部分进行维护。

# INSTALL

```apt: sudo apt install x11-xkb-utils```

```dnf: sudo dnf install setxkbmap```

```apk: sudo apk add setxkbmap```

```zypper: sudo zypper install setxkbmap```

```nix: nix profile install nixpkgs#setxkbmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xkbcomp](/man/xkbcomp)(1), [localectl](/man/localectl)(1), [loadkeys](/man/loadkeys)(1), [xmodmap](/man/xmodmap)(1)
