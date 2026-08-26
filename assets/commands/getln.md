# TAGLINE

从 zsh 缓冲区栈中读取一行

# TLDR

**从缓冲区栈读取一行到变量**

```getln [variable_name]```

**读取一行并处理**

```getln line && echo $line```

**压入一行再取出**

```print -z "hello world" && getln [variable_name]```

# SYNOPSIS

**getln** _name_ [_name_ ...]

# DESCRIPTION

**getln** 是一个 zsh 内建命令，从 shell 的**缓冲区栈**顶部读取一条记录并赋给指定变量。它等价于 **read -zr**。缓冲区栈是一种 LIFO（后进先出）数据结构，可以用 **print -z** 或 **pushln** 向其中压入文本行，之后再用 **getln** 取出。

如果给出了多个变量名，该行会被拆分成单词并按顺序赋给各个变量，类似于 **read**。整行读取时不做单词拆分（即 **-r** 行为）。

缓冲区栈通常用于程序化的输入操作：脚本预先准备好待执行的命令行，供稍后执行或处理。

# CAVEATS

仅在 **zsh** 中可用。缓冲区栈是 bash 和其他 shell 所没有的 zsh 特有特性。如果缓冲区栈为空，**getln** 会赋予空字符串。缓冲区栈与命令历史是分开的。通过行编辑器的 **push-line** 压入的行也会进入这个栈。

# HISTORY

**getln** 属于 **Z Shell**（zsh）的缓冲区栈机制，早在早期 zsh 版本中就已提供。缓冲区栈是 zsh 独有的特性，用于程序化地排队和取回文本行。

# SEE ALSO

[pushln](/man/pushln)(1), [print](/man/print)(1), [read](/man/read)(1), [zsh](/man/zsh)(1)
