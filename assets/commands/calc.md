# TAGLINE

任意精度计算器

# TLDR

**计算**表达式

```calc ["2 + 2"]```

**交互式**模式

```calc```

**定义**变量

```calc ["x = 5; y = 3; x * y"]```

**使用**函数

```calc ["sqrt(16)"]```

# SYNOPSIS

**calc** [_options_] [_expression_]

# DESCRIPTION

**calc** 是一个任意精度计算器。它提供交互式计算和脚本功能，支持复数运算、三角函数、统计以及用户自定义函数。

该工具比 bc 功能更丰富，同时保持了易用性。

# PARAMETERS

**-c**
> 出错后继续执行

**-d**
> 禁用 readline 编辑

**-p**
> 管道模式（无提示符）

**-q**
> 安静模式（不显示启动消息）

**-s**
> 强制严格模式

# FEATURES

- 任意精度算术
- 复数
- 三角函数
- 统计函数
- 用户自定义函数
- 变量赋值
- 矩阵运算
- 分数与有理数

# FUNCTIONS

**算术：**
- **sqrt(x)** - 平方根
- **abs(x)** - 绝对值
- **gcd(a,b)** - 最大公约数

**三角函数：**
- **sin(x), cos(x), tan(x)**
- **asin(x), acos(x), atan(x)**

**其他：**
- **ln(x)** - 自然对数
- **exp(x)** - 指数
- **rand()** - 随机数

# WORKFLOW

```bash
# Simple calculation
calc "2^100"

# Interactive mode
calc
> x = 5
> y = 10
> x * y + 3

# Script file
calc -f script.cal

# One-liner with precision
calc "pi(100)"  # Pi with 100 digits
```

# VARIABLES

```
> epsilon(1e-10)  # Set precision
> x = 5
> y = x^2 + 3*x + 1
```

# CAVEATS

语法与 bc 不同。预装率较低。某些函数需要理解 calc 的类型系统。错误信息可能难以理解。大型计算会消耗内存。

# HISTORY

**calc** 最初开发于 **1984** 年前后，此后一直作为功能丰富 bc 替代品维护至今。

# INSTALL

```apt: sudo apt install calc```

```dnf: sudo dnf install calc```

```pacman: sudo pacman -S calc```

```zypper: sudo zypper install calc```

```brew: brew install calc```

```nix: nix profile install nixpkgs#calc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [dc](/man/dc)(1), [qalc](/man/qalc)(1)

# RESOURCES

```[Source code](https://github.com/lcn2/calc)```

```[Homepage](http://www.isthe.com/chongo/tech/comp/calc/)```

<!-- verified: 2026-06-22 -->
