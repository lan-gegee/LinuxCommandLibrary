# TAGLINE

将 PNM 图像转换为 DEC DDIF 文档

# TLDR

**将 PNM 转换为 DDIF**

```pnmtoddif [input.pnm] > [output.ddif]```

以 DPI 为单位**指定输出分辨率**

```pnmtoddif -resolution [300] [input.pnm] > [output.ddif]```

**从标准输入读取**

```cat [input.pnm] | pnmtoddif > [output.ddif]```

# SYNOPSIS

**pnmtoddif** [_-resolution dpi_] [_pnmfile_]

# PARAMETERS

_PNMFILE_
> 输入的 PNM（PBM、PGM 或 PPM）图像。省略时，**pnmtoddif** 从标准输入读取。

**-resolution** _N_
> 在 DDIF 输出中嵌入给定的分辨率（每英寸点数）。默认为 75 DPI。

# DESCRIPTION

**pnmtoddif** 将 PNM 图像（PBM、PGM 或 PPM）转换为标准输出上的 DEC **DDIF**（Digital Document Interchange Format）文档。DDIF 是 DEC 的 CDA（Compound Document Architecture）所使用的复合文档格式，最突出地体现在随 VMS 和 Ultrix 附带的 DECwindows 应用程序与文档工具中。

转换器会保留输入的位深：PBM 变成 1 位的 DDIF 页面，PGM 变成灰度，PPM 变成 24 位彩色。记录在 DDIF 头中的输出分辨率由 **-resolution** 指定（默认 75 DPI），它会影响下游查看器缩放图像的方式。

# CAVEATS

DDIF 是一种遗留格式；在历史上的 DEC/Compaq 工具链之外，查看器和转换器都很少见。当前的 Netpbm 发行版中没有内置从 DDIF 转回 PNM 的转换器。

# HISTORY

**pnmtoddif** 是为实现与 **DEC** Compound Document Architecture 工具的互操作性而贡献给 **Netpbm** 的。它留在发行版中主要是出于存档和遗留兼容的目的。

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

[pnmtops](/man/pnmtops)(1), [pnmtopng](/man/pnmtopng)(1), [pamtopnm](/man/pamtopnm)(1)
