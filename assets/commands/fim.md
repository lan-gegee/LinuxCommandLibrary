# TAGLINE

帧缓冲与终端图像查看器

# TLDR

**在帧缓冲或终端中查看图像**

```fim [image.jpg]```

**查看目录中的所有图像**

```fim [path/to/directory/]```

**递归查看图像**并排序

```fim -R [path/to/directory/] --sort```

**强制 ASCII 艺术输出**（适用于无图形能力的终端）

```fim -t [image.jpg]```

**启用自动缩放**，使图像适配屏幕

```fim -a [image.jpg]```

**以 5 秒间隔放映幻灯片**

```fim --slideshow [5] [path/to/directory/]```

**显式指定输出设备**

```fim --output-device [sdl|fb|aa|ca] [image.jpg]```

# SYNOPSIS

**fim** [_OPTIONS_] [**--**] _IMAGEPATH_ [_IMAGEPATHS_...]

# PARAMETERS

**-a**, **--autozoom**
> 自动为每张图像选择合理的缩放系数。

**-t**, **--no-framebuffer**
> 使用 ASCII 艺术驱动（libcaca 支持彩色，aalib 支持单色）。

**-R**
> 递归加载目录中的图像。

**--sort**
> 按字母顺序对文件列表排序。

**--slideshow** _SECONDS_
> 以幻灯片模式运行，每张图像之间暂停指定秒数。

**--output-device** _DEVICE_
> 强制指定输出设备：fb（帧缓冲）、sdl、gtk、aa（aalib）、ca（libcaca）、dumb。

**-c** _COMMAND_
> 启动后执行命令。

**-F** _FILE_
> 执行脚本文件中的命令。

**--no-auto-scale**
> 禁用自动缩放。

**-v**, **--verbose**
> 详细模式：显示状态栏。

**-V**, **--version**
> 显示版本和编译标志，然后退出。

**-P**, **--text-reading**
> 启用文本阅读模式。将图像缩放到屏幕宽度并顶部对齐。

**-S**, **--sanity-check**
> 启动前先做一次快速合理性检查。

**-h**, **--help**
> 显示帮助信息。

# KEYBINDINGS

**h、j、k、l** 或方向键
> 向左、向下、向上、向右滚动大尺寸图像。

**+**, **-**
> 放大 / 缩小。

**n**, **PgDn**
> 下一张图像。

**p**, **PgUp**
> 上一张图像。

**Tab**
> 切换输出控制台是否可见。

**q**, **ESC**
> 退出。

# CONFIGURATION

**~/.fimrc**
> FIM 设置、按键绑定和启动命令的用户配置文件。

# DESCRIPTION

**FIM**（Fbi IMproved）是一款用途广泛的图像查看器，可以在不同图形环境下工作。它会自动挑选最合适的显示方式：在 X 下使用 SDL，在控制台使用帧缓冲，没有任何图形输出可用时则改用 ASCII 艺术（经 aalib/libcaca）。

FIM 原生支持常见图像格式（BMP、PCX），并通过各种库支持 JPEG、PNG、GIF、TIFF、PPM、WEBP、AVIF 等格式。其余格式可以借助外部转换器来支持。配套脚本 **fimgs** 能显示 PDF、PostScript、DVI 以及包含图像的压缩归档。

这款查看器完全以键盘为中心，没有图形菜单。它内置了一套命令语言供脚本化和定制使用，并且能够与标准输入/输出交互，方便接入管道。

# CAVEATS

访问帧缓冲通常需要相应权限（加入 video 组或使用 root）。ASCII 艺术输出的效果取决于终端能力以及 aalib/libcaca 库。部分图像格式需要额外安装对应的库才能支持。

# HISTORY

FIM 由 Michele Martone 开发，是对 Gerd Hoffmann 所创 **fbi**（Linux 帧缓冲图像查看器）的改进版本。FIM 在保留适合控制台场景的键盘驱动操作方式的同时，为 fbi 扩展了多个输出后端、内部脚本语言和众多增强功能。

# INSTALL

```apt: sudo apt install fim```

```nix: nix profile install nixpkgs#fim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fbi](/man/fbi)(1), [feh](/man/feh)(1), [display](/man/display)(1)
