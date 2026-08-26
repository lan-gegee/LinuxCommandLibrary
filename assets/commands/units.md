# TAGLINE

在度量单位之间换算

# TLDR

**启动交互模式**进行单位换算

```units```

**直接在单位之间换算**

```units "[from_unit]" "[to_unit]"```

**换算具体的量**

```units "[100 kilometers]" "[miles]"```

**显示某个单位的定义**

```units "[parsec]"```

**使用简洁输出**（适合脚本）

```units --terse "[from_unit]" "[to_unit]"```

**检查单位数据库**是否有错误

```units --check```

**使用自定义单位文件**

```units -f [custom_units.dat]```

**显示版本和数据文件位置**

```units -V```

# SYNOPSIS

**units** [_options_] [_from-unit_] [_to-unit_]

# PARAMETERS

**-f** _filename_, **--file** _filename_
> 使用指定的单位数据库文件。

**-c**, **--check**
> 检查所有单位是否都能化简为基本单位。

**-o** _format_, **--output-format** _format_
> 指定数值输出格式（printf 风格）。

**-d** _ndigits_, **--digits** _ndigits_
> 设置输出中的有效数字位数。

**-e**, **--exponential**
> 输出使用科学计数法（指数记数）。

**-t**, **--terse**
> 只打印换算系数（便于解析）。

**--compact**
> 输出不带运算符的紧凑结果。

**-q**, **--quiet**
> 抑制统计信息和提示符。

**-v**, **--verbose**
> 显示更详细的输出。

**--list-units**
> 列出所有已知单位并退出。

**--conformable**
> 显示与给定表达式量纲兼容的单位。

**-u** _system_, **--units** _system_
> 使用备选单位制（例如 si、cgs、natural）。

**--locale** _locale_
> 强制使用特定的 locale。

**--minus**
> 将 **-** 解释为减法（默认）。

**--product**
> 将 **-** 解释为乘法。

**-V**, **--version**
> 打印版本和数据文件位置。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**GNU Units** 可在不同度量系统之间换算，并能进行单位运算。它包含一个涵盖 3000 多个单位的综合数据库，其中包括历史单位和冷僻的度量方式。

在交互模式下，在 "You have:" 提示符处输入源单位，在 "You want:" 处输入目标单位。Units 会检查量纲兼容性，对不兼容的换算报告一致性错误。

该程序还可以作为内置函数的科学计算器（sin、cos、ln、exp 等），支持带单位的复杂表达式。

# CAVEATS

尝试在量纲不兼容的单位之间换算（例如米换秒）会产生一致性错误。单位数据库的位置因安装而异；用 **-V** 查找。自定义单位定义可以添加到个人单位文件中。

# HISTORY

最初的 Unix units 程序收录于早期 Unix 版本中。**GNU Units** 由 **Adrian Mariano** 编写，是一个带有扩充单位数据库的自由实现。它于 **1996 年**首次发布，作为 GNU 计划的一部分持续维护。该程序收录了来自古代文明、历史度量以及现代科学标准的各种单位。

# INSTALL

```apt: sudo apt install units```

```dnf: sudo dnf install units```

```apk: sudo apk add units```

```zypper: sudo zypper install units```

```nix: nix profile install nixpkgs#units```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [dc](/man/dc)(1), [calc](/man/calc)(1)
