# TAGLINE

GNOME 桌面的官方图片查看器

# TLDR

**打开**图片文件

```eog [path/to/image.png]```

打开**多张**图片

```eog [image1.jpg] [image2.png]```

以**全屏**模式打开图片

```eog --fullscreen [path/to/image.jpg]```

启动**幻灯片放映**

```eog --slide-show [path/to/directory]```

打开单张图片且**不显示**图片集面板

```eog --disable-gallery [path/to/image.jpg]```

在**新的**实例中打开图片

```eog --new-instance [path/to/image.jpg]```

# SYNOPSIS

**eog** [_options_] [_files..._]

# DESCRIPTION

**eog**（Eye of GNOME）是 GNOME 桌面环境的官方图片查看器。它提供快速、轻量的界面，可显示 JPEG、PNG、GIF、SVG、TIFF、BMP 等多种格式的图片。该查看器支持幻灯片放映、全屏浏览、缩放、旋转以及基本的图像操作。

该应用与 GNOME 桌面服务和文件管理器深度集成，支持拖放、缩略图生成和 EXIF 元数据显示。虽然为 GNOME 设计，eog 也可以在其他桌面环境中运行，但部分功能可能依赖 GNOME 库。

# PARAMETERS

**-f**, **--fullscreen**
> 以全屏模式打开。

**-s**, **--slide-show**
> 以幻灯片放映模式打开。

**-g**, **--disable-gallery**
> 禁用图片集（gallery）面板。

**-n**, **--new-instance**
> 在新实例中打开，而不是复用已有实例。

**-w**, **--single-window**
> 强制所有图片在同一个窗口中打开。

**--display=**_DISPLAY_
> 要使用的 X display。

**--version**
> 显示版本信息。

**-?**, **--help**
> 显示帮助消息。

# CONFIGURATION

**~/.config/eog/**
> 用户配置目录，存放通过 GNOME 管理的首选项。

**dconf/gsettings**
> 可通过 `gsettings` 访问的设置，对应 `org.gnome.eog` schema，控制界面、插件和行为。

# CAVEATS

为 GNOME 桌面设计；部分功能在 GNOME 之外可能无法使用。大图可能占用大量内存。自 GNOME 43 起，许多发行版已用 **Loupe**（用 Rust 编写的新一代 GNOME 默认图片查看器）取代 eog。

# INSTALL

```apt: sudo apt install eog```

```dnf: sudo dnf install eog```

```pacman: sudo pacman -S eog```

```apk: sudo apk add eog```

```zypper: sudo zypper install eog```

```nix: nix profile install nixpkgs#eog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [gpicview](/man/gpicview)(1), [gimp](/man/gimp)(1)
