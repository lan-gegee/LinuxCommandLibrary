# TAGLINE

连接 Microsoft SQL Server 数据库以执行查询和数据库操作

# TLDR

**连接 MSSQL 服务器**

```impacket-mssqlclient [domain]/[user]:[password]@[target]```

**使用 Windows 身份验证连接**

```impacket-mssqlclient -windows-auth [domain]/[user]:[password]@[target]```

**指定端口**

```impacket-mssqlclient -port [1433] [user]:[password]@[target]```

**执行查询**

```impacket-mssqlclient [user]:[password]@[target] -q "[SELECT @@version]"```

# SYNOPSIS

**impacket-mssqlclient** [_options_] _target_

# PARAMETERS

**-windows-auth**
> 使用 Windows 身份验证。

**-port** _port_
> SQL Server 端口（默认 1433）。

**-q** _query_
> 执行查询后退出。

**-file** _file_
> 执行文件中的 SQL。

**-hashes** _lm:nt_
> 使用 NTLM 哈希。

# DESCRIPTION

**impacket-mssqlclient** 连接 Microsoft SQL Server 数据库，用于执行查询和数据库操作。属于 Impacket 工具集。支持 SQL 和 Windows 身份验证。交互模式提供 SQL shell，可执行 xp_cmdshell 等命令。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sqlcmd](/man/sqlcmd)(1), [impacket-psexec](/man/impacket-psexec)(1)
