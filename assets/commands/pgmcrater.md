# TAGLINE

以灰度高度图形式生成带撞击坑的合成地形

# TLDR

**生成陨石坑地形**

```pgmcrater -number [5000] > [output.pgm]```

**指定尺寸**

```pgmcrater -width [512] -height [512] -number [1000] > [output.pgm]```

# SYNOPSIS

**pgmcrater** [_options_]

# PARAMETERS

**-width** _n_, **-xsize** _n_
> 输出宽度（像素）（默认 256）。

**-height** _n_, **-ysize** _n_
> 输出高度（像素）（默认 256）。

**-number** _n_
> 要生成的陨石坑数量。

**-gamma** _g_
> 应用于明暗浮雕输出的 gamma 校正值。

**-randomseed** _n_
> 随机数生成器的种子；使用固定值可获得可复现的输出。

# DESCRIPTION

**pgmcrater** 生成遍布撞击坑的合成地形，并以明暗浮雕方式渲染为灰度 PGM 高度图输出。它适合用于制作行星表面纹理和程序化地形。

从 Netpbm 10.27 起，**pgmcrater** 已被标记为过时；现在它只是一个薄封装，将 **pamcrater** 的输出通过管道传给 **pamshadedrelief** 和 **pamtopnm**。新的工作流程建议直接使用这些基础工具。

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

[pamcrater](/man/pamcrater)(1), [pgmnoise](/man/pgmnoise)(1)
