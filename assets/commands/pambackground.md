# TAGLINE

创建标识 PAM/PNM 图像背景像素的位图掩膜

# TLDR

**从图像创建背景掩膜**

```pambackground [input.pam] > [output.pbm]```

# SYNOPSIS

**pambackground** [_options_] [_file_]

# PARAMETERS

**-verbose**
> 打印处理信息。

# DESCRIPTION

**pambackground** 创建一个位图掩膜，用于标识 PAM/PNM 图像中的背景像素。它利用角落像素确定背景色，并通过泛洪填充找出连通的背景区域。属于 Netpbm 工具集。

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

[ppmcolormask](/man/ppmcolormask)(1), [pamcut](/man/pamcut)(1)
