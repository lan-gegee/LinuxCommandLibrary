# TAGLINE

一个类似 jq 的命令行工具，用于查询和转换 Markdown 文件

# TLDR

**提取 Markdown 文件中的所有标题**

```mq '.h' [path/to/file.md]```

按标题文本**选择特定章节**

```mq 'select("Section Name")' [path/to/file.md]```

**提取特定语言的代码块**

```mq '.code("python")' [path/to/file.md]```

**将 Markdown 转换为纯文本**

```mq 'to_text' [path/to/file.md]```

**以 HTML 输出**

```mq -F html '.h1' [path/to/file.md]```

**启动交互式 REPL** 模式

```mq repl [path/to/file.md]```

**从文件加载查询**

```mq -f [query.mq] [path/to/file.md]```

将多个文件**聚合为单个数组**

```mq -A '.h1' [*.md]```

# SYNOPSIS

**mq** [_options_] [_query_] [_files..._]

**mq** **repl** [_file_]

**mq** **fmt** [_options_] [_file_]

# PARAMETERS

**-A**, **--aggregate**
> 将所有输入文件合并为单个数组进行处理。

**-f** _file_, **--from-file** _file_
> 从文件而非命令行参数加载查询过滤器。

**-I** _format_, **--input-format** _format_
> 设置输入格式：markdown、mdx、html、text、null 或 raw。

**-F** _format_, **--output-format** _format_
> 设置输出格式：markdown、html、text、json 或 none。

**-U**, **--update**
> 用查询结果原地更新输入文件。

**-o** _file_, **--output** _file_
> 将输出写入指定文件。

**-C**, **--color-output**
> 为 Markdown 输出着色。

**-S** _query_, **--separator** _query_
> 处理多个输入时，在文件之间插入的查询。

**-L** _dir_, **--directory** _dir_
> 模块的搜索路径。

**-M** _modules_, **--module-names** _modules_
> 加载指定模块（json、csv、yaml、toml、xml）。

# DESCRIPTION

**mq** 是一个用于处理和查询 Markdown 文件的命令行工具，灵感来自处理 JSON 的 **jq**。它让你可以直接在终端中对结构化的 Markdown 内容进行切片、过滤、映射和转换，内置了选择器（`.h1`-`.h6`、`.code`、`.link`、`.image`、用于递归下降的 `..`）、函数（`select()`、`contains()`、`to_text()`、`to_link()`），并支持自定义扩展。

它适合用来为语言模型准备结构化提示词、自动化文档更新，以及分析跨多个 Markdown 文件的内容。可通过放置在 `~/.mq/bin/` 中的自定义子命令进行扩展。

# CAVEATS

查询遵循 mq 自己的过滤器语法，与 jq 类似。复杂的转换可能需要用管道（`|`）运算符串联多个过滤器。

# HISTORY

**mq** 由 **harehare** 创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install mq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [glow](/man/glow)(1)
