# TAGLINE

MATE 桌面环境的图形化计算器

# TLDR

**启动**计算器

```mate-calc```

计算**指定表达式**

```mate-calc -s "[2 + 5]"```

# SYNOPSIS

**mate-calc** [_options_] [_-s expression_]

# PARAMETERS

**-s**, **--solve** _expression_
> 计算给定的表达式并显示结果。

**--version**
> 显示版本信息

**--help**
> 显示帮助信息

# DESCRIPTION

**mate-calc** 是 MATE 桌面环境的图形化计算器。它提供基本、高级、财务和程序员计算器模式，支持任意精度算术。

功能包括三角函数、对数、阶乘、单位换算和位运算。该计算器支持多种进制（二进制、八进制、十进制、十六进制），并可处理复数。

使用 **--solve** 可以直接在命令行中求表达式的值而无需打开图形界面，适用于脚本和快速计算。

# INSTALL

```apt: sudo apt install mate-calc```

```dnf: sudo dnf install mate-calc```

```pacman: sudo pacman -S mate-calc```

```apk: sudo apk add mate-calc```

```zypper: sudo zypper install mate-calc```

```nix: nix profile install nixpkgs#mate-calc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mate-calc-cmd](/man/mate-calc-cmd)(1), [bc](/man/bc)(1), [gnome-calculator](/man/gnome-calculator)(1)
