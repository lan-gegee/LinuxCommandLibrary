# TAGLINE

简单轻量的 X11 图片查看器

# TLDR

**打开**图片

```sxiv path/to/image```

以**全屏**模式打开

```sxiv -f path/to/image```

从**标准输入**读取文件名

```echo path/to/file | sxiv -i```

以**幻灯片**方式打开

```sxiv -S 3 path/to/image1 path/to/image2```

以**缩略图**模式打开

```sxiv -t path/to/images/*```

**递归**搜索目录

```sxiv -r path/to/directory```

# SYNOPSIS

**sxiv** [_options_] _FILE_...

# DESCRIPTION

**sxiv** 是一个简单的 X 图片查看器。它有两种模式：用于显示单张图片的图像模式，以及用于网格视图选择的缩略图模式。它支持键盘导航、缩放、旋转和幻灯片功能。

# PARAMETERS

**-f**
> 以全屏模式启动

**-b**
> 不显示底部信息栏

**-t**
> 以缩略图模式启动

**-i**
> 从标准输入读取文件列表

**-r**
> 递归搜索目录中的图片

**-o**
> 退出时将被标记的文件写入标准输出

**-a**
> 播放多帧图片的动画

**-A FRAMERATE**
> 设置动画帧率

**-s MODE**
> 设置缩放模式（d=down，f=fit，F=fill，w=width，h=height）

**-z ZOOM**
> 以百分比设置缩放级别

**-g GEOMETRY**
> 设置窗口几何参数（WxH+X+Y）

**-G GAMMA**
> 设置伽马校正（-32 到 32）

**-S SECONDS**
> 以指定间隔启动幻灯片

**-n NUM**
> 从第 NUM 张图片开始

**-c**
> 清理缩略图缓存

**-q**
> 抑制警告信息

# CAVEATS

全屏功能需要符合 EWMH/NetWM 规范的窗口管理器。缩略图缓存存储在 $XDG_CACHE_HOME/sxiv/。自定义按键处理器可在 $XDG_CONFIG_HOME/sxiv/exec/key-handler 中定义。

# HISTORY

**sxiv**（Simple X Image Viewer）的定位是更重量级图片查看器的轻量替代品，专注于速度和键盘驱动的操作。

# INSTALL

```apt: sudo apt install sxiv```

```dnf: sudo dnf install sxiv```

```pacman: sudo pacman -S sxiv```

```zypper: sudo zypper install sxiv```

```nix: nix profile install nixpkgs#sxiv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [imv](/man/imv)(1), [nsxiv](/man/nsxiv)(1)
