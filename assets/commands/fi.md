# TAGLINE

用于结束条件语句块的 Shell 关键字

# TLDR

**结束**简单的 if 语句

```if [ condition ]; then commands; fi```

**结束** if/else 结构

```if [ condition ]; then commands; else other; fi```

**结束**带 elif 的链式结构

```if [ cond1 ]; then cmd1; elif [ cond2 ]; then cmd2; else cmd3; fi```

**结束**跨多行书写的 if（fi 前无需分号）

```if [ -f [file] ]
then
    cat [file]
fi```

根据任意命令的退出状态**分支**，而不只是 test

```if grep -q [pattern] [file]; then echo found; fi```

# SYNOPSIS

**if** _list_; **then** _list_; [**elif** _list_; **then** _list_;] ... [**else** _list_;] **fi**

# PARAMETERS

**if**
> 开始条件判断；执行其后的命令列表并检查退出状态。

**then**
> 引出在前面的条件成立时要运行的命令。

**elif**
> 当之前的所有条件都失败时，测试另一个条件。

**else**
> 所有条件都不成立时运行的命令。

**fi**
> if 块的结尾（"if" 的反向拼写）。

# DESCRIPTION

**fi** 终止一个 **if** 条件结构。它是保留字而不是命令，Shell 解析器只在命令可以出现的位置识别它，因此它前面必须是换行符或分号。

**if** 结构测试的是退出状态而非真假值：条件本身是一个命令列表，当其退出状态为 **0** 时进入相应分支。**[** 和 **[[** 只不过是退出 **0** 或 **1** 的普通命令，所以任何程序都能充当条件，这正是 **if grep -q ...** 之类的惯用法在 Shell 中如此自然的原因。

一个 **if** 可以包含任意数量的 **elif** 子句和至多一个 **else**。每个 **if** 都需要恰好一个与之匹配的 **fi**，嵌套的情形也不例外；整个块的退出状态等于最后执行的命令的退出状态，如果没有运行任何分支，则为 **0**。

# CAVEATS

由于只有在命令位置才会识别 **fi**，把代码写成 **if [ x = y ]; then echo hi fi** 会悄悄地把 **fi** 作为参数传给 **echo**，而不是关闭语句块，随后 Shell 会报告意外的文件结尾。请务必在它前面加上分号或换行。

空分支是语法错误：Shell 要求 **then** 和 **fi** 之间至少有一条命令。可以用 **:**（空命令）作为占位。

缺少 **fi** 时，报错位置通常在文件末尾而不是真正的出错之处，因此错误信息给出的行号很少就是问题所在的那一行。

# HISTORY

**fi** 源自 **Bourne shell**（**1977 年**），并被 POSIX 标准化。Stephen Bourne 从 **ALGOL 68** 借用了反向关键字的惯例，后者同样成对使用 **if**/**fi**；Shell 又在 **case**/**esac** 上沿用了这一做法。**do**/**done** 则打破了这个模式，因为 **od** 已经被八进制转储工具占用了。

# SEE ALSO

[if](/man/if)(1), [else](/man/else)(1), [elif](/man/elif)(1), [test](/man/test)(1), [true](/man/true)(1), [while](/man/while)(1), [until](/man/until)(1), [bash](/man/bash)(1)

# RESOURCES

```[Documentation](https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs)```

<!-- verified: 2026-07-16 -->

# INSTALL

```aur: yay -S fi```

<!-- packages: 2026-07-22 -->
