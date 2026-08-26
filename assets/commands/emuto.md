# TAGLINE

带查询语言的数据转换工具

# TLDR

**转换 JSON 数据**

```emuto '[.data.items | map(.name)]' [input.json]```

**从标准输入转换**

```cat [data.json] | emuto '[.items]'```

**输出格式化结果**

```emuto --pretty '[.]' [input.json]```

# SYNOPSIS

**emuto** [_options_] _expression_ [_file_]

# PARAMETERS

_EXPRESSION_
> Emuto 转换表达式。

_FILE_
> 输入的 JSON 文件。

**--pretty**
> 以美化格式打印输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**emuto** 是一个使用类 jq 查询语言的数据转换工具。它通过表达式处理 JSON、CSV、TSV、DSV 和纯文本，对数据结构进行选择、过滤和变换。

其表达式语言支持对象访问、数组操作、映射和过滤，以函数式的方式操作 JSON。

emuto 适用于脚本和管道中的数据提取、格式转换和 JSON 处理。

# CAVEATS

表达式语法与 jq 不同。可能无法覆盖所有 JSON 边界情况。性能随数据量而变化。

# HISTORY

emuto 是作为 JSON 转换工具开发的，凭借自己的表达式语法提供类似 jq 的数据处理功能。

# INSTALL

```aur: yay -S emuto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [gron](/man/gron)(1), [fx](/man/fx)(1)
