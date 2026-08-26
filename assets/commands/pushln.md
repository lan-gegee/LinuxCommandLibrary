# TAGLINE

将参数压入 shell 缓冲栈

# TLDR

**将字符串压入缓冲栈**

```pushln "[text to push]"```

**压入一条命令以便在执行前编辑**

```pushln "ls -la /tmp"```

**将多个单词作为一个条目压入缓冲栈**

```pushln [word1] [word2] [word3]```

# SYNOPSIS

**pushln** [_arg ..._]

# DESCRIPTION

**pushln** 是一个 zsh 内建命令，它将自己的参数（以空格连接）压入 shell 的**缓冲栈（buffer stack）**。缓冲栈是一种 LIFO（后进先出）数据结构。缓冲栈中的条目会作为下一个交互式命令行的编辑器缓冲区内容呈现出来，也可以通过 **getln** 以编程方式读取。

这等价于 **print -nz**（压入编辑缓冲栈但不带末尾换行符）。缓冲栈提供了一种预填充命令行或在 shell 函数之间传递数据的方式。

# CAVEATS

仅在 zsh 中可用。shell 退出时缓冲栈会被清空。在交互式使用中，被压入的行会以下一个提示符处可编辑输入的形式出现。参数以空格连接（类似 **print -nz**），而不是作为独立的栈条目压入。

# HISTORY

**pushln** 是 **zsh** 缓冲栈机制的一部分，作为 **getln** 的补充而引入，服务于 Z Shell 独特的行缓冲系统。

# SEE ALSO

[getln](/man/getln)(1), [print](/man/print)(1), [zsh](/man/zsh)(1)
