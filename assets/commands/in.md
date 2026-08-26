# TAGLINE

Shell 关键字，在 for 和 select 循环中分隔循环变量与列表

# TLDR

**遍历单词列表**

```for fruit in apple banana cherry; do echo "$fruit"; done```

**遍历通配符展开结果**

```for f in *.txt; do echo "$f"; done```

**遍历命令替换结果**

```for user in $(cat users.txt); do echo "$user"; done```

**遍历花括号展开的范围**

```for i in {1..10}; do echo "$i"; done```

**用 select 实现交互式菜单**

```select opt in start stop quit; do echo "$opt"; done```

# SYNOPSIS

**for** _name_ **in** [_words_ ...]**;** **do** _commands_**;** **done**

**select** _name_ **in** [_words_ ...]**;** **do** _commands_**;** **done**

# DESCRIPTION

**in** 是 POSIX shell 语法的保留字，在 **for** 和 **select** 复合命令以及 **case** 语句中用作循环变量与单词列表之间的分隔符。它不是一个独立的程序，无法直接调用；bash、zsh、dash 和 ksh 等 shell 会将其作为外围控制结构的一部分来解析。

在 **for** 循环内部，**in** 之前命名的变量会被依次赋值为 **in** 之后列表产生的每个单词（列表可以是字面单词、通配符展开、命令替换或参数展开）。当单词列表被完全省略时，循环会遍历位置参数 "$@"。

# CAVEATS

**in** 是关键字而不是可执行文件；`which in` 通常不会有任何输出。它自身没有任何标志或选项。其行为取决于外围的 shell 结构以及 POSIX 的引号/展开规则。

# HISTORY

**in** 源自 Bourne shell，自 POSIX shell 规范诞生之初便是其中一员。所有兼容 POSIX 的 shell（包括 bash、ksh、zsh 和 dash）都继承了它，C shell 家族也有类似形式的关键字。

# INSTALL

```aur: yay -S in```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[for](/man/for)(1), [while](/man/while)(1), [do](/man/do)(1), [done](/man/done)(1), [read](/man/read)(1)
