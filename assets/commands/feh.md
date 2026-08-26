# TAGLINE

轻量级 X11 图像查看器

# TLDR

**查看图像**

```feh [image.jpg]```

以幻灯片形式**查看目录**

```feh -D [5] [directory]```

**设置壁纸**

```feh --bg-scale [image.jpg]```

**缩略图模式**

```feh -t [directory]```

**全屏模式**

```feh -F [image.jpg]```

# SYNOPSIS

**feh** [_options_] [_files_|_directories_|_URLs_]

# PARAMETERS

_FILES_
> 要显示的图像。

**-F**, **--fullscreen**
> 以全屏模式启动。

**-D** _SEC_, **--slideshow-delay** _SEC_
> 幻灯片延迟（秒）。

**-t**, **--thumbnails**
> 缩略图浏览模式。

**--bg-scale** _IMAGE_
> 使图像适应屏幕（可能变形）。

**--bg-fill** _IMAGE_
> 填满屏幕并保持宽高比（可能裁剪）。

**--bg-max** _IMAGE_
> 缩放至适配且不裁剪（可能留有边框）。

**--bg-center** _IMAGE_
> 居中图像而不缩放。

**--bg-tile** _IMAGE_
> 平铺图像铺满屏幕。

**-g** _WxH_, **--geometry** _WxH_
> 限制窗口大小。

**-Z**, **--auto-zoom**
> 缩放以适配窗口。

**-r**, **--recursive**
> 递归进入子目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**feh** 是一款轻量、快速的 X11 图像查看器。它支持幻灯片放映、缩略图浏览、拼贴图，并可通过命令行控制设置桌面壁纸。

该查看器支持多种图像格式，提供键盘和鼠标控制进行导航和缩放。它可以从文件、目录、stdin 或 URL 读取图像。

feh 在缺少内置壁纸支持的窗口管理器中特别受欢迎，常用于设置壁纸。

# CAVEATS

仅支持 X11（无原生 Wayland 支持）。大图可能加载缓慢。壁纸设置需要在启动时运行。

# HISTORY

feh 由 **Tom Gilbert** 于 1999 年创建，是一款快速简洁的 X11 图像查看器。它至今仍广泛用于精简的 Linux 环境，尤其是其设置壁纸的功能。

# INSTALL

```apt: sudo apt install feh```

```dnf: sudo dnf install feh```

```pacman: sudo pacman -S feh```

```apk: sudo apk add feh```

```zypper: sudo zypper install feh```

```brew: brew install feh```

```nix: nix profile install nixpkgs#feh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sxiv](/man/sxiv)(1), [nsxiv](/man/nsxiv)(1), [imv](/man/imv)(1)
