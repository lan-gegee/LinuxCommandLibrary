# TAGLINE

跨平台 TUI 数据库管理工具

# TLDR

**启动数据库 TUI**

```lazysql```

**连接到数据库**

```lazysql -u [connection_string]```

# SYNOPSIS

**lazysql** [_options_]

# DESCRIPTION

**lazysql** 是一款跨平台的 TUI 数据库管理工具，支持 MySQL、PostgreSQL 和 SQLite。它提供带语法高亮的 SQL 查询编辑器、剪贴板支持、基于标签页的导航以及 Vim 风格的按键绑定。

功能包括交互式查询编辑器、可排序的结果表格、便于复制查询结果或单元格值的剪贴板集成，以及一个友好的界面——无需离开终端即可浏览数据库 schema 并执行查询。

# CAVEATS

连接 MySQL 和 PostgreSQL 需要有正在运行的数据库服务器。SQLite 直接使用本地文件。

# HISTORY

**lazysql** 由 **Jorge Rojas**（jorgerojas26）创建，使用 **Go** 编写，其灵感来自 lazygit。

# INSTALL

```brew: brew install lazysql```

```nix: nix profile install nixpkgs#lazysql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mysql](/man/mysql)(1), [psql](/man/psql)(1), [sqlite3](/man/sqlite3)(1)
