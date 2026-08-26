# TAGLINE

按任意角度旋转 PNM 图像

# TLDR

**旋转图像**

```pnmrotate [45] [input.pnm] > [output.pnm]```

**带背景色旋转**

```pnmrotate -background [white] [30] [input.pnm] > [output.pnm]```

**不使用抗锯齿旋转**

```pnmrotate -noantialias [30] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmrotate** [_options_] _angle_ [_file_]

# PARAMETERS

_angle_
> 旋转角度（度），必须介于 -90 与 90 之间。按逆时针方向度量。

**-background** _color_
> 背景填充色。默认情况下，pnmrotate 会选用原图中看似背景色的颜色。

**-noantialias**
> 禁用抗锯齿。仅移动像素，而不是由多个输入像素合成输出像素。

# DESCRIPTION

**pnmrotate** 按任意角度旋转 PNM 图像，角度以度为单位指定（介于 -90 与 90 之间，逆时针方向）。输出图像会根据需要扩大以容纳完整的旋转结果，新出现的区域用背景色填充。

默认应用抗锯齿使边缘平滑；在处理二值图像或希望更快时，可用 **-noantialias** 关闭它。若要按 90 度的整数倍旋转，请改用 **pamflip**。属于 Netpbm 工具集。

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

[pamflip](/man/pamflip)(1), [pnmflip](/man/pnmflip)(1), [pnmshear](/man/pnmshear)(1)
