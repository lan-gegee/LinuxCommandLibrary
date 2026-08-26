# TAGLINE

校验和清理 CSV 文件

# TLDR

检查 CSV 文件中**列数不匹配的行**

```csvclean --length-mismatch [data.csv]```

**报告列数不匹配**并在输出中剔除错误行

```csvclean --length-mismatch --omit-error-rows [data.csv]```

**报告空列**作为错误

```csvclean --empty-columns [data.csv]```

对 CSV 文件**启用所有检查**

```csvclean -a [data.csv]```

通过合并到前一行来**修复短行**

```csvclean --join-short-rows [data.csv]```

用指定值**填充短行**

```csvclean --fill-short-rows --fillvalue "N/A" [data.csv]```

使用自定义分隔符和编码进行校验

```csvclean --length-mismatch -d "[;]" -e [latin1] [data.csv]```

# SYNOPSIS

**csvclean** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要清理或校验的 CSV 文件。省略时从 stdin 读取。

**--length-mismatch**
> 报告比表头行更短或更长的行。

**--empty-columns**
> 将空列作为错误报告。

**-a**, **--enable-all-checks**
> 启用所有错误报告检查。

**--join-short-rows**
> 将连续的短行合并为一行。

**--separator** _SEPARATOR_
> 合并短行时使用的字符串（默认：换行符）。

**--fill-short-rows**
> 用缺失值填充短行。

**--fillvalue** _VALUE_
> 填充短行所用的值（默认：空字符串）。

**--omit-error-rows**
> 从标准输出中排除包含错误的行。

**--label** _LABEL_
> 在错误输出中添加标签列，便于自动化流程使用。

**--header-normalize-space**
> 去除表头的首尾空白并规范表头中的空白字符。

**-d** _CHAR_, **--delimiter** _CHAR_
> 字段分隔符（默认：逗号）。

**-t**, **--tabs**
> 使用制表符作为分隔符。

**-q** _CHAR_, **--quotechar** _CHAR_
> 引号字符（默认：双引号）。

**-p** _CHAR_, **--escapechar** _CHAR_
> 用于转义分隔符或引号字符的转义字符。

**-e** _ENCODING_, **--encoding** _ENCODING_
> 输入文件编码。

**-S**, **--no-header-row**
> 文件没有表头行。

**-H**
> 从输出中省略表头行。

**-K** _N_, **--skip-lines** _N_
> 跳过输入文件的前 N 行。

**-v**
> 详细错误输出。

# DESCRIPTION

**csvclean** 是 csvkit 的组成部分，用于校验和清理 CSV 文件。它能检测列数不一致、空列、编码问题等常见毛病。

自 csvkit 2.0 起，csvclean 默认不再报告或修复任何错误。你必须显式启用检查（如 **--length-mismatch** 或 **--empty-columns**）或修复选项（如 **--join-short-rows** 或 **--fill-short-rows**）。结果写入标准输出，错误写入标准错误。

该工具支持多种 CSV 方言，可处理使用不同分隔符、引号字符和编码的文件。它是分析前预处理杂乱数据的必备工具。

# CAVEATS

自动清理可能以意想不到的方式改动数据；请仔细审查清理后的输出。自 csvkit 2.0 起，不带任何检查或修复标志运行 csvclean 会直接报错。原文件不会被修改。

# HISTORY

csvclean 是 **csvkit** 的一部分。csvkit 由 Christopher Groskopf 创建，首次发布于 **2011** 年。它提供了一整套处理 CSV 文件的工具，旨在把 Unix 哲学的威力带到表格数据处理中。

# SEE ALSO

[csvstat](/man/csvstat)(1), [csvcut](/man/csvcut)(1), [csvlook](/man/csvlook)(1), [csvformat](/man/csvformat)(1), [csvgrep](/man/csvgrep)(1)
