# TAGLINE

混合相邻行以减少视频帧中的隔行扫描伪影

# TLDR

**使用默认 FIR 滤波器混合隔行视频场**

```pammixinterlace [input.pam] > [output.pam]```

**使用线性混合滤波器**

```pammixinterlace -filter=linear [input.pam] > [output.pam]```

**使用自适应滤波，只修改梳状图案的像素**

```pammixinterlace -adaptive [input.pam] > [output.pam]```

**将自适应模式与指定滤波器结合使用**

```pammixinterlace -adaptive -filter=ffmpeg [input.pam] > [output.pam]```

# SYNOPSIS

**pammixinterlace** [**-filter=**{**linear**|**fir**|**ffmpeg**}] [**-adaptive**] [_file_]

# PARAMETERS

**-filter=**{**linear**|**fir**|**ffmpeg**}
> 选择滤波机制。**linear** 使用线性混合公式。**fir** 使用尺寸为 5 的 FIR 低通滤波器。**ffmpeg** 使用来自 ffmpeg 文档的公式。默认为 **fir**。

**-adaptive**
> 启用自适应滤波模式。只修改明显属于"梳状"图案的像素，其余像素保持不变。

# DESCRIPTION

**pammixinterlace** 使输出的每一行成为输入中对应行及其两个相邻行的混合：主行占一半权重，两个相邻行各占四分之一。这种混合可以减少从隔行信号源采集的视频帧中的隔行伪影（拉丝现象）。

该工具适用于对隔行视频采集画面进行去隔行处理以用作静态图像。属于 Netpbm 工具集。

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

[pamdeinterlace](/man/pamdeinterlace)(1), [pamscale](/man/pamscale)(1), [netpbm](/man/netpbm)(1)
