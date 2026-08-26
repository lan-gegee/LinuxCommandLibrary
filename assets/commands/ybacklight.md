# TAGLINE

屏幕背光亮度控制工具

# TLDR

**获取亮度**

```ybacklight -get```

**设置亮度**

```ybacklight -set [50]```

**提高亮度**

```ybacklight -inc [10]```

**降低亮度**

```ybacklight -dec [10]```

# SYNOPSIS

**ybacklight** [_-get_] [_-set value_] [_-inc value_] [_-dec value_]

# PARAMETERS

**-get**
> 显示当前亮度等级。

**-set** _VAL_
> 设置为百分比亮度。

**-inc** _VAL_
> 按指定量增加亮度。

**-dec** _VAL_
> 按指定量降低亮度。

# DESCRIPTION

**ybacklight** 从命令行控制显示屏背光亮度。它提供了一个简单的接口，以百分比值的方式获取、设置和调节屏幕亮度。

可以使用 **-set** 将亮度设置为绝对的百分比，也可以用 **-inc** 和 **-dec** 相对于当前亮度进行调整。**-get** 选项用于查询当前的亮度等级。

该工具可作为 **xbacklight** 的替代品，在因驱动或硬件差异导致 xbacklight 无法正常工作的系统上提供类似功能。

# CAVEATS

依赖硬件。可能需要相应权限。属于背光控制工具。

# HISTORY

**ybacklight** 是一款类似于 xbacklight 的背光控制工具，用于调节显示器的亮度。

# INSTALL

```aur: yay -S ybacklight```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xbacklight](/man/xbacklight)(1), [brightnessctl](/man/brightnessctl)(1), [light](/man/light)(1)
