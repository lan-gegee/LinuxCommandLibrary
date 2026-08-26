# TAGLINE

用于 XML 转换的 Apache XSLT 处理器

# TLDR

**使用 XSLT 转换 XML**

```java org.apache.xalan.xslt.Process -IN [input.xml] -XSL [style.xsl] -OUT [output.html]```

**转换结果输出到 stdout**

```java org.apache.xalan.xslt.Process -IN [input.xml] -XSL [style.xsl]```

**设置样式表参数**

```java org.apache.xalan.xslt.Process -IN [input.xml] -XSL [style.xsl] -PARAM [name] [value]```

**以 XML 格式输出**

```java org.apache.xalan.xslt.Process -IN [input.xml] -XSL [style.xsl] -XML```

**检查环境**

```java org.apache.xalan.xslt.EnvironmentCheck```

**使用 XSLTC 编译器**

```java org.apache.xalan.xslt.Process -XSLTC -IN [input.xml] -XSL [style.xsl]```

# SYNOPSIS

**java org.apache.xalan.xslt.Process** [_options_]

# PARAMETERS

**-IN** _file_
> 输入 XML 文档的 URL。

**-XSL** _file_
> XSLT 样式表的 URL。

**-OUT** _file_
> 输出文件名。

**-PARAM** _name_ _value_
> 设置样式表参数。

**-XML**
> 以带声明的 XML 格式输出。

**-HTML**
> 以 HTML 格式输出。

**-TEXT**
> 以纯文本格式输出。

**-XSLTC**
> 使用 XSLTC 编译转换。

**-V**
> 显示版本。

**-EDUMP** _file_
> 出错时转储堆栈跟踪。

# DESCRIPTION

**Xalan** 是一款用于转换 XML 文档的 XSLT 处理器。它实现了 XSLT 1.0 和 XPath 1.0，依据样式表规则将 XML 转换为 HTML、文本或其他 XML 格式。

该处理器由 Java 编写，需要 JVM 并将 Xalan JAR 加入类路径。它支持 JAXP 转换 API，既可以作为库使用，也可以作为命令行工具使用。

XSLTC 模式将样式表编译为 Java 字节码，从而加快重复转换的速度。这对使用同一样式表处理大量文档的服务端应用很有用。

# CAVEATS

需要 Java 运行时并正确配置类路径。仅支持 XSLT 1.0；如需 XSLT 2.0 及以上版本请使用 Saxon。处理大文档可能需要调整 JVM 内存。

# HISTORY

**Xalan** 由 Apache 软件基金会开发，是 Apache XML 项目的一部分。它以一种乐器命名，后来成为使用最广泛的开源 XSLT 处理器之一，尤其在 Java 环境中。

# INSTALL

```apt: sudo apt install xalan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xsltproc](/man/xsltproc)(1), [saxon](/man/saxon)(1), [xmllint](/man/xmllint)(1)
