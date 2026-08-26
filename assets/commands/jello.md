# TAGLINE

使用 Python 表达式过滤 JSON 和 JSON Lines 数据

# TLDR

用 Python **过滤 JSON**

```echo '[1,2,3]' | jello '[x*2 for x in _]'```

**提取字段**

```cat [data.json] | jello '_.name'```

**过滤数组**

```cat [data.json] | jello '[x for x in _ if x["age"] > 30]'```

**获取嵌套值**

```cat [data.json] | jello '_.users[0].email'```

以 grep 可用的格式**打印 JSON schema**

```cat [data.json] | jello -s```

**按行输出**（便于赋值给 bash 数组）

```cat [data.json] | jello -l '_.items'```

从文件**加载输入**而不是 stdin

```jello -f [data.json] '_.name'```

# SYNOPSIS

**jello** [_options_] [_expression_]

# PARAMETERS

_EXPRESSION_
> Python 表达式（输入为 _）。

**-p**, **--pretty**
> 美化输出。

**-l**, **--lines**
> 输出 JSON lines。

**-r**, **--raw**
> 原始字符串输出。

**-c**, **--compact**
> 紧凑的 JSON 输出（不美化）。

**-C**
> 即使通过管道也强制彩色输出。

**-m**, **--mono**
> 单色输出（无颜色）。

**-n**, **--nulls**
> 打印选中的 null 值。

**-s**, **--schema**
> 以 grep 可用的格式打印 JSON schema。

**-t**, **--types**
> 在 schema 视图中打印类型注解。

**-e**
> 数据为空：将 _ 初始化为 None 而不是读取输入。

**-i**
> 将数据初始化为列表以便处理 JSON Lines。

**-f** _FILE_
> 从 JSON 文件加载输入数据。

**-q** _FILE_
> 从文件加载查询。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**jello** 使用 Python 表达式过滤 JSON 和 JSON Lines 数据。输入数据会被反序列化并通过下划线（**_**）变量提供。任何有效的 Python 表达式都可用于转换、过滤或提取数据。

该工具将类似 jq 的过滤能力与 Python 完整的表达式能力相结合，包括列表推导、字典方法、字符串操作和标准库函数。它同时支持 JSON 对象和 JSON Lines（换行分隔的 JSON）输入。

# CAVEATS

需要 Python 3.6 或更高版本。由于 Python 启动开销，处理简单任务时比 jq 慢。下划线（**_**）变量名是约定俗成的，无法更改。默认不支持导入外部模块。

# HISTORY

jello 由 **Kelly Brazil** 创建，作为 jq 的基于 Python 的替代品，供更熟悉 Python 语法的用户使用。

# INSTALL

```dnf: sudo dnf install jello```

```brew: brew install jello```

```nix: nix profile install nixpkgs#jello```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [jc](/man/jc)(1), [python](/man/python)(1), [gron](/man/gron)(1), [fx](/man/fx)(1), [yq](/man/yq)(1)
