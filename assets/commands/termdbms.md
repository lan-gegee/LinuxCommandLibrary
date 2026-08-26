# TAGLINE

用于查看和编辑数据库文件的 TUI

# TLDR

**打开 SQLite 数据库**

```termdbms [mydata.db]```

**将 CSV 文件转换为 SQLite 并打开**

```termdbms --csv [data.csv]```

**连接 MySQL 数据库**

```termdbms --url "[mysql://user:pass@host/db]"```

# SYNOPSIS

**termdbms** [_options_] [_database-file_]

# PARAMETERS

**--csv** _FILE_
> 将 CSV 文件转换为 SQLite 并打开。

**--url** _URL_
> 通过 URL 连接 MySQL 数据库。

# DESCRIPTION

**termdbms** 是一个用于查看和编辑 SQLite 与 MySQL 数据库的终端 UI。它支持带撤销/重做的 SQL 查询、CSV 到 SQLite 的转换、CSV/SQLite 导出，以及选择模式下对 JSON 的自动格式化。

# HISTORY

**termdbms** 由 **mathaou** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#termdbms```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[litecli](/man/litecli)(1), [harlequin](/man/harlequin)(1), [sqlit](/man/sqlit)(1)
