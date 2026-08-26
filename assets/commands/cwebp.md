# TAGLINE

Google WebP 图像编码器

# TLDR

将图像**转换为 WebP** 格式

```cwebp [input.png] -o [output.webp]```

以指定质量转换（0-100）

```cwebp -q [80] [input.jpg] -o [output.webp]```

创建无损 WebP

```cwebp -lossless [input.png] -o [output.webp]```

转换时调整大小

```cwebp -resize [800] [600] [input.jpg] -o [output.webp]```

转换时保留 alpha 通道

```cwebp -alpha_q [100] [input.png] -o [output.webp]```

使用近无损压缩

```cwebp -near_lossless [60] [input.png] -o [output.webp]```

最大压缩力度（最慢、最小）

```cwebp -m 6 -q [80] [input.jpg] -o [output.webp]```

使用针对照片调校的预设

```cwebp -preset photo -q [80] [input.jpg] -o [output.webp]```

# SYNOPSIS

**cwebp** [_options_] _input_file_ **-o** _output_file.webp_

# PARAMETERS

**-o** _FILE_
> 输出 WebP 文件路径。

**-q** _QUALITY_
> 压缩质量（0-100，默认 75）。数值越高质量越好。

**-lossless**
> 无损编码图像。

**-near_lossless** _LEVEL_
> 近无损预处理（0-100，默认 100 = 不做预处理；通常取 60）。会触发无损模式。

**-alpha_q** _QUALITY_
> Alpha 通道质量（0-100，默认 100 = 无损 alpha）。

**-resize** _WIDTH_ _HEIGHT_
> 缩放到指定尺寸。某一维取 0 时保持宽高比。

**-crop** _X_ _Y_ _W_ _H_
> 将输入图像裁剪到位于 (_X_,_Y_)、宽 _W_ 高 _H_ 的矩形区域。

**-preset** _NAME_
> 预设：default、photo、picture、drawing、icon、text。必须放在其他选项之前。

**-m** _METHOD_
> 压缩方法（0-6，默认 4；数值越高越慢但文件越小）。

**-z** _LEVEL_
> 无损压缩预设（0-9，0 最快 / 9 最慢；推荐 6）。

**-exact**
> 保留完全透明区域的 RGB 值（仅限无损模式）。

**-mt**
> 可用时启用多线程。

**-v**
> 详细输出。

# DESCRIPTION

**cwebp** 是 Google 的 WebP 图像格式编码器。与 JPEG 和 PNG 相比，WebP 提供更优的压缩率，同时支持有损和无损模式，还支持动画和 alpha 透明度。

该编码器接受 PNG、JPEG、TIFF 和 WebP 输入（不支持动画 PNG 和动画 WebP）。有损压缩时，**-q** 参数控制质量与大小的权衡。无损压缩时，**-z** 参数控制压缩力度。使用 **-o -** 会把编码结果输出到 stdout。

WebP 得到了浏览器的广泛支持，在同等质量下文件比 JPEG 小 25-34%。无损模式生成的文件通常比 PNG 小 26%。

# CAVEATS

极高的质量设置可能生成比源文件更大的文件。一些旧软件不支持 WebP。有损 WebP 会引入类似 JPEG 的压缩痕迹。近无损模式会轻微修改像素以获得更好的压缩率。

# HISTORY

WebP 由 **Google** 开发并于 **2010 年**发布，基于 VP8 视频编解码器。cwebp 编码器是 libwebp 参考实现的一部分。WebP 到 **2020 年**已获得各大浏览器的普遍支持，并被推荐用于 Web 图像优化。

# INSTALL

```apt: sudo apt install webp```

```dnf: sudo dnf install libwebp-tools```

```apk: sudo apk add libwebp-tools```

```zypper: sudo zypper install libwebp-tools```

```brew: brew install webp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dwebp](/man/dwebp)(1), [gif2webp](/man/gif2webp)(1), [cjpeg](/man/cjpeg)(1), [convert](/man/convert)(1)
