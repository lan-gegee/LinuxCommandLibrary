# TAGLINE

显示器配置的可视化前端

# TLDR

**启动图形化显示器配置**工具

```arandr```

在当前显示屏上显示 GUI 的同时**配置其他显示器**

```arandr --randr-display [DISPLAY]```

# SYNOPSIS

**arandr** [**--randr-display=**_DISPLAY_]

# PARAMETERS

**--randr-display=**_DISPLAY_
> 为 xrandr 操作使用指定的 X display，而 GUI 显示在环境变量指定的显示屏上

**-h**, **--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**ARandR**（Another RandR）是 XRandR 1.2 扩展的图形前端。它提供可视化界面，用于配置显示输出、分辨率、刷新率和多显示器布局。

该应用将已连接的显示器显示为可拖动的矩形，可以直观地排列显示器位置。更改立即生效，配置可保存为可执行的 Shell 脚本，供日后使用或登录时自动执行。

主要功能包括支持边缘吸附的拖放式显示器定位、旋转、分辨率选择以及启用/禁用输出。保存的脚本是纯文本，可以编辑以加入其他命令。

若要通过命令行控制显示设置，请直接使用 **xrandr**。ARandR 在内部生成 xrandr 命令，适合可视化和试验多显示器布局。

# CAVEATS

需要运行中的 X server 且支持 XRandR 1.2 或更高版本。不适用于 Wayland 合成器；请改用其原生的显示器配置工具。保存的配置只有在登录时执行脚本才会生效（通过 ~/.xprofile、~/.xinitrc 或会话自启动）。

# HISTORY

**ARandR** 由 **Christian Aichinger** 开发，作为 GNOME 和 KDE 显示器配置工具的替代品，面向轻量级窗口管理器的用户。该项目旨在提供一种简单、独立于桌面环境的显示器可视化配置方式，同时保持轻便和精简。

# INSTALL

```dnf: sudo dnf install arandr```

```pacman: sudo pacman -S arandr```

```apk: sudo apk add arandr```

```zypper: sudo zypper install arandr```

```nix: nix profile install nixpkgs#arandr```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[xrandr](/man/xrandr)(1)
