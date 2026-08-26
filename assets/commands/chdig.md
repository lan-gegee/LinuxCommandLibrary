# TAGLINE

用于 ClickHouse 监控与调试的 TUI 工具

# TLDR

**连接**本地 ClickHouse 实例并显示正在运行的查询

```chdig```

**连接**远程 ClickHouse 主机

```chdig -u 'user:password@clickhouse-host.com/?secure=true'```

使用配置文件中的命名连接进行**连接**

```chdig --config [/path/to/config.yaml] --connection [prod]```

跨所有分片**监控** ClickHouse 集群

```chdig -u '[host]' --cluster [my_cluster]```

从查询日志中**显示**超过 1 秒的慢查询

```chdig slowqueries```

**显示**服务器日志

```chdig serverlogs```

**查看** MergeTree 合并

```chdig merges```

# SYNOPSIS

**chdig** [_OPTIONS_] [_SUBCOMMAND_]

# PARAMETERS

**-u**, **--url** _URL_
> 连接 URL。也会读取 **CHDIG_URL** 环境变量。

**--host** _HOST_
> 覆盖主机（与 clickhouse-client 兼容）。

**--port** _PORT_
> 覆盖端口。

**--user** _USER_
> 覆盖用户名。也会读取 **CLICKHOUSE_USER**。

**--password** _PASS_
> 覆盖密码。也会读取 **CLICKHOUSE_PASSWORD**。

**--secure**
> 使用 TLS/SSL。

**--config** _FILE_
> 类 ClickHouse 风格的配置文件（YAML）。

**-C**, **--connection** _NAME_
> 配置文件中的命名连接配置。

**-c**, **--cluster** _NAME_
> 集群名称；启用跨分片的分布式查询。

**--history**
> 使用 merge() 聚合历史系统日志数据。

**-d**, **--delay-interval** _MS_
> 刷新间隔，单位为毫秒（默认：30000）。

**-g**, **--group-by**
> 对分布式查询分组（集群模式下的默认行为）。

**-b**, **--start** _TIME_
> 时间区间起点（默认：1 小时前）。

**-e**, **--end** _TIME_
> 时间区间终点。

**--completion** _SHELL_
> 生成 Shell 补全脚本。

# VIEWS

**queries** (default), **lastqueries**, **slowqueries**, **merges**, **mutations**, **replicationqueue**, **replicatedfetches**, **replicas**, **tables**, **tableparts**, **errors**, **backups**, **dictionaries**, **serverlogs**, **loggers**, **partlog**, **asynchronousinserts**, **s3queue**, **azurequeue**, **client**

# DESCRIPTION

**chdig** 为 ClickHouse 提供交互式终端仪表盘，类似于 **top** 或 **htop** 之于 Linux 系统进程。它将 ClickHouse 庞大的系统内省表整合为一个可导航的 TUI，包含直接在终端中显示的火焰图（CPU、实时、内存）、用于分析查询计划和管道的 EXPLAIN 集成、跨所有分片聚合查询的集群模式，以及检查轮转系统日志表的历史模式。

# KEY BINDINGS

```
F1     Help               F2     Switch views
F8     Show actions        /     Filter
j/k    Navigate            r     Refresh
p      Pause/resume        C     CPU flamegraph
R      Real-time flamegraph M     Memory flamegraph
S      Display query       y     Copy query
K      Kill query          l     Show query logs
q/Esc  Back/quit           Q     Force quit
```

# CAVEATS

该项目自述为 **pre-alpha** 阶段；快捷键、视图和功能可能随时变更而不另行通知。需要 ClickHouse 21.2 或更新版本。鼠标模式默认启用，这会干扰标准的终端文本选择；请配合 Alt/Shift/Ctrl 修饰键选择文本。

# HISTORY

**chdig** 由 ClickHouse 的首席软件工程师 **Azat Khuzhin** 开发。使用 Rust 编写，采用 MIT 许可证。最新版本为 v26.2.3。目前有一项持续进行的工作是将 chdig 打包进 ClickHouse 本体。

# INSTALL

```brew: brew install chdig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [top](/man/top)(1)
