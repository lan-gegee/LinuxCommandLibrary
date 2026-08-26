# TAGLINE

校验并测试 Elasticsearch cron 表达式

# TLDR

**求值一个 cron 表达式**（每天中午触发）

```elasticsearch-croneval "[0 0 12 * * ?]"```

**显示接下来的 N 次触发时间**

```elasticsearch-croneval -c [20] "[0 0/5 * * * ?]"```

求值一个在**工作日早晨**触发的表达式

```elasticsearch-croneval "[0 30 9 ? * MON-FRI]"```

当表达式被拒绝时**显示堆栈跟踪**

```elasticsearch-croneval -d "[0 0 12 * *]"```

# SYNOPSIS

**elasticsearch-croneval** _expression_ [**-c**|**--count** _count_] [**-d**|**--detail**] [**-s**|**--silent**] [**-v**|**--verbose**]

# PARAMETERS

_expression_
> 要求值的 cron 表达式。请加引号，因为它含有对 shell 有特殊意义的字符。

**-c**, **--count** _number_
> 要打印的未来触发时间数量。默认为 10。

**-d**, **--detail**
> 显示无效表达式的详细信息，解析失败时打印堆栈跟踪。

**-s**, **--silent**
> 显示最少输出。

**-v**, **--verbose**
> 显示详细输出。

**-h**, **--help**
> 显示命令参数。

# DESCRIPTION

**elasticsearch-croneval** 校验 Elasticsearch cron 表达式并打印其接下来的触发时间。这是把 Watcher 计划、快照生命周期策略或 ILM 滚动计划写入集群之前进行验证的最快方式。

该工具位于 $ES_HOME/bin 中，可离线运行：不需要正在运行的集群。

# CRON FORMAT

Elasticsearch cron 表达式采用 Quartz 风格，包含六到七个字段，而不是 Unix cron 的五个。秒在最前，年份可选。

```
<seconds> <minutes> <hours> <day_of_month> <month> <day_of_week> [year]
```

_day_of_month_ 和 _day_of_week_ 必须恰好有一个为 **?**（"不指定具体值"），因为二者不能同时受限。因此 crontab 表达式 `0 12 * * *` 在这里要写成 `0 0 12 * * ?`。

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [crontab](/man/crontab)(5)

# RESOURCES

```[Source code](https://github.com/elastic/elasticsearch)```

```[Homepage](https://www.elastic.co/elasticsearch)```

```[Documentation](https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/elasticsearch-croneval)```

<!-- verified: 2026-07-14 -->
