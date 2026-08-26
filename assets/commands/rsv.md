# TAGLINE

处理 CSV、TXT 和 Excel 文件的高速 CLI 工具箱

# TLDR

**查看开头行**

```rsv head [data.csv]```

**限定行数查看开头**

```rsv head -n [5] [data.csv]```

**显示表头**

```rsv headers [data.csv]```

**统计行数**

```rsv count [data.csv]```

**各列的频数表**

```rsv frequency [data.csv]```

**列统计信息**

```rsv stats [data.csv]```

**选择/筛选行**

```rsv select [data.csv]```

**用正则表达式搜索**

```rsv search [data.csv]```

**Excel 转 CSV**

```rsv excel2csv [data.xlsx]```

**格式化为表格**

```rsv table [data.csv]```

# SYNOPSIS

**rsv** *command* [*options*] [*file*]

# DESCRIPTION

**rsv** 是一个 Rust 编写的命令行工具，用于检查和转换 CSV、TXT 与 Excel 文件。它强调速度（在标注处采用 Rayon 并行处理）、长任务上的进度条，以及对管道友好的子命令。

可用命令包括 **head**、**tail**、**header**/**headers**、**count**、**estimate**、**clean**、**unique**、**frequency**、**split**、**select**、**flatten**、**slice**、**search**、**sort**、**sample**、**stats**、**excel2csv**、**to**（导出）和 **table**。除 **clean** 和 **excel2csv** 之外，大多数命令都可以串联使用。Excel 默认读取第一个工作表；在支持的地方可以用 **--sheet** 指定。

请从 GitHub releases 页面安装（并将二进制文件加入 **PATH**）。使用 **rsv** *command* **--help** 可查看各命令的标志。

# PARAMETERS

**head** / **tail** [**-n** *n*] [*file*]

> 预览前/后若干行（默认 10 行）。

**headers** [**-s** *sep*] [*file*]

> 打印列标题。

**count** / **estimate** [*file*]

> 精确或快速近似地统计行数。

**frequency** / **stats** / **unique** / **select** / **search** / **sort** / **sample** / **split** / **slice** / **flatten**

> 数据分析与重塑（其中多个命令支持并行处理和进度条）。

**excel2csv** / **to** / **table** / **clean**

> 进行转换、导出、格式化或清理字段。

# CAVEATS

**sort** 在内存中完成且功能有限（按上游文档说明，每次最多排两列）。特别宽或特别大的 Excel 工作表可能需要更多内存。处理 TSV 或非标准 CSV 文本时，请确认好分隔符标志。

# INSTALL

```aur: yay -S rsv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xsv](/man/xsv)(1), [csvkit](/man/csvkit)(1), [qsv](/man/qsv)(1), [mlr](/man/mlr)(1)

# RESOURCES

```[Source code](https://github.com/ribbondz/rsv)```

<!-- verified: 2026-07-19 -->
