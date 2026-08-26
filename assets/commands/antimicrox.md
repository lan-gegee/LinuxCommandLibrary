# TAGLINE

将手柄输入映射为键盘和鼠标操作

# TLDR

**启动图形界面**

```antimicrox```

**使用指定配置启动**

```antimicrox --profile [path/to/profile.gamecontroller.amgp]```

**最小化到系统托盘启动**

```antimicrox --tray```

**隐藏启动**（无窗口也无托盘图标）

```antimicrox --hidden```

**列出已连接的手柄**

```antimicrox --list```

**以守护进程模式启动**

```antimicrox --daemon```

# SYNOPSIS

**antimicrox** [_options_] [_profile_]

# PARAMETERS

**--profile** _file_
> 将指定的配置作为所选控制器的默认配置。

**--profile-controller** _value_
> 仅对具有给定编号或标识符的控制器应用该配置。

**--tray**
> 仅在系统托盘中启动。

**--hidden**
> 不显示主窗口启动。

**--no-tray**
> 启用时禁用托盘菜单。

**-d**, **--daemon**
> 以守护进程方式启动（后台运行）。

**-l**, **--list**
> 打印 SDL 检测到的控制器信息。

**--map** _value_
> 为给定控制器打开手柄映射窗口。

**--unload** [_value_]
> 卸载当前启用的配置。

**--startSet** _number_ [_value_]
> 从指定的 set 启动控制器。

**--next**
> 切换到下一个 profile 加载 set 选项。

**--log-level** {_debug_,_info_,_warn_}
> 以给定级别启用日志（默认：warn）。

**--eventgen** {_xtest_,_uinput_}
> 选择事件生成后端（默认：xtest）。

# DESCRIPTION

**AntiMicroX** 是一款图形化程序，用于将手柄按键和摇杆轴映射到键盘按键、鼠标移动和鼠标按钮。它让手柄可以用于缺乏原生手柄支持的应用程序，包括游戏、办公软件和媒体播放器。

该应用提供可视化编辑器来创建配置文件，定义每个控制器输入如何转换为键盘/鼠标动作。配置可包含复杂的映射，支持修饰键、连发模式、宏以及 set 切换，在单个配置中实现不同的操控方案。

AntiMicroX 支持多个同时使用的控制器，各自拥有独立的配置。它在 Linux 上通过 uinput 或 XTest 进行输入注入，同时支持 X11 和 Wayland（功能受限）。

# CONFIGURATION

**~/.local/share/antimicrox/**
> 控制器配置文件和应用数据的默认目录。

# CAVEATS

Wayland 支持有限；部分功能需要 XWayland。用户必须有权访问 **/dev/uinput** 才能创建虚拟设备；这通常需要将用户加入 **input** 组。某些带反作弊软件的游戏可能屏蔽合成输入。配置文件格式与原 AntiMicro 项目不同。

# HISTORY

AntiMicroX 是 **AntiMicro** 的分支，而 AntiMicro 本身受 **QJoyPad** 启发。原版 AntiMicro 由 **Travis Nickles** 于 **2013 年**前后创建。当开发停滞时，AntiMicroX 分支于 **2019 年**建立，以继续维护并添加新功能。它现在是活跃维护的后继项目，支持现代 Linux 发行版和更多类型的控制器。

# INSTALL

```apt: sudo apt install antimicro```

```dnf: sudo dnf install antimicrox```

```pacman: sudo pacman -S antimicrox```

```zypper: sudo zypper install antimicrox```

```nix: nix profile install nixpkgs#antimicrox```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[jstest](/man/jstest)(1), [xdotool](/man/xdotool)(1), [qjoypad](/man/qjoypad)(1), [evtest](/man/evtest)(1)

# RESOURCES

```[Source code](https://github.com/AntiMicroX/antimicrox)```

```[Documentation](https://antimicrox.github.io/)```

<!-- verified: 2026-06-11 -->
