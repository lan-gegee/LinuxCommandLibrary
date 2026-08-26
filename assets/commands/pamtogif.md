# TAGLINE

将 PAM/PNM 图像转换为 GIF 格式

# TLDR

**将 PAM 转换为 GIF**

```pamtogif [input.pam] > [output.gif]```

**创建交错式 GIF**

```pamtogif -interlace [input.pam] > [output.gif]```

**设置透明颜色**

```pamtogif -transparent [#ffffff] [input.pam] > [output.gif]```

# SYNOPSIS

**pamtogif** [_options_] [_file_]

# PARAMETERS

**-interlace**
> 创建交错式 GIF。

**-transparent** _color_
> 透明颜色。

**-alphacolor** _color_
> Alpha 颜色。

**-comment** _text_
> 添加注释。

# DESCRIPTION

**pamtogif** 将 PAM/PNM 图像转换为 GIF 格式。属于 Netpbm 工具集。会自动把颜色减少到 GIF 格式所要求的 256 色。

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

[giftopnm](/man/giftopnm)(1), [ppmtogif](/man/ppmtogif)(1)
