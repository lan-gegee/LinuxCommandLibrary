# TAGLINE

处理 Apache ORC 文件的实用工具集合

# TLDR

**显示 ORC 文件元数据**

```orc-metadata [file.orc]```

**显示文件内容**

```orc-contents [file.orc]```

**获取文件统计信息**

```orc-statistics [file.orc]```

**将 CSV 转换为 ORC**

```orc-tools convert [data.csv] -o [output.orc]```

**扫描 ORC 文件**

```orc-scan [file.orc]```

**合并 ORC 文件**

```orc-tools merge [file1.orc] [file2.orc] -o [merged.orc]```

# SYNOPSIS

**orc-tools** _command_ [_options_] _files_...

# PARAMETERS

**metadata**
> 显示文件元数据。

**contents**
> 显示内容。

**statistics**
> 显示统计信息。

**convert**
> 转换为 ORC。

**scan**
> 扫描并验证。

**merge**
> 合并文件。

**-o** _file_
> 输出文件。

# DESCRIPTION

**orc-tools** 是一组用于处理 Apache ORC（Optimized Row Columnar）文件的实用工具。ORC 是一种针对 Hadoop 工作负载优化的列式存储格式。

这些工具可用于检查、转换和操作 ORC 文件。

# ORC FEATURES

```
- Columnar storage
- Compression (ZLIB, Snappy, LZO)
- Predicate pushdown
- Type evolution
- ACID support
```

# CAVEATS

需要 Java。大文件可能需要调整内存设置。属于 Apache ORC 项目。

# HISTORY

Apache ORC 由 **Hortonworks** 为 Hive 创建，后来成为专注于高效列式存储的 Apache 顶级项目。

# INSTALL

```brew: brew install orc-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[parquet-tools](/man/parquet-tools)(1), [hive](/man/hive)(1), [spark](/man/spark)(1)
