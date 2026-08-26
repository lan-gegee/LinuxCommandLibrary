# TAGLINE

运行 PostgreSQL 数据库服务器进程

# TLDR

**启动 PostgreSQL 服务器**

```postgres -D [/var/lib/postgresql/data]```

**以前台模式启动并记录日志**

```postgres -D [/var/lib/postgresql/data] -c log_statement=all```

**在特定端口上启动**

```postgres -D [/var/lib/postgresql/data] -p [5433]```

**以单用户模式启动**

```postgres --single -D [/var/lib/postgresql/data] [database]```

**显示版本**

```postgres --version```

# SYNOPSIS

**postgres** [_-D datadir_] [_-p port_] [_-c name=value_] [_options_]

# PARAMETERS

**-D** _DIR_
> 数据目录。

**-p** _PORT_
> 端口号。

**-c** _NAME=VALUE_
> 设置运行时参数。

**-h** _HOST_
> 监听地址。

**-k** _DIR_
> Unix 套接字目录。

**-l** _FILE_
> 将服务器日志输出发送到文件。

**-d** _LEVEL_
> 设置调试级别（1-5）；数值越大输出越多。

**-B** _BUFFERS_
> 共享缓冲区数量。

**-N** _N_
> 最大连接数。

**--single**
> 单用户模式。必须是命令行上的第一个参数。

**-e**
> 将所有命令回显到标准输出（单用户模式）。

**-F**
> 禁用 fsync 以加快运行（有数据损坏风险）。

**--describe-config**
> 描述配置参数并退出。

**--version**
> 显示版本。

# DESCRIPTION

**postgres** 是 PostgreSQL 数据库服务器进程。它管理数据库文件、处理连接并执行 SQL 查询。

服务器通常通过 pg_ctl 或系统服务管理器启动，而不是直接运行。直接调用适用于调试或非标准配置场景。

配置参数可以在命令行或 postgresql.conf 中设置。运行时参数控制内存、连接、日志和行为。

单用户模式绕过正常启动流程进行维护。当数据库无法正常启动时，它用于恢复操作。

数据目录包含所有数据库文件。首次使用前必须用 initdb 初始化，且不能跨主版本移植。

日志选项有助于诊断问题。语句日志记录所有 SQL。连接日志跟踪客户端访问。

# CONFIGURATION

**postgresql.conf**
> 数据目录中的主配置文件，控制内存分配、连接限制、日志、查询计划器设置、WAL 行为和复制。

**pg_hba.conf**
> 基于主机的身份验证文件，控制哪些用户可以通过哪些身份验证方式（trust、md5、scram-sha-256、cert）从哪些主机连接。

**pg_ident.conf**
> 面向外部身份验证系统的用户名映射文件，将操作系统用户名映射到 PostgreSQL 角色。

**PGDATA**
> 指定数据目录路径的环境变量，在未提供 **-D** 时作为默认值使用。

# CAVEATS

直接运行会绕过服务管理。数据目录必须保证安全。配置对性能影响很大。主版本升级需要 pg_upgrade。

# HISTORY

**PostgreSQL** 的开发始于 **1986 年**的 **UC Berkeley**，当时名为 POSTGRES（Post-Ingres）。开源的 PostgreSQL 项目始于 **1996 年**。它现在是最高级的开源数据库之一。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

```brew: brew install postgres```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_ctl](/man/pg_ctl)(1), [initdb](/man/initdb)(1), [psql](/man/psql)(1), [pg_dump](/man/pg_dump)(1), [pg_upgrade](/man/pg_upgrade)(1), [pg_isready](/man/pg_isready)(1)
