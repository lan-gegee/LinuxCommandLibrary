# TAGLINE

将 GIF 图片转换为 WebP 格式

# TLDR

将 GIF 编码为 WebP 并**写出输出文件**

```gif2webp [input.gif] -o [output.webp]```

# SYNOPSIS

**gif2webp** [_options_] _input.gif_ **-o** _output.webp_

# PARAMETERS

**-o** _FILE_
> 输出的 WebP 文件名

**-q** _QUALITY_
> 质量因子（0-100），数值越高质量越好

**-m** _METHOD_
> 压缩方法（0-6），数值越高越慢但效果越好

**-lossy**
> 使用有损压缩（对 GIF 默认为无损）

**-mixed**
> 对每一帧混合使用有损/无损压缩

**-min_size**
> 最小化输出体积（更慢）

**-loop_compatibility**
> 对 GIF 循环次数使用兼容模式

**-f** _NUM_
> 滤波强度（0-100），用于有损压缩

**-metadata** _STRING_
> 要复制的元数据，逗号分隔（all、none、icc、xmp）

**-v**
> 详细输出

# DESCRIPTION

**gif2webp** 将 GIF 图片（包括动画 GIF）转换为 WebP 格式。WebP 通常在保持画质的同时提供比 GIF 更好的压缩率，生成的文件体积更小，适合网页使用。

对于动画 GIF，该工具会保留帧时序、循环次数和透明度。它同时支持无损压缩（精确保留像素值）和可获得更小文件的有损压缩。该工具是 Google 的 libwebp 软件包的一部分。

# CAVEATS

有损压缩可能引入伪影，在具有锐利边缘或文字的图像上尤为明显。一些旧版浏览器不支持动画 WebP。非常长或复杂的动画转换可能需要较长时间。

# HISTORY

gif2webp 是 Google 开发的 WebP 项目的一部分。WebP 于 **2010 年**发布，是一种面向 Web 的新图像格式，同时提供有损和无损压缩。动画 WebP 格式是后来加入的，用作动画 GIF 的替代方案。

# INSTALL

```apt: sudo apt install webp```

```dnf: sudo dnf install libwebp-tools```

```apk: sudo apk add libwebp-tools```

```zypper: sudo zypper install libwebp-tools```

```brew: brew install webp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cwebp](/man/cwebp)(1), [dwebp](/man/dwebp)(1), [convert](/man/convert)(1)
