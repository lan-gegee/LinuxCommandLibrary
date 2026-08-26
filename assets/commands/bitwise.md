# TAGLINE

支持位操作的交互式多进制计算器

# TLDR

**交互式**模式

```bitwise```

转换**十进制**数

```bitwise 12345```

转换**十六进制**数

```bitwise 0x563d```

**计算**表达式

```bitwise "0x123 + 0x20 - 30"```

# SYNOPSIS

**bitwise** [_OPTIONS_] [_value_|_expression_]

# DESCRIPTION

**bitwise** 是一个多进制交互式计算器，支持动态进制转换和位操作。它同时以十进制、十六进制、八进制和二进制显示数值。

# PARAMETERS

**-i, --interactive**
> 强制进入交互模式（未给定数值或表达式时的默认行为）

**-w, --width** _b8|b16|b32|b64_
> 设置计算的位宽

**--no-color**
> 禁用彩色输出

**-v, --version**
> 显示版本信息

**-h, --help**
> 显示帮助信息

数值可以用不同进制指定：
> 十进制：普通数字（123）
> 十六进制：0x 前缀（0x7B）
> 八进制：0 前缀（0173）
> 二进制：0b 前缀（0b1111011）

支持 C 语言风格的算术和位运算符（NOT、OR、AND、XOR 以及移位）。在命令行模式下，结果会同时以所有进制打印。

# CAVEATS

交互模式提供可视化的位翻转界面。含特殊 shell 字符的表达式需要加引号。适合底层编程和调试使用。

# HISTORY

**bitwise** 是由 **Ramon Fried**（mellowcandle）编写的基于 ncurses 的开源（GPL-3.0）计算器。它面向经常需要在不同进制间切换的底层开发者，如内核和设备驱动程序员。

# INSTALL

```apt: sudo apt install bitwise```

```dnf: sudo dnf install bitwise```

```apk: sudo apk add bitwise```

```zypper: sudo zypper install bitwise```

```brew: brew install bitwise```

```nix: nix profile install nixpkgs#bitwise```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [calc](/man/calc)(1)

# RESOURCES

```[Source code](https://github.com/mellowcandle/bitwise)```

<!-- verified: 2026-06-19 -->
