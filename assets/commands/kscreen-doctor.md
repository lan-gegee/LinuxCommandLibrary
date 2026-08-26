# TAGLINE

操作 KDE Plasma 上的显示设置

# TLDR

显示**显示输出**

```kscreen-doctor --outputs```

将显示器向右**旋转**

```kscreen-doctor output.1.rotation.right```

将显示器**缩放**设为 200%

```kscreen-doctor output.HDMI-2.scale.2```

**启用**一台显示器

```kscreen-doctor output.HDMI-A-1.enable```

**禁用**一台显示器

```kscreen-doctor output.DP-2.disable```

设置**主**显示器

```kscreen-doctor output.HDMI-A-1.primary```

设置显示器**分辨率和刷新率**

```kscreen-doctor output.HDMI-A-1.mode.1920x1080@60```

设置显示器**位置**

```kscreen-doctor output.DP-1.position.1920,0```

# SYNOPSIS

**kscreen-doctor** [_options_] [_output.ID.property.value_...]

# DESCRIPTION

**kscreen-doctor** 是一款在 KDE Plasma 桌面上操作显示设置的命令行工具。它使用简单的点号语法启用/禁用输出、设置旋转、缩放、分辨率、刷新率、位置和主显示器状态。单次命令调用可以指定多个输出变更。变更立即生效，无需重启。

# PARAMETERS

**-o, --outputs**
> 显示显示输出信息

**output.ID.enable**
> 启用指定的输出

**output.ID.disable**
> 禁用指定的输出

**output.ID.primary**
> 设为主显示器

**output.ID.rotation.VALUE**
> 设置旋转：none、left、right、inverted

**output.ID.scale.VALUE**
> 设置缩放因子（如 1、1.5、2）

**output.ID.mode.WxH@RATE**
> 设置分辨率和刷新率

**output.ID.position.X,Y**
> 设置显示器位置

# CAVEATS

输出 ID 可以是数字（1、2）或连接器名称（HDMI-A-1、DP-2）。请用 `--outputs` 查找正确的标识符。此工具仅适用于 KDE Plasma，要求 KScreen 后端正在运行。在 X11 上，xrandr 提供类似功能；在 KDE 以外的纯 Wayland 桌面上，请使用特定于合成器的工具。

# INSTALL

```apt: sudo apt install libkscreen-bin```

```dnf: sudo dnf install libkscreen```

```pacman: sudo pacman -S libkscreen```

```apk: sudo apk add libkscreen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kscreen-console](/man/kscreen-console)(1), [xrandr](/man/xrandr)(1)
