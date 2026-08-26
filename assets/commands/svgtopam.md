# TAGLINE

将 SVG 图形转换为 PAM 位图格式

# TLDR

**将 SVG 转换为 PAM**

```svgtopam [input.svg] > [output.pam]```

**以指定分辨率转换**

```svgtopam -resolution [300] [input.svg] > [output.pam]```

# SYNOPSIS

**svgtopam** [_options_] [_file_]

# PARAMETERS

**-resolution** _dpi_
> 输出分辨率。

**-dimension** _WxH_
> 输出尺寸。

# DESCRIPTION

**svgtopam** 将 SVG 矢量图形转换为 PAM 位图格式，按指定分辨率栅格化 SVG。属于 Netpbm 工具集。

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

[rsvg-convert](/man/rsvg-convert)(1), [inkscape](/man/inkscape)(1)
