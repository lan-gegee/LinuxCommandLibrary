# TAGLINE

SQL Server 命令行查询工具

# TLDR

**连接本地** SQL Server

```sqlcmd -S [localhost] -U [sa] -P "[password]"```

**连接远程服务器**

```sqlcmd -S [server.example.com] -U [username] -P "[password]"```

**执行查询**后退出

```sqlcmd -S [server] -U [user] -P "[password]" -Q "SELECT @@VERSION"```

**执行 SQL 脚本文件**

```sqlcmd -S [server] -U [user] -P "[password]" -i [script.sql]```

**将结果输出到文件**

```sqlcmd -S [server] -U [user] -P "[password]" -Q "[query]" -o [output.txt]```

**使用 Windows 身份验证**连接

```sqlcmd -S [server] -E```

**以加密可选方式**连接

```sqlcmd -S [server] -U [user] -P "[password]" -No```

# SYNOPSIS

**sqlcmd** [**-S** _server_] [**-U** _login_] [**-P** _password_] [_options_]

# PARAMETERS

**-S** _server_
> 要连接的 SQL Server 实例。格式：[protocol:]server[\instance][,port]。

**-U** _login_
> 用户登录名。

**-P** _password_
> 登录密码。

**-E**
> 使用 Windows 身份验证（受信任连接）。

**-d** _database_
> 初始使用的数据库。

**-Q** _query_
> 执行查询并退出。

**-q** _query_
> 执行查询并进入交互模式。

**-i** _file_
> 包含 SQL 语句的输入文件。

**-o** _file_
> 结果的输出文件。

**-N** _mode_
> 加密模式：**o**（可选）、**m**（强制，SQL Server 2025 中的默认值）、**s**（strict/TDS 8.0）。

**-No**
> 加密可选（简写）。

**-C**
> 信任服务器证书。

**-t** _timeout_
> 查询超时时间，以秒为单位。

**-l** _timeout_
> 登录超时时间，以秒为单位。

**-h** _headers_
> 列标题之间间隔的行数（-1 表示禁用）。

**-s** _separator_
> 列分隔符字符。

**-w** _width_
> 输出的屏幕宽度。

**-A** _size_
> 请求不同大小的数据包。必须介于 512 和 32767 之间。

**-W**
> 移除列尾部的空格。

**-?**
> 显示 ODBC 版 sqlcmd 标志的帮助。

**--help**
> 显示 go-sqlcmd 子命令的帮助。

# DESCRIPTION

**sqlcmd** 是 Microsoft 针对 SQL Server 和 Azure SQL 的命令行工具。它支持以交互或批处理模式执行 Transact-SQL 语句、存储过程和 SQL 脚本。现有两种实现：较新的基于 Go 的版本（go-sqlcmd）和传统的基于 ODBC 的版本。

该工具支持多种身份验证方式，包括 SQL Server 身份验证、Windows/Kerberos 身份验证以及 Azure Active Directory。结果可以输出到终端、文件，或通过管道传给其他命令。

在交互模式下，**:quit** 命令退出会话，**GO** 执行语句批处理，**:r** 引入脚本文件。提示符会显示当前行号。

# CAVEATS

从 SQL Server 2025 开始，默认采用强制加密（**-Nm**），这是相对早期版本的破坏性变更。连接旧服务器时可使用 **-No** 将加密设为可选。命令行上的密码会在进程列表中可见；建议改用环境变量或交互式提示输入。Linux 上需要来自 Microsoft 软件仓库的 mssql-tools 软件包。

# HISTORY

**sqlcmd** 由 Microsoft 推出，用于取代较旧的 **osql** 和 **isql** 工具。基于 ODBC 的版本自 SQL Server 2005 起可用，并在 **2017 年** Linux 版 SQL Server 发布时被移植到 Linux。**2022 年**，Microsoft 发布了 go-sqlcmd——一个具备现代特性和跨平台支持的 Go 语言重实现。开发仍在继续，SQL Server 2025 加入了对 TDS 8.0 的支持。

# INSTALL

```brew: brew install sqlcmd```

```nix: nix profile install nixpkgs#sqlcmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [mysql](/man/mysql)(1)
