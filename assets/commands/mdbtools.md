# TAGLINE

在 Unix 上读取 Microsoft Access (.mdb, .accdb) 数据库

# TLDR

**列出数据库中的表**

```mdb-tables [database.mdb]```

**将表导出**为 CSV 并输出到 stdout

```mdb-export [database.mdb] [tablename]```

**转储完整 schema** 为 SQL DDL

```mdb-schema [database.mdb]```

统计表中的**行数**

```mdb-count [database.mdb] [tablename]```

**打开交互式 SQL** 提示符

```mdb-sql [database.mdb]```

**将所有表导出**到 CSV 目录

```for t in $(mdb-tables -1 [database.mdb]); do mdb-export [database.mdb] "$t" > "$t.csv"; done```

**转换为 SQLite 数据库**

```mdb-schema [database.mdb] sqlite | sqlite3 [out.db] && for t in $(mdb-tables -1 [database.mdb]); do mdb-export -I sqlite [database.mdb] "$t" | sqlite3 [out.db]; done```

# SYNOPSIS

**mdb-tables** [_-1_] _database_

**mdb-schema** [_options_] _database_ [_backend_]

**mdb-export** [_options_] _database_ _tablename_

**mdb-sql** [_options_] _database_

**mdb-count** _database_ _tablename_

# PARAMETERS

_DATABASE_
> Microsoft Access 数据库文件（Jet/Access 97-2003 用 .mdb，Access 2007+ 用 .accdb）。

**mdb-tables** [**-1**]
> 列出表；**-1** 每行打印一个名称，便于 shell 迭代。

**mdb-schema** _backend_
> 转储 SQL CREATE 语句；backend 选择方言（access、sybase、oracle、sqlite、postgres、mysql）。

**mdb-export** [**-I** _backend_] [**-d** _delim_] [**-q** _quote_]
> 导出单个表。**-I** 为指定后端生成 INSERT 语句；否则输出 CSV。

**mdb-sql**
> 打开交互式 SQL 提示符，支持 SQL92 的子集。

**mdb-count**
> 打印表中的行数。

# DESCRIPTION

**mdbtools** 是一组工具，用于在类 Unix 系统上读取 Microsoft Access 数据库，而无需 Microsoft Jet 或 ACE 引擎。每个工具都是独立的二进制文件，作用于单个 **.mdb** 或 **.accdb** 文件：**mdb-tables** 列出表，**mdb-schema** 打印 DDL，**mdb-export** 导出行数据，**mdb-sql** 运行查询，**mdb-count** 统计行数，**mdb-prop** 列出对象属性，**mdb-ver** 显示文件中的 Access 版本。

典型工作流是迁移（使用 **-I** _backend_ 将每张表导出为 CSV 或其他 RDBMS）和检查（从 **mdb-sql** 运行 SELECT）。该套件还附带 libmdb 库，GUI 工具和 **mdb-export** ODBC 驱动都在底层使用它。

# CAVEATS

**只读**：mdbtools 无法创建或修改 Access 数据库。某些高级特性（加密文件、特定索引类型、复杂的链接表、附件列、多值字段）仅部分支持或不支持。旧版本处理 .accdb 文件时表现不佳；**mdbtools 1.0**（2021 年）增加了可靠的 .accdb 支持，因此请务必使用较新的版本。

# HISTORY

**mdbtools** 由 **Brian Bruns** 于 **2000 年**启动，一度停滞，直到 **Evan Miller** 在 **2014 年**重启该项目。**2021 年**发布的 **1.0** 版本带来了最新的 .accdb 支持、打包好的 libmdb API 以及持续维护的 ODBC 驱动。

# INSTALL

```dnf: sudo dnf install mdbtools```

```zypper: sudo zypper install mdbtools```

```brew: brew install mdbtools```

```nix: nix profile install nixpkgs#mdbtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdb-sql](/man/mdb-sql)(1), [sqlite3](/man/sqlite3)(1), [csvtool](/man/csvtool)(1)
