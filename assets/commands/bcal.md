# TAGLINE

用于存储表达式和字节换算的 REPL 命令行计算器

# TLDR

**求值带存储单位的算术表达式**

```bcal "(5kb+2mb)/3"```

**将数值换算**为所有存储单位

```bcal 0xaabbcc kb```

**显示数字的二进制、十进制和十六进制**表示

```bcal -c 20140115```

**执行位运算**

```bcal -b '0xFF & 0x0F'```

**用作通用计算器**

```bcal -b '3.5 * 2.1 + 5.7'```

**将 LBA 换算为 CHS**

```bcal -f l500```

**将 CHS 换算为 LBA**

```bcal -f c10-10-10```

**启动交互式 REPL 模式**

```bcal```

# SYNOPSIS

**bcal** [**-b** [_expr_]] [**-c** _N_] [**-p** _N_] [**-f** _loc_] [**-s** _bytes_] [_expr_] [_N_ [_unit_]] [**-m**] [**-d**] [**-h**]

# PARAMETERS

**-b** [_expr_]
> 启动通用 REPL 模式。若提供了表达式，则求值后退出。

**-c** _N_
> 显示正整数 N 的十进制、二进制和十六进制表示。

**-p** _N_
> 显示数字的位位置和位值。

**-f** _loc_
> 在 CHS 与 LBA 之间互相换算。位置采用连字符分隔的表示形式。

**-s** _bytes_
> 扇区大小，以字节为单位。默认值为 512。

**-m**
> 显示最简输出（例如仅显示十进制字节数）。

**-d**
> 启用调试信息和日志。

**-h**
> 显示帮助及系统上的存储容量信息并退出。

# DESCRIPTION

**bcal**（Byte CALculator）是一个命令行工具，用于处理涉及二进制前缀、SI/IEC 换算、字节寻址、进制转换以及 LBA/CHS 计算的表达式和运算。它还支持通用算术、位运算和数学函数。

存储表达式支持运算符 **+**、**-**、**\***、**/**、**%** 以及 B、KiB、MiB、GiB、TiB、kB、MB、GB、TB 等单位。单位不区分大小写。十六进制值以 **0x** 为前缀，二进制值以 **0b** 为前缀。

在通用模式（**-b**）下，bcal 支持位运算：AND（**&**）、OR（**|**）、XOR（**^**）、取反（**~**）、左移（**<<**）和右移（**>>**）。数学函数包括 **exp**(n)、**log**(base, n)、**ln**(n)、**pow**(n, exponent) 和 **root**(radical, n)。

不带参数启动时，bcal 进入交互式 REPL 模式。最近一次的有效结果保存在变量 **r** 中，可在后续表达式中复用。在 REPL 中，按 **b** 可在存储模式与通用模式间切换，**c N** 进行进制转换，**p N** 显示位位置，**s** 显示各存储类型的大小，**q** 或连按两次 Enter 退出。

bcal 支持管道输入和文件重定向，适合脚本化工作流。若 **__uint128_t** 可用则精度为 128 位，否则为 64 位。浮点运算使用 **long double** 算术。

# CONFIGURATION

**历史记录文件**
> REPL 历史保存在 **$XDG_CONFIG_HOME/bcal/history**；若未设置 XDG_CONFIG_HOME，则为 **$HOME/.config/bcal/history**。

**BCAL_BIT_ANSI_COLOR_CODE**
> 用于设置 ANSI 转义码的环境变量，控制 **-p** 输出中位值 1 的着色。设为空可禁用着色。

# CAVEATS

仅支持 64 位操作系统。不存在小数字节，也无法对其寻址；bcal 对非整数字节结果向下取整显示。存储表达式不支持负值。

LBA 和 CHS 格式的换算参数必须以连字符分隔。LBA 值以 **l** 为前缀，CHS 值以 **c** 为前缀。任何未指定的值默认为 0。

默认磁盘几何参数：扇区大小 512，每柱面最大磁头数 16，每磁道最大扇区数 63。

# HISTORY

**bcal** 由 **Arun Prakash Jana** 创建，于 **2016** 年以开源软件形式发布，采用 **GPLv3+** 许可证。它使用 C 编写，依赖极少（libc，可选 GNU Readline 或 BSD Editline）。

# INSTALL

```apt: sudo apt install bcal```

```dnf: sudo dnf install bcal```

```aur: yay -S bcal```

```zypper: sudo zypper install bcal```

```brew: brew install bcal```

```nix: nix profile install nixpkgs#bcal```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bc](/man/bc)(1), [dc](/man/dc)(1), [calc](/man/calc)(1), [units](/man/units)(1), [numfmt](/man/numfmt)(1)
