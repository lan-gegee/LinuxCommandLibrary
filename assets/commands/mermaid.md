# TAGLINE

将文本形式的 Mermaid 定义渲染为图片

# TLDR

**从文件生成图表**

```mmdc -i [input.mmd] -o [output.png]```

**输出为 SVG**

```mmdc -i [input.mmd] -o [output.svg]```

**输出为 PDF**

```mmdc -i [input.mmd] -o [output.pdf]```

**使用指定主题**

```mmdc -i [input.mmd] -o [output.png] -t [dark]```

**设置背景颜色**

```mmdc -i [input.mmd] -o [output.png] -b [white]```

**从标准输入读取**

```echo "graph LR; A-->B" | mmdc -o [diagram.png]```

# SYNOPSIS

**mmdc** [_options_]

# DESCRIPTION

**mmdc**（Mermaid CLI）将文本定义的 Mermaid 图表渲染为图片。Mermaid 是一种图表描述语言，可用于流程图、时序图、类图等多种图形。

该工具可在文档流水线和脚本中实现图表的自动化生成。

# PARAMETERS

**-i** _file_
> 输入的 mermaid 文件。

**-o** _file_
> 输出文件。

**-t** _theme_
> 主题（default、forest、dark、neutral）。

**-b** _color_
> 背景颜色。

**-c** _file_
> 配置 JSON 文件。

**-w** _width_
> 宽度（像素）。

**-H** _height_
> 高度（像素）。

**-p** _file_
> Puppeteer 配置文件。

**-s** _scale_
> 缩放系数（puppeteer 设备像素比）。

**-e** _format_
> 输出格式：_png_、_svg_、_pdf_ 或 _md_（覆盖扩展名推断）。

**-f**, **--pdfFit**
> 缩放 PDF 使图表适配单页。

**-q**, **--quiet**
> 不输出提示信息。

**-I** / **--svgId** _id_
> 在生成的 SVG 元素上设置 `id` 属性。

**--cssFile** _path_
> 向 SVG 注入自定义 CSS 样式表。

# DIAGRAM TYPES

**graph/flowchart**: 流程图
**sequenceDiagram**: 时序图
**classDiagram**: 类图
**stateDiagram**: 状态机
**gantt**: 甘特图
**pie**: 饼图

# CAVEATS

需要 Puppeteer/Chromium。复杂图表可能需要调参。PDF 质量参差不齐。大型图表可能较慢。

# HISTORY

**Mermaid** 由 **Knut Sveidqvist** 于 **2014 年**前后创建，旨在提供一种简单的基于文本的图表语言。CLI 工具实现了命令行渲染，与浏览器和文档工具中的网页端渲染相辅相成。

# SEE ALSO

[graphviz](/man/graphviz)(1), [plantuml](/man/plantuml)(1), [ditaa](/man/ditaa)(1), [drawio](/man/drawio)(1)
