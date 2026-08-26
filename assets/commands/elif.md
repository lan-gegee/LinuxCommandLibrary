# TAGLINE

Shell 脚本中的条件 else-if 构造

# TLDR

**在 bash 脚本中使用 elif**

```if [condition1]; then echo "first"; elif [condition2]; then echo "second"; fi```

**多个 elif** 条件

```if [ $x -lt 0 ]; then echo "negative"; elif [ $x -eq 0 ]; then echo "zero"; elif [ $x -gt 0 ]; then echo "positive"; fi```

**根据命令的退出状态而非测试结果进行分支**

```if command -v nvim; then echo "nvim"; elif command -v vim; then echo "vim"; else echo "none"; fi```

# SYNOPSIS

**if** _condition_; **then** _commands_; **elif** _condition_; **then** _commands_; **fi**

# DESCRIPTION

**elif** 是 bash 及其他 POSIX shell 中用于条件分支的关键字。它是 "else if" 的缩写，允许依次测试多个条件。

elif 位于 if 语句之后。多个 elif 块可以出现在可选的 else 之前。只有第一个匹配条件的代码块会执行。

这一构造是实现多路分支逻辑的 shell 脚本基础。

# CAVEATS

elif 是 shell 保留字而不是程序，因此 `which elif` 找不到任何东西，它也不能在 if 块之外使用。每个 elif 都需要自己的 **then**，而整个链条最后仍以单个 **fi** 结束。在 `[ ... ]` 内部每个记号都必须用空格分隔：`[$x -eq 1]` 是语法错误。条件是一个命令列表，分支依据的是退出状态，任何命令都可以放在那里，而不只是 test。

# HISTORY

elif 是 POSIX shell 语法的一部分，继承自 **Stephen Bourne** 于 20 世纪 70 年代在贝尔实验室创建的 Bourne shell。它提供了比嵌套 if-else 块更简洁的语法。

# SEE ALSO

[if](/man/if)(1), [else](/man/else)(1), [fi](/man/fi)(1), [test](/man/test)(1), [bash](/man/bash)(1)
