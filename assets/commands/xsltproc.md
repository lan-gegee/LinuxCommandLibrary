# TAGLINE

命令行 XSLT 处理器

# TLDR

**使用 XSLT 样式表转换 XML**

```xsltproc [stylesheet.xsl] [input.xml]```

**将输出保存到文件**

```xsltproc -o [output.html] [stylesheet.xsl] [input.xml]```

向样式表**传递字符串参数**

```xsltproc --stringparam [name] "[value]" [stylesheet.xsl] [input.xml]```

**传递 XPath 表达式**作为参数

```xsltproc --param [name] "[xpath]" [stylesheet.xsl] [input.xml]```

处理输入中的 **XInclude** 元素

```xsltproc --xinclude [stylesheet.xsl] [input.xml]```

转换 **HTML** 输入

```xsltproc --html [stylesheet.xsl] [input.html]```

**显示计时信息**

```xsltproc --timing [stylesheet.xsl] [input.xml]```

**禁用对外部资源的网络访问**

```xsltproc --nonet [stylesheet.xsl] [input.xml]```

# SYNOPSIS

**xsltproc** [_options_] [_stylesheet_] [_xml-file_]

# PARAMETERS

**-o**, **--output** _file_
> 将输出写入文件而不是 stdout。

**--stringparam** _name_ _value_
> 向样式表传递字符串参数。

**--param** _name_ _value_
> 传递 XPath 表达式的求值结果作为参数。

**--xinclude**
> 转换前先处理 XInclude 元素。

**--html**
> 将输入视为 HTML 而不是 XML。

**--nonet**
> 禁用网络访问（针对 DTD、实体和样式表）。

**--novalid**
> 跳过对输入文档的 DTD 校验。

**--noout**
> 不输出转换结果。

**--timing**
> 显示解析和转换的耗时。

**--profile**
> 输出用于优化的剖析信息。

**--maxdepth** _value_
> 模板栈的最大深度（默认：3000）。

**--nowrite**
> 拒绝写入任何文件。

**--nomkdir**
> 拒绝创建目录。

**-v**, **--verbose**
> 处理过程中输出每一步操作。

**-V**, **--version**
> 显示 libxml 和 libxslt 的版本号。

# DESCRIPTION

**xsltproc** 是一个命令行 XSLT 处理器，用于使用 XSLT 样式表转换 XML 文档。它是 libxslt（GNOME 的 XSLT C 库）的一部分，但可以独立于 GNOME 桌面运行。

如果输入的 XML 文档包含样式表处理指令，xsltproc 可以自动使用所引用的样式表，无需在命令行中指定。

该工具支持 XSLT 1.0 和 EXSLT 扩展。根据样式表的 **xsl:output** 指令，输出可以是 XML、HTML 或文本。

# CAVEATS

xsltproc 仅支持 XSLT 1.0；不支持 XSLT 2.0 和 3.0 特性。需要 XSLT 2.0+ 时可以考虑 Saxon 等其他处理器。返回码表示具体的错误类型（4 = 样式表解析错误，5 = 样式表错误，6 = 文档错误）。

# HISTORY

xsltproc 由 **Daniel Veillard** 为 GNOME 项目开发，是 **libxslt** 库的一部分，于 **2001 年**前后首次发布。它基于 libxml2 进行 XML 解析。该工具已成为类 Unix 系统上命令行 XSLT 处理的标准工具，包含在大多数 Linux 发行版中。

# INSTALL

```apt: sudo apt install xsltproc```

```dnf: sudo dnf install libxslt```

```pacman: sudo pacman -S libxslt```

```apk: sudo apk add libxslt```

```brew: brew install libxslt```

```nix: nix profile install nixpkgs#libxslt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xmlstarlet](/man/xmlstarlet)(1), [xmllint](/man/xmllint)(1), [saxon](/man/saxon)(1), [xalan](/man/xalan)(1)
