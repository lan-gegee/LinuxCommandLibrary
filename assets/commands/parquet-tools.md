# TAGLINE

检查 Apache Parquet 文件

# TLDR

**显示 schema**

```parquet-tools schema [file.parquet]```

**查看数据**

```parquet-tools cat [file.parquet]```

**显示元数据**

```parquet-tools meta [file.parquet]```

**查看前 N 行**

```parquet-tools head -n [10] [file.parquet]```

**显示行数**

```parquet-tools rowcount [file.parquet]```

**转换为 JSON**

```parquet-tools cat --json [file.parquet]```

**显示列索引信息**

```parquet-tools column-index [file.parquet]```

**输出指定的列**

```parquet-tools cat --columns [col1,col2] [file.parquet]```

# SYNOPSIS

**parquet-tools** _command_ [_options_] _file_

# PARAMETERS

**cat**
> 打印文件内容。

**head**
> 打印前几行。

**schema**
> 显示 schema。

**meta**
> 显示文件元数据。

**rowcount**
> 统计行数。

**column-index**
> 显示列索引。

**-n** _N_
> 行数。

**--json**
> JSON 输出格式。

**--columns** _COLS_
> 指定的列。

# DESCRIPTION

**parquet-tools** 检查 Apache Parquet 文件。Parquet 是大数据系统中使用的列式存储格式。

模式检查会显示列名、类型和嵌套结构。这有助于在不读取内容的情况下了解数据结构。

cat 和 head 命令显示实际数据。JSON 输出便于与其他工具集成。

元数据显示压缩方式、编码和统计信息。行组和列块则揭示物理布局。

来自 Spark、Hive 等系统的 Parquet 文件都可以检查。这对调试数据管道很有用。

# CAVEATS

大文件可能读取得很慢。某些复杂类型的显示方式有所不同。需要 Java 运行时。

# HISTORY

**Parquet** 格式于 **2013 年**前后由 **Twitter** 和 **Cloudera** 开发。parquet-tools 为这一广泛采用的列式格式提供命令行检查功能。

# INSTALL

```nix: nix profile install nixpkgs#parquet-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[parquet](/man/parquet)(1), [avro-tools](/man/avro-tools)(1), [orc-tools](/man/orc-tools)(1)
