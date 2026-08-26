# TAGLINE

把多图 PNM 文件拆分为单独的文件

# TLDR

**拆分多图 PNM 文件**

```pnmsplit [input.pnm] [output%d.pnm]```

**按自定义命名拆分**

```pnmsplit [input.pnm] [frame_%03d.pnm]```

# SYNOPSIS

**pnmsplit** [_options_] _input_ _output_

# PARAMETERS

_INPUT_
> 包含多幅图像的 PNM 文件。

_OUTPUT_
> 带 %d 的输出文件名模板。

**-padname** _N_
> 编号的零填充位数。

# DESCRIPTION

**pnmsplit** 把一个多图 PNM 流拆分为多个独立文件。PNM 文件可以包含串联在一起的多幅图像，该工具会将每一幅提取出来写入单独的输出文件。

输出文件名模板必须包含 **%d** 格式说明符（或 **%03d** 之类的变体），它会被替换为从 0 开始的图像序号。**-padname** 选项控制编号的零填充宽度。这对处理动画帧或批量图像序列非常有用。属于 Netpbm 工具集。

# CAVEATS

输出名称中必须含有 %d。属于 Netpbm 套件。

# HISTORY

pnmsplit 作为 **Netpbm** 的一部分创建，用于处理含多幅图像的文件。

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

[pnmcat](/man/pnmcat)(1), [pnmindex](/man/pnmindex)(1), [pamcut](/man/pamcut)(1)
