# TAGLINE

在终端中显示图像和视频

# TLDR

在终端中**显示图像**

```timg [path/to/image.png]```

以网格形式**显示多张图片**

```timg --grid=2 [image1.png] [image2.png]```

在终端中**播放视频**

```timg [path/to/video.mp4]```

无限循环**显示动图 GIF**

```timg --loops=-1 [animation.gif]```

**显示来自 stdin 的图像**

```curl -s [url/to/image.png] | timg -```

**使用 Kitty 图形协议**获得高分辨率输出

```timg -pk [path/to/image.png]```

**以指定尺寸显示**

```timg -g [80x24] [path/to/image.png]```

# SYNOPSIS

**timg** [_options_] _file_ [_file_...]

# PARAMETERS

**-g** _WxH_
> 以字符单元格表示的输出几何尺寸。默认为终端大小。

**-p** _mode_
> 像素化模式：h（半块）、q（四分之一块）、k（kitty 协议）、i（iTerm2 协议）、s（sixel）。

**--grid**=_cols_
> 将图像排成具有指定列数的网格。

**--loops**=_num_
> 动画循环次数。-1 表示无限；视频默认为 1，GIF 默认为无限。

**--frames**=_num_
> 只显示动画的前 num 帧。

**--color8**
> 为较旧的终端使用 8 位颜色模式（216 色）。

**--center**
> 在可用空间内居中显示图像。

**--clear**
> 显示前清屏。

**-C**
> 动画播放时每帧前都清屏。

**-V**
> 将 stdin 解释为视频流。

**--threads**=_n_
> 图像解码线程数。默认为 CPU 核心数的 3/4。

**--verbose**
> 打印终端、像素化和帧率相关信息。

**-h**, **--help**
> 显示帮助信息或详细 manpage。

**--version**
> 打印版本信息后退出。

# DESCRIPTION

**timg** 是一款终端图像和视频查看器，使用 Unicode 方块字符和 24 位 ANSI 颜色直接在终端中显示图形。它支持多种格式，包括 JPEG、PNG、GIF、WebP、BMP，以及 MP4、AVI、MKV 等视频格式。

该查看器能适配不同的终端能力：基础终端使用半块或四分之一块 Unicode 字符，支持的终端则使用原生图形协议（Kitty、iTerm2、Sixel）以获得更高分辨率的输出。这让它非常适合在 SSH 会话、脚本或终端工作流中预览图像。

图像可以单独显示、依次显示或排列成网格布局。动态 GIF 和视频可以直接在终端中播放，循环次数和帧率均可配置。

# CAVEATS

画质取决于终端能力。基础的 Unicode 方块渲染只能提供近似颜色和低分辨率。要获得最佳效果，请使用支持 Kitty 图形协议、iTerm2 图形或 Sixel 协议的终端。视频播放性能取决于终端的渲染速度。

# HISTORY

**timg** 由 **Henner Zeller** 创建，开发始于约 **2016 年**。它的目标是把图像和视频查看能力带到终端中，利用了 24 位颜色支持和图形协议等现代终端特性。该项目持续活跃开发，定期加入新特性和格式支持。

# INSTALL

```apt: sudo apt install timg```

```dnf: sudo dnf install timg```

```apk: sudo apk add timg```

```zypper: sudo zypper install timg```

```brew: brew install timg```

```nix: nix profile install nixpkgs#timg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[imgcat](/man/imgcat)(1), [viu](/man/viu)(1), [chafa](/man/chafa)(1), [feh](/man/feh)(1)
