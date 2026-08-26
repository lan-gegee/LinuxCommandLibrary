# TAGLINE

简单快速的图片查看器

# TLDR

**打开图片文件**

```viewnior [path/to/image.jpg]```

**以全屏模式打开图片**

```viewnior --fullscreen [path/to/image.jpg]```

**从图片或目录开始幻灯片放映**

```viewnior --slideshow [path/to/image.jpg]```

**浏览目录中的所有图片**

```viewnior [path/to/folder/]```

# SYNOPSIS

**viewnior** [_OPTIONS_] [_FILES_|_FOLDERS_]...

# DESCRIPTION

**viewnior** 是一个简洁优雅的图片查看器，设计上追求极简、速度和易用性。它提供干净的界面，最大化利用屏幕空间来查看图片。

# PARAMETERS

**--fullscreen**
> 以全屏模式启动查看器。

**--slideshow**
> 以幻灯片模式启动。

**--version**
> 显示版本信息并退出。

**-?, --help**
> 显示帮助信息并退出。

# CAVEATS

通过 GDK-Pixbuf 支持常见图片格式（JPEG、PNG、GIF、BMP、SVG 等）。使用方向键或鼠标滚轮在文件夹中的图片之间切换。幻灯片间隔可在首选项对话框中配置。

# HISTORY

**viewnior** 由 Siyan Panayotov 开发，作为更臃肿的图片查看器的快速、简单替代品，专注于为 Linux 桌面用户提供极简界面。

# INSTALL

```apt: sudo apt install viewnior```

```dnf: sudo dnf install viewnior```

```pacman: sudo pacman -S viewnior```

```zypper: sudo zypper install viewnior```

```nix: nix profile install nixpkgs#viewnior```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [sxiv](/man/sxiv)(1), [eog](/man/eog)(1), [gpicview](/man/gpicview)(1)
