# TAGLINE

在图像的各种地图投影之间转换

# TLDR

**应用墨卡托投影**

```pnmmercator [input.pnm] > [output.pnm]```

**逆投影变换**

```pnmmercator -inverse [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmmercator** [_options_] [_file_]

# PARAMETERS

**-inverse**
> 从墨卡托投影转换为等距圆柱投影。

# DESCRIPTION

**pnmmercator** 在等距圆柱（plate carr&eacute;e）投影与墨卡托投影之间转换 PNM 图像。输入图像被当作一幅地图处理：行对应纬线，列对应经线。

正向变换会把等距圆柱投影转换为墨卡托投影，并拉伸靠近两极的区域。**-inverse** 选项执行相反的过程，把墨卡托投影转换回等距圆柱投影。属于 Netpbm 工具集。

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

[pamscale](/man/pamscale)(1), [pnmshear](/man/pnmshear)(1)
