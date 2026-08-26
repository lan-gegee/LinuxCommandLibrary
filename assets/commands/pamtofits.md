# TAGLINE

将 PAM/PNM 图像转换为天文学使用的 FITS 格式

# TLDR

**将 PAM 转换为 FITS 格式**

```pamtofits [input.pam] > [output.fits]```

# SYNOPSIS

**pamtofits** [_options_] [_file_]

# PARAMETERS

**-max** _n_
> 最大输出值。

**-min** _n_
> 最小输出值。

# DESCRIPTION

**pamtofits** 将 PAM/PNM 图像转换为天文学中使用的 FITS（Flexible Image Transport System）格式。属于 Netpbm 工具集。

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

[fitstopnm](/man/fitstopnm)(1), [pnmtofits](/man/pnmtofits)(1)
