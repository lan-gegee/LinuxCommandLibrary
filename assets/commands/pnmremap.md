# TAGLINE

把图像颜色重映射到指定调色板

# TLDR

**将图像重映射到调色板**

```pnmremap -mapfile=[palette.pnm] [input.pnm] > [output.pnm]```

**使用 Floyd-Steinberg 抖动**

```pnmremap -floyd -mapfile=[palette.pnm] [input.pnm] > [output.pnm]```

**不使用抖动**

```pnmremap -nofloyd -mapfile=[palette.pnm] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmremap** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PNM 文件。

**-mapfile** _FILE_
> 调色板图像。

**-floyd**
> 使用 Floyd-Steinberg 抖动。

**-nofloyd**
> 不使用抖动。

**-norandom**
> 禁用随机抖动。

**-firstisdefault**
> 将调色板中的第一种颜色用作默认色。

# DESCRIPTION

**pnmremap** 把 PNM 图像中每个像素的颜色替换为指定调色板图像中最接近的颜色。适用于强制图像只使用特定的一组颜色，例如目标显示格式只支持有限色彩时。

**-floyd** 选项启用 Floyd-Steinberg 误差扩散抖动，使视觉效果更平滑。调色板通过 **-mapfile** 以 PNM 图像的形式提供，其中每种不同的像素颜色代表一种允许使用的颜色。属于 Netpbm 工具集。

# CAVEATS

需要提供调色板文件。属于 Netpbm 套件。

# HISTORY

pnmremap 作为 **Netpbm** 的一部分创建，用于调色板映射。

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

[ppmquant](/man/ppmquant)(1), [pnmcolormap](/man/pnmcolormap)(1), [ppmtogif](/man/ppmtogif)(1)
