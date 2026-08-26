# TAGLINE

控制笔记本屏幕和其他设备的背光亮度

# TLDR

获取当前**背光**值

```light```

将背光**设置**为 50%

```light -S 50```

将背光**提高** 20%

```light -A 20```

将背光**降低** 20%

```light -U 20```

# SYNOPSIS

**light** [_options_]

# DESCRIPTION

**light** 控制笔记本屏幕和其他可控背光的亮度。它无需 X 或 Wayland 即可工作，并能保存和恢复亮度级别。

# PARAMETERS

**-S PERCENT**
> 将亮度设置为指定百分比

**-A PERCENT**
> 在当前亮度上增加指定百分比

**-U PERCENT**
> 从当前亮度中减去指定百分比

**-G**
> 获取当前亮度（默认）

**-O**
> 保存当前亮度

**-I**
> 恢复之前保存的亮度

**-N PERCENT**
> 设置最低亮度上限

**-P**
> 获取最低亮度上限

**-L**
> 列出可用设备

**-s DEVICE**
> 选择特定设备

**-r**
> 以原始模式解释数值（设备特定值而非百分比）

# CAVEATS

非 root 访问可能需要 udev 规则。适用于通过 /sys/class/backlight 暴露的设备。最低亮度上限（-N）可防止在 0 值时会关闭屏幕的控制器使显示器完全变黑。

# INSTALL

```apt: sudo apt install light```

```dnf: sudo dnf install light```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xbacklight](/man/xbacklight)(1), [brightnessctl](/man/brightnessctl)(1)
