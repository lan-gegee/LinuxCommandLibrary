# TAGLINE

支持任意精度的计算器 REPL

# TLDR

**计算表达式**

```eva "[2 + 3 * 4]"```

**使用函数计算**

```eva "[sin(pi/2)]"```

三角函数**使用弧度模式**

```eva --radian "[sin(pi/2)]"```

**交互式 REPL 模式**

```eva```

**设置小数精度**（固定小数位数，1-64）

```eva --fix [20] "[pi]"```

**更改输出的进制**（1-36）

```eva --base [16] "[255]"```

# SYNOPSIS

**eva** [_options_] [_expression_]

# PARAMETERS

_INPUT_
> 要求值的数学表达式字符串（非交互模式）。

**-f**, **--fix** _N_
> 输出的小数位数（1-64，默认 10）。

**-b**, **--base** _N_
> 计算结果的进制（1-36，默认 10）。

**-r**, **--radian**
> 三角函数使用弧度。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**eva** 是一个用 Rust 编写的计算器 REPL 和命令行工具，用于求值数学表达式。它支持标准算术运算、三角函数、对数以及 **pi** 和 **e** 等常量。

在交互式 REPL 模式下，之前的结果可以通过 **_** 引用，并且可以调出历史记录。直接在命令行传入表达式即可进行一次性求值。

eva 提供了一个快捷的命令行计算器，语法比 **bc** 更直观。

# CAVEATS

复杂的表达式可能需要加引号，以免被 shell 解释。变量在一次性命令模式下不会保留；多步计算请使用交互式 REPL。

# HISTORY

eva 作为一个现代命令行计算器而创建，凭借更直观的语法和更多功能，成为 bc 及类似工具的替代品。

# INSTALL

```pacman: sudo pacman -S eva```

```brew: brew install eva```

```nix: nix profile install nixpkgs#eva```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [calc](/man/calc)(1), [qalc](/man/qalc)(1)
