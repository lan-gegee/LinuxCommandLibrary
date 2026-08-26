# TAGLINE

将 XML 转换为多种输出格式

# TLDR

**转换为 HTML**

```xmlto html [document.xml]```

**转换为 PDF**

```xmlto pdf [document.xml]```

**转换为 man page**

```xmlto man [document.xml]```

**指定输出目录**

```xmlto -o [output/] html [document.xml]```

**使用样式表**

```xmlto -x [custom.xsl] html [document.xml]```

# SYNOPSIS

**xmlto** [_-o dir_] [_-x stylesheet_] [_options_] _format_ _file_

# PARAMETERS

**-o** _DIR_
> 输出目录。

**-x** _XSL_
> 自定义样式表。

**-v**
> 详细模式。

**--skip-validation**
> 跳过 DTD 校验。

_format_
> 输出格式。

# DESCRIPTION

**xmlto** 是一个前端工具，使用 XSL 样式表将 XML 文档转换为多种输出格式。它支持从 XML 源文件生成 HTML、PDF、man 页面、纯文本等格式，尤其擅长处理 DocBook 文档。

该工具充当 XSLT 处理器和排版后端的包装器，负责处理样式表选择和工具调用等细节。可以通过 **-x** 选项提供自定义样式表，覆盖默认转换行为，使输出符合特定需求。

xmlto 常用于软件文档工作流：源文档以 DocBook XML 格式维护，需要发布成面向不同读者的多种输出格式。

# CAVEATS

需要安装 DocBook XSL 样式表和 XSLT 处理器（xsltproc）。PDF 输出还需要 FOP 或 dblatex 之类的排版后端。主要为 DocBook XML 设计；其他 XML 词表需要自定义样式表。

# HISTORY

**xmlto** 的创建目的是将 XML 文档（尤其是 DocBook）转换为多种输出格式。

# INSTALL

```apt: sudo apt install xmlto```

```dnf: sudo dnf install xmlto```

```pacman: sudo pacman -S xmlto```

```apk: sudo apk add xmlto```

```zypper: sudo zypper install xmlto```

```brew: brew install xmlto```

```nix: nix profile install nixpkgs#xmlto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xsltproc](/man/xsltproc)(1), [docbook2html](/man/docbook2html)(1), [pandoc](/man/pandoc)(1)
