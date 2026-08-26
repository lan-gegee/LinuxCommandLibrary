# TAGLINE

归一化 PNM 图像的对比度

# TLDR

**归一化图像对比度**

```pnmnorm [input.pnm] > [output.pnm]```

**指定亮度范围**

```pnmnorm -bpercent [5] -wpercent [5] [input.pnm] > [output.pnm]```

**保留中间调**

```pnmnorm -midvalue [127] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmnorm** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PNM 文件。

**-bpercent** _N_
> 黑场百分比。

**-wpercent** _N_
> 白场百分比。

**-bvalue** _N_
> 黑场截断值。

**-wvalue** _N_
> 白场截断值。

**-midvalue** _N_
> 要保留的中间灰度值。

# DESCRIPTION

**pnmnorm** 通过拉伸直方图、使其占满整个动态范围来归一化 PNM 图像的对比度。它会找出最暗和最亮的像素值，并把它们线性映射到可能的最小值与最大值。

**-bpercent** 和 **-wpercent** 选项控制黑场和白场裁剪的激进程度，即忽略两端一定比例的离群像素。**-midvalue** 选项可在归一化过程中保留某个特定的中间灰度值。属于 Netpbm 工具集。

# CAVEATS

可能会截断极端数值。属于 Netpbm 套件。

# HISTORY

pnmnorm 作为 **Netpbm** 的一部分创建，用于自动增强对比度。

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

[pnmhisteq](/man/pnmhisteq)(1), [pnmgamma](/man/pnmgamma)(1), [ppmnorm](/man/ppmnorm)(1)
