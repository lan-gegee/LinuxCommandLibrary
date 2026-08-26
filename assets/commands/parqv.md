# TAGLINE

用于可视化和分析 Parquet 及表格文件的交互式 TUI

# TLDR

**查看 Parquet 文件**

```parqv [path/to/file.parquet]```

**查看 CSV 文件**

```parqv [path/to/file.csv]```

**查看 JSON 或 NDJSON 文件**

```parqv [path/to/file.json]```

**查看 TSV 文件**

```parqv [path/to/file.tsv]```

# SYNOPSIS

**parqv** [_options_] _file_

# DESCRIPTION

**parqv** 是一个 Python 编写的交互式 TUI，用于可视化和分析多种格式的文件，包括 Parquet、JSON、NDJSON、CSV 和 TSV。它提供包含文件信息的元数据面板（路径、格式、大小、总行数、列数）、显示列名、数据类型和可空性的交互式 schema 视图、保留数据类型的可滚动数据预览、按列统计信息（计数、最小值/最大值、均值、标准差、去重计数），以及 Parquet 特有的行组详情。

# CAVEATS

需要 Python 3.10 或更高版本。

# HISTORY

**parqv** 由 **sanspareilsmyn** 开发，使用 **Python** 编写。

# SEE ALSO

[parqeye](/man/parqeye)(1), [csvlens](/man/csvlens)(1), [visidata](/man/visidata)(1)
