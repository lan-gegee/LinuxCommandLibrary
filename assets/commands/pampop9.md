# TAGLINE

创建波普艺术风格图像

# TLDR

**应用波普艺术效果**

```pampop9 [input.pam] > [output.pam]```

**生成 3x3 颜色变体**

```pampop9 [photo.pam] > [popart.pam]```

# SYNOPSIS

**pampop9** [_file_]

# PARAMETERS

_FILE_
> 输入的 PAM/PNM 图像。

# DESCRIPTION

**pampop9** 创建波普艺术风格的图像。生成 3x3 网格排列的颜色变体。

该工具产生安迪·沃霍尔风格的输出。属于 Netpbm。

# CAVEATS

属于 Netpbm。输出尺寸为原图的 3 倍。属于艺术化效果。

# HISTORY

pampop9 是 **Netpbm** 的组成部分，用于创建波普艺术风格的颜色变体。

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

[ppmquant](/man/ppmquant)(1), [netpbm](/man/netpbm)(1)
