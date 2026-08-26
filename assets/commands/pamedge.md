# TAGLINE

对 PNM/PAM 图像进行边缘检测

# TLDR

在图像中**检测边缘**

```pamedge [input.pam] > [output.pam]```

**通过管道检测边缘**

```cat [image.pam] | pamedge > [edges.pam]```

**检测边缘并做阈值化**转为黑白

```pamedge [input.pam] | pamditherbw -threshold > [edges.pbm]```

# SYNOPSIS

**pamedge** [_imagefile_]

# PARAMETERS

_imagefile_
> 输入的 PAM 或 PNM 图像文件。省略时从标准输入读取。

# DESCRIPTION

**pamedge** 读取 Netpbm 图像（PNM 或 PAM），生成一幅勾勒边缘的输出图像。它使用相互成 90 度角的两个 **Sobel 梯度算子**的勾股和进行边缘检测。

输出格式与输入一致，只是最小 maxval 为 255。PBM 输入会转换为 PGM 输出。要获得更锐利的双级边缘图像，可将输出通过管道传给 **pamditherbw -threshold**。

属于 **Netpbm** 工具集。取代了只支持 PGM 和 PBM 格式的 **pgmedge**。

# CAVEATS

除标准 libnetpbm 选项外没有其他命令行选项。对于 maxval 较低的图像，可在处理前先用 **pamdepth** 提高 maxval 以获得更好的效果。

# HISTORY

**pamedge** 于 **2003 年**加入 Netpbm，作为 **pgmedge** 的替代品，将支持范围扩展到所有 PAM 和 PNM 图像格式。

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

[pgmedge](/man/pgmedge)(1), [pgmenhance](/man/pgmenhance)(1), [pamditherbw](/man/pamditherbw)(1), [pamdepth](/man/pamdepth)(1), [pnmconvol](/man/pnmconvol)(1), [netpbm](/man/netpbm)(1)
