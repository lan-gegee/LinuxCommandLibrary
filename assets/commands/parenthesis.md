# TAGLINE

Shell 中的圆括号：子 shell、数组与算术运算

# TLDR

**在子 shell 中运行命令**

```(cd [/tmp] && [command])```

**创建数组**

```array=([one] [two] [three])```

**不用子 shell 进行命令分组**

```{ [command1]; [command2]; }```

**函数定义**

```function_name() { [commands]; }```

**算术求值**

```(( count++ ))```

# SYNOPSIS

**(** _commands_ **)**

**((**_arithmetic_**))**

# DESCRIPTION

圆括号 **( )** 在 Shell 中根据上下文有多种不同用途：

**子 shell 执行**：**(...)** 中的命令在一个子 shell 中运行。环境变更（cd、变量赋值）不会影响父 shell。

**数组字面量**：在 bash/zsh 中，**array=(a b c)** 创建一个数组。

**函数定义**：**name() { ... }** 定义一个函数（圆括号是语法的一部分，并非分组）。

**命令替换**：**$(...)** 捕获命令的输出。

**算术运算**：**((...))** 执行算术求值，**$((...))** 展开为结果。

# SUBSHELL BEHAVIOR

```bash
# Changes don't affect parent
(cd /tmp; pwd)  # prints /tmp
pwd             # still original directory

# Variables don't leak
(x=5)
echo $x         # empty or original value
```

# ARITHMETIC (( ))

```bash
(( x = 5 + 3 ))    # Assignment
(( x++ ))          # Increment
(( x > 5 )) && echo "big"  # Condition
result=$(( a * b ))         # Capture result
```

# CAVEATS

子 shell 有进程创建带来的开销。若只是想分组而不需要隔离，请改用花括号 **{ ...; }**。

**{ }** 分组要求 **{** 之后有空格、**}** 之前有分号；圆括号则无此要求。

父 shell 能看到子 shell 的退出状态，但看不到它的变量变更。

嵌套的圆括号可能需要小心加引号，以避免语法问题。

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [test](/man/test)(1)
