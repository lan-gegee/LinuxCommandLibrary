# TAGLINE

合成两幅图像

# TLDR

**合成图像**

```pamcomp [overlay.pam] [base.pam] > [output.pam]```

**带透明度**

```pamcomp -alpha=[mask.pgm] [overlay.pam] [base.pam] > [output.pam]```

**指定位置**

```pamcomp -xoff=[100] -yoff=[50] [overlay.pam] [base.pam] > [output.pam]```

# SYNOPSIS

**pamcomp** [_options_] _overlay_ _base_

# PARAMETERS

_OVERLAY_
> 前景图像。

_BASE_
> 背景图像。

**-alpha** _FILE_
> Alpha 掩膜文件。

**-xoff** _PIXELS_
> X 偏移。

**-yoff** _PIXELS_
> Y 偏移。

**-align** _POS_
> 对齐位置。

# DESCRIPTION

**pamcomp** 合成两幅图像。支持带透明度的叠加。

该工具合并 PAM/PNM 图像。属于 Netpbm 的一部分。

# CAVEATS

属于 Netpbm。PAM/PNM 格式。支持 alpha 通道。

# HISTORY

pamcomp 是 **Netpbm** 的一部分，用于图像合成操作。

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

[pnmcomp](/man/pnmcomp)(1), [pnmpaste](/man/pnmpaste)(1), [netpbm](/man/netpbm)(1)
