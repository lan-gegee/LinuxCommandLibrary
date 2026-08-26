# TAGLINE

将图片转换为 AVIF 格式

# TLDR

**将图片转换为 AVIF 格式**

```cavif [path/to/image.png]```

**以指定质量转换（1-100）**

```cavif --quality [80] [path/to/image.jpg]```

**以更快的编码速度转换（1-10）**

```cavif --speed [6] [path/to/image.png]```

**转换并指定输出路径**

```cavif -o [path/to/output.avif] [path/to/image.png]```

**将多张图片转换到某个目录**

```cavif -o [path/to/output_dir/] [image1.png] [image2.jpg]```

**覆盖已有的 AVIF 文件**

```cavif --overwrite [path/to/image.png]```

# SYNOPSIS

**cavif** [**--quality** _1-100_] [**--speed** _1-10_] [**-o** _path_] [**--overwrite**] [**--quiet**] _file..._

# DESCRIPTION

**cavif** 是一个用 Rust 编写的命令行工具，用于将 PNG 和 JPEG 图片转换为 AVIF（AV1 Image File Format）。AVIF 采用 AV1 视频编解码器的压缩技术，在保持画质的同时提供优于 JPEG 的压缩率。

默认情况下，输出文件使用相同的文件名，但扩展名为 **.avif**。除非指定 **--overwrite**，否则不会覆盖已有文件。

# PARAMETERS

**--quality** _1-100_
> 输出质量等级。数值越高画质越好、文件越大。默认：80

**--speed** _1-10_
> 编码速度。1 最慢但压缩率最好，10 最快但质量较低。默认：4

**-o** _path_
> 输出路径。有多个输入时视为目录

**--overwrite**
> 替换已有的 .avif 文件而不是跳过它们

**--quiet**
> 转换过程中抑制输出

**--dirty-alpha**
> 保留全透明像素的 RGB 值（会增大文件体积）

**--color=rgb**
> 以 RGB 色彩空间而不是 YCbCr 编码。避免色彩偏移但生成的文件更大

**--depth=**_8_
> 使用 8 位色深编码而不是默认的 10 位，以获得更好的兼容性

# CAVEATS

速度 1-2 极慢，但生成的文件小约 3-5%。速度 7 及以上会明显降低压缩效果，不建议使用。

没有无损压缩模式；quality 100 会产生大得离谱的文件，而且并非真正无损。

从源码构建需要 Rust 1.67 或更高版本。

# HISTORY

**cavif** 由 Kornel Lesinski 创建，是 AVIF 编码器的纯 Rust 实现。AVIF 本身由开放媒体联盟（Alliance for Open Media）于 **2019** 年标准化，利用 AV1 视频编解码器进行静态图像压缩。

# INSTALL

```nix: nix profile install nixpkgs#cavif```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cwebp](/man/cwebp)(1), [convert](/man/convert)(1)
