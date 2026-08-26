# TAGLINE

在终端中显示图片

# TLDR

**显示图片**

```viu [image.png]```

**设置宽度**

```viu -w [80] [image.png]```

**设置高度**

```viu -h [40] [image.png]```

**显示多张图片**

```viu [image1.png] [image2.png]```

**使用整块字符代替半块字符**

```viu -b [image.png]```

**透明背景**

```viu -t [image.png]```

**从标准输入读取**

```cat [image.png] | viu -```

# SYNOPSIS

**viu** [_-w width_] [_-h height_] [_options_] _files_

# PARAMETERS

**-w**, **--width** _N_
> 输出宽度。

**-h**, **--height** _N_
> 输出高度。

**-b**, **--blocks**
> 使用整块字符。

**-t**, **--transparent**
> 透明背景。

**-n**, **--name**
> 显示文件名。

**-r**, **--recursive**
> 递归处理目录。

**-f**, **--frame-rate** _N_
> GIF 帧率。

# DESCRIPTION

**viu** 是一个用 Rust 编写的终端图片查看器，它使用 Unicode 半块字符和 24 位 ANSI 颜色代码直接在终端中渲染图片。它支持 PNG、JPEG、GIF、WebP 和 BMP 等常见图片格式，按终端字符网格所决定的分辨率进行显示。

输出尺寸可以通过宽度和高度选项控制；当只指定其中一个维度时，默认会保持纵横比。另一种块状渲染模式使用整块字符，呈现不同的视觉密度；对于带 alpha 通道的图片，可以启用透明背景。

动画 GIF 可直接在终端中播放，帧率可配置。该工具还能从标准输入读取，因此可以接入管道：用 curl 获取或由其他程序生成的图片可以直接通过管道传给 viu 显示。

# CAVEATS

画质取决于终端。支持真彩色可改善输出。大图片速度较慢。

# HISTORY

**viu** 是一个基于 Rust 的终端图片查看器。它在现代终端中提供快速、高质量的图片显示。

# INSTALL

```pacman: sudo pacman -S viu```

```apk: sudo apk add viu```

```zypper: sudo zypper install viu```

```brew: brew install viu```

```nix: nix profile install nixpkgs#viu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chafa](/man/chafa)(1), [catimg](/man/catimg)(1), [tiv](/man/tiv)(1)
