# TAGLINE

按非整数倍数缩放 Netpbm 图像

# TLDR

**缩放图像**，倍数为非整数 N

```pamstretch-gen [2.5] [input.pam] > [output.pam]```

**从标准输入读取**

```cat [input.pam] | pamstretch-gen [1.75] > [output.pam]```

# SYNOPSIS

**pamstretch-gen** _N_ [_pnmfile_]

# PARAMETERS

_N_
> 缩放倍数（可以是非整数，如 `1.5` 或 `2.75`）。作用于两个维度。

_pnmfile_
> 输入的 Netpbm 图像文件。省略时从标准输入读取。

# DESCRIPTION

**pamstretch-gen** 按任意（可能是非整数）倍数缩放 Netpbm 图像。它内部先用 **pamstretch** 放大到相邻的整数倍（pamstretch 只支持整数倍），再用 **pamscale** 缩回到所需尺寸。对于适度的放大，这样得到的效果比单独使用 pamscale 更好。

pamstretch-gen 没有专属的命令行选项；它能识别 libnetpbm 的通用选项（例如较新版本中的 `-quiet` 和 `-plain`）。

# CAVEATS

需要同时具备 **pamstretch** 和 **pamscale**。只适用于 Netpbm（PNM/PAM）图像。

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

[pamstretch](/man/pamstretch)(1), [pamscale](/man/pamscale)(1)
