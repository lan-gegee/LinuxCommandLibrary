# TAGLINE

打开 Rails 应用的数据库控制台

# TLDR

**打开数据库控制台**连接当前环境

```rails db```

**打开数据库控制台**连接生产环境

```rails db -e production```

**使用指定的数据库配置打开数据库控制台**

```rails db --database=[database_name]```

# SYNOPSIS

**rails db** [**-e** _environment_] [**--database** _name_] [**-h**]

# PARAMETERS

**-e**, **--environment** _ENV_
> 指定 Rails 环境（development、test、production）

**--database** _name_
> 配置了多个数据库时连接指定的数据库

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**rails db**（也称为 **rails dbconsole**）会打开一个交互式会话，连接为 Rails 应用配置的数据库。它会自动检测数据库适配器并启动相应的客户端（PostgreSQL 用 psql、MySQL 用 mysql、SQLite 用 sqlite3 等）。

该命令从 **config/database.yml** 读取数据库配置，并使用其中指定的凭据和连接信息进行连接。无需手动记忆连接字符串即可快速访问数据库。

# CAVEATS

需要系统上已安装相应的数据库客户端（psql、mysql、sqlite3 等）。如果客户端不在 PATH 中，命令将失败。

数据库凭据从配置文件读取。请确保敏感凭据得到妥善保护，尤其是在生产环境中。

# SEE ALSO

[rails](/man/rails)(1), [rails-console](/man/rails-console)(1), [psql](/man/psql)(1), [mysql](/man/mysql)(1), [sqlite3](/man/sqlite3)(1)
