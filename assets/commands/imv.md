# TAGLINE

面向 Wayland 和 X11 的轻量级图像查看器，专为平铺窗口管理器设计

# TLDR

**查看**多张图像

```imv [path/to/image1] [path/to/image2]```

以**全屏**模式查看

```imv -f [path/to/image]```

**递归**加载目录中的图像并以幻灯片方式查看

```imv -r --slideshow [path/to/directory]```

以 10 秒间隔进行**幻灯片放映**

```imv -t 10 [path/to/directory]```

从 **stdin** 打开图像

```find . -name "*.svg" | imv```

# SYNOPSIS

**imv** [_options_] [_paths_]

# PARAMETERS

**-f**
> 以全屏模式启动

**-r**
> 递归加载目录

**-t** _SECONDS_
> 幻灯片间隔（秒）

**--slideshow**
> 以幻灯片模式启动

**-s** _MODE_
> 缩放模式（none、shrink、full、crop）

**-b** _COLOR_
> 设置背景颜色

**-d**
> 显示包含图像信息的叠加层

# DESCRIPTION

**imv** 是一款面向 Wayland 和 X11 的轻量级图像查看器，专为实现平铺式窗口管理器的工作流而设计。它支持大量图像格式，包括 PSD（Photoshop）、SVG 和动画 GIF。

该查看器以键盘驱动，默认采用类似 vim 的按键绑定。它可以从 stdin 读取文件列表，非常适合与其他命令行工具集成。功能包括缩放、平移、旋转和幻灯片模式。

# CAVEATS

格式支持需要相应的后端库。某些格式（如 PSD）需要可选依赖。按键绑定由配置文件控制。

# HISTORY

imv 的创建目的是提供一款适合平铺窗口管理器工作流的快速极简图像查看器。它同时支持 X11 和 Wayland，可在各种 Linux 桌面环境中通用。

# INSTALL

```apt: sudo apt install renameutils```

```dnf: sudo dnf install renameutils```

```pacman: sudo pacman -S renameutils```

```apk: sudo apk add imv```

```zypper: sudo zypper install renameutils```

```brew: brew install renameutils```

```nix: nix profile install nixpkgs#renameutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [sxiv](/man/sxiv)(1), [mpv](/man/mpv)(1)
