# TAGLINE

CSV 转制表符分隔值转换器

# TLDR

**将 CSV 转换为 TSV**

```csv2tsv [input.csv] > [output.tsv]```

**从 stdin 转换**

```cat [input.csv] | csv2tsv > [output.tsv]```

使用自定义字段分隔符转换输入（如分号）

```csv2tsv -c ";" [input.csv]```

**拼接多个文件**，只保留第一行表头

```csv2tsv -H [file1.csv] [file2.csv] > [combined.tsv]```

**选择字段内嵌制表符和换行符的替换字符**

```csv2tsv --tab-replacement " " --newline-replacement " " [input.csv]```

# SYNOPSIS

**csv2tsv** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 输入 CSV 文件。未指定或指定为 **-** 时从 stdin 读取。

**-H**, **--header**
> 把每个文件的第一行视为表头。拼接多个文件时，只写入第一个文件的表头。

**-c** _CHR_, **--csv-delim** _CHR_
> CSV 输入中的字段分隔符（默认：逗号）。

**-t** _CHR_, **--tsv-delim** _CHR_
> TSV 输出中的字段分隔符（默认：TAB）。

**-r** _STR_, **--tab-replacement** _STR_
> 替换字段内 TAB 字符的字符串（默认：空格）。

**-n** _STR_, **--newline-replacement** _STR_
> 替换字段内换行字符的字符串（默认：空格）。

**-q** _CHR_, **--quote** _CHR_
> CSV 输入中的引号字符（默认：双引号）。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**csv2tsv** 将逗号分隔值（CSV）文件转换为制表符分隔值（TSV）格式。TSV 更便于用 cut、awk、sort 等 Unix 工具处理，因为制表符和换行符绝不会出现在字段内部。

该工具遵循 RFC 4180 的 CSV 引号规则：带引号的字段可以包含逗号、换行符和转义引号。转换时，字段内的任何 TAB 或换行字符都会被替换（默认替换为空格），从而保证输出的 TSV 每行恰好一条记录且列数固定。外围的引号会被去掉。

输入中常见的三种换行约定（CR、CRLF、LF）都会被自动识别，输出始终使用 Unix（LF）换行符。

csv2tsv 是 eBay tsv-utils 工具集的一员，常作为预处理步骤，配合该套件的其他工具或标准 Unix 文本工具一起使用。

# CAVEATS

按照设计，字段内的 TAB 和换行字符是被替换而非转义，因此转换不可严格逆转。超大文件以流式方式处理，节省内存。该工具假定输入为 UTF-8 兼容编码。

# HISTORY

csv2tsv 隶属于 **eBay 的 tsv-utils**，这是一套用于处理大型表格数据文件的命令行工具，由 Jon Degenhardt 用 D 语言编写。该套件于 2017 年由 eBay 开源，专为在大数据集上的速度做了优化。

# SEE ALSO

[csvkit](/man/csvkit)(1), [cut](/man/cut)(1), [miller](/man/miller)(1), [awk](/man/awk)(1)

# RESOURCES

```[Source code](https://github.com/eBay/tsv-utils)```

```[Documentation](https://github.com/eBay/tsv-utils/blob/master/docs/tool_reference/csv2tsv.md)```

<!-- verified: 2026-06-26 -->
