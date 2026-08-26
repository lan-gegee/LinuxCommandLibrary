# TAGLINE

在 X11 上自动隐藏闲置的鼠标光标

# TLDR

**闲置后隐藏光标**

```unclutter```

**自定义超时时间**

```unclutter -idle [3]```

**忽略窗口**

```unclutter -not [window-name]```

**后台运行**

```unclutter -b```

**不触碰根窗口**

```unclutter -noevents```

# SYNOPSIS

**unclutter** [_-idle seconds_] [_-b_] [_options_]

# PARAMETERS

**-idle** _SEC_
> 隐藏前的等待秒数。

**-b**
> 后台守护进程。

**-not** _NAME_
> 忽略指定窗口。

**-noevents**
> 不处理根窗口事件。

**-display** _DPY_
> X display。

# DESCRIPTION

**unclutter** 在 X11 桌面上经过一段可配置的不活动时间后自动隐藏鼠标光标。当用户移动鼠标时，光标会立即重新出现，因此在正常使用中隐藏过程完全无感。

该工具特别适合演示、信息亭（kiosk）显示屏以及以键盘为主的工作流，在这些场景中静止的鼠标指针会造成视觉干扰。它可以作为后台守护进程运行，并支持将特定窗口排除在光标隐藏之外，使光标在需要它的应用程序中保持可见。

目前存在两个主要实现：原始的 X11 版本和 **unclutter-xfixes**，后者使用 XFixes 扩展以更现代的方式实现。两者目的相同，但在实现细节以及与合成窗口管理器的兼容性上有所不同。

# CAVEATS

仅支持 X11。存在多个版本。可能与某些应用程序冲突。

# HISTORY

**unclutter** 的设计目的是在鼠标不被使用时隐藏它，让 X11 显示更整洁。

# INSTALL

```pacman: sudo pacman -S unclutter```

```zypper: sudo zypper install unclutter```

```nix: nix profile install nixpkgs#unclutter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdotool](/man/xdotool)(1), [xsetroot](/man/xsetroot)(1)
