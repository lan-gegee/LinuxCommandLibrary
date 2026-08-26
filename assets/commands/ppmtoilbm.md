# TAGLINE

将 PPM 转换为 Amiga IFF ILBM 格式

# TLDR

**将 PPM 转换为 IFF ILBM 格式**

```ppmtoilbm [input.ppm] > [output.ilbm]```

**指定位平面数**

```ppmtoilbm -planes [8] [input.ppm] > [output.ilbm]```

# SYNOPSIS

**ppmtoilbm** [_options_] [_file_]

# PARAMETERS

**-planes** _n_
> 位平面的数量。

**-ham6**
> 使用 HAM6 模式。

**-ham8**
> 使用 HAM8 模式。

# DESCRIPTION

**ppmtoilbm** 将 PPM 图像转换为 Amiga 计算机使用的 IFF ILBM（Interleaved Bitmap）格式。支持 HAM（Hold-And-Modify）模式。属于 Netpbm 工具集。

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

[ilbmtoppm](/man/ilbmtoppm)(1), [ppmtoneo](/man/ppmtoneo)(1)
