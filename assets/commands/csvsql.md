# TAGLINE

面向 CSV 的 SQL 查询执行器与数据库导入工具

# TLDR

对 CSV 文件**执行 SQL 查询**

```csvsql --query "[SELECT * FROM data WHERE id > 10]" [data.csv]```

为 CSV **生成 CREATE TABLE** 语句

```csvsql [data.csv]```

**将 CSV 导入数据库**

```csvsql --db [postgresql:///mydb] --insert [data.csv]```

**查询多个文件**（表名取自文件名）

```csvsql --query "[SELECT * FROM file1 JOIN file2 ON file1.id = file2.id]" [file1.csv] [file2.csv]```

在 SQLite 中**创建表并插入**数据

```csvsql --db [sqlite:///data.db] --insert --create-if-not-exists [data.csv]```

**带聚合的查询**

```csvsql --query "[SELECT category, COUNT(*) FROM data GROUP BY category]" [data.csv]```

# SYNOPSIS

**csvsql** [_options_] _file_...

# PARAMETERS

**--query** _SQL_
> 对 CSV 数据执行 SQL 查询。

**--db** _CONNECTION_
> 数据库连接字符串（SQLAlchemy 格式）。

**--insert**
> 将数据插入数据库（需要 --db）。

**--create-if-not-exists**
> 若表不存在则创建。

**--tables** _NAMES_
> 逗号分隔的表名（默认：文件名）。

**--no-create**
> 不生成 CREATE TABLE 语句。

**-d** _CHAR_, **--delimiter** _CHAR_
> 字段分隔符（默认：逗号）。

**-e** _ENCODING_, **--encoding** _ENCODING_
> 输入文件的编码。

**--no-inference**
> 禁用类型推断。

# DESCRIPTION

**csvsql** 是 csvkit 的一部分，可对 CSV 文件执行 SQL 查询，或将 CSV 数据导入数据库。查询时它会创建一个内存中的 SQLite 数据库；导入时则连接外部数据库进行操作。

不使用 **--query** 时，它会输出适合该数据的 CREATE TABLE 语句，可用于生成数据库模式。使用 **--query** 时，它会对 CSV 数据执行 SQL，支持连接、聚合等所有 SQL 操作。

导入数据库时，csvsql 通过 SQLAlchemy 连接字符串支持多种数据库，包括 PostgreSQL、MySQL、SQLite 等。它会进行类型推断，以生成合适的列定义。

# CAVEATS

内存查询会将所有数据载入 RAM，对大文件执行复杂查询可能较慢。类型推断可能误判列的类型。数据库导入需要安装相应的驱动程序。

# HISTORY

csvsql 是 **csvkit** 的组成部分，由 Christopher Groskopf 于 **2011 年**创建。它弥合了 CSV 文件与数据库之间的鸿沟，无需手动搭建数据库即可进行基于 SQL 的数据分析。

# SEE ALSO

[csvkit](/man/csvkit)(1), [sqlite3](/man/sqlite3)(1)
