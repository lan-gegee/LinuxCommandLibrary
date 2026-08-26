# TAGLINE

生成色彩斑斓的等离子分形图像

# TLDR

**生成等离子图案**

```ppmplasma [width] [height] > [plasma.ppm]```

**指定随机种子**

```ppmplasma -randomseed [42] [512] [512] > [plasma.ppm]```

**输出为 PNG**

```ppmplasma [800] [600] | pnmtopng > [plasma.png]```

# SYNOPSIS

**ppmplasma** [_options_] _width_ _height_

# PARAMETERS

**width**
> 图像宽度（像素）。

**height**
> 图像高度（像素）。

**-randomseed** _n_
> 用于保证结果可复现的种子。

# DESCRIPTION

**ppmplasma** 生成带有彩色云雾状图案的等离子分形图像。它使用递归细分来创建平滑、自然的纹理。

属于 Netpbm 工具集。

# EXAMPLES

```bash
# Basic plasma
ppmplasma 640 480 > plasma.ppm

# Reproducible result
ppmplasma -randomseed 12345 512 512 > plasma.ppm

# Convert to PNG
ppmplasma 800 600 | pnmtopng > plasma.png

# Create desktop background
ppmplasma 1920 1080 | pnmtojpeg > wallpaper.jpg
```

# ALGORITHM

使用中点位移算法：
1. 设置四角颜色
2. 递归细分
3. 以随机位移对颜色取平均

# CAVEATS

调色板固定。若需灰度输出，可通过管道交给 [ppmtopgm](/man/ppmtopgm)。属于 Netpbm 工具集。不同的随机种子会产生不同的图案。

# HISTORY

ppmplasma 是 **Netpbm** 的组成部分，实现了自 20 世纪 90 年代以来在 demoscene 和计算机图形领域流行的等离子云算法（中点位移）。

# SEE ALSO

[ppmforge](/man/ppmforge)(1), [pgmnoise](/man/pgmnoise)(1), [ppmmake](/man/ppmmake)(1), [netpbm](/man/netpbm)(1)
