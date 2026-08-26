# TAGLINE

framebuffer 图像查看器

# TLDR

**显示**图像

```sudo fbi [path/to/file]```

显示**多张**图像

```sudo fbi [path/to/file1] [path/to/file2]```

以自定义延迟启动**幻灯片放映**

```sudo fbi [-t|--timeout] [delay] [path/to/files/*]```

**缩放**图像以适配屏幕

```sudo fbi [-a|--autozoom] [path/to/file]```

显示**帮助**

```fbi [-h|--help]```

# SYNOPSIS

**fbi** [_options_] _files_

# DESCRIPTION

**fbi**（framebuffer imageviewer）直接在 Linux framebuffer 控制台上显示图像，无需 X11 或 Wayland。它支持多种图像格式，包括 JPEG、PNG、GIF 和 TIFF。

适用于在无头服务器或精简系统上查看图像。

# PARAMETERS

**-t**, **--timeout** _seconds_
> 幻灯片放映中图像之间的延迟

**-a**, **--autozoom**
> 缩放以适配屏幕

**-h**, **--help**
> 显示帮助

**-1**, **--once**
> 不循环播放幻灯片

**-u**, **--random**
> 随机化幻灯片顺序

# CAVEATS

需要 framebuffer 支持。通常需要 root 或控制台访问权限。fbida 软件包的一部分。不适用于 X11/Wayland 会话。

# INSTALL

```apt: sudo apt install fbi```

```apk: sudo apk add fbida-fbi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fim](/man/fim)(1), [feh](/man/feh)(1), [fbset](/man/fbset)(1)
