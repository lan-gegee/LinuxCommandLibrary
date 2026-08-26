# TAGLINE

blink(1) USB RGB LED 控制器命令行工具

# TLDR

将 **blink(1) 设置为红色**

```blink1-tool --red```

设置为指定的**十六进制颜色**

```blink1-tool --rgb [ff00ff]```

**闪烁** LED 若干次

```blink1-tool --blink [3]```

在指定毫秒时长内**渐变**到某个颜色

```blink1-tool --rgb [00ff00] --fade [500]```

**关闭** LED

```blink1-tool --off```

设置要播放的 LED **图案**

```blink1-tool --play [1]```

列出**已连接的 blink(1) 设备**

```blink1-tool --list```

# SYNOPSIS

**blink1-tool** [_options_]

# PARAMETERS

**--rgb** _RRGGBB_
> 按十六进制 RGB 值设置颜色。

**--red**
> 将 LED 设为红色。

**--green**
> 将 LED 设为绿色。

**--blue**
> 将 LED 设为蓝色。

**--off**
> 关闭 LED。

**--blink** _N_
> 让 LED 闪烁 _N_ 次。

**--fade** _MILLIS_
> 在 _MILLIS_ 毫秒内渐变到目标颜色。

**--play** _N_
> 播放存储的图案 _N_。

**--list**
> 列出已连接的 blink(1) 设备。

**--savergb** _RRGGBB_,_POS_
> 将 RGB 颜色保存到图案中的指定位置。

**--savepattern**
> 将当前图案保存到设备。

**-l** _N_, **--led** _N_
> 选择要控制的 LED（0=全部，1=顶部，2=底部），适用于 blink(1) mk2 及以上。

**-q**, **--quiet**
> 抑制输出。

# DESCRIPTION

**blink1-tool** 是控制 ThingM 出品的 **blink(1)** USB RGB LED 指示灯的命令行界面。它可以设置颜色、创建闪烁模式、在颜色之间渐变，并管理设备上存储的灯光图案。

blink(1) 是一个内置可编程 RGB LED 的小型 USB 加密狗。它常被用作构建状态指示灯、通知灯、环境信息显示，以及由脚本或监控系统触发的可视化警报。

该工具通过 USB HID 直接与 blink(1) 硬件通信，无需特殊驱动。多个设备可以被独立寻址。

# CAVEATS

需要连接物理 blink(1) USB 设备。在 Linux 上，可能需要配置 udev 规则以允许非 root 用户访问。mk1 硬件仅支持单个 LED，而 mk2 及之后版本支持两个可独立寻址的 LED。

# HISTORY

**blink(1)** 由 **ThingM** 的 **Tod Kurt** 设计，于 **2012 年**在 Kickstarter 上成功众筹。blink1-tool 命令行工具是托管在 GitHub 上的开源 blink1 软件套件的一部分，支持 Linux、macOS 和 Windows。

# INSTALL

```brew: brew install blink```

```nix: nix profile install nixpkgs#blink```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsusb](/man/lsusb)(8)
