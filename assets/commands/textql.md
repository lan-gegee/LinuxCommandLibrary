# TAGLINE

对 CSV 文件执行 SQL 查询

# TLDR

**查询 CSV**

```textql -sql "[SELECT * FROM file]" [data.csv]```

**含表头**

```textql -header -sql "[SELECT name FROM file]" [data.csv]```

**自定义分隔符**

```textql -dlm=";" -sql "[query]" [data.csv]```

**保存到 SQLite**

```textql -save-to [output.db] [data.csv]```

**输出到文件**

```textql -output-file [result.csv] -sql "[query]" [data.csv]```

# SYNOPSIS

**textql** [_-sql query_] [_-header_] [_-dlm delim_] [_options_] _files_

# PARAMETERS

**-sql** _QUERY_
> SQL 查询语句。

**-header**
> 第一行是表头。

**-dlm** _CHAR_
> 字段分隔符。

**-save-to** _FILE_
> 保存到 SQLite。

**-output-file** _FILE_
> 输出文件。

**-output-dlm** _CHAR_
> 输出分隔符。

# DESCRIPTION

**textql** 允许对 CSV、TSV 等结构化文本文件运行 SQL 查询。它把文件加载到内存中的 SQLite 数据库，将每个文件视为一张表，然后对其执行标准 SQL 查询。

指定 **-header** 时，第一行用作列名；否则列被命名为 c0、c1 等。可同时加载多个文件并使用 SQL JOIN 语法进行连接。**-save-to** 选项可将导入的数据持久化到 SQLite 数据库文件中以便进一步分析。通过 **-dlm** 标志支持自定义分隔符。

# CAVEATS

大文件受内存限制。存在 SQLite 的固有限制。基于 Go 的工具。

# HISTORY

**textql** 的创建目的是借助 SQLite 对 CSV 等结构化文本文件执行 SQL 查询。

# INSTALL

```apt: sudo apt install textql```

```nix: nix profile install nixpkgs#textql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [csvq](/man/csvq)(1), [q](/man/q)(1), [miller](/man/miller)(1)
