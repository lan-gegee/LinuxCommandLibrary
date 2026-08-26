# TAGLINE

使用 jq 语法的 XML 处理器

# TLDR

**将 XML 转换为 JSON**

```xq . [file.xml]```

**使用 jq 语法提取值**

```xq '.[key]' [file.xml]```

**转换并格式化 XML**

```cat [file.xml] | xq .```

**将 JSON 转回 XML**

```xq -x . [file.json]```

**处理多个 XML 文件**

```xq . [a.xml] [b.xml]```

**流式处理大型 XML 文档**

```xq . --xml-item-depth [2] [large.xml]```

**用 XML 根元素包裹输出**

```xq -x --xml-root [root] . [file.json]```

# SYNOPSIS

**xq** [_options_] _jq-filter_ [_file_...]

# PARAMETERS

**-x**, **--xml-output**
> 将输出转码回 XML。

**--xml-item-depth** _n_
> 在深度 n 处流式处理元素（用于大型文档）。

**--xml-dtd**
> 保留文档类型定义（DTD）。

**--xml-root** _name_
> 用以此命名的元素包裹 XML 输出。

**--xml-force-list** _element_
> 强制某元素始终为列表。

**-i**, **--in-place**
> 就地编辑文件。

**-c**, **--compact-output**
> 紧凑的 JSON 输出。

**-r**, **--raw-output**
> 原始字符串输出。

**--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**xq** 是一个封装了 jq 的命令行 XML 处理器。它使用 xmltodict 将 XML 文档转换为 JSON，通过 jq 进行处理，并可选地将结果转回 XML。

该工具让你可以在 XML 数据上使用 jq 强大的 JSON 查询语法。所有标准的 jq 过滤器和操作都可用于转换后的 JSON 表示。

对于大型 XML 文档，--xml-item-depth 选项可启用流式模式，在指定深度处理元素而无需将整个文档载入内存。

出于安全考虑，实体展开和 DTD 解析默认被禁用。安装方式：`pip install yq` 或 `brew install python-yq`

# CAVEATS

XML 属性的顺序可能无法保留。某些 XML 特性在 JSON 中的表示能力有限。属于 yq 软件包的一部分（不是基于 Go 的 yq）。需要 Python 和 jq。

# HISTORY

**xq** 由 Andrey Kislyuk 作为 yq 项目的一部分创建，旨在为 YAML 和 XML 提供 jq 风格的功能。它填补了用熟悉的 jq 语法进行命令行 XML 处理的空白。

# INSTALL

```apt: sudo apt install xq```

```dnf: sudo dnf install xq```

```apk: sudo apk add xq```

```brew: brew install xq```

```nix: nix profile install nixpkgs#xq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [xmllint](/man/xmllint)(1), [xmlstarlet](/man/xmlstarlet)(1)
