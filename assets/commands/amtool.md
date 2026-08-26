# TAGLINE

从命令行管理 Prometheus Alertmanager

# TLDR

**列出当前所有告警**

```amtool alert```

**查询匹配某个标签的告警**

```amtool alert query [alertname="HighMemory"]```

为告警**创建静默**

```amtool silence add [alertname="HighMemory"] --comment="[Maintenance]" --duration=[2h]```

**列出所有生效中的静默**

```amtool silence query```

按 ID 使**静默过期**

```amtool silence expire [silence_id]```

**检查 Alertmanager 配置**

```amtool check-config [alertmanager.yml]```

**显示集群状态**

```amtool cluster show```

# SYNOPSIS

**amtool** _command_ [_options_] [_arguments_]

# PARAMETERS

**alert query**
> 查看和搜索当前告警。

**alert add**
> 向 Alertmanager 添加新告警。

**silence add** _matchers_
> 创建一个匹配指定标签的新静默。

**silence query**
> 列出生效中的静默。

**silence update** _id_
> 更新已有的静默（如延长其持续时间）。

**silence expire** _id_
> 按 ID 移除静默。

**silence import**
> 从 JSON 文件或标准导入静默。

**check-config** _file_
> 校验 Alertmanager 配置文件。

**cluster show**
> 显示集群成员状态和对等节点。

**config show**
> 显示当前的 Alertmanager 配置。

**config routes show**
> 显示配置中的路由树。

**config routes test** _labels_
> 测试给定的标签会匹配哪条路由。

**template render**
> 渲染模板定义以供测试。

**--alertmanager.url** _url_
> Alertmanager URL（默认：**http://localhost:9093/**）。

**--comment** _text_
> 静默的备注（除非另有配置，否则必填）。

**--author** _name_
> 静默的作者（CreatedBy 字段）。

**--duration** _duration_
> 静默的持续时间（默认：1h，如 30m、2h）。

**--end** _time_
> 以 RFC3339 时间戳设置静默的过期时间。

**--timeout** _duration_
> API 请求的超时时间（默认：30s）。

**-o**, **--output** _format_
> 输出格式：simple、extended、json（默认：simple）。

# DESCRIPTION

**amtool** 是与 Prometheus Alertmanager 交互的官方命令行客户端。它提供查询告警、管理静默、测试路由配置和校验配置文件等功能。

该工具通过 Alertmanager 实例的 HTTP API 执行操作。它在维护窗口期间创建静默、调试告警路由，以及将 Alertmanager 管理集成到自动化脚本中时特别有用。

可以使用 **check-config** 在离线状态下校验配置，无需运行中的 Alertmanager 实例。**config routes test** 命令有助于验证告警是否会根据其标签路由到预期的接收器。

# CONFIGURATION

**~/.config/amtool/config.yml**
> 持久化保存 Alertmanager URL、作者和输出格式默认值的配置文件。

# CAVEATS

需要能访问 Alertmanager API 端点的网络。静默必须附带备注；缺少 **--comment** 时创建会失败。如果 Alertmanager 不在 localhost:9093 上运行，则必须指定 **--alertmanager.url**。配置文件校验可能无法发现所有运行时问题。

# HISTORY

**amtool** 与 Alertmanager 一同开发，是 Prometheus 生态的一部分。它的诞生是为了给运维人员提供可脚本化的告警管理接口，与 Web UI 形成互补，便于自动化和 CI/CD 集成。该工具由 Prometheus 项目维护，随 Alertmanager 发布一同分发。

# INSTALL

```apt: sudo apt install prometheus-alertmanager```

```dnf: sudo dnf install alertmanager```

```pacman: sudo pacman -S alertmanager```

```apk: sudo apk add alertmanager```

```nix: nix profile install nixpkgs#prometheus-alertmanager```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[alertmanager](/man/alertmanager)(1), [prometheus](/man/prometheus)(1), [promtool](/man/promtool)(1)

# RESOURCES

```[Source code](https://github.com/prometheus/alertmanager)```

```[Documentation](https://prometheus.io/docs/alerting/latest/alertmanager/)```

<!-- verified: 2026-06-11 -->
