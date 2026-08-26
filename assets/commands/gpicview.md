# TAGLINE

LXDE 的轻量级图像查看器

# TLDR

**打开图像**

```gpicview [image.jpg]```

**启动 GPicView**

```gpicview```

# SYNOPSIS

**gpicview** [_options_] [_file_]

# PARAMETERS

_file_
> 要打开的图像文件。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**GPicView** 是 LXDE 桌面环境的轻量级图像查看器。它以极低的资源占用提供快速的图像浏览，支持 JPEG、PNG、GIF 和 BMP 等常见格式。

该查看器提供基本的导航、缩放、旋转和幻灯片放映功能。它的设计目标是简洁和响应迅速，非常适合资源有限的系统。

# KEYBOARD SHORTCUTS

```
Space/N     Next image
Backspace/P Previous image
+/=         Zoom in
-           Zoom out
1           Original size
F           Fit to window
R           Rotate right
L           Rotate left
F11         Fullscreen
```

# CAVEATS

编辑功能有限。不支持 RAW 格式。属于 LXDE 但也可独立运行。功能可能不及 gThumb 等更重量级的查看器丰富。

# HISTORY

GPicView 作为 **LXDE**（Lightweight X11 Desktop Environment）项目的一部分创建，专为在低资源系统上实现快速性能而设计。它遵循 LXDE 轻量、简洁的理念。

# INSTALL

```apt: sudo apt install gpicview```

```dnf: sudo dnf install gpicview```

```pacman: sudo pacman -S gpicview```

```apk: sudo apk add gpicview```

```zypper: sudo zypper install gpicview```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [eog](/man/eog)(1), [sxiv](/man/sxiv)(1), [imv](/man/imv)(1)

# RESOURCES

```[Source code](https://github.com/lxde/gpicview)```

```[Homepage](https://wiki.lxde.org/en/GPicView)```

<!-- verified: 2026-07-17 -->
