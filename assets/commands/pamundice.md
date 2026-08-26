# TAGLINE

重新拼合分块图像

# TLDR

**重新拼合分块图像**

```pamundice -across=[4] -down=[3] -listfile=[tiles.txt] > [output.pam]```

**使用命名模式**

```pamundice -across=[4] -down=[3] tile%02d_%02d.pam > [output.pam]```

# SYNOPSIS

**pamundice** [_options_] [_input_pattern_]

# PARAMETERS

**-across** _N_
> 水平方向的分块数。

**-down** _N_
> 垂直方向的分块数。

**-listfile** _FILE_
> 列出各分块名称的文件。

**-hoverlap** _PIXELS_
> 水平重叠量。

**-voverlap** _PIXELS_
> 垂直重叠量。

# DESCRIPTION

**pamundice** 重新拼合被分块的图像。是 pamdice 操作的逆过程。

该工具用于合并图像分块。属于 Netpbm。

# CAVEATS

属于 Netpbm。各分块必须相互匹配。提供重叠处理选项。

# HISTORY

pamundice 是 **Netpbm** 的组成部分，用于重新拼合分块图像。

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

[pamdice](/man/pamdice)(1), [pnmcat](/man/pnmcat)(1), [netpbm](/man/netpbm)(1)
