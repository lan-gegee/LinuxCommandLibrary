# TAGLINE

在终端中查询和流式查看 CloudWatch 日志组。

# TLDR

实时**流式查看** CloudWatch 日志

```awslogs get [/aws/lambda/my-function] --watch```

从**指定时间**范围获取日志

```awslogs get [/aws/lambda/my-function] --start='[2h ago]'```

按模式**过滤**日志

```awslogs get [/aws/lambda/my-function] --filter-pattern '[ERROR]'```

列出可用的**日志组**

```awslogs groups```

列出日志组内的**日志流**

```awslogs streams [/aws/lambda/my-function]```

# SYNOPSIS

**awslogs** _command_ [_options_] _log-group_

# DESCRIPTION

**awslogs** 是一款用于查询和流式查看 AWS CloudWatch Logs 的命令行工具。它提供了简单的界面，可查看来自 Lambda 函数、EC2 实例、ECS 容器和其他 AWS 服务的日志。

该工具支持实时日志流式输出和基于时间的过滤，无需使用 AWS 控制台。

# PARAMETERS

**get** _log-group_ [_stream-expression_]
> 从日志组中获取与可选流表达式匹配的日志。

**groups**
> 列出可用的日志组。

**streams** _log-group_
> 列出某个日志组内的日志流。

**--watch**, **-w**
> 持续监视新生成的日志（实时流式输出）。

**--watch-interval**, **-i** _seconds_
> 配合 --watch 轮询新日志事件的时间间隔（秒）。

**--start** _time_, **-s** _time_
> 开始时间（如 '2h ago'、'2023-01-01'）。

**--end** _time_, **-e** _time_
> 结束时间。

**--filter-pattern** _pattern_, **-f** _pattern_
> CloudWatch Logs 过滤模式。

**--query** _query_, **-q** _query_
> 用于从 JSON 日志事件中提取字段的 JMESPath 风格查询。

**--timestamp**
> 打印每个事件的时间戳。

**--ingestion-time**
> 打印每个事件的摄取时间。

**--profile** _profile_
> 要使用的 AWS CLI profile。

**--aws-region** _region_
> AWS 区域（或设置 AWS_REGION 环境变量）。

**--no-group**, **-G**
> 不显示日志组名称。

**--no-stream**, **-S**
> 不显示日志流名称。

# TIME SPECIFICATIONS

- **2h ago** - 2 小时前
- **30m ago** - 30 分钟前
- **2d ago** - 2 天前
- **2023-01-01** - 具体日期
- **2023-01-01 10:30** - 具体日期时间

# CAVEATS

需要已配置 AWS 凭证。大范围的日志查询可能较慢。会产生 CloudWatch Logs 费用。时间规格采用 UTC。--watch 可能很快消耗大量 API 调用。

# HISTORY

**awslogs** 由 Jorge Bastida 于 **2015 年**前后创建，旨在相比官方 AWS CLI 提供更好的 CloudWatch Logs 命令行查看体验。

# INSTALL

```aur: yay -S awslogs```

```brew: brew install awslogs```

```nix: nix profile install nixpkgs#awslogs```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-logs](/man/aws-logs)(1), [tail](/man/tail)(1)

# RESOURCES

```[Source code](https://github.com/jorgebastida/awslogs)```

<!-- verified: 2026-06-18 -->
