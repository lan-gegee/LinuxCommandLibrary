# TAGLINE

Prometheus 配置与查询工具

# TLDR

**检查 Prometheus 配置语法**

```promtool check config [prometheus.yml]```

**检查告警规则**

```promtool check rules [rules.yml]```

**测试告警规则**

```promtool test rules [test.yml]```

**查询 Prometheus 指标**

```promtool query instant [http://localhost:9090] "[up]"```

**查询指标范围**

```promtool query range [http://localhost:9090] "[up]" --start [1h]```

**校验指标暴露格式**

```curl -s [http://localhost:9100/metrics] | promtool check metrics```

**调试指标解析**

```promtool debug metrics [http://localhost:9090]```

# SYNOPSIS

**promtool** _command_ _subcommand_ [_options_] [_arguments_]

# PARAMETERS

**check config** _FILE_
> 校验 Prometheus 配置文件。

**check rules** _FILES_
> 校验告警/记录规则。

**check metrics**
> 从 stdin 校验指标格式。

**test rules** _FILES_
> 对告警规则进行单元测试。

**query instant** _SERVER_ _QUERY_
> 执行即时查询。

**query range** _SERVER_ _QUERY_
> 执行范围查询。

**query labels** _SERVER_ _LABEL_
> 查询标签值。

**query series** _SERVER_ _MATCH_
> 查询时间序列。

**debug pprof** _TYPE_
> 获取调试剖析数据。

**debug metrics** _SERVER_
> 调试指标端点。

**debug all** _SERVER_
> 获取全部调试信息。

**tsdb** _subcommand_
> TSDB 数据库操作（`analyze`、`dump`、`create-blocks-from`、`list`、`bench write`）。

**check service-discovery** _FILE_ _JOB_
> 校验服务发现配置。

**check web-config** _FILE_
> 校验 Prometheus Web / TLS 配置。

**push metrics** _URL_ _FILE_
> 将一个 Prometheus 暴露格式文件推送到指定的 remote write 端点。

**--start** _TIME_
> 查询起始时间。

**--end** _TIME_
> 查询结束时间。

**--step** _DURATION_
> 查询步长间隔。

# DESCRIPTION

**promtool** 是 Prometheus（流行的监控和告警系统）的命令行工具，用于校验配置、测试规则和查询指标。

配置检查能在应用更改之前捕获语法错误和无效设置，避免 Prometheus 因配置问题而无法启动。

规则校验确保告警和记录规则在语法上正确。结合单元测试（test rules），可以在部署前验证告警行为。测试文件指定样本数据和预期的告警状态。

查询命令对运行中的 Prometheus 服务器执行 PromQL 查询。即时查询返回当前值；范围查询返回时间序列数据。这使得围绕 Prometheus 数据的脚本化和自动化成为可能。

tsdb 子命令提供直接的 TSDB（时间序列数据库）操作：分析、基准测试和维护存储层。

# CAVEATS

需要具备 Prometheus 相关知识才能有效使用。查询命令需要运行中的 Prometheus 服务器。规则测试需要精心构造测试数据。某些命令会访问远程服务器。输出格式因命令而异。

# HISTORY

**promtool** 是 **Prometheus** 的一部分。Prometheus 由 Matt T. Proud 和 Julius Volz 于 **2012 年**前后在 **SoundCloud** 创建，于 **2015 年**开源，并在 **2016 年**加入 CNCF。promtool 随 Prometheus 一同演进，为配置管理和故障排查提供运维工具。

# INSTALL

```apt: sudo apt install promtool```

```dnf: sudo dnf install prometheus```

```pacman: sudo pacman -S prometheus```

```apk: sudo apk add prometheus```

```brew: brew install prometheus```

```nix: nix profile install nixpkgs#prometheus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prometheus](/man/prometheus)(1), [alertmanager](/man/alertmanager)(1), [grafana](/man/grafana)(1)
