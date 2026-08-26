# TAGLINE

从 PAM 高程图生成晕渲地貌图

# TLDR

**创建晕渲地貌图**，以高程图为输入

```pamshadedrelief [heightmap.pam] > [relief.pam]```

**应用伽马校正**到渲染出的地貌图

```pamshadedrelief -gamma [2.0] [heightmap.pam] > [relief.pam]```

**通过管道传给 pamtopnm** 以 PPM 格式查看

```pamshadedrelief [heightmap.pam] | pamtopnm > [relief.ppm]```

**渲染并编码**为 PNG

```pamshadedrelief [heightmap.pam] | pnmtopng > [relief.png]```

# SYNOPSIS

**pamshadedrelief** [**-gamma** _value_] [_pamfile_]

# DESCRIPTION

**pamshadedrelief** 读取包含灰度高程图的 Netpbm PAM 文件，并生成一幅渲染为晕渲地貌的 PAM 图像，模拟虚拟光源对三维地形的照射。每个输出像素编码的是由高度场局部坡度推导出的亮度，从而产生类似地形图上的山体阴影效果。

输入必须是单通道（灰度）PAM 图像；采样值被解释为海拔高度。光照角度由程序固定。输出采样值可通过 **-gamma** 进行伽马校正，因而无需重新渲染源数据即可调节地貌图的对比度。

# PARAMETERS

_PAMFILE_
> 输入的灰度 PAM 高程图。省略时从标准输入读取。

**-gamma** _VALUE_
> 对输出应用伽马校正。值大于 1 会增强暗部区域的对比度；值小于 1 则会减弱。默认为 1.0。

# CAVEATS

属于 **Netpbm**。输入必须是单平面（灰度）PAM 图像；PGM 输入应先提升为 PAM。光照方向是硬编码的，无法通过命令行更改。输出为 PAM 图像；如需显示，可用 **pamtopnm** 或 **pnmtopng** 转换为 PPM 或 PNG。

# HISTORY

**pamshadedrelief** 被加入 **Netpbm**，用于支持制图和地形可视化任务。Netpbm 提供了一族历史悠久、小巧且可组合的图像工具，用于处理 PNM/PAM 系列格式。

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

[pamtopnm](/man/pamtopnm)(1), [pnmtopng](/man/pnmtopng)(1), [pamflip](/man/pamflip)(1)
