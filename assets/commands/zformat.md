# TAGLINE

Zsh 字符串格式化与对齐内建命令

# TLDR

**格式化字符串**，使用命名说明符

```zformat -f REPLY "Name: %n, Age: %a" n:Alice a:30```

**格式化时指定字段宽度**、填充与截断

```zformat -f REPLY "%-20n %5a" n:Alice a:30```

**使用三元表达式**条件输出文本

```zformat -f REPLY "Status: %(s.active.inactive)" s:1```

**对齐字符串**成列，使用分隔符

```zformat -a result " = " "key1:value1" "key2:value2" "longkey:value3"```

**基于存在性的三元表达式**格式化（非空测试）

```zformat -F REPLY "%(n.Name: %n.anonymous)" n:Alice```

# SYNOPSIS

**zformat** **-f** _param_ _format_ _spec_ ...
**zformat** **-F** _param_ _format_ _spec_ ...
**zformat** **-a** _array_ _sep_ _spec_ ...

# PARAMETERS

**-f** _param_ _format_ _spec_ ...
> 格式化字符串。每个 _spec_ 为 **char:string**。_format_ 中的每个 **%char** 都会被替换为对应的 _string_。结果存储在 _param_ 中。支持字段宽度和带数值比较的三元表达式。

**-F** _param_ _format_ _spec_ ...
> 类似 **-f**，但三元表达式依据格式说明符是否**存在且非空**来在真/假文本之间选择，而不是数值比较。

**-a** _array_ _sep_ _spec_ ...
> 对齐字符串。每个 _spec_ 为 **left:right**。冒号会被替换为 _sep_，左侧字符串用空格填充，使所有分隔符垂直对齐。结果存储在 _array_ 中。

# DESCRIPTION

**zformat** 是由 **zsh/zutil** 模块提供的内建命令。它执行字符串格式化和对齐操作，常用于 zsh 补全系统内部以及自定义脚本。

**-f** 形式将格式字符串中的 **%char** 序列替换为命名说明符给出的值。每个说明符是一个字符，后跟冒号和值字符串。可选的最小和最大字段宽度可以指定为 **%min.maxc**，其中负的最小宽度表示向左填充。三元表达式形如 **%(X.true_text.false_text)**，会将说明符的值与测试数字（默认 0）进行数值比较。

**-F** 形式的工作方式相同，只是三元表达式测试说明符的值是否存在且非空，而不是进行数值比较。

**-a** 形式对齐一组 **left:right** 字符串对，用空格填充左侧部分，使分隔符字符串在垂直显示时全部对齐。这对格式化选项列表和帮助文本很有用。

使用前必须先用 **zmodload zsh/zutil** 加载模块。

# FIELD WIDTH

格式说明符支持 **%min.maxc** 记法：

**%20n** 用空格向右填充至最小宽度 20
**%-20n** 用空格向左填充至最小宽度 20
**%.10n** 在 10 个字符后截断
**%20.30n** 填充至 20，在 30 处截断
**%12.12i** 恰好显示 12 个字符（适合截断哈希值）

# TERNARY EXPRESSIONS

使用 **-f** 时，三元表达式采用数值比较：

**%(X.true.false)** 当 X 等于 0（默认测试数字）时输出 true
**%3(X.true.false)** 当 X 等于 3 时输出 true
**%-1(X.true.false)** 当 X 等于 -1 时输出 true

使用 **-F** 时，三元表达式测试存在性：

**%(X.true.false)** 当 X 存在且非空时输出 true
**-F** 中的测试数字表示该值的最小宽度

三元表达式可以嵌套，且说明符之后的定界符可以是任意字符（不限于点号）。

# CAVEATS

**zformat** 需要先通过 **zmodload zsh/zutil** 加载 **zsh/zutil** 模块。它是 zsh 特有的，在其他 Shell 中不可用。单字符说明符的限制意味着每个格式字符串只有 62 个可用的格式变量（a-z、A-Z、0-9）。三元表达式的定界符不得与说明符的值冲突。

# HISTORY

**zformat** 作为 **zsh/zutil** 模块的一部分随 **zsh 4.0**（2001 年）引入。它的设计主要是为了满足 zsh 补全系统的格式化需求，特别是基于 **zstyle** 的配置和 **vcs_info** 版本控制状态显示。用于存在性三元测试的 **-F** 选项是后来加入的，用以补充 **-f** 的数值比较。

# SEE ALSO

[zsh](/man/zsh)(1), [zstyle](/man/zstyle)(1)
