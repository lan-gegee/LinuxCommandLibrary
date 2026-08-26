# TAGLINE

生成带有陨石坑的合成地形，适用于创建行星

# TLDR

**生成带陨石坑的地形**

```pamcrater -width [512] -height [512] > [output.pam]```

**以指定陨石坑数量生成**

```pamcrater -number [1000] -width [256] -height [256] > [output.pam]```

# SYNOPSIS

**pamcrater** [_options_]

# PARAMETERS

**-width** _n_
> 输出宽度（像素）。

**-height** _n_
> 输出高度（像素）。

**-number** _n_
> 要生成的陨石坑数量。

**-randomseed** _n_
> 用于可复现性的随机种子。

# DESCRIPTION

**pamcrater** 生成带有撞击陨石坑的合成地形，可用于创建行星表面纹理或高度图。输出为灰度高程数据。属于 Netpbm 工具集。

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

[pgmcrater](/man/pgmcrater)(1)
