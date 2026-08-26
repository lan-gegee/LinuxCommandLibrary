# TAGLINE

对 XML 应用 XSLT 样式表

# TLDR

**应用 XSLT 转换**

```xml transform [stylesheet.xsl] [input.xml]```

**带参数转换**

```xml transform --xinclude -p "[param=value]" [stylesheet.xsl] [input.xml]```

**输出到文件**

```xml transform [stylesheet.xsl] [input.xml] > [output.xml]```

# SYNOPSIS

**xml transform** [_options_] _stylesheet_ _file_

# PARAMETERS

**-p**, **--param** _name=value_
> 向样式表传递参数。

**-s**, **--stringparam** _name=value_
> 传递字符串参数。

**--xinclude**
> 处理 XInclude。

**--html**
> 输入为 HTML。

**--omit-decl**
> 省略 XML 声明。

# DESCRIPTION

**xml transform** 将 XSLT 样式表应用于 XML 文档。属于 xmlstarlet 工具集。使用 XSLT 1.0 处理器转换 XML，用于文档转换和处理。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-select](/man/xml-select)(1), [xsltproc](/man/xsltproc)(1)
