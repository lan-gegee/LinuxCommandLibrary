# TAGLINE

图像差异检测与比较工具

# TLDR

**比较两张图像**

```compare [image1.png] [image2.png] [diff.png]```

**用红色高亮显示差异**

```compare -highlight-color red [image1.png] [image2.png] [diff.png]```

**获取差异度量值**

```compare -metric AE [image1.png] [image2.png] null:```

**带容差系数（fuzz）进行比较**

```compare -fuzz [5]% [image1.png] [image2.png] [diff.png]```

**只输出有差异的区域**

```compare -compose src [image1.png] [image2.png] [diff.png]```

**使用指定颜色通道**

```compare -channel red [image1.png] [image2.png] [diff.png]```

# SYNOPSIS

**compare** [_options_] _image1_ _image2_ [_difference_]

# DESCRIPTION

**compare** 是一个 ImageMagick 实用工具，用于比较两张图像并高亮显示它们之间的差异。它可以输出可视化的差异图像，和/或计算数值化的差异度量。

该工具适用于视觉回归测试、检测渲染输出的变化以及质量保证工作流。各种度量指标可量化图像之间的差异程度。

# PARAMETERS

**-metric** _type_
> 输出差异度量（AE、RMSE、MAE、PSNR 等）。

**-fuzz** _percent_
> 允许比较时的颜色容差。

**-highlight-color** _color_
> 用于高亮差异的颜色。

**-lowlight-color** _color_
> 匹配区域使用的颜色。

**-compose** _method_
> 差异输出的合成方式。

**-channel** _type_
> 比较指定的颜色通道。

**-subimage-search**
> 在大图中搜索子图。

**-dissimilarity-threshold** _value_
> 子图匹配的阈值。

**-verbose**
> 显示详细的比较信息和计算出的度量值。

# METRICS

**AE**: 绝对误差（不同像素的数量）
**RMSE**: 均方根误差（0 = 完全相同）
**MAE**: 平均绝对误差（0 = 完全相同）
**MSE**: 均方误差
**PSNR**: 峰值信噪比（越高越相似）
**SSIM**: 结构相似性指数（1 = 完全相同）
**NCC**: 归一化互相关（默认度量）
**PHASH**: 感知哈希

# CAVEATS

除非使用子图搜索，否则两幅图像必须尺寸相同。大图的比较可能较慢。有损格式可能因压缩而显示出差异。

# HISTORY

**compare** 是 **ImageMagick** 的一部分，后者由 **John Cristy** 于 **1987 年**创建。ImageMagick 在图像处理与转换领域持续发展至今。compare 工具已成为软件开发中自动化视觉测试的重要手段。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[magick](/man/magick)(1), [convert](/man/convert)(1), [identify](/man/identify)(1), [diff](/man/diff)(1)
