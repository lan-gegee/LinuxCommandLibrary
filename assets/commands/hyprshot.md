# TAGLINE

专为 Hyprland Wayland 合成器设计的截图工具

# TLDR

选择并截图一个**区域**

```hyprshot -m region```

选择并截图**指定窗口**

```hyprshot -m window```

选择并截图**指定输出**

```hyprshot -m output```

截图**活动窗口**

```hyprshot -m active -m window```

**冻结**屏幕并截图选定区域

```hyprshot -z -m region```

截图保存到指定的**输出目录**

```hyprshot -o [path/to/directory] -m window```

仅截图到**剪贴板**

```hyprshot --clipboard -m output```

# SYNOPSIS

**hyprshot** [_options_] **-m** _mode_

# PARAMETERS

**-m**, **--mode** _MODE_
> 截图模式：region、window、output、active

**-o**, **--output-folder** _DIR_
> 将截图保存到指定目录

**-f**, **--filename** _NAME_
> 设置输出文件名

**--clipboard**
> 仅复制到剪贴板（不保存为文件）

**-z**, **--freeze**
> 选择时冻结屏幕

**-s**, **--silent**
> 截图后不发送通知

**-r**, **--raw**
> 将原始图像数据输出到 stdout

**-d**, **--delay** _SECONDS_
> 截图前等待的时间

# DESCRIPTION

**hyprshot** 是一款专为 Hyprland Wayland 合成器设计的截图工具。它提供针对区域、窗口和输出的交互式选择，并与剪贴板集成。

模式：
- **region** — 选择矩形区域
- **window** — 选择特定窗口
- **output** — 选择显示器/输出
- **active** — 与 window/output 组合使用，表示当前焦点

截图默认保存到 **~/Pictures/Screenshots**。该工具使用 slurp 进行区域选择，使用 grim 进行捕获。

# CAVEATS

需要 Hyprland、grim、slurp 和 wl-clipboard。freeze 选项并非在所有系统上都可用。窗口选择依赖于 Hyprland 的客户端列表。

# HISTORY

hyprshot 由 Gustash 创建，是为 Hyprland 用户封装截图工具的便捷方案。相比手动组合 grim 和 slurp，它提供了更精简的界面。

# INSTALL

```pacman: sudo pacman -S hyprshot```

```zypper: sudo zypper install hyprshot```

```nix: nix profile install nixpkgs#hyprshot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hyprctl](/man/hyprctl)(1), [grim](/man/grim)(1), [slurp](/man/slurp)(1), [wl-copy](/man/wl-copy)(1)
