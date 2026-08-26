# TAGLINE

为 Kodak Photo CD 创建索引图

# TLDR

从 Photo CD 概览文件**生成索引图**

```pcdovtoppm [overview.pcd] > [index.ppm]```

**设置结果图像的最大宽度**

```pcdovtoppm -m 768 [overview.pcd] > [index.ppm]```

**设置缩略图尺寸**和每行图像数

```pcdovtoppm -s 96 -a 4 [overview.pcd] > [index.ppm]```

使用自定义字体标注并以白色为背景

```pcdovtoppm -f [smallfont.pbm] -w [overview.pcd] > [index.ppm]```

# SYNOPSIS

**pcdovtoppm** [**-m** _width_] [**-s** _size_] [**-a** _across_] [**-c** _colors_] [**-f** _font_] [**-b**|**-w**] [_pcdfile_]

# PARAMETERS

**-m** _width_
> 结果图像的最大宽度（默认：1152）。

**-s** _size_
> 每个缩略图的最大尺寸（像素，默认：192）。

**-a** _across_
> 每行最多显示的图像数（默认：6）。

**-c** _colors_
> 输出中的最大颜色数，或用 **n** 禁用量化。

**-f** _font_
> 用于标注的 PBM 字体文件（默认：内部字体）。

**-b**
> 使用黑色背景（默认）。

**-w**
> 使用白色背景。

# DESCRIPTION

**pcdovtoppm** 根据 Kodak Photo CD 概览文件生成 PPM 格式的索引图。它将 Photo CD 中的缩略图排成网格，并可用可配置字体标注图像编号。该程序旧称 **pcdindex**。属于 **Netpbm** 工具集。

# CAVEATS

需要有效的 Photo CD 概览文件作为输入。输出为 PPM 格式，用于其他用途时可能需要转换。Photo CD 是 20 世纪 90 年代的过时格式。

# HISTORY

**pcdovtoppm** 原名 **pcdindex**，后按 Netpbm 的命名规范更名，转换类程序遵循 _源to目标_ 的命名模式。

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

[pcdindex](/man/pcdindex)(1), [ppmtojpeg](/man/ppmtojpeg)(1)
