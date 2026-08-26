# TAGLINE

Zsh 增强版文本输出内建命令

# TLDR

**打印文本**

```print "Hello"```

**打印到 stderr**

```print -u2 "Error"```

**打印数组元素**

```print -l ${array[@]}```

**按格式打印**

```print -f "%s: %d\n" "Count" [5]```

**展开目录栈提示符**

```print -P "%~"```

# SYNOPSIS

**print** [_options_] [_args_]

# PARAMETERS

**-n**
> 不输出换行符。

**-r**
> 原始模式。

**-l**
> 每个参数占一行。

**-u** _N_
> 文件描述符。

**-f** _FORMAT_
> printf 风格的格式。

**-P**
> 执行提示符展开。

# DESCRIPTION

zsh 中的 **print** 是一个增强的文本输出内建命令，在 ksh 版本的基础上扩展了更多功能。它通过 **-f** 支持 printf 风格的格式化，通过 **-P** 支持提示符展开（用于显示 %~ 之类的提示符转义序列以表示当前目录），并可用 **-l** 将数组元素每行一个地打印。

与 echo 相比，该命令提供了更可靠的文本输出行为——echo 对反斜杠转义和类选项参数的处理因 shell 而异。输出可以通过 **-u** 定向到特定文件描述符，用于写入 stderr 或其他已打开的描述符。

# CAVEATS

Zsh 专用。与 ksh 的 print 不同。

# HISTORY

print 是功能扩展的 **zsh 内建命令**。

# SEE ALSO

[echo](/man/echo)(1), [printf](/man/printf)(1), [print](/man/print)(1)
