# TAGLINE

任意精度计算器语言

# TLDR

**计算**表达式

```echo ["2+2"] | bc```

带小数的**除法**

```echo ["scale=2; 10/3"] | bc```

**运行** bc 脚本

```bc [script.bc]```

**数学库**

```bc -l```

直接**求值表达式**

```bc -e "[scale=2; 100/3]"```

**交互式**计算器

```bc```

# SYNOPSIS

**bc** [_options_] [_file_...]

# DESCRIPTION

**bc** 是一种任意精度计算器语言。它支持交互式计算、脚本编写和数学运算，小数计算精度可由用户定义。

该工具几十年来一直是 Unix 标准的一部分，广泛用于 Shell 脚本中的算术运算。

# PARAMETERS

**-l**, **--mathlib**
> 加载数学库（包含 s、c、a、l、e 等函数，并将 scale 设为 20）

**-s**, **--standard**
> POSIX 标准模式；遇到任何非 POSIX 扩展即报错

**-q**, **--quiet**
> 不打印 GNU bc 常规的欢迎横幅

**-i**, **--interactive**
> 强制交互模式

**-w**, **--warn**
> 对不符合 POSIX 的用法发出警告

**-e** _expression_, **--expression** _expression_
> 求值表达式；多个 -e 选项按顺序处理

**-v**, **--version**
> 打印版本号并退出

# SPECIAL VARIABLES

**scale**
> 小数位数（默认：0）

**ibase**
> 输入进制（默认：10）

**obase**
> 输出进制（默认：10）

# OPERATORS

- **+, -, *, /** - 基本算术
- **%** - 取模
- **^** - 幂运算
- **++, --** - 自增/自减
- **==, !=, <, >** - 比较

# FUNCTIONS

使用 -l 时可用（同时将 scale 设为 20）：
- **s(x)** - 正弦（x 为弧度）
- **c(x)** - 余弦（x 为弧度）
- **a(x)** - 反正切（返回弧度）
- **l(x)** - 自然对数
- **e(x)** - 指数（e 的 x 次方）
- **sqrt(x)** - 平方根（无需 -l 即可使用）

# WORKFLOW

```bash
# Simple math
echo "2+2" | bc

# Floating point
echo "scale=4; 22/7" | bc

# Hex to decimal
echo "ibase=16; FF" | bc

# Square root
echo "sqrt(2)" | bc -l

# Multiple operations
bc <<< "
scale=2
x = 5
y = 3
x / y
"
```

# CAVEATS

对程序员来说语法较为特别。默认为整数除法（需设置 scale）。交互模式下变量会保留。字符串处理能力有限。现代脚本可考虑改用 awk 或编程语言。

# HISTORY

**bc** 由 Robert Morris 和 Lorinda Cherry 于 **1975** 年在贝尔实验室为 Unix 开发，基于更早的 **dc** 计算器。如今使用最广泛的 GNU 版本由 Philip A. Nelson 编写。

# INSTALL

```apt: sudo apt install bc```

```dnf: sudo dnf install bc```

```pacman: sudo pacman -S bc```

```apk: sudo apk add bc```

```zypper: sudo zypper install bc```

```brew: brew install bc```

```nix: nix profile install nixpkgs#bc```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[dc](/man/dc)(1), [calc](/man/calc)(1), [awk](/man/awk)(1)
