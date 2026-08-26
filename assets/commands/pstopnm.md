# TAGLINE

将 PostScript 和 PDF 转换为 PNM 格式

# TLDR

**将 PostScript 转换为 PNM**

```pstopnm [input.ps]```

**以指定分辨率转换**

```pstopnm -dpi [300] [input.ps]```

**转换为特定格式**

```pstopnm -ppm [input.ps]```

**转换 PDF**

```pstopnm [input.pdf]```

# SYNOPSIS

**pstopnm** [_options_] _file_

# PARAMETERS

**-dpi** _n_
> 输出分辨率。

**-xsize** _n_
> 输出宽度。

**-ysize** _n_
> 输出高度。

**-ppm**
> 强制输出 PPM。

**-pgm**
> 强制输出 PGM。

**-pbm**
> 强制输出 PBM。

**-stdout**
> 写入 stdout。

# DESCRIPTION

**pstopnm** 将 PostScript 和 PDF 文件转换为 PNM 格式。它使用 Ghostscript 进行渲染，是 Netpbm 文档转换工具集的一部分。

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

[gs](/man/gs)(1), [pnmtops](/man/pnmtops)(1)
