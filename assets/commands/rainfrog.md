# TAGLINE

轻量级终端数据库管理 TUI

# TLDR

**连接 PostgreSQL 数据库**

```rainfrog --url postgres://[user]:[password]@[host]/[database]```

**连接 MySQL 数据库**

```rainfrog --url mysql://[user]:[password]@[host]/[database]```

**连接 SQLite 数据库**

```rainfrog --url sqlite://[path/to/db.sqlite]```

**使用指定驱动连接**

```rainfrog --url [connection_string] --driver [postgres]```

# SYNOPSIS

**rainfrog** [_options_]

# PARAMETERS

**--url** _CONNECTION_STRING_
> 数据库连接字符串。

**--driver** _DRIVER_
> 要使用的数据库驱动（postgres、mysql、sqlite）。

**--username** _USER_
> 数据库用户名。

**--password** _PASS_
> 数据库密码。

**--host** _HOST_
> 数据库主机。

**--port** _PORT_
> 数据库端口。

**--database** _NAME_
> 数据库名称。

# DESCRIPTION

**rainfrog** 是一个轻量级的基于终端的数据库管理工具，定位为 pgAdmin 和 DBeaver 的替代品。它具有类 vim 的按键绑定、带关键字高亮的查询编辑器、会话历史、收藏夹，以及快速复制数据、筛选表和在 schema 之间切换等功能。支持 PostgreSQL、MySQL 和 SQLite。

# CAVEATS

仍在积极开发中，可能出现破坏性变更。不建议用于生产数据库的写操作。密码中含特殊字符的连接字符串可能需要进行 URL 编码。

# HISTORY

**rainfrog** 由 **achristmascarl** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S rainfrog```

```brew: brew install rainfrog```

```nix: nix profile install nixpkgs#rainfrog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [lazysql](/man/lazysql)(1), [mycli](/man/mycli)(1)
