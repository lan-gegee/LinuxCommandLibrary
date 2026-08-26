# TAGLINE

将 framebuffer 截图捕获为 PNG

# TLDR

对当前 framebuffer **截图**

```fbgrab [screenshot.png]```

从指定的 framebuffer 设备**截图**

```fbgrab -d [/dev/fb1] [screenshot.png]```

对指定的虚拟控制台**截图**

```fbgrab -c [1] [screenshot.png]```

截图前**等待 5 秒**

```fbgrab -s [5] [screenshot.png]```

**将原始 framebuffer 转储**转换为 PNG

```fbgrab -w [1920] -h [1080] -b [32] -f [framebuffer.dump] [screenshot.png]```

设置 PNG 压缩**级别**（0=最快，9=最佳）

```fbgrab -z [9] [screenshot.png]```

# SYNOPSIS

**fbgrab** [_options_] _filename_

# PARAMETERS

**-?**
> 显示用法信息。

**-a**
> 忽略 alpha 通道。对于 BGR32 等驱动程序错误报告 alpha 的像素格式很有用。

**-b** _bitdepth_
> 每像素位数。从设备读取时可选。

**-c** _console_
> 指定要抓取的控制台（虚拟终端）。

**-C** _console_
> 切换控制台并延迟后捕获。

**-d** _device_
> 要使用的 framebuffer 设备。默认为 FRAMEBUFFER 环境变量或 /dev/fb0。

**-f** _filename_
> 从文件而非设备读取。需要同时给出 -w、-h 和 -b 选项。

**-h** _height_
> framebuffer 的高度（像素）。从设备读取时可选。

**-i**
> 关闭输出 PNG 中的 ADAM7 隔行扫描。

**-l** _line_length_
> 每行起点之间的行长（步长，以像素为单位）。从设备读取时可选。

**-s** _seconds_
> 截图前等待的秒数。

**-v**
> 启用详细输出。

**-w** _width_
> framebuffer 的宽度（像素）。从设备读取时可选。

**-z** _compression_
> 设置 PNG 压缩级别（0=最快，9=最佳）。

# DESCRIPTION

**fbgrab** 读取 Linux framebuffer 设备（/dev/fb*）或其转储文件，并保存为 PNG 图像文件。它几乎可以为任何应用截图——从传统的文本程序到 X 窗口桌面和 framebuffer 应用。

该工具特别适用于在没有运行 X 服务器的系统、嵌入式系统上截图，或直接在 Linux 控制台下工作的情况。

# CAVEATS

**-c** 选项可能需要 root 权限或 CAP_SYS_TTY_CONFIG 能力。从原始转储文件读取时，必须同时指定 **-w**、**-h** 和 **-b** 选项。framebuffer 设备必须具有适当的访问权限。

# HISTORY

**fbgrab** 由 Gunnar Monell 编写，是对 Stephan Beyer 所写 fbshot 的重写。该工具自 2002 年以来持续维护，基于 GPL 第 2 版授权。

# INSTALL

```apt: sudo apt install fbcat```

```pacman: sudo pacman -S fbgrab```

```apk: sudo apk add fbgrab```

```zypper: sudo zypper install fbcat```

```nix: nix profile install nixpkgs#fbcat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scrot](/man/scrot)(1), [import](/man/import)(1), [fbi](/man/fbi)(1), [fbset](/man/fbset)(8)
