# TAGLINE

XSL-FO 转 PDF 处理器

# TLDR

**将 XSL-FO 转换为 PDF**

```fop [input.fo] [output.pdf]```

**用 XSLT 转换 XML** 为 PDF

```fop -xml [input.xml] -xsl [style.xsl] -pdf [output.pdf]```

**转换为 PostScript**

```fop [input.fo] -ps [output.ps]```

**转换为 PNG**

```fop [input.fo] -png [output.png]```

**使用指定配置文件**

```fop -c [fop.xconf] [input.fo] [output.pdf]```

**仅校验 XSL-FO**

```fop -fo [input.fo] -v```

# SYNOPSIS

**fop** [_options_] [_input_] [_output_]

# DESCRIPTION

**fop**（Formatting Objects Processor）是 Apache 项目，将 XSL-FO（XSL Formatting Objects）文档转换为多种输出格式。它常用于从 XML 数据生成 PDF。

该工具支持从 XML 经 XSLT 到 XSL-FO 再到最终输出的转换流水线。它能够处理复杂的页面布局、表格和排版。

# PARAMETERS

**-fo** _file_
> 输入的 XSL-FO 文件。

**-xml** _file_
> 输入的 XML 文件。

**-xsl** _file_
> XSLT 样式表。

**-pdf** _file_
> 输出为 PDF。

**-ps** _file_
> 输出为 PostScript。

**-png** _file_
> 输出为 PNG。

**-awt**
> 在 AWT 查看器中显示。

**-c** _file_
> 配置文件。

**-v**
> 详细输出。

**-d**
> 调试模式。

# CONFIGURATION

**fop.xconf**
> 用于字体、渲染器和连字符设置的配置文件。

# CAVEATS

需要 Java。复杂布局可能需要调优。大文档内存占用较高。字体配置可能比较麻烦。

# HISTORY

**FOP** 始于 **1999** 年的 **Apache XML** 项目，是最早的开源 XSL-FO 处理器之一。经过多个版本的成熟演进，FOP 2.x 在标准符合性和性能方面带来显著提升。

# INSTALL

```dnf: sudo dnf install fop```

```pacman: sudo pacman -S fop```

```brew: brew install fop```

```nix: nix profile install nixpkgs#fop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xsltproc](/man/xsltproc)(1), [pdflatex](/man/pdflatex)(1), [wkhtmltopdf](/man/wkhtmltopdf)(1), [pandoc](/man/pandoc)(1)

# RESOURCES

```[Homepage](https://xmlgraphics.apache.org/fop/)```

```[Documentation](https://xmlgraphics.apache.org/fop/quickstartguide.html)```

<!-- verified: 2026-07-15 -->
