# TAGLINE

使用 JSONPath 表达式查询 JSON 数据

# TLDR

使用 JSONPath **查询** JSON 文件

```ajson '$.store.book[*].author' [file.json]```

从 **stdin** 查询

```echo '{"name":"John"}' | ajson '$.name'```

按**条件**过滤

```ajson '$.store.book[?(@.price < 10)]' [file.json]```

读取**多行** JSON（每行一个 JSON 对象）

```ajson -m '$.name' [file.jsonl]```

对 JSON 数据**求值**表达式

```ajson 'avg($..price)' [file.json]```

# SYNOPSIS

**ajson** [**-mq**] _jsonpath_ [_file_]

# DESCRIPTION

**ajson** 是一个用 Go 编写的命令行工具，用于通过 JSONPath 表达式查询和求值 JSON 数据。它从文件或标准输入读取 JSON，支持过滤器、通配符、递归下降，以及 **avg**、**sum**、**length**、**first**、**last** 等求值函数和数学函数。

JSONPath 语法类似于面向 XML 的 XPath：**$** 表示根对象，**.** 表示属性访问，**[]** 用于数组索引或过滤，**..** 表示递归下降。

# PARAMETERS

**jsonpath**
> 要求值的 JSONPath 表达式或求值字符串。

**file**
> JSON 文件路径（省略时读取标准输入）。

**-m**, **--multiline**
> 将输入作为多行 JSON 读取，其中每一行都是一个独立的合法 JSON 对象。

**-q**, **--quiet**
> 不向 stderr 打印错误。

# CAVEATS

不同 JSONPath 实现支持的特性可能不同。复杂嵌套查询在大文件上可能较慢。非法的 JSONPath 表达式会产生错误而不是空结果。

# HISTORY

**ajson** 实现 Stefan Goessner 于 **2007** 年提出的 JSONPath 查询语言，为这种流行的 JSON 查询方法提供命令行入口。

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [fx](/man/fx)(1), [gron](/man/gron)(1)
