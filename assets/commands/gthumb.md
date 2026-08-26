# TAGLINE

GNOME 图像查看器和浏览器

# TLDR

**打开图像浏览器**

```gthumb```

**打开特定文件夹**

```gthumb [/path/to/photos]```

**打开特定图像**

```gthumb [image.jpg]```

**开始幻灯片放映**

```gthumb --slideshow [folder]```

**从相机导入**

```gthumb --import-photos```

# SYNOPSIS

**gthumb** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要打开的文件或文件夹。

**--slideshow**
> 开始幻灯片放映。

**--import-photos**
> 从设备导入。

**--fullscreen**
> 以全屏模式启动。

**-n**, **--new-window**
> 打开新窗口。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gThumb** 是一款 GNOME 图像查看器和浏览器。它支持查看、组织和编辑照片，并提供幻灯片放映和批量操作等功能。

该应用支持常见图像格式，提供调整大小、裁剪和色彩调整等工具。它与 GNOME 桌面深度集成。

# CAVEATS

依赖 GNOME 组件。某些功能需要插件。内存占用随图库大小增长。

# HISTORY

gThumb 由 **Paolo Bacchilega** 创建，是面向 **GNOME** 桌面环境的图像查看器。

# INSTALL

```apt: sudo apt install gthumb```

```dnf: sudo dnf install gthumb```

```pacman: sudo pacman -S gthumb```

```apk: sudo apk add gthumb```

```zypper: sudo zypper install gthumb```

```nix: nix profile install nixpkgs#gthumb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eog](/man/eog)(1), [feh](/man/feh)(1)
