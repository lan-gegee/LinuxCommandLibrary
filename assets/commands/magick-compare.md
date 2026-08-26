# TAGLINE

比较两张图像并输出它们的差异

# TLDR

**比较两张图像**

```magick compare [image1.png] [image2.png] [diff.png]```

**计算差异度量值**

```magick compare -metric AE [image1.png] [image2.png] null:```

**使用指定的比较方法**

```magick compare -metric RMSE [image1.png] [image2.png] null:```

**用红色高亮差异**

```magick compare -highlight-color red [image1.png] [image2.png] [diff.png]```

在大图中**搜索子图像**

```magick compare -subimage-search [haystack.png] [needle.png] [result.png]```

**打印每个通道的详细**失真统计

```magick compare -verbose -metric AE [image1.png] [image2.png] null:```

# SYNOPSIS

**magick** **compare** [_options_] _image1_ _image2_ [_diff_]

# PARAMETERS

**-metric** _type_
> 比较度量（AE、RMSE、PSNR、MAE、MSE、NCC、PHASH、DSSIM）。默认：RMSE。

**-highlight-color** _color_
> 用于标记不同像素的颜色。

**-lowlight-color** _color_
> 用于相同像素的颜色。

**-fuzz** _percent_
> 比较时的颜色容差。

**-subimage-search**
> 在较大图像中搜索较小的图像。

**-dissimilarity-threshold** _value_
> 匹配允许的最大失真度（默认：0.2）。

**-similarity-threshold** _value_
> 视为相似的最小失真度（默认：0.0）。

**-channel** _type_
> 将比较限制在指定的通道上。

**-verbose**
> 打印每个通道的失真指标。

# DESCRIPTION

**magick compare** 比较两张图像并输出其差异。它是 ImageMagick 的一部分，可生成差异图像和/或计算数值化的度量指标。适用于回归测试和质量保证。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[magick](/man/magick)(1), [magick-convert](/man/magick-convert)(1)
