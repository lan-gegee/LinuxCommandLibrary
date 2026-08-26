# TAGLINE

读取一行输入并存入 shell 变量

# TLDR

**读入一行**并存入变量

```read [variable]```

**带自定义提示符读取**

```read -p "Enter your name: " [name]```

**静默读取**（用于密码）

```read -s -p "Password: " [password]```

**限时读取**（5 秒）

```read -t 5 [variable]```

**读取单个字符**而不等待回车

```read -n 1 [char]```

**读入数组**（单词按 IFS 分割）

```read -a [array]```

**从文件逐行读取**

```while read line; do echo "$line"; done < [file]```

# SYNOPSIS

**read** [**-p** _prompt_] [**-t** _timeout_] [**-n** _nchars_] [**-s**] [**-a** _array_] [**-d** _delim_] [_name_...]

# PARAMETERS

**-p** _prompt_
> 读取前显示提示字符串（bash）

**-s**
> 安静模式；不回显输入（用于密码）

**-t** _timeout_
> 在指定秒数后超时；无输入则失败

**-n** _nchars_
> 读满指定字符数后返回

**-N** _nchars_
> 精确读取 N 个字符，忽略分隔符

**-a** _array_
> 将单词读入数组变量

**-d** _delim_
> 使用指定分隔符而不是换行符

**-r**
> 不把反斜杠当作转义字符（原始模式）

**-u** _fd_
> 从文件描述符而不是 stdin 读取

**-e**
> 使用 readline 处理输入（启用行编辑）

# DESCRIPTION

**read** 是一个 shell 内建命令，从标准输入（或文件描述符）读取一行并将其拆分为单词，赋值给各变量。它是交互式 shell 脚本和文本文件处理的基础。

不给变量名时，输入存储在 **REPLY** 变量中。给定多个变量时，单词按顺序赋值，剩余的单词全部归入最后一个变量。单词按 **IFS**（内部字段分隔符）变量的定义进行拆分。

大多数情况下建议使用 **-r** 选项，因为它能阻止对反斜杠的解释——否则处理文件路径或特殊字符时可能出现意外行为。

在 **while read** 循环中，read 在遇到文件末尾时返回假（退出码 1），因此非常适合逐行处理文件。

# CAVEATS

**read** 是 shell 内建命令，不同 shell（bash、zsh、dash）的选项有所差异。诸如 **-p**、**-a**、**-t** 之类的选项是 bash 扩展，POSIX sh 中不可用。

不加 **-r** 时，反斜杠会被解释为转义字符。除非确实需要转义处理，请始终使用 **read -r**。

根据 IFS 的设置，首尾空白会被去除。要保留空白，请在 read 前设置 **IFS=**：`IFS= read -r line`

**-t** 超时选项不一定在所有 shell 或所有输入源上都有效（仅适用于终端/管道，普通文件不行）。

# SEE ALSO

[echo](/man/echo)(1), [printf](/man/printf)(1), [bash](/man/bash)(1), [sh](/man/sh)(1)
