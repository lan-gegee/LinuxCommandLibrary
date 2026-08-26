# TAGLINE

快速命令行计算器

# TLDR

**快速计算**

```qc "[expression]"```

**交互模式**

```qc```

**以精度计算**

```qc "[1/3]"```

# SYNOPSIS

**qc** [_expression_]

# PARAMETERS

_EXPRESSION_
> 数学表达式。

# DESCRIPTION

**qc** 是一个轻量级命令行计算器，用于在终端中快速求值数学表达式。它接受算术表达式作为参数并输出结果，也可交互式地连续进行多次计算。

该工具支持标准运算，包括加、减、乘、除以及用于分组的括号。当只需要简单算术时，它是启动 **bc** 或 **qalc** 等完整计算器的更快替代。

# CAVEATS

功能基础的计算器。存在多种实现。

# HISTORY

qc 用于从命令行进行**快速计算**。

# INSTALL

```nix: nix profile install nixpkgs#qc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [qalc](/man/qalc)(1), [calc](/man/calc)(1)
