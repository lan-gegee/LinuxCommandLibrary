# TAGLINE

从命令行检查 Apache Parquet 文件

# TLDR

**打印 schema**

```pqrs schema [file.parquet]```

**打印内容**

```pqrs cat [file.parquet]```

**JSON lines 输出**

```pqrs cat [file.parquet] --json```

**CSV 输出**

```pqrs cat [file.parquet] --csv```

**前 N 条记录**

```pqrs head [file.parquet] --records [10] --json```

**行数统计**

```pqrs rowcount [file.parquet]```

**文件大小明细**

```pqrs size [file.parquet]```

**随机采样**

```pqrs sample [file.parquet]```

# SYNOPSIS

**pqrs** [*flags*] *subcommand* [*args*]

# DESCRIPTION

**pqrs** 是一个用于检查 Apache Parquet 文件的 Rust 命令行工具（大致相当于"Rust 版 parquet-tools"）。它基于 Arrow/Parquet 的 Rust crate 构建，在 schema、内容和大小检查方面替代了大部分已弃用的 Java **parquet-tools** 工作流。

可从 GitHub releases、**cargo install pqrs** 或 Homebrew（**manojkarthick/tap/pqrs**）安装。

# PARAMETERS

**cat** *files*...

> 打印记录。**--json**、**--csv**、**--csv-data-only** / **--no-header** 控制输出格式。会递归进入目录。

**head** *file*

> 前 N 条记录（**--records**）。支持 **--json**。

**schema** *files*...

> 打印 Parquet schema。

**rowcount** *files*...

> 打印行数。

**size** *files*...

> 打印大小信息。

**sample** *file*

> 随机采样记录。

**merge** *files*...

> 通过串联 row group 将多个文件合并为另一个 Parquet 文件。

**-d**, **--debug**

> 调试输出。

# CAVEATS

包含 Struct 或 Byte 字段的文件不支持 CSV 输出。嵌套数据最好以默认格式或 **--json** 查看。非常大的文件可能需要采样而非完整 **cat**。

# INSTALL

```nix: nix profile install nixpkgs#pqrs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[parquet-tools](/man/parquet-tools)(1), [duckdb](/man/duckdb)(1), [arrow-tools](/man/arrow-tools)(1)

# RESOURCES

```[Source code](https://github.com/manojkarthick/pqrs)```

<!-- verified: 2026-07-19 -->
