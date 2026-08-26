# TAGLINE

ODBC 命令行 SQL 客户端

# TLDR

**连接到数据源**

```isql [dsn_name]```

**使用凭据连接**

```isql [dsn_name] [username] [password]```

**连接时输出详细的错误信息**

```isql -v [dsn_name]```

**以批处理模式运行（无表头）**

```isql -b [dsn_name] < [query.sql]```

**使用自定义列分隔符**（逗号）

```isql -d, [dsn_name]```

**输出为 HTML 表格**

```isql -w [dsn_name]```

**使用带制表符分隔符的列头**（十六进制）

```isql -b -c -x0x09 [dsn_name]```

# SYNOPSIS

**isql** [_options_] _dsn_ [_user_] [_password_]

# PARAMETERS

_DSN_
> odbc.ini 中定义的数据源名称。

_USER_
> 数据库用户名。

_PASSWORD_
> 数据库密码。

**-v**
> 详细模式，输出完整的错误描述。

**-b**
> 批处理模式（无表头、无提示符）。

**-d** _DELIMITER_
> 列分隔符字符（如 -d, 表示逗号）。

**-x** _HEX_
> 以十六进制码指定的列分隔符（如 -x0x09 表示 TAB）。

**-c**
> 在第一行输出列名（与 -d 或 -x 配合使用）。

**-m** _NUM_
> 将列显示宽度限制为 NUM 个字符。

**-w**
> 将输出格式化为 HTML 表格。

**-n**
> 启用换行处理（以 GO 结尾的多行 SQL）。

**-e**
> 使用 SQLExecDirect 而不是 Prepare。

**-k**
> 使用 SQLDriverConnect（无 DSN 连接字符串）。

**-l** _LOCALE_
> 设置区域设置。

**-3**
> 使用 ODBC 3 调用。

**-L** _NUM_
> 每个字段的最大字符数（默认：300）。

**-q**
> 用双引号包裹字符字段。

**--version**
> 打印版本并退出。

# DESCRIPTION

**isql** 是 unixODBC 自带的 ODBC 命令行 SQL 客户端。它使用在 odbc.ini 中配置的 DSN 连接到任何具有 ODBC 驱动的数据库，并可交互式或从标准输入管道传入的脚本中执行 SQL 查询。

内置的运行时命令包括 `help`（列出表）、`help <table>`（列出列）以及退出会话的 `quit`。

# CAVEATS

需要 ODBC 驱动以及在 /etc/odbc.ini 或 ~/.odbc.ini 中配置好的 DSN。是 unixODBC 的一部分。

# HISTORY

isql 是 **unixODBC** 的一部分，通过开放数据库互连（Open Database Connectivity，ODBC）标准提供命令行数据库访问能力。

# INSTALL

```apt: sudo apt install unixodbc```

```pacman: sudo pacman -S unixodbc```

```apk: sudo apk add unixodbc```

```brew: brew install unixodbc```

```nix: nix profile install nixpkgs#unixodbc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [mysql](/man/mysql)(1), [sqlcmd](/man/sqlcmd)(1)
