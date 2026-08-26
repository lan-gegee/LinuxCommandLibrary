# TAGLINE

自由的开源计算机代数系统

# TLDR

**启动计算器**

```yacas```

**求值表达式**

```yacas -c "[Solve(x^2-4==0,x)]"```

**运行脚本**

```yacas [script.ys]```

**安静模式**

```yacas -p```

# SYNOPSIS

**yacas** [_-c expr_] [_-p_] [_options_] [_file_]

# PARAMETERS

**-c** _EXPR_
> 求值表达式。

**-p**
> 纯文本输出。

**-d** _DIR_
> 脚本目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**yacas**（Yet Another Computer Algebra System）是一个自由的符号数学程序，提供代数计算的交互式环境。它支持表达式的符号操作、方程求解、包括导数和积分在内的微积分运算以及线性代数。

该系统包含自己的脚本语言，可用于定义自定义函数和数学过程。它既可以在命令行中交互式使用，也可以通过运行脚本文件使用，同时支持精确符号计算和数值计算。

# CAVEATS

有学习曲线。拥有自己的语法。不如 Mathematica 功能全面。

# HISTORY

**Yacas**（Yet Another Computer Algebra System）作为一个自由的计算机代数系统而创建。

# INSTALL

```apt: sudo apt install yacas```

```brew: brew install yacas```

```nix: nix profile install nixpkgs#yacas```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[maxima](/man/maxima)(1), [octave](/man/octave)(1), [bc](/man/bc)(1)
