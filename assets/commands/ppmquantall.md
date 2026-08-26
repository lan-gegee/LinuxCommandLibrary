# TAGLINE

将多幅 PPM 图像量化到共享的调色板

# TLDR

**将图像量化为同一个 256 色调色板**

```ppmquantall [256] [*.ppm]```

**输出到新文件进行量化**（通过扩展名）

```ppmquantall -ext [.quant] [256] [*.ppm]```

# SYNOPSIS

**ppmquantall** [**-ext** _extension_] _ncolors_ _files_...

# PARAMETERS

**-ext** _extension_
> 为输出文件追加此扩展名，而不是覆盖原文件。

_ncolors_
> 共享调色板中的最大颜色数。

_files_
> 要量化的 PPM 文件。

# DESCRIPTION

**ppmquantall** 接收多幅 PPM 图像作为输入，挑选出最能代表所有图像的 _ncolors_ 种颜色，把现有颜色映射到新的调色板，并用量化后的版本覆盖输入文件。适用于制作 GIF 动画——所有帧必须共享同一调色板。

属于 Netpbm 工具集。已被 **pnmquantall**（Netpbm 10.58，2012 年 3 月）取代，后者支持所有 Netpbm 输入格式。

# CAVEATS

除非指定 **-ext**，否则会直接修改输入文件。请使用 **-ext** 来保留原始文件。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm-extras```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pnmquantall](/man/pnmquantall)(1), [ppmquant](/man/ppmquant)(1)
