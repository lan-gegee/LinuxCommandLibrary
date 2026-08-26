# TAGLINE

控制 UVC 网络摄像头的动态设置

# TLDR

**列出已连接的摄像头**

```uvcdynctrl -l```

**列出默认设备的可用控件**

```uvcdynctrl -c```

**列出指定设备的可用控件**

```uvcdynctrl -d [device_name] -c```

**获取控件的当前值**

```uvcdynctrl -g "[control_name]"```

**将控件设置为特定值**

```uvcdynctrl -s "[control_name]" -- [value]```

**列出支持的帧格式**

```uvcdynctrl -f```

**将当前控件状态保存到文件**

```uvcdynctrl -W [filename]```

**从文件加载控件状态**

```uvcdynctrl -L [filename]```

# SYNOPSIS

**uvcdynctrl** [_OPTIONS_] [_VALUES_]

# PARAMETERS

**-l**, **--list**
> 列出所有已连接的 UVC 摄像头。

**-d**, **--device** _NAME_
> 使用指定的设备（默认：video0）。

**-c**, **--clist**
> 列出所选设备的可用控件。

**-g**, **--get** _CONTROL_
> 获取控件的当前值。

**-G**, **--get_raw** _unit_id:selector_
> 通过单元 ID 和选择器获取原始控件值。

**-s**, **--set** _CONTROL_ _VALUE_
> 将控件设置为给定的值。

**-S**, **--set_raw** _unit_id:selector_ _VALUE_
> 设置原始控件值（十六进制字符串；大端序需加 (BE) 前缀）。

**-f**, **--formats**
> 列出支持的帧格式。

**-i**, **--import** _FILE_
> 从 XML 文件导入动态控件。

**-a**, **--addctrl** _VID_
> 从系统默认位置加载某个厂商 ID 的动态控件。

**-W**, **--save** _FILE_
> 将设备控件状态保存到文件。

**-L**, **--load** _FILE_
> 从文件加载设备控件状态。

**-v**, **--verbose**
> 启用详细输出。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**uvcdynctrl** 管理 Linux 内核 uvcvideo 驱动中的动态控件。它可以调整亮度、对比度、曝光、白平衡等摄像头设置，以及其他 UVC 特有的控件。

该工具可与兼容 USB Video Class（UVC）的网络摄像头配合使用。它还能从 XML 文件导入自定义控件定义，用于厂商特有的扩展功能。

# CAVEATS

只适用于兼容 UVC 的摄像头。可用控件取决于硬件。对于负值，请在数值前使用 **--**，以防止被解析为选项标志。

# INSTALL

```apt: sudo apt install uvcdynctrl```

```dnf: sudo dnf install uvcdynctrl```

```zypper: sudo zypper install uvcdynctrl```

```nix: nix profile install nixpkgs#uvcdynctrl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[v4l2-ctl](/man/v4l2-ctl)(1), [v4l2loopback-ctl](/man/v4l2loopback-ctl)(1)
