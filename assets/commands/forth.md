# TAGLINE

基于栈的交互式编程语言

# TLDR

**启动 Forth 解释器（Gforth）**

```gforth```

**运行 Forth 脚本**

```gforth [script.fs]```

**求值表达式**

```gforth -e "[1 2 + .] [bye]"```

**加载文件后进入交互模式**

```gforth [script.fs] -```

# SYNOPSIS

**gforth** [_options_] [_file_...]

# PARAMETERS

**-e** _code_
> 求值 Forth 代码。

**-m** _size_
> 字典大小。

**-d** _size_
> 数据栈大小。

**-r** _size_
> 返回栈大小。

_file_
> 要加载的 Forth 源文件。

**-**
> 从 stdin 读取。

# DESCRIPTION

**Forth** 是一种基于栈的编程语言，以简洁和可扩展性著称。Gforth 是 GNU 的 Forth 实现，符合 ANS Forth 标准。

Forth 使用显式栈上的逆波兰表示法（RPN）。单词（函数）用 `:` 和 `;` 定义。这门语言高度交互且可扩展，常用于嵌入式系统。

# BASIC OPERATIONS

```forth
\ Push numbers, add, print
2 3 + .   \ prints 5

\ Define a word
: square ( n -- n^2 ) dup * ;
5 square .   \ prints 25

\ Stack manipulation
1 2 3 swap   \ 1 3 2
dup          \ duplicates top
drop         \ removes top
```

# CAVEATS

基于栈的范式与大多数语言不同。需要手动内存管理。与现代语言相比标准库有限。调试可能比较困难。

# HISTORY

Forth 由 **Charles H. Moore** 在 **1960** 年代末为控制射电望远镜而发明。凭借极小的体积和高效率，它在嵌入式系统中广受欢迎。Gforth 于 **1992** 年由 Anton Ertl 和 Bernd Paysan 启动开发。

# SEE ALSO

[dc](/man/dc)(1)
