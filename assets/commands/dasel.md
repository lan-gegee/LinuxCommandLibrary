# TAGLINE

用于查询和修改结构化数据的通用数据选择器

# TLDR

**从 JSON 文件查询值**

```dasel -f [file.json] '[selector]'```

**从 YAML 查询嵌套值**

```dasel -f [config.yaml] '.database.host'```

**将 JSON 转换为 YAML**

```dasel -f [input.json] -p json -w yaml```

**修改 JSON 文件中的值**

```dasel put -f [file.json] -v '[new_value]' '[selector]'```

**从 YAML 文件删除键**

```dasel delete -f [file.yaml] '[selector]'```

**从 stdin 读取**并以 JSON 输出

```cat [file.yaml] | dasel -p yaml -w json```

**从 XML 查询值**

```dasel -f [file.xml] '.root.element'```

# SYNOPSIS

**dasel** [_command_] [_flags_] [_selector_]

**dasel** select [_-f file_] [_-p parser_] [_-w writer_] _selector_

**dasel** put [_-f file_] [_-t type_] [_-v value_] _selector_

**dasel** delete [_-f file_] _selector_

# PARAMETERS

**-f**, **--file** _PATH_
> 输入文件路径；省略时从 stdin 读取

**-p**, **--parser** _FORMAT_
> 输入数据的解析器（json、yaml、toml、xml、csv、ini、hcl）；根据文件扩展名自动检测

**-w**, **--write** _FORMAT_
> 输出格式；默认与输入解析器类型相同

**-t**, **--type** _TYPE_
> put 命令的值类型（string、int、bool、json）

**-v**, **--value** _VALUE_
> put 命令要设置的值

**-o**, **--out** _FILE_
> 输出文件路径；省略时写到 stdout

**-r**, **--read** _FORMAT_
> --parser 的别名

**--pretty**
> 美化打印输出以提高可读性

**-n**, **--null**
> 显式输出 null 值

**--colour**, **--color**
> 启用彩色输出

**--escape-html**
> 转义输出中的 HTML 实体

**-h**, **--help**
> 显示帮助信息

**-v**, **--version**
> 显示版本信息

# DESCRIPTION

**dasel**（Data Selector）是一个用于查询和修改结构化数据文件的命令行工具。它以统一的选择器语法处理 JSON、YAML、TOML、XML、CSV、INI 和 HCL 格式，提供一致的接口。

该工具支持三种主要操作：用于查询数据的 **select**、用于修改或添加值的 **put**，以及用于移除键的 **delete**。选择器使用点号表示法访问嵌套结构（如 `.database.host`），使用方括号表示法访问数组下标（如 `.users.[0].name`）。

Dasel 通过指定不同的输入和输出解析器实现格式之间的转换，非常适合配置文件转换场景。它可以从文件或 stdin 读取，写入文件或 stdout，与 shell 管道配合良好。

# CAVEATS

受解析器限制，写入 YAML 和 TOML 文件时会丢弃注释。整个文档会加载进内存，因此非常大的文件可能占用大量内存。数组下标从零开始。修改文件时，原始格式可能无法完全保留。

# HISTORY

Dasel 由 **Tom Wright** 创建并于 **2020 年**首次发布。它用 **Go** 编写，被设计为 **jq**（JSON）、**yq**（YAML）和 **xmlstarlet**（XML）等特定格式工具的通用替代品。名字是 "data" 和 "select" 的合成词。它因能在多种数据格式上使用相同的选择器语法，以及单二进制无依赖的分发方式而广受欢迎。

# INSTALL

```apt: sudo apt install dasel```

```apk: sudo apk add dasel```

```brew: brew install dasel```

```nix: nix profile install nixpkgs#dasel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [xmlstarlet](/man/xmlstarlet)(1), [mlr](/man/mlr)(1)
