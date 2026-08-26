# TAGLINE

在人类可读表示与数字之间相互转换

# TLDR

**将字节转换为人类可读格式**

```numfmt --to=iec [1048576]```

**使用 IEC 单位转换**（Ki、Mi、Gi）

```echo [1073741824] | numfmt --to=iec```

**使用 SI 单位转换**（K、M、G）

```numfmt --to=si [1000000]```

**将人类可读格式解析为数字**

```numfmt --from=iec [10M]```

**转换输入中的特定字段**

```df -B1 | numfmt --header --field 2-4 --to=iec```

**添加后缀**

```numfmt --to=si --suffix=B [1000000]```

**设置输出填充宽度**

```numfmt --to=iec --padding=10 [1048576]```

# SYNOPSIS

**numfmt** [_--from=UNIT_] [_--to=UNIT_] [_--field=N_] [_options_] [_numbers_]

# PARAMETERS

**--from=** _UNIT_
> 解析输入单位（auto、si、iec、iec-i）。

**--to=** _UNIT_
> 转换为目标单位（si、iec、iec-i）。

**--field=** _N_
> 转换第 N 个字段（默认：1）。

**--header**[=_N_]
> 跳过 N 行表头（默认：1）。

**--padding=** _N_
> 将输出填充到 N 个字符宽。

**--suffix=** _STR_
> 在输出后附加后缀。

**--format=** _FMT_
> printf 风格的格式。

**--round=** _METHOD_
> 舍入方式：up、down、from-zero、towards-zero、nearest。

**--grouping**
> 按区域设置进行数字分组（如 1,000）。

**--delimiter=** _D_
> 使用 D 作为字段分隔符。

**--invalid=** _MODE_
> 处理无效输入的方式：abort、fail、warn、ignore。

**-d** _D_
> --delimiter 的简写。

**--debug**
> 打印转换警告。

# DESCRIPTION

**numfmt** 在数字与人类可读表示之间相互转换。它同时支持 SI 单位（1000 的幂：K、M、G）和 IEC 单位（1024 的幂：Ki、Mi、Gi）。

输入解析（--from）解释带后缀的数字：10K 会变为 10000（SI）或 10240（IEC）。输出转换（--to）用适当的后缀格式化数字以提高可读性。

处理命令输出时，--field 选择要转换的列，--header 则保留表头行。这样就可以把 df 或 ls 等命令的输出通过管道传给 numfmt 做人类可读转换。

--format 选项提供 printf 风格的控制：`%10.2f` 表示固定宽度的十进制输出。配合 --grouping，数字会按区域设置显示千位分隔符。

舍入模式控制小数值的处理方式。默认四舍五入到最近值，但存储容量计算可能更适合向上取整（up）或向下取整（down）。

# CAVEATS

在大数值下 SI 和 IEC 单位差异显著。'iec-i' 格式使用明确的 "Ki" 后缀，而 'iec' 只用 "K"。浮点精度可能影响非常大的数字。并非所有区域设置都支持分组。

# HISTORY

**numfmt** 属于 **GNU coreutils**，加入它是为了在各实用工具间提供标准化的数字格式化功能。它解决了不同命令之间人类可读输出不一致的问题，提供了一个同时遵循 SI 和 IEC 标准的统一数字转换工具。

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

[printf](/man/printf)(1), [bc](/man/bc)(1), [units](/man/units)(1), [factor](/man/factor)(1)
