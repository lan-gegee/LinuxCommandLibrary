# TAGLINE

为 PPM 图像添加投影效果

# TLDR

**添加默认投影**

```ppmshadow [input.ppm] > [output.ppm]```

**指定模糊半径以控制阴影柔和度**

```ppmshadow -b [8] [input.ppm] > [output.ppm]```

**指定阴影偏移方向**

```ppmshadow -x [5] -y [5] [input.ppm] > [output.ppm]```

**创建半透明阴影**

```ppmshadow -t [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmshadow** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PPM 文件。省略时从 stdin 读取。

**-b** _N_
> 控制阴影柔和度的模糊半径（默认：11）。

**-x** _N_
> 水平方向的阴影偏移量（像素）（默认：模糊半径 / 2）。

**-y** _N_
> 垂直方向的阴影偏移量（像素）（默认：与 -x 相同）。

**-t**
> 创建半透明阴影而不是纯黑阴影。

# DESCRIPTION

**ppmshadow** 为 PPM 图像添加投影效果，营造出图像悬浮在背景之上的观感。阴影的实现方式是：将图像的一份调暗副本做模糊处理，然后以偏移方式放置在原图后面。

模糊半径控制阴影的柔和程度，x 和 y 偏移量则控制表观光照方向。**-t** 选项可创建半透明阴影，让背景透出来。属于 Netpbm 工具集。

输入图像必须带有透明（黑色）背景区域，阴影才能显现。输出图像会比输入图像大出一个阴影偏移量。

# CAVEATS

要求主体周围有透明（黑色）背景，阴影才能正确显示。内部使用 pnmconvol 进行模糊，模糊半径较大时可能较慢。属于 Netpbm 套件。

# HISTORY

ppmshadow 由 **John Walker** 创建，作为 **Netpbm** 工具集的一部分，用于生成图像阴影效果。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm-extras```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppm](/man/ppm)(5), [pnmcomp](/man/pnmcomp)(1), [netpbm](/man/netpbm)(1), [pnmconvol](/man/pnmconvol)(1)
