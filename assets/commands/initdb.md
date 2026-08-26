# TAGLINE

创建新的 PostgreSQL 数据库簇

# TLDR

**初始化 PostgreSQL 数据库簇**

```initdb -D [/var/lib/postgresql/data]```

**以指定编码初始化**

```initdb -D [/var/lib/postgresql/data] -E UTF8```

**以指定 locale 初始化**

```initdb -D [/var/lib/postgresql/data] --locale=[en_US.UTF-8]```

**带身份验证初始化**

```initdb -D [/var/lib/postgresql/data] -A [scram-sha-256] -W```

**以指定用户初始化**

```initdb -D [/var/lib/postgresql/data] -U [postgres]```

# SYNOPSIS

**initdb** [_options_] **-D** _directory_

# PARAMETERS

**-D**, **--pgdata** _dir_
> 数据目录位置。

**-E**, **--encoding** _encoding_
> 默认数据库编码。

**--locale** _locale_
> 默认 locale。

**-U**, **--username** _user_
> 数据库超级用户名。

**-W**, **--pwprompt**
> 提示输入超级用户密码。

**-A**, **--auth** _method_
> 身份验证方法。

**--auth-local** _method_
> 本地连接的身份验证方法。

**--auth-host** _method_
> 主机连接的身份验证方法。

**-k**, **--data-checksums**
> 启用数据校验和。

**--wal-segsize** _size_
> WAL 段大小。

# DESCRIPTION

**initdb** 创建一个新的 PostgreSQL 数据库簇。簇是由单个 PostgreSQL 服务器实例管理的数据库集合，存储在一个数据目录中。

首次启动 PostgreSQL 之前必须先运行此命令。它会创建模板数据库、配置文件和目录结构。

# CAVEATS

必须以 PostgreSQL 用户身份运行。目录必须为空或不存在。编码和 locale 会影响所有数据库。数据校验和一旦启用便无法事后更改。

# HISTORY

initdb 是 PostgreSQL 的一部分，自 **1996 年**起由 PostgreSQL Global Development Group 开发。它起源于加州大学伯克利分校的 POSTGRES 项目。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_ctl](/man/pg_ctl)(1), [postgres](/man/postgres)(1), [createdb](/man/createdb)(1)
