# TAGLINE

翻转和旋转 PAM/PNM 图像

# TLDR

**水平翻转**

```pamflip -leftright [input.pam] > [output.pam]```

**垂直翻转**

```pamflip -topbottom [input.pam] > [output.pam]```

**顺时针旋转 90 度**

```pamflip -rotate90 [input.pam] > [output.pam]```

**旋转 180 度**

```pamflip -rotate180 [input.pam] > [output.pam]```

# SYNOPSIS

**pamflip** [_options_] [_file_]

# PARAMETERS

**-leftright**
> 水平翻转。

**-topbottom**
> 垂直翻转。

**-rotate90**
> 顺时针旋转 90 度。

**-rotate180**
> 旋转 180 度。

**-rotate270**
> 顺时针旋转 270 度。

**-transpose**
> 转置图像。

# DESCRIPTION

**pamflip** 翻转和旋转 PAM/PNM 图像。是 pnmflip 的现代替代版并增加了 PAM 支持。属于 Netpbm 工具集。

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

[pnmflip](/man/pnmflip)(1), [pnmrotate](/man/pnmrotate)(1)
