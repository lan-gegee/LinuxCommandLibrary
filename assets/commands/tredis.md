# TAGLINE

用于查看和管理 Redis 数据的终端界面

# TLDR

启动 Redis TUI

```tredis```

连接到特定的 Redis 服务器

```tredis --host [localhost] --port [6379]```

连接到特定的数据库

```tredis --host [localhost] --port [6379] --db [2]```

# SYNOPSIS

**tredis** [_options_]

# DESCRIPTION

**tredis** 是一个基于终端的 Redis 数据查看与管理工具，是传统 redis-cli 的现代 TUI 替代品。它让你通过直观的终端界面浏览、查看和管理 Redis 数据。

# HISTORY

**tredis** 由 **Huseyin Babal**（huseyinbabal）创建，使用 **Rust** 编写。

# SEE ALSO

[redis-cli](/man/redis-cli)(1)
