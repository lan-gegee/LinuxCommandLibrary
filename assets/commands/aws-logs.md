# TAGLINE

管理 CloudWatch 日志组、日志流和查询。

# TLDR

**列出所有日志组**

```aws logs describe-log-groups```

**列出**日志组中的**日志流**

```aws logs describe-log-streams --log-group-name [/aws/lambda/function-name]```

从日志流中**获取日志事件**

```aws logs get-log-events --log-group-name [group_name] --log-stream-name [stream_name]```

实时**跟踪日志**

```aws logs tail [/aws/lambda/function-name] --follow```

从最近 10 分钟开始**跟踪日志**

```aws logs tail [/aws/lambda/function-name] --since [10m]```

用模式**过滤日志**

```aws logs filter-log-events --log-group-name [group_name] --filter-pattern "[ERROR]"```

**创建日志组**

```aws logs create-log-group --log-group-name [group_name]```

为日志组**设置保留策略**

```aws logs put-retention-policy --log-group-name [group_name] --retention-in-days [30]```

**删除日志组**

```aws logs delete-log-group --log-group-name [group_name]```

# SYNOPSIS

**aws logs** _subcommand_ [_options_]

# DESCRIPTION

**aws logs** 是 AWS CLI 的一个子命令，用于管理 Amazon CloudWatch Logs。这是一项用于监控、存储以及访问来自 AWS 资源和应用程序的日志文件的服务。

日志按日志组（容器）和日志流（来自单一来源的事件序列）进行组织。日志事件包含时间戳和原始消息。许多 AWS 服务（如 Lambda、ECS 和 API Gateway）会自动将日志发送到 CloudWatch。

CloudWatch Logs Insights 支持以类似 SQL 的方式查询日志数据。指标过滤器可以从日志模式中提取指标。订阅过滤器可将日志实时流式传输到 Lambda、Kinesis 或 Firehose。

# PARAMETERS

**describe-log-groups**
> 列出日志组及其元数据。

**create-log-group**
> 创建新的日志组。

**delete-log-group**
> 删除日志组及其所有数据。

**describe-log-streams**
> 列出日志组中的日志流。

**get-log-events**
> 从日志流中获取日志事件。

**filter-log-events**
> 用过滤模式搜索日志。

**tail**
> 实时流式输出日志（类似 tail -f）。

**put-log-events**
> 向日志流发送日志事件。

**put-retention-policy**
> 设置日志过期期限。

**delete-retention-policy**
> 将日志设为永不过期。

**put-metric-filter**
> 创建指标过滤器。

**put-subscription-filter**
> 将日志流式传输到其他服务。

**start-query**
> 运行 CloudWatch Logs Insights 查询；返回查询 ID。

**get-query-results**
> 获取由 start-query 启动的查询的结果。

**--log-group-name** _name_
> 日志组的名称。

**--log-stream-name** _name_
> 日志流的名称。

**--filter-pattern** _pattern_
> 用于匹配日志事件的模式。

**--start-time** _timestamp_
> 开始时间，以自纪元以来的毫秒数表示。

**--end-time** _timestamp_
> 结束时间，以自纪元以来的毫秒数表示。

**--follow**
> 持续流式输出新日志（tail 命令）。

**--since** _time_
> 从相对时间（如 5m、2h 或 1d）或绝对时间戳开始 tail。

**--retention-in-days** _days_
> 保留期限（1、3、5、7、14、30、60、90、120、150、180、365、400、545、731、1096、1827、2192、2557、2922、3288、3653 天或不限）。

# CAVEATS

日志组没有默认保留策略；除非另行配置，日志会永久保留。tail 命令需要 aws-cli v2。过滤模式的语法较为特殊，与正则表达式不同。存储的日志数据会根据摄取量和存储量产生费用。跨账户日志共享需要订阅过滤器和目标策略。

# HISTORY

**Amazon CloudWatch Logs** 于 **2014 年 7 月**上线，是 CloudWatch 监控功能的扩展，最初通过 CloudWatch 代理支持 EC2 日志。**CloudWatch Logs Insights** 在 **re:Invent 2018** 上发布，用于交互式日志分析。**Live Tail** 于 **2023 年**推出，支持在控制台中实时流式查看日志。该服务已扩展到能够处理几乎所有 AWS 服务的日志。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-cloudwatch](/man/aws-cloudwatch)(1), [journalctl](/man/journalctl)(1), [tail](/man/tail)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/logs/index.html)```

<!-- verified: 2026-06-18 -->
