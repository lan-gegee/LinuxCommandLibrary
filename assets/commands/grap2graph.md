# TAGLINE

Grap 图形转图像转换器

# TLDR

**将 grap 转换为图像**

```grap2graph [file.grap] > output.png```

**指定输出格式**

```grap2graph -Tpng [file.grap] > output.png```

**创建 SVG 输出**

```grap2graph -Tsvg [file.grap] > output.svg```

**从标准输入处理**

```echo ".G1 ... .G2" | grap2graph > output.png```

# SYNOPSIS

**grap2graph** [_options_] [_file_]

# PARAMETERS

_FILE_
> 包含 grap 代码的输入文件。

**-T** _FORMAT_
> 输出格式（png、svg、pdf 等）。

**-resolution** _DPI_
> 设置图像分辨率。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grap2graph** 将 grap 图形转换为图像格式。它是一个封装工具，将 grap 输出通过 groff 管道处理，并把结果转换为 PNG、SVG、PDF 等多种图像格式。

该工具是 groff 套件的一部分，会自动处理中间步骤，从 grap 源码生成独立图像。

# CAVEATS

需要 groff 和 grap。图像质量取决于分辨率设置。属于 groff 软件包的一部分。

# HISTORY

grap2graph 作为 **GNU groff** 项目的一部分开发，旨在简化从 grap 源码创建图形图像的过程。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grap](/man/grap)(1), [groff](/man/groff)(1)
