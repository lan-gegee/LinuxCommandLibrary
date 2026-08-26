# TAGLINE

从一系列输入图像创建动画 WebP 文件

# TLDR

**从图像序列创建动画 WebP**

```img2webp [frame1.png] [frame2.png] [frame3.png] -o [animation.webp]```

# SYNOPSIS

**img2webp** [_options_] _input_ **-o** _output_

# PARAMETERS

**-o** _FILE_
> 输出的 WebP 文件名

**-lossy**
> 使用有损压缩

**-lossless**
> 使用无损压缩（默认）

**-q** _QUALITY_
> 质量因子（0-100，默认 75）

**-m** _METHOD_
> 压缩方法（0-6，默认 4）

**-loop** _COUNT_
> 动画的循环次数（0 = 无限循环）

**-d** _MS_
> 动画每帧的持续时间（毫秒）

# DESCRIPTION

**img2webp** 从一系列输入图像创建动画 WebP 文件。每个输入帧可以有各自的压缩设置（有损或无损）和持续时间。若要将单张图像转换为 WebP，请改用 **cwebp**。

该工具对每一帧都支持有损和无损两种压缩模式，并可配置动画循环次数和帧持续时间。

# CAVEATS

属于 libwebp 软件包。输入格式的支持取决于所链接的库。非常老的浏览器可能不支持 WebP 格式。部分图像编辑器对 WebP 的支持有限。

# HISTORY

WebP 由 Google 开发，于 **2010 年**发布，是一种开放的网络压缩图像标准。该格式基于 VP8 视频编解码器，与传统格式相比可显著减小文件体积。

# INSTALL

```apt: sudo apt install webp```

```dnf: sudo dnf install libwebp-tools```

```apk: sudo apk add libwebp-tools```

```zypper: sudo zypper install libwebp-tools```

```brew: brew install webp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cwebp](/man/cwebp)(1), [dwebp](/man/dwebp)(1), [gif2webp](/man/gif2webp)(1)
