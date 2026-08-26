# TAGLINE

交互式时区名称选择器

# TLDR

**选择**时区（交互式）

```tzselect```

按**坐标**查找时区

```tzselect -c [coordinates]```

# SYNOPSIS

**tzselect** [_OPTIONS_]

# PARAMETERS

**-c** _COORDINATES_
> 查找距离给定 ISO 6709 坐标最近的时区

**-n** _LIMIT_
> 最多显示这么多选项

# DESCRIPTION

**tzselect** 提供一个交互式菜单来选择时区。它会逐级遍历地理区域，帮助你确定正确的时区。所选时区的名称会被打印到标准输出。

注意：此程序并不会真正设置系统时区。它只帮你找出正确的时区名称，之后可以用其他工具来配置系统。

# CAVEATS

不修改系统配置。其输出必须配合其他工具才能设置时区。交互模式需要终端输入。

# INSTALL

```apt: sudo apt install libc-bin```

```zypper: sudo zypper install tzselect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timedatectl](/man/timedatectl)(1), [date](/man/date)(1)
