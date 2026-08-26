# TAGLINE

对 PNM 图像应用卷积滤波器

# TLDR

**应用卷积矩阵**

```pnmconvol [matrix.pgm] [input.pnm] > [output.pnm]```

**创建模糊效果**

```pnmconvol -matrix=[1,1,1;1,1,1;1,1,1] [input.pnm] > [output.pnm]```

**边缘检测**

```pnmconvol -matrix=[-1,-1,-1;-1,8,-1;-1,-1,-1] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmconvol** [_options_] _convolution_ _input_

# PARAMETERS

_CONVOLUTION_
> 以 PGM 文件形式给出的卷积矩阵。

_INPUT_
> 输入的 PNM 图像文件。

**-matrix** _SPEC_
> 内联指定卷积矩阵（例如 "1,1,1;1,1,1;1,1,1"）。

**-matrixfile** _FILE_
> 从文件读取卷积矩阵。

**-normalize**
> 将权重缩放为总和为一，以保持整幅图像的亮度不变。

**-bias** _n_
> 加到每个卷积采样值上的数值，可用于处理负值结果。

**-nooffset**
> 通过除以 maxval 来归一化矩阵值，而不是采用偏移计算。

# DESCRIPTION

**pnmconvol** 对 PNM 图像应用卷积矩阵滤波器，可实现模糊、锐化和边缘检测等效果。卷积核可以用 PGM 文件指定，也可以通过 **-matrix** 选项内联给出。

每个输出像素都根据核值计算为其周围输入像素的加权和。属于 Netpbm 图像处理工具集。

# CAVEATS

属于 Netpbm。具体效果由矩阵决定。核较大时速度较慢。

# HISTORY

pnmconvol 是 **Netpbm** 中负责卷积运算的工具。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pamedge](/man/pamedge)(1), [pnmsmooth](/man/pnmsmooth)(1), [netpbm](/man/netpbm)(1)
