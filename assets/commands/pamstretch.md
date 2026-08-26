# TAGLINE

通过插值按整数倍放大 Netpbm 图像

# TLDR

**将图像在两个维度上各拉伸 2 倍**

```pamstretch [2] [input.pam] > [output.pam]```

**拉伸 3 倍并丢弃多余的边缘像素**，得到更规整的尺寸

```pamstretch -dropedge [3] [input.pam] > [output.pam]```

**只横向拉伸**（宽度 4 倍，高度不变）

```pamstretch -xscale=[4] -yscale=[1] [input.pam] > [output.pam]```

**只纵向拉伸**（宽度不变，高度 2 倍）

```pamstretch -xscale=[1] -yscale=[2] [input.pam] > [output.pam]```

**在右侧/底部边缘向黑色插值**

```pamstretch -blackedge [2] [input.pam] > [output.pam]```

**在 Netpbm 管道中从标准输入读取**并拉伸

```cat [input.pnm] | pamstretch [2] > [output.pnm]```

# SYNOPSIS

**pamstretch** [**-xscale=**_X_] [**-yscale=**_Y_] [**-blackedge**|**-dropedge**] _N_ [_file_]

# PARAMETERS

_N_
> 未给出 **-xscale**/**-yscale** 时，应用于两个轴的统一整数拉伸倍数。

**-xscale=**_X_
> 整数水平缩放倍数（若只给出 **-yscale**，则默认为 1）。

**-yscale=**_Y_
> 整数垂直缩放倍数（若只给出 **-xscale**，则默认为 1）。

**-blackedge**
> 在右边缘和底边缘向黑色插值，保持输出尺寸不变。

**-dropedge**
> 在右边缘和底边缘各丢弃一个源像素。结果更干净，但输出尺寸是非标准的（_width_ * _N_ - _N_ + 1）。

_file_
> 输入的 PAM/PNM 文件。省略时从标准输入读取。

# DESCRIPTION

**pamstretch** 按整数倍放大 PAM、PNM、PPM、PGM 或 PBM 图像，它在相邻源像素之间进行插值，而不是简单地复制像素。对于照片和其他连续色调图像，这比单纯复制像素能得到更平滑的结果。

该工具可通过 **-xscale** 和 **-yscale** 分别指定水平和垂直倍数，也可以用最后一个位置参数给出统一的倍数。边缘行为可配置：默认会合成额外的像素，**-blackedge** 向黑色渐变，而 **-dropedge** 会裁掉末尾的行和列。

# CAVEATS

只支持整数缩放倍数；如需非整数缩放，请使用 **pamstretch-gen** 或 **pamscale**。选项名接受最短无歧义缩写，可使用单连字符或双连字符。

# HISTORY

**pamstretch** 是 **Netpbm** 工具集的一部分，该工具集是一组图形文件处理工具，源自 Jef Poskanzer 的 **pbmplus** 软件包（1988 年）。它是作为 **pnmenlarge**（只会复制像素）的插值替代方案而推出的。

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

[pamstretch-gen](/man/pamstretch-gen)(1), [pamscale](/man/pamscale)(1), [pnmenlarge](/man/pnmenlarge)(1), [pnmscale](/man/pnmscale)(1), [pam](/man/pam)(5), [pnm](/man/pnm)(5)
