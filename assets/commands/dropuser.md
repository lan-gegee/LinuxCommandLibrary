# TAGLINE

PostgreSQL 用户删除工具

# TLDR

**删除用户**

```dropuser [username]```

**删除前确认**

```dropuser -i [username]```

在**远程主机上删除**

```dropuser -h [hostname] [username]```

以**指定的管理员用户**身份删除

```dropuser -U [admin_user] [username]```

**存在才删除**

```dropuser --if-exists [username]```

# SYNOPSIS

**dropuser** [_options_] _username_

# PARAMETERS

_USERNAME_
> 要删除的 PostgreSQL 角色/用户。

**-h**, **--host** _HOST_
> 服务器主机名。

**-p**, **--port** _PORT_
> 服务器端口。

**-U**, **--username** _USER_
> 以此用户身份连接。

**-i**, **--interactive**
> 删除前提示确认。

**--if-exists**
> 角色不存在时不报错。

**-e**, **--echo**
> 打印发送给服务器的 SQL 命令。

**-w**, **--no-password**
> 从不提示输入密码。脚本中很有用，此时密码必须来自 `~/.pgpass` 或环境变量。

**-W**, **--password**
> 强制提示输入密码。

**--maintenance-db**=_dbname_
> 为执行命令而连接的数据库。默认为 `postgres`。

**-V**, **--version**
> 打印版本并退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dropuser** 删除一个 PostgreSQL 角色。它是对 `DROP ROLE` SQL 语句的轻量封装，让你可以在 shell 中脚本化管理用户而不必调用 `psql`。

在 PostgreSQL 中，用户和组是同一个东西：**角色（role）**。`dropuser` 和 `createuser` 是为照顾习惯而保留的历史名称，"用户"与"角色"的区别仅在于角色是否具有 LOGIN 属性。

运行它需要你是超级用户，或持有 CREATEROLE 权限且被授予了所要删除角色的成员资格。

# CAVEATS

**角色仍拥有对象时无法删除。**PostgreSQL 会报出依赖错误并列出这些对象，解决办法是先重新指派或删除它们：

```REASSIGN OWNED BY [olduser] TO [newuser]```

```DROP OWNED BY [olduser]```

`DROP OWNED` 还会移除该角色对非其所有对象的权限，这是 `REASSIGN OWNED` 不会处理的。两条命令都必须在该角色拥有对象的**每个数据库**中运行，因为所有权是按数据库记录的，而 `dropuser` 只连接一个数据库。

删除角色不会终止其打开的会话，也不会触及你在其他尚未清理的数据库中的对象。此外，不能删除你当前连接所使用的角色。

# HISTORY

dropuser 是 PostgreSQL 最原始的一批客户端封装脚本之一，可以追溯到它们确实还是围绕 `psql` 的 shell 脚本的年代；如今它们已是 C 程序，但接口未变。这个名称早于 **PostgreSQL 8.1**（2005 年）将用户和组统一为角色的变革，所以工具名叫 `dropuser`，而它发出的 SQL 却是 `DROP ROLE`。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[createuser](/man/createuser)(1), [psql](/man/psql)(1), [dropdb](/man/dropdb)(1), [createdb](/man/createdb)(1)

# RESOURCES

```[Source code](https://git.postgresql.org/gitweb/?p=postgresql.git)```

```[Homepage](https://www.postgresql.org)```

```[Documentation](https://www.postgresql.org/docs/current/app-dropuser.html)```

<!-- verified: 2026-07-14 -->
