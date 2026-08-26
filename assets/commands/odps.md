# TAGLINE

阿里云 MaxCompute（ODPS）的命令行客户端

# TLDR

**启动交互式客户端**

```odps```

**执行单条 SQL 语句**

```odps -e "[SELECT * FROM table LIMIT 10;]"```

**运行 SQL 脚本文件**

```odps -f [query.sql]```

**指定目标项目**和端点

```odps --project [my_project] --endpoint [https://service.cn-shanghai.maxcompute.aliyun.com/api]```

**将输出格式设置为 CSV**

```odps -e "[SELECT * FROM table;]" --format csv```

# SYNOPSIS

**odps** [_options_]

# PARAMETERS

**-e** _SQL_
> 执行单条语句后退出。多条语句可用分号分隔。

**-f** _FILE_
> 执行从 _FILE_ 读取的 SQL 脚本。

**--project** _NAME_
> 本次会话使用的 MaxCompute 项目。覆盖 **odps_config.ini** 中的值。

**--endpoint** _URL_
> MaxCompute 服务端点 URL。未在配置文件中设置时必须提供。

**--access-id** _ID_
> 阿里云 Access Key ID。默认从 **odps_config.ini** 读取。

**--access-key** _KEY_
> 阿里云 Access Key Secret。

**--format** _FORMAT_
> 输出格式：text（默认）、csv、json。

**-r**, **--retry** _N_
> 失败网络调用的重试次数。

**--help**
> 显示用法信息。

# DESCRIPTION

**odps** 是阿里云 MaxCompute 服务（原名 Open Data Processing Service，简称 ODPS）的官方命令行客户端。它会针对某个 MaxCompute 项目打开一个交互式 SQL 提示符，用户可以在其中运行 SQL 查询，管理表、分区、资源和函数，并提交 MapReduce 或 Spark 作业。

该客户端也支持非交互式使用：通过 **-e** 执行一次性语句，通过 **-f** 执行 SQL 文件，这是定时流水线中的常见模式。客户端从 **conf/odps_config.ini** 读取端点 URL 和凭证，因此同一个程序可以通过更换配置文件来访问多个地域。

# CAVEATS

需要拥有目标 MaxCompute 项目权限的有效阿里云 Access Key 对。每条语句都会消耗计费的计算和存储资源。端点 URL 与地域绑定；通常不允许跨地域访问。由于客户端是封装在 shell 脚本中的 Java JAR，需要 Java 8 或更高版本。

# HISTORY

MaxCompute 服务最初作为 **ODPS** 在阿里巴巴内部基础设施中运行，约于 **2014** 年向公有云客户开放。即使服务更名为 MaxCompute 之后，客户端仍保留了 **odps** 这个名字，因此旧脚本和文档中两种名称经常混用。

# SEE ALSO

[odpscmd](/man/odpscmd)(1), [odps-tunnel](/man/odps-tunnel)(1)
