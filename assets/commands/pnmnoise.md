# TAGLINE

生成随机噪声 PNM 图像（通常只是 pgmnoise 的别称）

# TLDR

**创建灰度噪声图像**（借助 pgmnoise）

```pgmnoise [width] [height] > [noise.pgm]```

通过合并三个灰度噪声通道**构建彩色噪声**

```rgb3toppm <(pgmnoise 256 256) <(pgmnoise 256 256) <(pgmnoise 256 256) > noise.ppm```

**为现有图像添加噪声**

```pamaddnoise -type=gaussian -lsigma=0.1 [image.pnm] > [noisy.pnm]```

# SYNOPSIS

**pgmnoise** [**-randomseed** _n_] _width_ _height_

# PARAMETERS

**width**
> 图像宽度（像素）。

**height**
> 图像高度（像素）。

**-randomseed** _n_
> 为伪随机数生成器设定种子，使输出可以复现。

# DESCRIPTION

现代 Netpbm 中并不存在独立的 **pnmnoise** 程序。这个名称有时被宽泛地用来指代 Netpbm 的噪声生成器家族。

使用 **pgmnoise** 生成白噪声的灰度 PGM，用 **pbmnoise** 生成随机黑白像素组成的 PBM（位图），再将三份 **pgmnoise** 输出通过 **rgb3toppm** 合成为彩色 PPM 噪声图像。**pamaddnoise** 则可为现有图像叠加多种噪声分布（高斯、脉冲、乘性高斯等）。

# EXAMPLES

```bash
# Grayscale noise 512x512
pgmnoise 512 512 > noise.pgm

# Reproducible grayscale noise
pgmnoise -randomseed 12345 100 100 > noise.pgm

# Color noise by merging three channels
rgb3toppm <(pgmnoise 256 256) <(pgmnoise 256 256) <(pgmnoise 256 256) > noise.ppm

# Convert to PNG
pgmnoise 200 200 | pnmtopng > noise.png
```

# CAVEATS

**pnmnoise** 并非一个独立的可执行文件；pgmnoise/pbmnoise 只能产生单通道噪声。其随机分布为均匀分布；若需要其他分布，请对基础图像使用 pamaddnoise。

# HISTORY

这些 Netpbm 噪声生成器是 **Netpbm** 软件包的一部分（最初为 **Jef Poskanzer** 于 1988 年编写的 **pbmplus**）。较旧的 **pnmaddnoise** 在 Netpbm 10.30 中更名为 **pamaddnoise**。

# SEE ALSO

[pgmnoise](/man/pgmnoise)(1), [ppmforge](/man/ppmforge)(1), [ppmmake](/man/ppmmake)(1), [netpbm](/man/netpbm)(1)
