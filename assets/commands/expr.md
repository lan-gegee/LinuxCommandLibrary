# TAGLINE

在 shell 中求算术和字符串表达式的值

# TLDR

**求算术表达式**的值

```expr [5] + [3]```

**相乘**（运算符需转义）

```expr [5] \* [3]```

**字符串长度**

```expr length "[string]"```

**提取子串**（从 1 开始计数）

```expr substr "[string]" [1] [5]```

**模式匹配**

```expr "[string]" : '[regex]'```

**比较数值**（运算符需转义）

```expr [10] \> [5]```

查找首个字符匹配的**位置**

```expr index "[string]" "[chars]"```

# SYNOPSIS

**expr** _expression_

# PARAMETERS

_EXPRESSION_
> 要求值的数学表达式或字符串表达式。

**+**, **-**, **\***, **/**, **%**
> 算术运算符（乘号必须转义）。

**=**, **!=**, **\<**, **\>**, **\<=**, **\>=**
> 比较运算符（< 和 > 需转义）。

**length** _STRING_
> 返回字符串长度。

**substr** _STRING_ _POS_ _LEN_
> 提取子串（从 1 开始计数）。

**index** _STRING_ _CHARS_
> 查找字符首次出现的位置。

**match** _STRING_ _REGEX_
> 模式匹配（等同于 STRING : REGEX）。

**|**
> 逻辑 OR：ARG1 | ARG2 在 ARG1 非空且非零时返回 ARG1，否则返回 ARG2。

**&**
> 逻辑 AND：ARG1 & ARG2 在两者均非空且非零时返回 ARG1，否则返回 0。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**expr** 对表达式求值并输出结果。它支持整数算术、字符串操作和比较。结果打印到标准输出，退出状态码用于表示布尔结果。

运算符必须作为独立参数传递，shell 元字符需转义。在算术中 expr 只处理整数。字符串操作包括求长度、提取子串和正则匹配。

expr 常用于 shell 脚本中的计算和字符串处理，不过现代 shell 已提供内建的替代方案。

# CAVEATS

运算符需要转义（乘法用 \*，比较用 \>）。仅支持整数算术。结果为零/假时返回退出码 1。正则仅支持基本正则表达式。

# HISTORY

expr 起源于 **Version 7 Unix**（1979 年），作为通用的表达式求值器。它仍是 POSIX 和 GNU coreutils 的一部分，但许多功能现在已由 shell 内建命令承担。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [test](/man/test)(1), [bash](/man/bash)(1)
