# TAGLINE

专业矢量图形编辑器

# TLDR

**在 GUI 中打开文件**

```inkscape [file.svg]```

**导出为 PNG**

```inkscape [input.svg] -o [output.png]```

**按指定尺寸导出**

```inkscape [input.svg] -w [1024] -h [768] -o [output.png]```

**导出为 PDF**

```inkscape [input.svg] -o [output.pdf]```

**将 SVG 转换为 EPS**

```inkscape [input.svg] -o [output.eps]```

**导出指定区域**

```inkscape [input.svg] --export-area-page -o [output.png]```

**仅导出绘图区域（裁剪到内容）**

```inkscape [input.svg] -D -o [output.png]```

**无 GUI 运行**

```inkscape --export-type=[png] [input.svg]```

**从命令行运行批量操作**

```inkscape --actions="open:[input.svg];export-filename:[output.png];export-do" --batch-process```

# SYNOPSIS

**inkscape** [_options_] [_file_...]

# PARAMETERS

**-o** _FILE_
> 输出文件名。

**-w** _WIDTH_
> 导出宽度（像素）。

**-h** _HEIGHT_
> 导出高度（像素）。

**-d** _DPI_
> 导出分辨率。

**--export-type** _TYPE_
> 导出格式（png、pdf、eps、ps、svg、emf、wmf）。多种格式用逗号分隔。

**-C**, **--export-area-page**
> 导出整个页面区域。

**-D**, **--export-area-drawing**
> 仅导出绘图边界框（裁剪到内容）。

**-i**, **--export-id** _ID_
> 按 ID 导出特定对象。多个对象用分号分隔。

**-l**, **--export-plain-svg**
> 导出为不含 Inkscape 专有命名空间的纯 SVG。

**-T**, **--export-text-to-path**
> 导出时将文本对象转换为路径。

**--actions** _ACTIONS_
> 执行分号分隔的操作序列，用于批量处理。

**--shell**
> 进入交互式命令行 Shell 模式。

**--batch-process**
> 处理文件后关闭，不启动 GUI。

**--pdf-page** _N_
> 从多页 PDF 导入的页码（从 1 开始）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Inkscape** 是一款专业矢量图形编辑器。它以 SVG 为原生格式，可导出为 PNG、PDF、EPS 等其他格式。

该应用提供全面的绘图工具、路径操作和文本处理能力，还可以无界面（headless）方式运行进行批量转换。

# CAVEATS

大文件可能较慢。部分 SVG 特性不受支持。1.0 版本的命令行接口变化很大（`-e`、`-A` 等旧标志已被替换）。

# HISTORY

Inkscape 于 2003 年从 **Sodipodi** 分支而来，后来成为 Adobe Illustrator 的主要开源替代品。

# INSTALL

```apt: sudo apt install inkscape```

```dnf: sudo dnf install inkscape```

```pacman: sudo pacman -S inkscape```

```apk: sudo apk add inkscape```

```zypper: sudo zypper install inkscape```

```nix: nix profile install nixpkgs#inkscape```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inkview](/man/inkview)(1), [convert](/man/convert)(1), [rsvg-convert](/man/rsvg-convert)(1), [svgo](/man/svgo)(1), [gimp](/man/gimp)(1)
