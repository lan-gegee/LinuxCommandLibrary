# TAGLINE

跨平台 TUI 数据库管理工具

# TLDR

**使用默认配置启动 gobang**

```gobang```

**使用自定义配置文件启动**

```gobang -c [path/to/config.toml]```

**显示帮助**

```gobang -h```

# SYNOPSIS

**gobang** [_options_]

# PARAMETERS

**-c**, **--config-path** _PATH_
> 设置配置文件路径。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 显示版本并退出。

# DESCRIPTION

**gobang** 是一个用 Rust 编写的跨平台终端数据库管理工具，支持 MySQL、PostgreSQL 和 SQLite。它提供交互式 TUI，可用于浏览数据库、执行查询和管理表。

数据库连接在 TOML 配置文件中设置（默认：**~/.config/gobang/config.toml**）。该工具配有支持语法高亮的 SQL 编辑器，并以表格形式展示结果。

# KEYBINDINGS

**↑/↓**
> 在表/列之间导航

**Enter**
> 选择表 / 查看各列

**Tab**
> 在面板之间切换

**e**
> 编辑连接

**d**
> 删除记录

**q**
> 退出

**>**
> 打开查询编辑器

**?**
> 显示帮助

# CAVEATS

需要数据库凭据。过大的查询结果可能影响性能。部分特定于数据库的功能可能不受支持。

# HISTORY

**gobang** 的定位是通用的终端数据库客户端，类似于 DBeaver 等 GUI 工具，但运行在终端中。

# SEE ALSO

[psql](/man/psql)(1), [mysql](/man/mysql)(1), [litecli](/man/litecli)(1), [pgcli](/man/pgcli)(1)
