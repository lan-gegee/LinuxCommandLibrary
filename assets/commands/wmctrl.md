# TAGLINE

命令行窗口管理器控制工具

# TLDR

**列出**窗口

```wmctrl -l```

按标题**激活**窗口

```wmctrl -a [window_title]```

**移动**窗口并聚焦

```wmctrl -R [window_title]```

**切换**工作区

```wmctrl -s [workspace_number]```

切换**全屏**状态

```wmctrl -r [window_title] -b toggle,fullscreen```

将窗口移动到其他**工作区**

```wmctrl -r [window_title] -t [workspace_number]```

# SYNOPSIS

**wmctrl** [_OPTIONS_]

# PARAMETERS

**-l**
> 列出窗口

**-a** _TITLE_
> 激活标题匹配的窗口

**-R** _TITLE_
> 将窗口移动到当前工作区并聚焦

**-s** _N_
> 切换到工作区 N

**-r** _TITLE_
> 为操作选择目标窗口

**-b** _ACTION_
> 修改窗口状态（toggle、add、remove）

**-t** _N_
> 将窗口移动到工作区 N

# DESCRIPTION

**wmctrl** 是一个命令行工具，用于与支持 EWMH/NetWM 规范的 X 窗口管理器交互。它可以在脚本或终端中列出、切换和操作窗口。

窗口标题支持部分匹配。多个操作可以组合使用。

# CAVEATS

仅支持 X11。需要符合 EWMH 规范的窗口管理器。部分功能取决于窗口管理器的支持程度。

# INSTALL

```apt: sudo apt install wmctrl```

```dnf: sudo dnf install wmctrl```

```pacman: sudo pacman -S wmctrl```

```zypper: sudo zypper install wmctrl```

```brew: brew install wmctrl```

```nix: nix profile install nixpkgs#wmctrl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdotool](/man/xdotool)(1), [xprop](/man/xprop)(1)
