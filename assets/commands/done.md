# TAGLINE

结束循环体的 Shell 保留字

# TLDR

结束 **for** 循环

```for f in *.txt; do echo "$f"; done```

结束 **while** 循环

```while read -r line; do echo "$line"; done < [file.txt]```

结束 **until** 循环

```until ping -c1 [host]; do sleep 1; done```

**重定向整个循环**的输出

```for i in 1 2 3; do echo "$i"; done > [out.txt]```

将整个循环**通过管道传给**另一命令

```for i in 1 2 3; do echo "$i"; done | sort -r```

# SYNOPSIS

**for** _name_ [**in** _words_]; **do** _commands_; **done**

**while** _condition_; **do** _commands_; **done**

**until** _condition_; **do** _commands_; **done**

**select** _name_ [**in** _words_]; **do** _commands_; **done**

# DESCRIPTION

**done** 是 Shell 保留字而非程序：它用来终结由 **do** 开启的 **for**、**while**、**until** 或 **select** 循环体。每个 **do** 必须有一个对应的 **done**，二者共同框住每次迭代要执行的命令。

由于 **done** 终结的是一条复合命令，写在它后面的重定向和管道作用于整个循环，而不是循环内部的最后一条命令。`done > out.txt` 会把每一次迭代的输出发送到同一文件，而且只打开一次，这比在每轮循环中分别重定向更快也更正确。

这个词只在语法上期望出现命令的位置才有特殊含义。在其他场合——比如作为参数——它只是普通字符串，所以 `echo done` 只会把这个词原样打印出来。

循环的退出状态等于循环体内最后一条命令的退出状态；如果循环体从未执行，则为 0。

# CAVEATS

**done** 是保留字，不加引号就无法用作函数名或命令名。只写了 **do** 却缺少匹配 **done** 时，Shell 会一直等待后续输入，表现为脚本挂起或出现续行提示符，而不是清晰的语法错误。

它并非在所有 Shell 中通用：**fish** 和 **csh** 使用 **end** 来结束循环，`done` 属于 Bourne 家族（sh、bash、dash、ksh、zsh）。它与 Taskwarrior 的 `task done` 也毫无关系——那里的 `done` 只是该程序的普通子命令，并不是 Shell 语法。

# HISTORY

`do ... done` 这种配对写法来自 Unix Version 7（**1979 年**）的 **Bourne shell**。Stephen Bourne 借鉴了 ALGOL 68 的风格——复合语句通过反转起始关键字来闭合，Shell 里的 `if ... fi` 和 `case ... esac` 出于同样的直觉。循环一直没有等到反转形式的 `od`，于是被安排了朴实无华的 `done`。POSIX 后来将这套语法标准化，如今它在所有 Bourne 家族 Shell 中行为完全一致。

# INSTALL

```aur: yay -S done```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[for](/man/for)(1), [while](/man/while)(1), [until](/man/until)(1), [break](/man/break)(1), [continue](/man/continue)(1), [bash](/man/bash)(1)
