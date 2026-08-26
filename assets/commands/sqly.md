# TAGLINE

对 CSV、TSV、JSON 和 Excel 文件执行 SQL

# TLDR

**用 CSV 文件打开交互式 SQL Shell**

```sqly [user.csv]```

**直接运行查询**

```sqly --sql "[SELECT * FROM user WHERE age > 30]" [user.csv]```

**以 CSV 格式输出结果**

```sqly --sql "[SELECT * FROM user LIMIT 2]" --csv [user.csv]```

# SYNOPSIS

**sqly** [**--sql** _query_] [**--csv**|**--tsv**] [_files_...]

# DESCRIPTION

**sqly** 将 CSV、TSV、LTSV、JSON 和 Excel 文件导入内存中的 SQLite3 数据库，让你可以对这些数据运行 SQL 查询。它既支持带 SQL 补全和命令历史记录的交互式 Shell 模式，也支持直接执行一次性查询。输出可格式化为 ASCII 表格、CSV、TSV 或 LTSV。

# HISTORY

**sqly** 由 **nao1215** 创建，使用 **Go** 编写。

# SEE ALSO

[csvq](/man/csvq)(1), [qsv](/man/qsv)(1), [miller](/man/miller)(1)
