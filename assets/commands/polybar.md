# TAGLINE

面向 X11 窗口管理器的可自定义状态栏

# TLDR

**以默认状态栏启动 polybar**

```polybar```

**启动特定状态栏**

```polybar [bar_name]```

**使用配置文件启动**

```polybar -c [~/.config/polybar/config.ini] [bar_name]```

**列出可用的状态栏**

```polybar -m```

**重新加载配置**

```polybar-msg cmd restart```

**向模块发送操作**

```polybar-msg action [module_name] [action]```

**检查配置**

```polybar -c [config.ini] --check```

# SYNOPSIS

**polybar** [_-c config_] [_-m_] [_--check_] [_bar_name_]

# PARAMETERS

**-c**, **--config** _FILE_
> 配置文件的路径。

**-m**, **--list-monitors**
> 列出可用的显示器/输出。

**-r**, **--reload**
> 配置变更时重新加载。

**-q**, **--quiet**
> 抑制输出。

**-l**, **--log** _LEVEL_
> 日志级别：error、warning、info、trace。

**--check**
> 校验配置语法。

**-w**, **--print-wmname**
> 打印 WM 名称并退出。

# MODULES

**internal/battery**
> 电池状态与电量。

**internal/network**
> 网络连接信息。

**internal/cpu**
> CPU 使用率。

**internal/memory**
> 内存使用率。

**internal/date**
> 日期和时间。

**internal/volume** / **internal/pulseaudio**
> 音量控制。

**internal/xworkspaces**
> 工作区指示器。

**internal/temperature**
> 系统温度。

**custom/script**
> 自定义脚本的输出。

**custom/ipc**
> 进程间通信。

# DESCRIPTION

**Polybar** 是一款面向 X11 窗口管理器的快速、可自定义的状态栏。它通过模块化配置显示系统信息、工作区指示器和自定义内容。

配置采用 INI 格式，包含状态栏和模块相关的节。状态栏定义外观（颜色、字体、位置）以及要包含的模块。模块提供内容——内置模块用于系统信息，自定义模块用于脚本。

状态栏分为左、中、右三个区域。模块可以显示文本、图标（通过图标字体）、进度条和可点击区域。格式化使用标签来设置颜色、字体和间距。

自定义脚本模块执行外部命令并显示其输出。IPC 模块支持外部程序通过 polybar-msg 进行实时更新。

多个状态栏可以在不同显示器上同时运行。-m 标志列出可用的输出，便于多显示器配置。

# CONFIGURATION

**~/.config/polybar/config.ini**
> 主配置文件，采用 INI 格式，定义状态栏、模块、颜色和字体。

**~/.config/polybar/launch.sh**
> 常用的启动脚本，用于配合窗口管理器启动 polybar。

# CAVEATS

仅支持 X11——没有原生 Wayland 支持（请使用 Waybar）。符号需要图标字体。复杂的配置可能相当冗长。部分窗口管理器需要特定的设置。重新加载会丢失一些状态。脚本模块过多会增加 CPU 占用。

# HISTORY

**Polybar** 由 **Michael Carlberg** 于 **2016 年**前后创建，是对 lemonbar 的重写，配置更加简单。它旨在提供强大的状态栏功能而不要求用户掌握 shell 脚本知识。它用 C++ 编写，在 r/unixporn 社区的桌面定制圈中广受欢迎。

# INSTALL

```apt: sudo apt install polybar```

```dnf: sudo dnf install polybar```

```pacman: sudo pacman -S polybar```

```apk: sudo apk add polybar```

```zypper: sudo zypper install polybar```

```nix: nix profile install nixpkgs#polybar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[polybar-msg](/man/polybar-msg)(1), [waybar](/man/waybar)(1), [i3status](/man/i3status)(1), [lemonbar](/man/lemonbar)(1), [dunst](/man/dunst)(1)
