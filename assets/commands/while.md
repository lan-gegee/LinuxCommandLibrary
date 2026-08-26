# TAGLINE

条件执行的 Shell 循环

# TLDR

**基本 while 循环**

```while [condition]; do [command]; done```

**无限循环**

```while true; do [command]; sleep [1]; done```

**逐行读取文件**

```while read -r line; do echo "$line"; done < [file.txt]```

**循环直到命令失败**

```while [command]; do echo "still running"; done```

**计数器循环**

```i=0; while [ $i -lt 10 ]; do echo $i; i=$((i+1)); done```

**处理命令输出**

```[command] | while read -r line; do echo "$line"; done```

**带 break 的循环**

```while true; do if [condition]; then break; fi; done```

# SYNOPSIS

**while** _CONDITION_; **do** _COMMANDS_; **done**

# DESCRIPTION

**while** 是一种 shell 控制结构，只要条件命令返回零（成功）退出状态，就反复执行一段命令。当条件返回非零值时循环终止。

条件通常是一个 **test** 命令（或其等价形式 **[**），但可以使用任何命令。只要该命令执行成功，循环就会继续。

常见模式包括用 **read** 逐行读取文件、实现重试逻辑，以及创建无限运行的守护进程式进程。

# PARAMETERS

**break**
> 立即退出循环。

**break** _N_
> 退出 N 层嵌套循环。

**continue**
> 跳过剩余命令并开始下一次迭代。

**continue** _N_
> 从第 N 层外层循环继续。

# CAVEATS

通过管道连接到 while 会创建子 shell，因此循环内部对变量的修改在外部不可见。可使用进程替换或 here-string 来避免：**while read line; do ...; done < <(command)**。始终使用 **read -r** 以防止反斜杠被解释。

# HISTORY

自 Unix Version 7（1979 年）的原始 Bourne shell 起，while 循环就是 shell 的基础控制结构。其语法由 POSIX 规定，在所有符合 POSIX 的 shell（包括 bash、dash、ksh 和 zsh）中行为完全一致。

# SEE ALSO

[for](/man/for)(1), [until](/man/until)(1), [test](/man/test)(1), [bash](/man/bash)(1)
