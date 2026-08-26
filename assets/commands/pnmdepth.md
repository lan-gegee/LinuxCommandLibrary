# TAGLINE

更改 PNM 图像的颜色深度

# TLDR

**更改图像深度**

```pnmdepth [newdepth] [input.pnm] > [output.pnm]```

**降至 8 位**

```pnmdepth 255 [input.pnm] > [output.pnm]```

**降至 4 位**

```pnmdepth 15 [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmdepth** _newmaxval_ [_file_]

# PARAMETERS

_NEWMAXVAL_
> 新的最大采样值（深度）。

_FILE_
> 输入的 PNM 文件。

# DESCRIPTION

**pnmdepth** 通过按比例重新缩放所有像素值，来更改 PNM 图像的最大采样值（颜色深度）。例如，把 maxval 从 65535（16 位）转换为 255（8 位）时，每个采样值都会相应地缩放。

这有助于通过降低位深来减小文件体积，或确保与要求特定深度值的工具兼容。属于 Netpbm 工具集；已被 **pamdepth** 取代。

# CAVEATS

数值按比例缩放。属于 Netpbm 套件。

# HISTORY

pnmdepth 作为 **Netpbm** 的一部分创建，用于图像深度转换。

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

[pamdepth](/man/pamdepth)(1), [pnm](/man/pnm)(5), [ppmquant](/man/ppmquant)(1)
