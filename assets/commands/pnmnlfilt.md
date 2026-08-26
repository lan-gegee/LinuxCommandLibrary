# TAGLINE

对图像应用非线性平滑滤波器

# TLDR

使用 alpha 截断均值滤波器**平滑噪声**

```pnmnlfilt [0.4] [0.8] [input.pnm] > [output.pnm]```

**最优估计平滑**（alpha 取 1.0-2.0）

```pnmnlfilt [1.2] [1.0] [input.pnm] > [output.pnm]```

**边缘增强**（负 alpha）

```pnmnlfilt [-0.3] [0.8] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmnlfilt** _alpha_ _radius_ [_pnmfile_]

# PARAMETERS

_alpha_
> 滤波模式选择器。0.0-0.5：alpha 截断均值（平滑）。1.0-2.0：最优估计平滑。-0.1 到 -0.9：边缘增强。

_radius_
> 六边形邻域半径。平滑建议取 0.55-1.0，边缘增强建议取 0.5-0.9。值越小效果越弱。

# DESCRIPTION

**pnmnlfilt** 对 PNM 图像应用非线性滤波器，在降噪的同时保留边缘。单一的 alpha 参数可在三种不同模式之间选择：用于平滑和降噪的 alpha 截断均值滤波器（alpha 为 0.0-0.5）、能适应局部方差的最优估计平滑（alpha 为 1.0-2.0），以及锐化过渡区域的边缘增强（负 alpha）。

radius 参数控制六边形像素邻域的大小。半径越大效果越强，但可能模糊细节。与简单卷积滤波器不同，pnmnlfilt 能避免在平滑过程中破坏清晰的边缘。

# CAVEATS

不存在 pnmnlfilt 特有的命令行标志；只有标准的 libnetpbm 选项可用。属于 Netpbm 工具集。

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

[pnmsmooth](/man/pnmsmooth)(1), [pnmconvol](/man/pnmconvol)(1)
