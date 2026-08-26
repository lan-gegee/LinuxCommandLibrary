# TAGLINE

使用 XPath 查询 XML 文档

# TLDR

**用 XPath 选择节点**

```xml select -t -v "[//element]" [file.xml]```

**提取多个值**

```xml select -t -m "[//item]" -v "[@name]" -n [file.xml]```

**带命名空间选择**

```xml select -N [ns=http://example.com] -t -v "[//ns:element]" [file.xml]```

**复制匹配的节点**

```xml select -t -c "[//element]" [file.xml]```

# SYNOPSIS

**xml select** [_options_] _xpath_ [_file_...]

# PARAMETERS

**-t**, **--template**
> 开始模板。

**-v**, **--value-of** _xpath_
> 输出 XPath 表达式的值。

**-m**, **--match** _xpath_
> 匹配 XPath 表达式。

**-c**, **--copy-of** _xpath_
> 复制匹配的节点。

**-n**, **--nl**
> 输出换行符。

**-N** _prefix=uri_
> 定义命名空间前缀。

**-T**
> 文本输出模式。

# DESCRIPTION

**xml select** 使用 XPath 表达式查询 XML 文档。属于 xmlstarlet 工具集。从 XML 文件中提取值、属性和节点集。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-edit](/man/xml-edit)(1), [xml-format](/man/xml-format)(1), [xmllint](/man/xmllint)(1)
