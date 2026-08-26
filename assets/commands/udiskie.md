# TAGLINE

可移动介质自动挂载器

# TLDR

以**托盘**图标和通知启动

```udiskie --tray --notify```

以**智能托盘**启动（无可用设备时自动隐藏）

```udiskie --smart-tray```

禁用**自动挂载**但保留托盘

```udiskie --no-automount --tray```

使用自定义**配置**文件

```udiskie --config [path/to/config.yml]```

为 LUKS 设备使用自定义**密码**提示命令

```udiskie --password-prompt '[command]'```

启用**详细输出**

```udiskie --verbose```

# SYNOPSIS

**udiskie** [_OPTIONS_]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息并退出

**-V**, **--version**
> 显示版本信息并退出

**-v**, **--verbose**
> 启用详细输出

**-q**, **--quiet**
> 抑制输出消息

**-c** _FILE_, **--config**=_FILE_
> 使用指定的配置文件

**-C**, **--no-config**
> 忽略所有配置文件

**-a**, **--automount**
> 启用新设备的自动挂载（默认）

**-A**, **--no-automount**
> 禁用新设备的自动挂载

**-n**, **--notify**
> 启用弹窗通知

**-N**, **--no-notify**
> 禁用弹窗通知

**-t**, **--tray**
> 显示系统托盘图标

**-s**, **--smart-tray**
> 显示在没有可执行操作时自动隐藏的托盘图标

**-T**, **--no-tray**
> 禁用托盘图标（默认）

**-f** _PROGRAM_, **--file-manager**=_PROGRAM_
> 设置打开已挂载目录的程序

**-F**, **--no-file-manager**
> 禁用目录浏览

**-p** _COMMAND_, **--password-prompt**=_COMMAND_
> 设置获取密码的命令（LUKS 设备）

**-P**, **--no-password-prompt**
> 阻止解锁 LUKS 加密设备

**--appindicator**
> 状态图标使用 AppIndicator3

**--password-cache** _MINUTES_
> 将密码缓存指定的分钟数

**--no-password-cache**
> 禁用密码缓存

**--event-hook** _COMMAND_
> 在设备事件发生时执行命令

# DESCRIPTION

**udiskie** 是基于 udisks2 的用户级可移动介质自动挂载器。当 USB 驱动器、光盘及其他可移动设备插入时会自动挂载。

该守护进程可以显示系统托盘图标以便轻松管理设备，并在设备挂载或卸载时发送桌面通知。默认从 **~/.config/udiskie/config.yml** 读取配置。

# CAVEATS

需要 udisks2 守护进程在运行。桌面通知需要通知守护进程。托盘图标需要系统托盘支持。某些加密设备需要配置密码获取方式。

# INSTALL

```dnf: sudo dnf install udiskie```

```pacman: sudo pacman -S udiskie```

```apk: sudo apk add udiskie```

```zypper: sudo zypper install udiskie```

```nix: nix profile install nixpkgs#udiskie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[udiskie-mount](/man/udiskie-mount)(1), [udiskie-umount](/man/udiskie-umount)(1), [udisksctl](/man/udisksctl)(1)
