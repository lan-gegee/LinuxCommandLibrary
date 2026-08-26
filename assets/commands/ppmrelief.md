# TAGLINE

为图像应用浮雕效果

# TLDR

**创建浮雕效果**

```ppmrelief [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmrelief** [_file_]

# PARAMETERS

_FILE_
> 输入的 PPM 文件。

# DESCRIPTION

**ppmrelief** 对 PPM 图像应用一种卷积滤波器，产生浮雕效果，使图像呈现立体的凿刻外观。原图中的边缘表现为从某个方向受光的凸起棱线，而平坦区域则变为中性灰。

该效果通过计算相邻像素之间的差异实现，从而突出边缘并抑制均匀区域。属于 Netpbm 工具集。

# CAVEATS

简单的卷积滤波器。属于 Netpbm 套件。

# HISTORY

ppmrelief 作为 **Netpbm** 的一部分被创建，用于生成浮雕效果。

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

[ppm](/man/ppm)(5), [pnmconvol](/man/pnmconvol)(1), [pgmedge](/man/pgmedge)(1), [pnmsmooth](/man/pnmsmooth)(1)
