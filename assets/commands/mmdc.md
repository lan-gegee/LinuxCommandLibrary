# TAGLINE

用于从文本生成图表的 Mermaid CLI

# TLDR

**从文件生成 SVG 图表**

```mmdc -i [input.mmd] -o [output.svg]```

**生成深色主题的 PNG**

```mmdc -i [input.mmd] -o [output.png] -t dark```

**生成缩放以适应图表的 PDF**

```mmdc -i [input.mmd] -o [output.pdf] -f```

**设置自定义页面尺寸和缩放比例**

```mmdc -i [input.mmd] -o [output.png] -w [1200] -H [800] -s [2]```

**使用自定义的 Mermaid 配置文件**

```mmdc -i [input.mmd] -o [output.svg] -c [config.json]```

**从 stdin 读取**并使用透明背景

```cat [diagram.mmd] | mmdc -i - -o [output.svg] -b transparent```

**处理 Markdown 文件**并提取其中内嵌的图表

```mmdc -i [document.md] -o [document-out.md]```

# SYNOPSIS

**mmdc** [_options_]

# PARAMETERS

**-i**, **--input** _FILE_
> 输入文件路径。使用 `-` 表示 stdin。以 .md 或 .markdown 结尾的文件会被当作 Markdown 处理。

**-o**, **--output** _FILE_
> 输出文件路径。使用 `-` 表示 stdout。默认为 `{input}.svg`。

**-e**, **--outputFormat** _FORMAT_
> 输出格式：svg、png 或 pdf。默认根据输出扩展名推断。

**-t**, **--theme** _THEME_
> Mermaid 主题：default、dark、forest 或 neutral。

**-b**, **--backgroundColor** _COLOR_
> PNG/SVG 输出的背景颜色（默认：白色）。

**-w**, **--width** _WIDTH_
> 页面宽度，单位为像素（默认：800）。

**-H**, **--height** _HEIGHT_
> 页面高度，单位为像素（默认：600）。

**-s**, **--scale** _FACTOR_
> Puppeteer 的 deviceScaleFactor 缩放因子（默认：1）。

**-f**, **--pdfFit**
> 缩放 PDF 输出以适应图表尺寸。

**-c**, **--configFile** _FILE_
> 用于配置 Mermaid 行为的 JSON 配置文件。

**-C**, **--cssFile** _FILE_
> 注入页面的自定义 CSS 文件路径。

**-I**, **--svgId** _ID_
> SVG 元素的 ID 属性（默认：my-svg）。

**-p**, **--puppeteerConfigFile** _FILE_
> 用于 Puppeteer 启动选项的 JSON 配置文件。

**-a**, **--artefacts** _PATH_
> 处理 Markdown 文件时图片的输出路径。

**-q**, **--quiet**
> 抑制输出到 stdout 的日志。

**-V**, **--version**
> 显示版本号。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**mmdc** 是 Mermaid 绘图库的命令行界面。它借助 Puppeteer 驱动无头 Chromium 浏览器，把以 Mermaid 文本语法定义的图表渲染成 SVG、PNG 或 PDF 输出。

支持的图表类型包括流程图、时序图、类图、状态图、甘特图、饼图、ER 图等。当输入是 Markdown 文件时，mmdc 会提取并渲染其中内嵌的 Mermaid 代码块，并用生成的图片替换它们。

**--configFile** 选项接受一个 JSON 文件来配置 Mermaid 的行为，并与 **--theme** 选项合并，配置文件优先。

# CAVEATS

需要 **Node.js**，并通过 **Puppeteer** 下载一个 Chromium 浏览器用于渲染。首次运行可能因下载浏览器而耗时较长。缩放因子（**-s**）只影响 PNG 输出的分辨率。

# HISTORY

**mmdc** 是 **Mermaid** 的 CLI，Mermaid 是由 **Knut Sveidqvist** 创建的基于 JavaScript 的绘图与图表工具。该 CLI 软件包以 **@mermaid-js/mermaid-cli** 之名发布在 npm 上。

# SEE ALSO

[graphviz](/man/graphviz)(1), [plantuml](/man/plantuml)(1), [dot](/man/dot)(1)
