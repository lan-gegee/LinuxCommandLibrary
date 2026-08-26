# TAGLINE

带自动补全的 SQLite CLI

# TLDR

**连接数据库**

```litecli [database.db]```

**创建新数据库**

```litecli [new.db]```

**执行查询**

```litecli [database.db] -e "[SELECT * FROM table]"```

**使用特定输出格式**

```litecli [database.db] --table```

**连接内存数据库**

```litecli :memory:```

**运行 SQL 文件**

```litecli [database.db] < [script.sql]```

# SYNOPSIS

**litecli** [_options_] [_database_]

# PARAMETERS

_DATABASE_
> SQLite 数据库文件路径。

**-e**, **--execute** _QUERY_
> 执行查询后退出。

**--table**
> 以表格格式输出。

**--csv**
> 以 CSV 格式输出。

**--auto-vertical-output**
> 宽行时自动切换为垂直输出。

**-l**, **--list-dsn**
> 列出已配置的 DSN。

**--llm-api-key** _KEY_
> 用于 AI 辅助 SQL 功能的 API 密钥。

**--help**
> 显示帮助信息。

# DESCRIPTION

**litecli** 是一个带自动补全的 SQLite CLI。它提供语法高亮和智能建议。

相比 sqlite3，该工具凭借多行编辑和历史记录提供了更好的交互体验。

# CAVEATS

基于 Python。需要 pip 安装。仅适用于 SQLite 数据库。

# HISTORY

litecli 受 **pgcli** 和 **mycli** 启发，为 SQLite 带来了类似的增强 CLI 特性。

# INSTALL

```dnf: sudo dnf install litecli```

```apk: sudo apk add litecli```

```brew: brew install litecli```

```nix: nix profile install nixpkgs#litecli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [mycli](/man/mycli)(1), [pgcli](/man/pgcli)(1)
