# TAGLINE

为智能体用法优化的 Grafana Cloud CLI

# TLDR

**通过浏览器 OAuth 认证**到 Grafana Cloud 或本地部署实例

```gcx auth login --server [https://myorg.grafana.net]```

**运行 PromQL** 指标查询，查询最近一小时的数据

```gcx metrics query '[rate(http_requests_total[5m])]' --since [1h]```

**对 Loki 运行 LogQL** 日志查询

```gcx logs query '[{app="api"} |= "error"]' --since [30m]```

**列出当前正在告警的告警规则**

```gcx alert rules list --state [firing]```

**导出仪表盘和文件夹**到本地 YAML 文件

```gcx resources pull -p [./resources] -o [yaml]```

**校验并将**本地资源推送回 Grafana

```gcx resources push -p [./resources] --on-error [abort]```

**列出服务级别目标**

```gcx slo definitions list```

**向 Grafana Assistant 提问**

```gcx assistant prompt "[why is latency high on checkout?]"```

**生成 Shell 补全**

```gcx completion [bash]```

# SYNOPSIS

**gcx** _command_ [_subcommand_] [_options_] [_args_]

# PARAMETERS

**auth login** **--server** _URL_
> 通过浏览器发起对 Grafana 实例的 OAuth 登录。

**config set** _key value_
> 设置配置值（例如 **contexts.my-grafana.grafana.token**）。

**config use-context** _name_
> 切换当前活动的配置上下文。

**config check**
> 校验当前的身份验证和连接状态。

**metrics query** _PROMQL_
> 对 Prometheus / Mimir 执行 PromQL 查询。

**logs query** _LOGQL_
> 对 Loki 执行 LogQL 查询。

**traces query** _QUERY_
> 从 Tempo 查询链路追踪数据。

**profiles query** _QUERY_
> 从 Pyroscope 查询性能剖析数据。

**alert rules list** [**--state** _STATE_]
> 显示告警规则及其状态、健康度和暂停情况。

**alert groups list**
> 显示告警组。

**resources pull** [**-p** _DIR_] [**-o** _FORMAT_]
> 将仪表盘、文件夹及其他资源导出为本地文件。

**resources push** [**-p** _DIR_] [**--dry-run**] [**--on-error** _MODE_]
> 将本地资源部署回 Grafana。

**resources delete**, **edit**, **validate**, **get**
> 管理资源：删除、交互式修改、检查或列出。

**slo definitions list**, **slo reports list**
> 管理服务级别目标。

**synth checks list**, **synth probes list**
> 合成监控的检查项与探测点。

**irm oncall schedules list**, **irm incidents list**
> 事件响应与值班管理。

**k6 load-tests list**, **k6 runs list**
> 使用 k6 进行负载测试。

**fleet pipelines list**, **fleet collectors list**
> Fleet 管理。

**kg status**, **kg search**, **kg entities show**
> Grafana 知识图谱。

**assistant investigations list**, **assistant prompt** _TEXT_
> 驱动 Grafana Assistant AI。

**frontend apps list**
> 前端可观测性。

**aio11y conversations list**, **aio11y agents list**
> AI 可观测性。

**dev scaffold**, **dev import**, **dev serve**, **dev lint**
> 可观测性即代码工作流：脚手架生成、导入、热重载和 lint。

**api** _PATH_
> 直接透传调用 Grafana HTTP API。

**skills list**, **skills install**
> 显示并部署智能体技能包。

**completion** _SHELL_
> 为 bash、zsh 或 fish 生成 Shell 补全。

**--since** _DURATION_
> 查询的时间窗口（例如 **1h**、**24h**）。

**-o**, **--output** _FORMAT_
> 输出格式：_json_ 或 _yaml_。

**--dry-run**
> 预览更改而不实际应用。

**--on-error** _MODE_
> 错误处理策略：_abort_、_fail_ 或 _ignore_。

**-p** _PATH_
> _resources_ 命令使用的资源目录。

**-f** _FILE_
> _resources_ 命令使用的输入文件。

# DESCRIPTION

**gcx** 是 Grafana Cloud 的官方命令行界面，提供一流的信号查询支持（指标、日志、链路追踪、性能剖析），可管理告警规则和 SLO，并可针对仪表盘和文件夹执行可观测性即代码工作流。它既适合人类使用，也适合需要结构化访问生产可观测性数据的智能体编程助手。

每个 Grafana 产品都有自己的顶层命令（**metrics**、**logs**、**traces**、**profiles**、**alert**、**slo**、**synth**、**irm**、**k6**、**fleet**、**assistant** 等）。资源可以通过 **gcx resources pull** 导出为本地 YAML 或 JSON，再通过 **gcx resources push** 推送回去，从而实现 GitOps 风格的 Grafana 对象管理。

# CONFIGURATION

配置存储在指向某个 Grafana 服务器和身份验证令牌的上下文（context）中：

```
gcx config set contexts.my-grafana.grafana.server [https://your-instance.grafana.net]
gcx config set contexts.my-grafana.grafana.token [your-service-account-token]
gcx config use-context [my-grafana]
```

环境变量 **GRAFANA_SERVER**、**GRAFANA_TOKEN** 和 **GRAFANA_CLOUD_TOKEN** 同样会被识别，这在 CI 中非常方便。使用 **gcx config check** 可以校验当前凭据是否有效。

# CAVEATS

**gcx** 支持 Grafana Cloud、Grafana Enterprise 以及 Grafana OSS **12+**。云专属产品（**slo**、**synth**、**irm** 以及 **fleet** 和 **kg** 的部分功能）需要 Grafana Cloud；功能可用性因部署类型而异。自动化场景应使用服务账号令牌而非个人令牌。

# HISTORY

**gcx** 由 **Grafana Labs** 发布，明确定位为"为智能体用法优化"，弥合了只能看到源码的 AI 编程工具与代码实际运行的生产系统之间的鸿沟。

# INSTALL

```brew: brew install gcx```

```nix: nix profile install nixpkgs#gcx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grafana-cli](/man/grafana-cli)(1), [promtool](/man/promtool)(1), [k6](/man/k6)(1)
