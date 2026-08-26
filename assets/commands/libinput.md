# TAGLINE

用于处理 Linux 输入设备的库和命令行工具

# TLDR

**列出**所有输入设备

```sudo libinput list-devices```

**调试**输入事件

```sudo libinput debug-events```

启动**调试 GUI**

```sudo libinput debug-gui```

调试**数位板**设备

```sudo libinput debug-tablet```

显示**帮助**

```libinput --help```

# SYNOPSIS

**libinput** [_--help_|_--version_] _command_ [_args_]

# SUBCOMMANDS

**list-devices**
> 列出 libinput 识别的所有设备及其能力。

**debug-events** [_--verbose_] [_--device_ _DEV_]
> 将来自设备的所有输入事件打印到标准输出。

**debug-gui**
> 以图形界面可视化已连接设备的输入事件。

**debug-tablet**
> 打印已连接数位板的坐标轴和触控笔状态。

**measure** _feature_
> 测量设备特定的属性，例如触摸板压力或数位板压力曲线。

**analyze** _subcommand_
> 分析 libinput record 文件中记录的事件。

**record** [_options_] [_device_]
> 将输入事件记录到 YAML 文件，供日后重放或分析。

**replay** _file_
> 重放先前录制文件中的事件。

# PARAMETERS

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**libinput** 是用于处理 Linux 输入设备的库和命令行工具。它为 X11 和 Wayland 系统上的鼠标、键盘、触摸板和数位板提供统一接口。

CLI 采用基于动词的接口：用 **list-devices** 枚举设备，用 **debug-events** 监视输入，用 **record**/**replay** 捕获并重现输入轨迹以便调试。

# CAVEATS

大多数命令需要 root 权限（或加入 **input** 组）才能访问输入设备。**debug-gui** 子命令需要图形环境。

# INSTALL

```apt: sudo apt install libinput-tools```

```dnf: sudo dnf install libinput```

```pacman: sudo pacman -S libinput-tools```

```apk: sudo apk add libinput```

```zypper: sudo zypper install libinput-tools```

```nix: nix profile install nixpkgs#libinput```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xinput](/man/xinput)(1), [evtest](/man/evtest)(1)
