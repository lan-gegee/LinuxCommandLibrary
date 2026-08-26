# TAGLINE

平面文件提取器

# TLDR

使用配置**从平面文件提取字段**

```ffe -c [config.ffe] [data.txt]```

**以命名的打印格式输出**

```ffe -c [config.ffe] -p [csv] [data.txt]```

过滤匹配表达式的记录

```ffe -c [config.ffe] -e [field=value] [data.txt]```

显示配置中的结构信息后退出

```ffe -c [config.ffe] -I```

# SYNOPSIS

**ffe** [_options_] [_files_]

# DESCRIPTION

**ffe**（Flat File Extractor）根据配置文件提供的结构定义解析定宽和分隔符平面文件。它可提取字段，并将数据转换为 CSV 或 XML 等格式。

配置文件定义记录布局，包括字段名、宽度和类型。该工具可处理单个文件中的多种记录类型，这在大型机和批处理数据格式中很常见。

# PARAMETERS

**-c**, **--configuration** _file_
> 配置文件，定义记录结构和打印格式。

**-p**, **--print** _format_
> 选择配置文件中定义的命名打印格式。

**-o**, **--output** _file_
> 将输出写入指定文件而非 stdout。

**-f**, **--field-list** _fields_
> 只打印列出的字段（逗号分隔）。

**-e**, **--expression** _expr_
> 只打印表达式匹配的记录。

**-a**, **--and**
> 用逻辑 AND 组合多个表达式（默认为 OR）。

**-X**, **--casecmp**
> 表达式求值不区分大小写。

**-v**, **--invert-match**
> 只打印不匹配表达式的记录。

**-r**, **--replace** _field=value_
> 在输出中将字段内容替换为给定值。

**-l**, **--loose**
> 遇到无效输入行时不中止。

**-d**, **--debug**
> 将无效输入行写入 `ffe_error_<pid>.log`。

**-I**, **--info**
> 显示配置文件中的结构信息并退出。

# CAVEATS

需要配置文件。复杂的记录结构需要仔细定义。`-p` 标志选择的是配置中定义的命名打印格式，而非通用的格式名。

# INSTALL

```apt: sudo apt install ffe```

```brew: brew install ffe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[awk](/man/awk)(1), [cut](/man/cut)(1), [csvtool](/man/csvtool)(1)
