# TAGLINE

解码 WebP 图像为其他格式

# TLDR

**将 WebP 转换为 PNG**

```dwebp [image.webp] -o [output.png]```

**转换为 PPM**

```dwebp [image.webp] -ppm -o [output.ppm]```

**转换为 BMP**

```dwebp [image.webp] -bmp -o [output.bmp]```

**仅显示图像信息**

```dwebp -info [image.webp]```

解码时**缩放图像**（0 表示保持宽高比）

```dwebp [image.webp] -resize [800] [0] -o [output.png]```

从图像中**裁剪**一个矩形区域

```dwebp [image.webp] -crop [x] [y] [width] [height] -o [output.png]```

**垂直翻转图像**

```dwebp -flip [image.webp] -o [output.png]```

# SYNOPSIS

**dwebp** [_options_] _input.webp_ **-o** _output_

# PARAMETERS

_INPUT_
> 要解码的 WebP 文件。

**-o** _FILE_
> 输出文件路径。

**-ppm**
> 输出 PPM 格式。

**-bmp**
> 输出 BMP 格式。

**-tiff**
> 输出 TIFF 格式。

**-pgm**
> 输出 PGM 格式（灰度）。

**-pam**
> 输出 PAM 格式（保留 alpha 通道）。

**-alpha**
> 仅输出 alpha 平面为灰度图像。

**-info**
> 仅打印图像信息。

**-flip**
> 垂直翻转图像。

**-crop** _x_ _y_ _w_ _h_
> 只解码图像的指定矩形区域。

**-resize** _width_ _height_（或 **-scale**）
> 对解码后的图像重新缩放。某一维取 0 时保持宽高比。

**-nofancy**
> 禁用高质量（fancy）上采样。

**-nodither**
> 禁用抖动。

**-mt**
> 使用多线程解码。

**-quiet**
> 抑制提示性输出。

**-v**
> 打印解码耗时。

**-version**
> 打印库版本并退出。

**-h**
> 显示帮助信息。

# DESCRIPTION

**dwebp** 将 WebP 图像解码为其他格式。它是 libwebp 软件包的一部分，提供 WebP 编解码的参考实现。

该工具同时支持有损和无损 WebP 图像，包括带 alpha 透明通道的图像。除非另行指定，输出格式默认为 PNG。

dwebp 适用于将来自网络的 WebP 图像转换为那些原生不支持 WebP 的工具所能处理的格式。

# CAVEATS

输出文件的扩展名不决定格式；请使用格式标志。dwebp 不处理动画 WebP 文件，只会输出其第一帧或什么都不输出：动画请使用 anim_dump 或 webpmux。PNG 是默认输出格式，且在构建时需要 libpng。

# HISTORY

dwebp 是 **libwebp** 的一部分，后者是 Google 的 WebP 图像格式参考实现。WebP 由 Google 于 **2010 年**推出，是一种面向网络使用的高效图像格式。

# INSTALL

```apt: sudo apt install webp```

```dnf: sudo dnf install libwebp-tools```

```apk: sudo apk add libwebp-tools```

```zypper: sudo zypper install libwebp-tools```

```brew: brew install webp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cwebp](/man/cwebp)(1), [gif2webp](/man/gif2webp)(1), [convert](/man/convert)(1)

# RESOURCES

```[Source code](https://chromium.googlesource.com/webm/libwebp)```

```[Homepage](https://developers.google.com/speed/webp)```

```[Documentation](https://developers.google.com/speed/webp/docs/dwebp)```

<!-- verified: 2026-07-14 -->
