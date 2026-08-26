# TAGLINE

命令行 JSON 处理器

# TLDR

**格式化输出 JSON**

```cat [data.json] | jq '.'```

**提取字段**

```cat [data.json] | jq '.name'```

**数组索引**

```cat [data.json] | jq '.[0]'```

**过滤数组**

```cat [data.json] | jq '.[] | select(.age > 30)'```

**映射变换**

```cat [data.json] | jq '[.[] | {name, age}]'```

**原始字符串输出**

```cat [data.json] | jq -r '.name'```

**紧凑输出**

```cat [data.json] | jq -c '.'```

# SYNOPSIS

**jq** [_options_] _filter_ [_file_...]

# PARAMETERS

_FILTER_
> jq 过滤表达式。

_FILE_
> 输入 JSON 文件。

**-r**, **--raw-output**
> 输出原始字符串。

**-c**, **--compact-output**
> 紧凑输出。

**-s**, **--slurp**
> 将整个输入读入为一个数组。

**-n**, **--null-input**
> 不使用输入。

**--arg** _NAME_ _VAL_
> 设置变量。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jq** 是一款轻量级的命令行 JSON 处理器，常被称为 "JSON 界的 sed"。它从文件或标准输入读取 JSON 数据，应用过滤器表达式，并将变换后的结果写入标准输出。过滤器可以用管道操作符（`|`）串联起来，在单次调用中完成提取字段、重构对象、计算数值和聚合数组等多步变换。

其过滤器语言支持对象和数组索引（`.foo`、`.[0]`）、迭代（`.[]`）、条件语句（`if-then-else`）、比较与逻辑运算符，以及 `map`、`select`、`group_by`、`sort_by` 等内建函数，还有字符串插值和正则表达式。因此 jq 非常适合诸如从 API 响应中提取嵌套值、把 JSON 记录转换为 CSV、或为下游工具重塑数据等任务。输出可以是格式化形式（默认），用 `-c` 压缩以便管道传输，或用 `-r` 输出原始字符串以集成到 shell 中。

# CAVEATS

复杂查询有学习门槛。处理大文件时可使用流式模式。null 的处理可能比较棘手。

# HISTORY

jq 由 **Stephen Dolan** 开发，定位为 JSON 领域的 sed/awk 替代品，如今已成为标准的 CLI JSON 工具。

# INSTALL

```apt: sudo apt install jq```

```dnf: sudo dnf install jq```

```pacman: sudo pacman -S jq```

```apk: sudo apk add jq```

```zypper: sudo zypper install jq```

```brew: brew install jq```

```nix: nix profile install nixpkgs#jq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jo](/man/jo)(1), [jc](/man/jc)(1), [yq](/man/yq)(1), [gron](/man/gron)(1)
