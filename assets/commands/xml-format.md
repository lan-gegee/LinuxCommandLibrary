# TAGLINE

美化打印 XML 文档

# TLDR

**以默认缩进格式化 XML 文件**

```xml format [input.xml]```

**以指定数量的空格缩进格式化**

```xml format --indent-spaces [4] [input.xml]```

**以制表符缩进格式化**

```xml format --indent-tab [input.xml]```

**格式化并省略 XML 声明**

```xml format --omit-decl [input.xml]```

**恢复并格式化格式错误的 XML 文件**

```xml format --recover [input.xml]```

**格式化并输出到文件**

```xml format [input.xml] > [output.xml]```

# SYNOPSIS

**xml format** [_options_] [_file_]

# PARAMETERS

**-n**, **--noindent**
> 去除输出中的缩进。

**-t**, **--indent-tab**
> 用制表符缩进。

**-s** _n_, **--indent-spaces** _n_
> 用 n 个空格缩进。

**-o**, **--omit-decl**
> 省略 XML 声明。

**-D**, **--dropdtd**
> 移除 DTD 声明。

**-R**, **--recover**
> 尝试恢复格式错误的 XML。

**-C**, **--nocdata**
> 将 CDATA 区段转换为文本节点。

**-N**, **--nsclean**
> 移除冗余的命名空间声明。

**-e** _encoding_, **--encode** _encoding_
> 以指定编码输出（例如 utf-8）。

**-H**, **--html**
> 将输入视为 HTML。

# DESCRIPTION

**xml format**（也可写作 **xml fo**）用于美化打印 XML 文档。属于 xmlstarlet 工具集。通过适当的缩进和换行重新排版 XML 以提高可读性。还可以恢复格式错误的 XML 并在不同编码之间转换。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-validate](/man/xml-validate)(1), [xml-select](/man/xml-select)(1), [xmllint](/man/xmllint)(1), [xmlstarlet](/man/xmlstarlet)(1)
