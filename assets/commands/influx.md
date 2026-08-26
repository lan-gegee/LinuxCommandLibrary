# TAGLINE

InfluxDB 时序数据库的命令行界面

# TLDR

**启动交互式 Shell**

```influx```

**连接到主机**

```influx -host [hostname] -port [8086]```

**执行查询**

```influx -execute "[SELECT * FROM measurement]"```

**使用指定数据库**

```influx -database [mydb]```

**导入数据**

```influx -import -path [data.txt]```

**执行查询**并以 JSON 输出

```influx -database [mydb] -execute "[SELECT * FROM measurement]" -format json```

**进行身份验证**

```influx -username [user] -password [pass]```

# SYNOPSIS

**influx** [_options_]

# PARAMETERS

**-host** _HOST_
> InfluxDB 服务器主机名。

**-port** _PORT_
> 服务器端口（默认 8086）。

**-database** _DB_
> 要使用的数据库。

**-execute** _QUERY_
> 执行查询并退出。

**-import**
> 从文件导入数据。

**-path** _FILE_
> 导入用的文件路径。

**-username** _USER_
> 身份验证用户名。

**-password** _PASS_
> 身份验证密码。

**-precision** _UNIT_
> 时间戳精度（ns、u、ms、s、m、h）。

**-ssl**
> 使用 HTTPS 发送请求。

**-format** _FORMAT_
> 输出格式：column、csv、json（默认：column）。

**-type** _TYPE_
> 查询类型：influxql 或 flux。

**--help**
> 显示帮助信息。

# DESCRIPTION

**influx** 是 InfluxDB 时序数据库的命令行界面，提供一个交互式 Shell 用于查询和管理数据。

v1 CLI 使用直接连接标志（-host、-port、-username），支持 InfluxQL。v2 CLI 是一个独立的工具，采用基于令牌的身份验证和配置 profile，同时支持 InfluxQL 和 Flux 查询语言。本文档介绍的选项适用于 v1 CLI。

# CAVEATS

InfluxDB 必须处于运行状态。可能需要进行身份验证。InfluxQL 语法与 SQL 不同。

# HISTORY

influx 是 **InfluxDB** 的一部分，由 **InfluxData** 创建，是一个开源时序数据库平台。

# INSTALL

```apt: sudo apt install influxdb-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grafana-cli](/man/grafana-cli)(1), [mysql](/man/mysql)(1), [psql](/man/psql)(1)
