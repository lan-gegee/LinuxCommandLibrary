# TAGLINE

Shell 条件语句中的兜底分支

# TLDR

**在 bash 脚本中使用 else**

```if [condition]; then echo "true"; else echo "false"; fi```

**elif 之后的 else**

```if [ $x -lt 0 ]; then echo "negative"; elif [ $x -eq 0 ]; then echo "zero"; else echo "positive"; fi```

**文件缺失时的兜底处理**

```if [ -f [config.yml] ]; then echo "using config"; else echo "using defaults"; fi```

# SYNOPSIS

**if** _condition_; **then** _commands_; **else** _commands_; **fi**

# DESCRIPTION

**else** 是一个 shell 关键字，为条件语句提供替代分支。当前面的 if（及任何 elif）条件都为假时，它会被执行。

else 出现在 if/elif 块之后、fi 之前。它不能带条件——它捕获所有剩余情况。每个 if 语句只允许一个 else 块。

这是 shell 脚本中处理条件逻辑"否则"情形的基础构造。

# CAVEATS

else 是 shell 保留字而不是程序，因此不能在 if 块之外使用。与 if 和 elif 不同，它不带条件也没有 **then**，且每个 if 语句只能有一个 else，始终作为 **fi** 之前的最后一个分支。`case` 语句没有 else：它的兜底分支是 `*)` 模式。

# HISTORY

else 是 POSIX shell 语法的一部分，源自贝尔实验室 **Stephen Bourne** 创建的 Bourne shell。它在 shell 条件语句中提供了标准的回退机制。

# SEE ALSO

[if](/man/if)(1), [elif](/man/elif)(1), [fi](/man/fi)(1), [test](/man/test)(1), [bash](/man/bash)(1)
