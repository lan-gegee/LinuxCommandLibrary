# TAGLINE

用于 XML 转换的 XSLT 和 XQuery 处理器

# TLDR

**使用 XSLT 样式表转换 XML 文件**

```saxon -s:[source.xml] -xsl:[stylesheet.xsl] -o:[output.xml]```

**对 XML 文件执行 XQuery**

```saxon -s:[source.xml] -q:[query.xq] -o:[output.xml]```

**带参数进行转换**

```saxon -s:[source.xml] -xsl:[stylesheet.xsl] param=[value]```

**执行独立的 XQuery 文件**

```saxon -q:[query.xq]```

**执行感知模式的转换**

```saxon -sa -s:[source.xml] -xsl:[stylesheet.xsl]```

**以更大内存进行转换**

```java -Xmx1024m net.sf.saxon.Transform -s:[source.xml] -xsl:[stylesheet.xsl]```

# SYNOPSIS

**saxon** [_options_] [_-s:source_] [_-xsl:stylesheet_] [_-q:query_] [_-o:output_] [_params_]

# PARAMETERS

**-s:**_file_
> 要处理的源 XML 文档

**-xsl:**_file_
> 用于转换的 XSLT 样式表

**-q:**_file_
> 要执行的 XQuery 文件

**-o:**_file_
> 结果输出文件

**-sa**
> 启用感知模式的处理

**-t**
> 显示耗时信息

**-explain**
> 显示编译后的表达式树

**-versionmsg:off**
> 抑制版本消息

**-xsd:**_file_
> 用于验证的模式文档

# DESCRIPTION

**Saxon** 是一款 XSLT 和 XQuery 处理器，用于转换 XML 文档。它支持 XSLT 3.0、XPath 3.1 和 XQuery 3.1，能够执行复杂的文档转换和查询。

该工具针对 XSLT 样式表或 XQuery 表达式处理 XML 输入，生成转换后的输出。在许多系统上，**saxonb-xslt** 和 **saxonb-xquery** 等包装脚本提供了便捷的命令行访问方式。

Saxon 有三个版本：Saxon-HE（MPL-2.0 开源）、Saxon-PE（专业版）和 Saxon-EE（企业版，具备模式感知能力）。它可运行在 Java、.NET 和 JavaScript 平台上。

# CAVEATS

复杂转换所需的内存通过 Java 的 **-Xmx** 选项控制。感知模式的特性需要 Saxon-EE。命令语法在不同 Saxon 版本和平台包装脚本之间有所差异。

# HISTORY

Saxon 由 **Michael Kay** 创建，他曾是 W3C XSLT 规范的编辑。开发始于 **1998 年**，Kay 随后创立了 **Saxonica** 来维护该处理器并将其商业化。自 **2023 年**起，Saxon 仅在 Saxonica 网站上发布，不再托管于 SourceForge。

# INSTALL

```brew: brew install saxon```

```nix: nix profile install nixpkgs#saxon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xsltproc](/man/xsltproc)(1), [xmllint](/man/xmllint)(1), [xq](/man/xq)(1), [java](/man/java)(1)
