# TAGLINE

CSV 格式与分隔符转换器

# TLDR

**将 CSV 转换为制表符分隔**

```csvformat -T [input.csv]```

**更改分隔符**

```csvformat -D "[;]" [input.csv]```

**给所有字段加引号**

```csvformat -U 1 [input.csv]```

**跳过前 N 行**

```csvformat -K [1] [input.csv]```

**更改行终止符**

```csvformat -M "\r\n" [input.csv]```

# SYNOPSIS

**csvformat** [_options_] [_file_]

# PARAMETERS

**-T**
> 输出使用制表符分隔。

**-D** _delimiter_
> 设置输出分隔符。

**-U** _style_
> 加引号风格：0=最小化、1=全部、2=非数字字段、3=不加。

**-K** _n_
> 跳过前 n 行。

**-M** _char_
> 设置输出行终止符。

**-d** _CHAR_, **--delimiter** _CHAR_
> 输入字段分隔符（默认：逗号）。

**-e** _ENCODING_, **--encoding** _ENCODING_
> 输入文件编码。

# DESCRIPTION

**csvformat** 是 csvkit 的组成部分，用于在各种分隔格式之间转换 CSV 文件。它可以在保持 CSV 结构正确的前提下更改字段分隔符、引号字符、加引号风格和行终止符。

该工具适合把 CSV 转成制表符分隔格式供 Unix 工具使用、统一各文件的引号处理方式，或者按目标系统的分隔符要求重新格式化数据。转换过程中它能正确遵循 CSV 引号规则。

加引号风格包括：最小化（仅在必要时加引号）、全部字段、仅非数字字段以及不加引号。该工具还能跳过表头行，并可调整行尾以兼容跨平台场景。

# CAVEATS

属于 csvkit，需要 Python 环境。最小化模式下的加引号行为由类型推断决定。某些选项组合可能产生对特定解析器无效的 CSV。

# HISTORY

csvformat 是 **csvkit** 的一部分，由 Christopher Groskopf 于 **2011** 年创建。它满足了在保留数据完整性的前提下于各种 CSV 方言和分隔格式之间转换的常见需求。

# SEE ALSO

[csvkit](/man/csvkit)(1), [csvlook](/man/csvlook)(1), [csvcut](/man/csvcut)(1), [csvgrep](/man/csvgrep)(1)
