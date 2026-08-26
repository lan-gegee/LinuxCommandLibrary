# TAGLINE

AI 驱动的 GPU 加速图像放大工具

# TLDR

**放大图像**

```realsr-ncnn-vulkan -i [input.jpg] -o [output.png]```

**指定放大倍数**

```realsr-ncnn-vulkan -i [input.jpg] -o [output.png] -s [4]```

**使用特定模型**

```realsr-ncnn-vulkan -i [input.jpg] -o [output.png] -m [models-DF2K]```

**指定 GPU**

```realsr-ncnn-vulkan -i [input.jpg] -o [output.png] -g [0]```

# SYNOPSIS

**realsr-ncnn-vulkan** [_options_] **-i** _input_ **-o** _output_

# PARAMETERS

**-i** _path_
> 输入图像文件。

**-o** _path_
> 输出图像文件。

**-s** _scale_
> 放大倍数（默认 4）。

**-m** _path_
> 模型目录。

**-g** _gpu_
> GPU 设备 ID（-1 表示 CPU）。

**-t** _size_
> 分块大小。

**-j** _threads_
> 处理线程数。

# DESCRIPTION

**realsr-ncnn-vulkan** 是一款基于 ncnn 神经网络框架并采用 Vulkan GPU 加速的 Real-ESRGAN/Real-SR 图像放大工具。它能够生成高质量的放大图像。

# EXAMPLES

```bash
# Basic 4x upscale
realsr-ncnn-vulkan -i photo.jpg -o photo_4x.png

# 2x scale
realsr-ncnn-vulkan -i photo.jpg -o photo_2x.png -s 2

# Use specific model
realsr-ncnn-vulkan -i anime.png -o anime_up.png -m models-DF2K_JPEG

# CPU only
realsr-ncnn-vulkan -i input.jpg -o output.png -g -1

# Batch process (use loop)
for f in *.jpg; do
  realsr-ncnn-vulkan -i "$f" -o "upscaled_$f"
done
```

# MODELS

```
models-DF2K       - General purpose
models-DF2K_JPEG  - JPEG artifact reduction
```

# CAVEATS

需要支持 Vulkan 的 GPU。处理大图像时内存占用较高，处理速度可能较慢。

# HISTORY

realsr-ncnn-vulkan 基于 **Real-ESRGAN** 研究，由 **nihui** 移植到 ncnn 以实现高效的跨平台推理。

# INSTALL

```aur: yay -S realsr-ncnn-vulkan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[waifu2x-ncnn-vulkan](/man/waifu2x-ncnn-vulkan)(1), [imagemagick](/man/imagemagick)(1)
