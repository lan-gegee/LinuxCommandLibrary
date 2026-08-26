# TAGLINE

自动化 Inkscape 导出，便于批量处理

# TLDR

**导出所有图层**

```inkmake [input.svg]```

**按指定尺寸导出**

```inkmake -w [1024] [input.svg]```

**导出到目录**

```inkmake -o [output/] [input.svg]```

**以指定格式导出**

```inkmake -f [png|pdf|svg] [input.svg]```

**导出指定图层**

```inkmake -l "[layer1,layer2]" [input.svg]```

# SYNOPSIS

**inkmake** [_options_] _file_

# PARAMETERS

**-w** _WIDTH_
> 输出宽度（像素）。

**-h** _HEIGHT_
> 输出高度（像素）。

**-o** _DIR_
> 输出目录。

**-f** _FORMAT_
> 输出格式（png、pdf、svg）。

**-l** _LAYERS_
> 逗号分隔的图层名称。

**-d** _DPI_
> 输出分辨率。

**--help**
> 显示帮助信息。

# DESCRIPTION

**inkmake** 自动化 Inkscape 的导出流程，便于批量处理。它可将 SVG 文件中的图层或对象导出为多种格式。

该工具适合从单一源文件生成图标、素材或多尺寸输出。它是 Inkscape 导出能力的封装。

# CAVEATS

需要安装 Inkscape。SVG 图层命名很重要。本质上是包装脚本。

# HISTORY

inkmake 的创建是为了简化从 **Inkscape** SVG 文件的批量导出，用于素材生成工作流。

# SEE ALSO

[inkscape](/man/inkscape)(1), [convert](/man/convert)(1), [rsvg-convert](/man/rsvg-convert)(1)
