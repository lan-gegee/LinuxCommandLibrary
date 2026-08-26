# TAGLINE

归一化 Netpbm 图像中的对比度

# TLDR

**归一化图像对比度**

```pgmnorm [input.pgm] > [output.pgm]```

**以自定义百分位截断进行归一化**

```pgmnorm -bpercent [2] -wpercent [1] [input.pgm] > [output.pgm]```

**为黑白映射指定精确的像素值**

```pgmnorm -bvalue [30] -wvalue [220] [input.pgm] > [output.pgm]```

在彩色图像中**归一化的同时保留色调**

```pgmnorm -keephues [input.ppm] > [output.ppm]```

# SYNOPSIS

**pgmnorm** [_options_] [_file_]

# PARAMETERS

**-bpercent** _n_
> 映射为黑色的最暗像素百分比。默认：2。

**-wpercent** _n_
> 映射为白色的最亮像素百分比。默认：1。

**-bvalue** _n_
> 映射为黑色的精确像素值（若产生的改变更小，则覆盖 -bpercent）。

**-wvalue** _n_
> 映射为白色的精确像素值（若产生的改变更小，则覆盖 -wpercent）。

**-keephues**
> 保持每个像素的色调不变，只调整亮度。不加此选项时，各分量会被独立归一化，可能导致色调偏移。

**-brightmax**
> 使用最强的 RGB 分量而非亮度作为像素的亮度值。

# DESCRIPTION

**pgmnorm** 读取 PNM 图像（PBM、PGM 或 PPM），通过将最暗的像素强制变为黑色、最亮的像素强制变为白色来归一化对比度，并对中间值做线性缩放。输出与输入同类别的图像。它是 **pnmnorm** 的旧名称。

默认情况下，最暗的 2% 像素被映射为黑色，最亮的 1% 被映射为白色。这些阈值可通过 **-bpercent** 和 **-wpercent** 更改，也可用 **-bvalue** 和 **-wvalue** 指定精确的截断值。如果对同一端同时给出了百分比和数值选项，则采用产生改变较小的那个。

属于 **Netpbm** 工具集。

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

[pnmnorm](/man/pnmnorm)(1), [pgmhist](/man/pgmhist)(1), [pnmhisteq](/man/pnmhisteq)(1), [pgmenhance](/man/pgmenhance)(1)
