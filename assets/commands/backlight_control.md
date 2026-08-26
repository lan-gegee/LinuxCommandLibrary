# TAGLINE

按百分比调节屏幕背光亮度。

# TLDR

将背光**提高**指定百分比

```backlight_control +[5]```

将背光**降低**指定百分比

```backlight_control -[5]```

将背光**设置**为特定百分比

```backlight_control [90]```

显示**帮助**

```backlight_control```

# SYNOPSIS

**backlight_control** [**+**|**-**]_percentage_

# DESCRIPTION

**backlight_control** 使用百分比值调节 Linux 系统上的屏幕背光亮度。它为内核背光子系统提供了简单的接口。

该工具适用于笔记本显示屏以及其他通过 **/sys/class/backlight/** 暴露背光控制的设备。

# PARAMETERS

**+**_n_
> 将亮度提高 n 个百分点

**-**_n_
> 将亮度降低 n 个百分点

_n_
> 将亮度设置为 n 个百分点（0-100）

# CAVEATS

需要适当的权限才能写入背光控制文件，可能需要将用户加入 video 或类似用户组。仅适用于通过 sysfs 接口暴露背光控制的硬件。

# SEE ALSO

[xbacklight](/man/xbacklight)(1), [brightnessctl](/man/brightnessctl)(1), [light](/man/light)(1)

# RESOURCES

```[Source code](https://github.com/Hendrikto/backlight_control)```

<!-- verified: 2026-06-22 -->
