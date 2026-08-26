# TAGLINE

面向 X11 的轻量级键盘驱动图像查看器

# TLDR

**打开图片**

```nsxiv [path/to/file1 path/to/file2 ...]```

以图像模式打开**目录**中的图片

```nsxiv [path/to/directory1 path/to/directory2 ...]```

**递归**搜索目录中的图片并查看

```nsxiv -r [path/to/directory1 path/to/directory2 ...]```

**退出** nsxiv

```q```

切换到**缩略图模式**或打开选中的图片

```Enter```

查看**下一张/上一张**图片

```n / p```

# SYNOPSIS

**nsxiv** [_options_] _files_|_directories_...

# PARAMETERS

**-r, --recursive**
> 递归搜索目录中的图片

**-t, --thumbnail**
> 以缩略图模式启动

**-f, --fullscreen**
> 以全屏模式启动

**-s _mode_**
> 缩放模式：fit、fill、width、height

**-g _geometry_**
> 窗口几何尺寸（WxH+X+Y）

**-b**
> 隐藏信息栏

**-q**
> 安静模式；抑制警告

**-o**
> 退出时将选中的文件输出到 stdout

# DESCRIPTION

**nsxiv**（Neo Simple X Image Viewer）是一个面向 X11 的轻量级键盘驱动图像查看器。它是原 sxiv 的分支，增加了新功能并获得积极维护。

该查看器有两种模式：用于查看单张图片（支持缩放和平移）的**图像模式**，以及用于浏览多张图片的**缩略图模式**。导航使用类似 vim 的按键绑定：**h/j/k/l** 或方向键，**n/p** 切换下一张/上一张。

图片可以被标记以便批量操作，选中结果可输出到 stdout 供脚本使用。外部命令可以通过 shell 脚本进行配置。

# CAVEATS

仅支持 X11；在没有 XWayland 的情况下无法在 Wayland 中工作。通过 imlib2 支持常见图片格式（JPEG、PNG、GIF 等）。动画 GIF 支持有限。自定义按键绑定需要重新编译。

# HISTORY

nsxiv 是 sxiv（simple X image viewer）的社区分支，在原项目停止维护后创建。它在保持极简理念的同时继续积极开发新功能。

# INSTALL

```apt: sudo apt install nsxiv```

```pacman: sudo pacman -S nsxiv```

```apk: sudo apk add nsxiv```

```nix: nix profile install nixpkgs#nsxiv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sxiv](/man/sxiv)(1), [feh](/man/feh)(1), [imv](/man/imv)(1), [viewnior](/man/viewnior)(1)
