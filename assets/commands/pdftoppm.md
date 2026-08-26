# TAGLINE

将 PDF 文档页面转换为图像格式

# TLDR

指定要转换的**页码范围**（n 为第一页，m 为最后一页）

```pdftoppm -f [n] -l [m] [path/to/file.pdf] [image_name_prefix]```

只转换 PDF 的**第一页**

```pdftoppm -singlefile [path/to/file.pdf] [image_name_prefix]```

生成**单色 PBM** 文件（而非彩色 PPM）

```pdftoppm -mono [path/to/file.pdf] [image_name_prefix]```

生成**灰度 PGM** 文件（而非彩色 PPM）

```pdftoppm -gray [path/to/file.pdf] [image_name_prefix]```

生成 **PNG 文件**而非 PPM

```pdftoppm -png [path/to/file.pdf] [image_name_prefix]```

# SYNOPSIS

**pdftoppm** [_options_] _pdf_file_ _image_root_

# PARAMETERS

**-f _n_**
> 要转换的第一页

**-l _n_**
> 要转换的最后一页

**-singlefile**
> 只写入第一页，不添加页码后缀

**-mono**
> 生成单色 PBM 输出

**-gray**
> 生成灰度 PGM 输出

**-png**
> 生成 PNG 输出

**-jpeg**
> 生成 JPEG 输出

**-tiff**
> 生成 TIFF 输出

**-r _dpi_**
> 以 DPI 表示的分辨率（默认：150）

**-rx _dpi_**
> X 方向分辨率

**-ry _dpi_**
> Y 方向分辨率

**-scale-to _size_**
> 缩放到指定尺寸

# DESCRIPTION

**pdftoppm** 将 PDF 文档页面转换为图像格式（PPM、PGM、PBM、PNG、JPEG、TIFF）。它是 **poppler-utils** 软件包的一部分，以指定的分辨率将每一页渲染为光栅图像。

输出文件以给定前缀加页码命名（例如 image-001.png）。若只需转换单页且不加编号，请使用 **-singlefile**。

该工具常用于制作缩略图、为 OCR 预处理 PDF，或将文档转换为适合图像化工作流的格式。

# CAVEATS

高 DPI 设置会生成大文件并占用更多内存。处理大量页面可能较慢。矢量图形会被光栅化，从而失去可缩放性。属于 poppler-utils 软件包。

# INSTALL

```apt: sudo apt install poppler-utils```

```dnf: sudo dnf install poppler-utils```

```apk: sudo apk add poppler-utils```

```nix: nix profile install nixpkgs#poppler-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdftohtml](/man/pdftohtml)(1), [pdftotext](/man/pdftotext)(1), [pdfinfo](/man/pdfinfo)(1), [convert](/man/convert)(1)
