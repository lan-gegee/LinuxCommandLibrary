# TAGLINE

面向大数据的列式存储格式

# TLDR

**显示文件 schema**

```parquet-tools schema [file.parquet]```

**显示元数据**

```parquet-tools meta [file.parquet]```

**显示前几行**

```parquet-tools head [file.parquet]```

**转换为 JSON**

```parquet-tools cat --json [file.parquet]```

**显示行数**

```parquet-tools rowcount [file.parquet]```

**合并文件**

```parquet-tools merge [file1.parquet] [file2.parquet] [output.parquet]```

# SYNOPSIS

**parquet-tools** _command_ [_options_] _file_

# PARAMETERS

**schema**
> 显示 schema。

**meta**
> 显示元数据。

**head**
> 显示前几行。

**cat**
> 输出所有行。

**rowcount**
> 统计行数。

**merge**
> 合并文件。

**--json**
> JSON 输出。

**-n** _num_
> 行数。

# DESCRIPTION

**Parquet** 是一种面向大数据的列式存储格式。parquet-tools（或 parquet-cli）用于检查和操作 Parquet 文件，可显示 schema、元数据和内容。

Parquet 为分析型工作负载提供高效的压缩与编码。

# PARQUET FEATURES

```
- Columnar storage
- Schema embedded
- Compression (Snappy, GZIP, etc.)
- Predicate pushdown
- Nested data support
```

# PYTHON ALTERNATIVE

```python
import pyarrow.parquet as pq
table = pq.read_table('file.parquet')
print(table.schema)
```

# CAVEATS

基于 Java 的工具需要 JVM。Python 工作流可以考虑 pyarrow。处理大文件需要内存。

# HISTORY

Apache Parquet 于 **2013 年**由 **Twitter** 与 **Cloudera** 合作创建，旨在实现高效的大数据存储。

# SEE ALSO

[orc-tools](/man/orc-tools)(1), [avro-tools](/man/avro-tools)(1), [spark](/man/spark)(1)
