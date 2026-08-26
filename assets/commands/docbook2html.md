# TAGLINE

DocBook 转 HTML 转换器

# TLDR

**将 DocBook 转换为 HTML**

```docbook2html [document.xml]```

**转换为单个 HTML 文件**

```docbook2html --nochunks [document.xml]```

**指定输出目录**

```docbook2html -o [output_dir] [document.xml]```

**使用自定义样式表转换**

```docbook2html --stylesheet [custom.xsl] [document.xml]```

**直接使用 XSLT 处理器**

```xsltproc /usr/share/xml/docbook/stylesheet/docbook-xsl/html/docbook.xsl [document.xml]```

# SYNOPSIS

**docbook2html** [_options_] _xmlfile_

# PARAMETERS

**-o**, **--output** _dir_
> 生成文件的输出目录。

**--nochunks**
> 生成单个 HTML 文件而非多个。

**--stylesheet** _xsl_
> 自定义 XSLT 样式表。

**-V** _param=value_
> 设置 XSLT 参数。

**--skip-validation**
> 跳过 DTD 校验。

**--help**
> 显示帮助。

# DESCRIPTION

**docbook2html** 将 DocBook XML 文档转换为 HTML 格式。DocBook 是一种面向技术文档的语义标记语言，它将内容与呈现方式分离。

该工具使用 XSLT 样式表把 DocBook 元素转换为 HTML。默认情况下，它会生成带导航的分块输出（多个 HTML 文件）；**--nochunks** 则生成单个文件。

现代实现通常直接使用 **xsltproc** 配合 DocBook XSL 样式表，以便更精细地控制转换参数。docbook2html 封装脚本简化了常见的转换操作。

# XSLTPROC USAGE

```bash
# Chunked HTML
xsltproc \
  --output output_dir/ \
  /usr/share/xml/docbook/stylesheet/docbook-xsl/html/chunk.xsl \
  document.xml

# Single HTML
xsltproc \
  /usr/share/xml/docbook/stylesheet/docbook-xsl/html/docbook.xsl \
  document.xml > output.html
```

# CAVEATS

需要安装 DocBook XSL 样式表。DTD 校验需要网络访问权限或本地 catalog。大文档处理速度可能较慢。输出的样式取决于 CSS；默认 HTML 外观可能比较朴素。

# HISTORY

DocBook 于 **20 世纪 90 年代初**起源于 **HaL Computer Systems** 和 **O'Reilly**，最初是一个用于计算机文档的 SGML 应用。90 年代末过渡到 XML。包括 docbook2html 在内的 docbook-utils 软件包就是为简化转换而创建的。**Norman Walsh** 自 **1999 年**起一直是 DocBook XSL 样式表的主要维护者。

# SEE ALSO

[xsltproc](/man/xsltproc)(1), [pandoc](/man/pandoc)(1), [xmllint](/man/xmllint)(1)
