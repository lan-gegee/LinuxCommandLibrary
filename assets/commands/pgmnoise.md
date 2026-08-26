# TAGLINE

创建由随机灰度像素填充的 PGM 图像

# TLDR

**创建 100x100 白噪声图像**

```pgmnoise [100] [100] > [noise.pgm]```

**创建全高清噪声图像**

```pgmnoise [1920] [1080] > [noise.pgm]```

**创建噪声并转换为 PNG**

```pgmnoise [256] [256] | pnmtopng > [noise.png]```

**使用固定种子创建可复现的噪声**

```pgmnoise -randomseed [12345] [100] [100] > [noise.pgm]```

**创建小噪声瓦片并平铺**

```pgmnoise [64] [64] | pnmtile [256] [256] > [texture.pgm]```

# SYNOPSIS

**pgmnoise** [_options_] _width_ _height_

# PARAMETERS

_width_
> 图像宽度（像素）。

_height_
> 图像高度（像素）。

**-randomseed** _n_
> 随机数生成器的种子，可获得可复现的输出。

**-maxval** _n_
> 像素的最大灰度值。默认为 PGM 的编译期最大值（通常为 255 或 65535）。

# DESCRIPTION

**pgmnoise** 创建一幅 portable graymap（PGM）图像，其中每个像素被独立赋予一个介于 0 与最大值之间、均匀分布的随机灰度值。输出以 PGM 格式写入标准输出。

该工具可用于测试图像处理流水线、创建噪声纹理，或生成可通过管道送入其他 Netpbm 工具的随机图案。

# CAVEATS

只使用均匀随机分布。若需高斯或其他噪声类型，请使用 **pamaddnoise** 或与其他工具组合使用。输出发送到 stdout，必须进行重定向。属于 Netpbm 工具集。

# HISTORY

**pgmnoise** 是 **Netpbm** 图形工具集的一部分，该工具集最初由 **Jef Poskanzer** 于 20 世纪 80 年代末创建，自 2000 年起由 **Bryan Henderson** 维护。

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

[pnmnoise](/man/pnmnoise)(1), [pgmmake](/man/pgmmake)(1), [ppmforge](/man/ppmforge)(1), [pnmtopng](/man/pnmtopng)(1), [netpbm](/man/netpbm)(1)
