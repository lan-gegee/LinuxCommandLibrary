# TAGLINE

带单位换算的命令行计算器

# TLDR

**计算表达式**

```qalc "[2 + 2]"```

**单位换算**

```qalc "[5 kilometers to miles]"```

**交互模式**

```qalc```

**货币换算**

```qalc "[100 USD to EUR]"```

**科学计算**

```qalc "[sin(45 degrees)]"```

**以十六进制显示结果**

```qalc -b 16 "[255]"```

**精简输出**（只显示结果，适合脚本使用）

```qalc -t "[2^16]"```

# SYNOPSIS

**qalc** [_options_] [_expression_]

# PARAMETERS

_EXPRESSION_
> 要求值的数学表达式。

**-t**, **--terse**
> 将输出精简为仅结果。

**-f** _FILE_, **--file** _FILE_
> 先执行文件中的命令。

**-e**, **--exrates**
> 更新汇率。

**-b** _BASE_, **--base** _BASE_
> 设置结果的数字进制。

**-c**, **--color**
> 使用颜色高亮表达式和结果。

**-i**, **--interactive**
> 以交互模式启动。

**-l** [_TERM_], **--list** [_TERM_]
> 列出匹配的变量、函数、单位和词头。

**-s** _"OPTION VALUE"_, **--set** _"OPTION VALUE"_
> 设置配置选项（例如 -s "base 16"）。

**-p** [_BASE_], **--prog** [_BASE_]
> 以带进制转换的编程模式启动。

**-n**, **--nodefs**
> 不从文件加载任何函数、单位或变量。

# DESCRIPTION

**qalc** 是 Qalculate 库的命令行界面，提供强大的计算器，支持数学表达式、单位换算、汇率换算和符号计算。它既能处理基本算术，也能应对涉及三角函数、对数、积分和物理常数的复杂表达式。

其突出特性是内置对物理单位和货币的感知，可以直接写 "5 kilometers to miles" 或 "100 USD to EUR" 这样的自然表达式。汇率可自动更新。在交互模式下，qalc 提供带有命令历史和 Tab 补全的持久会话。

# CAVEATS

需要 libqalculate。支持汇率换算。

# HISTORY

Qalculate 作为支持单位的**多用途**计算器而创建。

# INSTALL

```apt: sudo apt install qalc```

```apk: sudo apk add qalc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [calc](/man/calc)(1), [units](/man/units)(1)
