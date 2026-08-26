# TAGLINE

极速的 CSV 与表格数据处理工具集

# TLDR

**统计 CSV 文件的行数**

```qsv count [data.csv]```

**搜索某个模式**

```qsv search '[pattern]' [data.csv]```

**选择特定列**

```qsv select [col1,col2] [data.csv]```

**对 CSV 文件执行 SQL 查询**

```qsv sqlp "SELECT * FROM data WHERE value > 100" [data.csv]```

**获取汇总统计信息**

```qsv stats [data.csv]```

# SYNOPSIS

**qsv** _command_ [_options_] [_file_]

# DESCRIPTION

**qsv** 是一套全面的命令行工具集，用于查询、转换、验证和分析 CSV 及表格数据。它提供 50 多个子命令，包括 sort、join、dedup、frequency、stats、search、validate，以及内嵌的 Luau 脚本 DSL。它支持 CSV、JSON、JSONL、Parquet、Arrow、Avro 和 Excel 格式，并可通过流式、多线程处理任意大的文件。

# HISTORY

**qsv** 由 **jqnatividad**（dathere）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S qsv```

```brew: brew install qsv```

```nix: nix profile install nixpkgs#qsv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[csvlens](/man/csvlens)(1), [xsv](/man/xsv)(1), [miller](/man/miller)(1), [cut](/man/cut)(1)
