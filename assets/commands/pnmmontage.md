# TAGLINE

将多幅图像合并为拼贴图

# TLDR

**创建图像拼贴**

```pnmmontage [image1.pnm] [image2.pnm] [image3.pnm] > [montage.pnm]```

**创建带边框的拼贴图**

```pnmmontage -margin [5] [image*.pnm] > [montage.pnm]```

**按指定布局创建**

```pnmmontage -across [3] [image*.pnm] > [montage.pnm]```

# SYNOPSIS

**pnmmontage** [_options_] _files_...

# PARAMETERS

**-across** _n_
> 每行图像数量。

**-margin** _pixels_
> 图像之间的间距。

**-border** _pixels_
> 拼贴图四周的边框。

**-back** _color_
> 背景色。

# DESCRIPTION

**pnmmontage** 将多幅 PNM 图像合并为一幅拼贴图，以网格布局排列各图像。属于 Netpbm 图像合成工具集。

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

[pamundice](/man/pamundice)(1), [pnmcat](/man/pnmcat)(1)
