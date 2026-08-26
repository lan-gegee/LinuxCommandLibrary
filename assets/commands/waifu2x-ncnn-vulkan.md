# TAGLINE

基于 Vulkan 的 AI 图像放大工具

# TLDR

**放大图像**

```waifu2x-ncnn-vulkan -i [input.png] -o [output.png]```

**2 倍缩放**

```waifu2x-ncnn-vulkan -i [input.png] -o [output.png] -s [2]```

**降噪**

```waifu2x-ncnn-vulkan -i [input.png] -o [output.png] -n [2]```

**使用指定 GPU**

```waifu2x-ncnn-vulkan -i [input] -o [output] -g [0]```

**分块大小**

```waifu2x-ncnn-vulkan -i [input] -o [output] -t [400]```

# SYNOPSIS

**waifu2x-ncnn-vulkan** [_-i input_] [_-o output_] [_-s scale_] [_-n noise_]

# PARAMETERS

**-i** _FILE_
> 输入文件。

**-o** _FILE_
> 输出文件。

**-s** _SCALE_
> 缩放倍率（2）。

**-n** _LEVEL_
> 降噪级别（-1,0,1,2,3）。

**-g** _GPU_
> GPU 设备。

**-t** _SIZE_
> 分块大小。

# DESCRIPTION

**waifu2x-ncnn-vulkan** 是一款基于 AI 的图像放大与降噪工具，利用卷积神经网络在放大图像的同时保留细节。它对动漫风格的作品和插画尤其有效，效果比传统插值方法更干净。

该工具支持 2 倍放大和多个降噪级别，用于去除 JPEG 压缩伪影。它采用 ncnn 神经网络推理框架并结合 Vulkan GPU 加速，无需 CUDA 或特定厂商驱动即可在各种图形硬件上快速处理。

可通过分块大小选项调节处理过程，以控制大图像的 GPU 显存占用，并且在多 GPU 系统上可以选择特定的 GPU。输入和输出支持 PNG、JPEG、WebP 等常见图像格式。

# CAVEATS

建议使用 GPU。最适合动漫/插画。处理大图像需要较大显存。

# HISTORY

**waifu2x-ncnn-vulkan** 是 **waifu2x** 的 Vulkan 实现，后者是由 nagadomi 开发的 AI 图像放大工具。

# INSTALL

```pacman: sudo pacman -S waifu2x-ncnn-vulkan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[imagemagick](/man/imagemagick)(1), [realsr-ncnn-vulkan](/man/realsr-ncnn-vulkan)(1)
