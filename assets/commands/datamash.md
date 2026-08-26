# TAGLINE

执行基本数值与统计运算的命令行工具

# TLDR

获取某一列的**最大值、最小值、均值和中位数**

```seq 3 | datamash max 1 min 1 mean 1 median 1```

**按第一列分组并对第二列求和**（CSV 输入）

```datamash -t, -g 1 sum 2 < [file.csv]```

以**指定精度**获取均值

```echo -e '1\n2\n3' | datamash -R [decimals] mean 1```

**忽略 NA/NaN 值**计算均值

```echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1```

# SYNOPSIS

**datamash** [_options_] _operation_ _column_ [_operation_ _column_...]

# DESCRIPTION

**datamash** 在命令行对输入数据执行基本的数值、文本和统计运算。它面向那些原本需要编写脚本或使用统计软件的快速数据分析任务，支持求和、均值、中位数、标准差、方差等多种操作。

输入从 stdin 或文件读取，列由空白字符或指定的分隔符分隔。该工具可以按字段对数据分组并为每组计算聚合统计量，类似 SQL 的 GROUP BY 功能。

datamash 是 GNU 项目的一部分，擅长用单行命令做数据探索。它常用于管道中分析 CSV 文件、日志数据或任何表格文本数据。该工具既能处理数值运算也能处理文本运算，包括唯一值计数、字符串操作和随机抽样。

# PARAMETERS

**-R, --round** _digits_
> 数值输出四舍五入到指定小数位

**--narm**
> 忽略 NA 和 NaN 值

**-t** _char_
> 使用指定的字段分隔符

**-g, --group** _fields_
> 按指定字段分组

**-H, --headers**
> 第一行为表头（输入和输出均适用）

**-s, --sort**
> 分组前先对输入排序（若输入尚未按分组字段排序则必需）

**-W, --whitespace**
> 使用空白字符（一个或多个空格/制表符）作为字段分隔符

**--full**
> 在运算结果之前打印整行输入

# OPERATIONS

**sum, min, max, mean, median**
> 基本统计

**pstdev, sstdev**
> 总体/样本标准差

**count, unique, collapse**
> 计数与分组

**first, last, rand**
> 选择类操作

# CAVEATS

小数分隔符跟随当前区域设置（C 区域为句点，德语等区域为逗号）。分组（-g）要求输入已排序，除非给出 -s。列编号从 1 开始。

# INSTALL

```apt: sudo apt install datamash```

```dnf: sudo dnf install datamash```

```pacman: sudo pacman -S datamash```

```apk: sudo apk add datamash```

```zypper: sudo zypper install datamash```

```brew: brew install datamash```

```nix: nix profile install nixpkgs#datamash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[awk](/man/awk)(1), [cut](/man/cut)(1), [sort](/man/sort)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/datamash/)```

```[Documentation](https://www.gnu.org/software/datamash/manual/)```

<!-- verified: 2026-07-11 -->
