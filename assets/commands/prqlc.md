# TAGLINE

将 PRQL 查询编译为 SQL

# TLDR

**将 PRQL 编译为 SQL**

```prqlc compile [query.prql]```

**从 stdin 编译**

```echo "from employees | select name" | prqlc compile```

**格式化 PRQL**

```prqlc fmt [query.prql]```

**输出到文件**

```prqlc compile [query.prql] -o [output.sql]```

# SYNOPSIS

**prqlc** _command_ [_options_] [_file_]

# PARAMETERS

**compile**
> 将 PRQL 编译为 SQL。

**fmt**
> 格式化 PRQL 代码。

**-o** _FILE_
> 输出文件。

**--target** _DB_
> 目标数据库。

# DESCRIPTION

**prqlc** 是 PRQL（Pipelined Relational Query Language）的编译器。PRQL 是一种现代查询语言，旨在成为比 SQL 更易读、更易组合的替代方案。它将 PRQL 源代码转译为标准 SQL，可在任何受支持的数据库上执行。

PRQL 采用管道语法，数据转换通过管道运算符串联，使复杂查询比等价的嵌套 SQL 更易于阅读和编写。编译器通过 **--target** 选项支持多种 SQL 方言，可为 PostgreSQL、MySQL、SQLite、BigQuery 等生成特定数据库的 SQL。

**fmt** 子命令按统一风格格式化 PRQL 源代码；编译器接受来自文件或 stdin 的输入，可用于构建流水线。

# CAVEATS

PRQL 尚处于实验阶段。支持多种 SQL 方言。

# HISTORY

PRQL 的定位是作为 SQL 语法的**现代化替代方案**。

# INSTALL

```brew: brew install prqlc```

```nix: nix profile install nixpkgs#prqlc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [sqlite3](/man/sqlite3)(1)
