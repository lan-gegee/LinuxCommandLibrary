# TAGLINE

具有流畅动画和视觉效果的动态平铺 Wayland 合成器

# TLDR

**启动 Hyprland**

```Hyprland```

**重载配置**

```hyprctl reload```

**列出窗口**

```hyprctl clients```

**触发按键绑定动作**

```hyprctl dispatch [workspace] [3]```

**获取活动窗口**

```hyprctl activewindow```

**显示显示器**

```hyprctl monitors```

# SYNOPSIS

**Hyprland** [_options_]

**hyprctl** [_command_] [_args_]

# PARAMETERS

**hyprctl dispatch** _action_ [_args_]
> 执行 dispatcher 动作。

**hyprctl keyword** _option_ _value_
> 在运行时设置配置选项。

**hyprctl reload**
> 重载配置。

**hyprctl clients**
> 列出窗口。

**hyprctl monitors**
> 列出显示器。

**hyprctl activewindow**
> 显示活动窗口信息。

**hyprctl workspaces**
> 列出工作区。

**hyprctl version**
> 显示版本。

# DESCRIPTION

**Hyprland** 是一款动态平铺 Wayland 合成器，拥有流畅的动画、精美的视觉效果和高度的可定制性。它提供现代化的桌面体验，具备窗口动画、模糊、阴影和工作区管理等特性。

配置通过 ~/.config/hypr/hyprland.conf 完成，使用自定义语法设置按键绑定、装饰和布局选项。

# CONFIGURATION EXAMPLE

```
monitor=,preferred,auto,1
exec-once = waybar
bind = SUPER, Return, exec, kitty
bind = SUPER, Q, killactive
bind = SUPER, 1, workspace, 1
windowrule = float, ^(pavucontrol)$
```

# CAVEATS

仅支持 Wayland。需要兼容的显卡驱动。部分 X11 应用需要 XWayland。配置语法与其他窗口管理器不同。

# HISTORY

Hyprland 由 **vaxerski** 于 **2022 年**创建，是一款功能丰富的 Wayland 合成器。它凭借美观与性能迅速流行，成为 Wayland 平铺窗口管理器用户的主流选择之一。

# INSTALL

```pacman: sudo pacman -S hyprland```

```apk: sudo apk add hyprland```

```zypper: sudo zypper install hyprland```

```nix: nix profile install nixpkgs#hyprland```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [waybar](/man/waybar)(1)
