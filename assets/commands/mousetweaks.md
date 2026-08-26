# TAGLINE

为 GNOME 提供鼠标辅助功能

# TLDR

**启动 mousetweaks**

```mousetweaks```

**启用停留点击**

```mousetweaks --dwell```

**启用次级点击**

```mousetweaks --ssc```

**设置停留时间**

```mousetweaks --dwell-time=[1.2]```

**禁用动画**

```mousetweaks --animate=false```

# SYNOPSIS

**mousetweaks** [_options_]

# PARAMETERS

**--dwell**
> 启用停留点击。

**--ssc**
> 启用模拟次级点击。

**--dwell-time** _SECS_
> 停留点击的延迟时间。

**--animate** _BOOL_
> 启用/禁用动画。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mousetweaks** 为 GNOME 提供鼠标辅助功能。它支持停留点击等辅助手段。

该工具为运动障碍用户提供帮助，基于指针停留实现自动点击。

# CAVEATS

仅适用于 GNOME。属于 GNOME 辅助功能套件。需要 X11 或 Wayland。

# HISTORY

mousetweaks 作为 **GNOME 辅助功能**计划的一部分开发，旨在协助行动不便的用户。

# INSTALL

```apt: sudo apt install mousetweaks```

```dnf: sudo dnf install mousetweaks```

```pacman: sudo pacman -S mousetweaks```

```zypper: sudo zypper install mousetweaks```

```nix: nix profile install nixpkgs#mousetweaks```

<!-- packages: 2026-07-22 -->

# SEE ALSO

