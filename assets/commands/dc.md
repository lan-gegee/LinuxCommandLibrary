# TAGLINE

任意精度逆波兰表示法计算器

# TLDR

**启动交互式**计算器

```dc```

**直接求值表达式**

```echo "[5 3 + p]" | dc```

**两数相乘**

```echo "[4 7 * p]" | dc```

**以小数精度计算**

```echo "[10 k 22 7 / p]" | dc```

**从文件执行**

```dc [script.dc]```

**存储和读取**数值

```echo "[5 sa la 3 + p]" | dc```

**计算 5 的阶乘**

```echo "[5 [d 1 - d 1 <f *] d sf x p]" | dc```

# SYNOPSIS

**dc** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 包含待执行 dc 命令的文件。

**-e** _EXPR_, **--expression** _EXPR_
> 从命令行求值表达式。

**-f** _FILE_, **--file** _FILE_
> 从文件读取命令。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**dc** 是一个使用逆波兰表示法（RPN）的任意精度桌面计算器。数字和运算符按顺序输入，运算符作用于栈中的值。它支持算术运算、比较以及可编程宏。

基本操作是将数字压入栈中再应用运算符：5 3 + 先压入 5 和 3，然后相加。p 命令打印栈顶值。k 命令设置除法等运算的小数精度。

dc 提供寄存器（a-z）用于存储数值，支持条件执行、通过宏实现循环以及字符串操作。尽管语法简洁晦涩，它仍能实现包括递归在内的复杂算法。

# CAVEATS

对于习惯中缀表示法的用户来说，RPN 语法可能不够直观。错误信息很少。复杂程序难以阅读和调试。部分扩展特性在不同实现之间存在差异。

# HISTORY

dc 是最古老的 Unix 实用程序之一，由贝尔实验室的 **Lorinda Cherry** 和 **Robert Morris** 于约 **1969-1971 年**编写。它的诞生早于 C 语言，最初用 B 语言实现。bc 计算器后来作为 dc 的预处理器被编写出来。

# INSTALL

```apt: sudo apt install dc```

```dnf: sudo dnf install bc```

```pacman: sudo pacman -S bc```

```apk: sudo apk add bc```

```zypper: sudo zypper install bc```

```brew: brew install bc```

```nix: nix profile install nixpkgs#bc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [calc](/man/calc)(1), [expr](/man/expr)(1)
