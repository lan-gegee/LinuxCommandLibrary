# TAGLINE

带透明度地合成 PNM 图像

# TLDR

**合成图像**

```pnmcomp [overlay.pnm] [background.pnm] > [output.pnm]```

**使用 Alpha 遮罩**

```pnmcomp -alpha=[mask.pgm] [overlay.pnm] [background.pnm] > [output.pnm]```

**定位叠加层**

```pnmcomp -xoff=[100] -yoff=[50] [overlay.pnm] [background.pnm] > [output.pnm]```

# SYNOPSIS

**pnmcomp** [_options_] _overlay_ _background_

# PARAMETERS

_OVERLAY_
> 前景图像。

_BACKGROUND_
> 背景图像。

**-alpha** _FILE_
> Alpha 遮罩。

**-xoff** _PIXELS_
> X 方向偏移。

**-yoff** _PIXELS_
> Y 方向偏移。

**-align** _POS_
> 对齐方式。

# DESCRIPTION

**pnmcomp** 通过把一幅 PNM 图像叠加到另一幅之上来合成图像，并支持可选的 Alpha 透明度。Alpha 遮罩（PGM 文件）控制叠加像素与背景像素之间的混合程度。

位置偏移（**-xoff**、**-yoff**）控制叠加层放置在背景上的位置。属于 Netpbm 工具集；在较新版本中已被 **pamcomp** 取代。

# CAVEATS

属于 Netpbm。较新版本请使用 pamcomp。

# HISTORY

pnmcomp 是 **Netpbm** 中负责图像合成的工具。

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

[pamcomp](/man/pamcomp)(1), [pnmpaste](/man/pnmpaste)(1), [netpbm](/man/netpbm)(1)
