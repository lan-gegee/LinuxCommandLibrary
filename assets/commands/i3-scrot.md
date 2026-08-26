# TAGLINE

为 i3 窗口管理器封装的 scrot 包装脚本

# TLDR

截取**全屏**截图

```i3-scrot```

截取**活动窗口**

```i3-scrot --window```

截取**选定区域**

```i3-scrot --select```

截取全屏并复制到**剪贴板**

```i3-scrot --xclip --desk```

截取活动窗口并复制到**剪贴板**

```i3-scrot --xclip --window```

截取选定区域并复制到**剪贴板**

```i3-scrot --xclip --select```

带**延迟**（秒）截取全屏

```i3-scrot --desk [5]```

# SYNOPSIS

**i3-scrot** [_options_] [_delay_]

# PARAMETERS

**-d**, **--desk**
> 截取全屏（默认动作）。

**-w**, **--window**
> 截取当前活动窗口。

**-s**, **--select**
> 截取用户选择的矩形区域。

**-x**, **--xclip**
> 将截图复制到剪贴板，而不只是保存为文件。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**i3-scrot** 是围绕 scrot 截图工具的包装脚本，专为配合 i3 窗口管理器使用而设计。它为常见的截图操作提供了便捷选项，并在完成后发送桌面通知。

截图默认保存到 **~/Pictures**。保存位置及其他设置可在 **~/.config/i3-scrot.conf** 中修改。不带任何标志时的默认动作是全屏截图。

# CAVEATS

需要安装 scrot 和 xclip。虽然为 i3/Manjaro 设计，但也可在其他 X11 窗口管理器下工作。不支持 Wayland；请改用 grim 或 hyprshot。

# HISTORY

i3-scrot 由 Manjaro Linux 开发，是其 i3 版本的一部分，提供与 i3 窗口管理器工作流集成的便捷截图功能。

# INSTALL

```apt: sudo apt install i3-wm```

```dnf: sudo dnf install i3```

```pacman: sudo pacman -S i3-wm```

```apk: sudo apk add i3wm```

```zypper: sudo zypper install i3```

```nix: nix profile install nixpkgs#i3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scrot](/man/scrot)(1), [xclip](/man/xclip)(1), [i3](/man/i3)(1), [maim](/man/maim)(1), [grim](/man/grim)(1)
