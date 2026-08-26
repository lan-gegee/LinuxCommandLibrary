# TAGLINE

Sway 合成器的默认状态栏

# TLDR

**启动 swaybar**（通常由 sway 自动启动）

```swaybar```

**以指定的栏 ID 启动**

```swaybar -b [bar-0]```

**使用自定义配置启动**

```swaybar -c [~/.config/sway/config]```

**启用调试日志**

```swaybar -d```

# SYNOPSIS

**swaybar** [_options_]

# PARAMETERS

**-b**, **--bar_id** _id_
> 要获取其配置的栏 ID。

**-c**, **--config** _file_
> sway 配置文件的路径。

**-d**, **--debug**
> 启用调试日志。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**swaybar** 是 Sway Wayland 合成器的默认状态栏。它显示工作区按钮、窗口标题以及可自定义的状态区域。

状态栏通常由 Sway 根据 sway 配置文件中的 bar 配置自动启动。状态区域的内容通过执行 status_command 生成，该命令向标准输出输出文本或 JSON。

Swaybar 支持 i3bar JSON 协议，可输出带颜色和点击事件的结构化状态。它还通过 StatusNotifierItem 协议为应用程序提供系统托盘。

颜色、位置、字体和行为等配置都在 sway 配置文件的 bar 块内完成。

# CONFIGURATION

在 sway 配置文件中配置：

```
bar {
    status_command i3status
    position top
    colors {
        background #323232
        statusline #ffffff
    }
}
```

# CAVEATS

必须在 Sway 合成器下运行。系统托盘支持不如独立状态栏完善。需要高级定制时可考虑改用 Waybar。status_command 的输出必须与 swaybar 或 i3bar 协议兼容。

# HISTORY

**swaybar** 是 Sway 项目的一部分，提供原生的 Wayland 状态栏。Sway 由 Drew DeVault 创建，致力于在 Wayland 上实现 i3 兼容。该状态栏遵循 i3bar 惯例，同时运行在纯 Wayland 环境中而不依赖 X11。

# INSTALL

```apt: sudo apt install sway```

```dnf: sudo dnf install sway```

```pacman: sudo pacman -S sway```

```apk: sudo apk add swaybar```

```zypper: sudo zypper install sway```

```nix: nix profile install nixpkgs#sway```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [i3status](/man/i3status)(1), [waybar](/man/waybar)(1)
