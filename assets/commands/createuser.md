# TAGLINE

PostgreSQL 用户创建工具

# TLDR

**交互式创建用户**

```createuser [username]```

**创建超级用户**

```createuser -s [username]```

**创建用户并提示输入密码**

```createuser -P [username]```

**创建可以创建数据库的用户**

```createuser -d [username]```

**携带连接选项创建用户**

```createuser -h [localhost] -p [5432] -U [admin] [username]```

**创建可以创建角色的用户**

```createuser -r [username]```

**创建没有登录权限的用户（仅作为角色）**

```createuser --no-login [rolename]```

# SYNOPSIS

**createuser** [_options_] [_username_]

# DESCRIPTION

**createuser** 是一个 PostgreSQL 实用工具，用于创建新的数据库用户（角色）。它是对 SQL CREATE ROLE 命令的封装，提供便捷的命令行接口。

该工具能够创建具有各种权限的用户，包括超级用户身份、创建数据库的权利以及创建角色的能力。它会连接数据库服务器并执行相应的 SQL。

# PARAMETERS

**-s**, **--superuser**
> 创建超级用户。

**-d**, **--createdb**
> 允许创建数据库。

**-r**, **--createrole**
> 允许创建角色。

**-l**, **--login**
> 允许登录（默认）。

**-P**, **--pwprompt**
> 提示输入密码。

**-e**, **--echo**
> 显示生成的 SQL。

**-h** _host_
> 数据库服务器主机。

**-p** _port_
> 数据库服务器端口。

**-U** _user_
> 以指定用户身份连接。

**-W**
> 强制提示输入密码。

**-i**, **--inherit**
> 角色继承权限（默认）。

**--no-inherit**
> 角色不继承其所属角色的权限。

**--interactive**
> 交互式询问缺失的角色属性。

**--no-login**
> 角色不能登录（适用于组角色）。

**--replication**
> 允许复制连接。

**--no-replication**
> 角色不能发起复制（默认）。

**--bypassrls**
> 允许角色绕过行级安全策略。

**--connection-limit** _n_
> 该角色的最大并发连接数（-1 表示不限制）。

**-V**, **--version**
> 打印版本并退出。

# CAVEATS

创建角色需要相应的权限。创建超级用户要求以超级用户身份连接。通过 -P 设置密码时采用交互式输入。

# HISTORY

**createuser** 自早期版本起就是 PostgreSQL 的一部分，为角色管理提供了 Shell 接口。PostgreSQL 源于 **UC Berkeley** 在 **1980 年代**开展的 **POSTGRES** 项目。用户与角色的区分在 PostgreSQL 8.1 中被统一。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dropuser](/man/dropuser)(1), [psql](/man/psql)(1), [createdb](/man/createdb)(1), [dropdb](/man/dropdb)(1), [pg_dump](/man/pg_dump)(1), [pg_restore](/man/pg_restore)(1)
