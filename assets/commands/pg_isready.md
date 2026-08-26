# TAGLINE

检查 PostgreSQL 服务器是否可以接受连接

# TLDR

**检查服务器是否就绪**

```pg_isready```

**检查特定主机**

```pg_isready -h [host] -p [port]```

**带超时的检查**

```pg_isready -t [seconds]```

**安静模式**

```pg_isready -q```

# SYNOPSIS

**pg_isready** [_options_]

# PARAMETERS

**-h**, **--host** _host_
> 服务器主机名。

**-p**, **--port** _port_
> 服务器端口。

**-t**, **--timeout** _seconds_
> 连接超时时间。

**-q**, **--quiet**
> 抑制输出。

**-d**, **--dbname** _name_
> 数据库名称。

# DESCRIPTION

**pg_isready** 检查 PostgreSQL 服务器是否已准备好接受连接。返回表示服务器状态的退出码。适合脚本使用，也可在连接前做健康检查。

# INSTALL

```apk: sudo apk add postgresql17-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[psql](/man/psql)(1), [pg_ctl](/man/pg_ctl)(1)
