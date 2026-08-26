# TAGLINE

为 Prometheus 处理告警去重、分组和路由

# TLDR

使用默认配置**启动 Alertmanager**

```alertmanager --config.file=[alertmanager.yml]```

以**自定义存储路径**启动

```alertmanager --config.file=[alertmanager.yml] --storage.path=[/var/lib/alertmanager]```

**以集群模式启动**并指定 peers

```alertmanager --config.file=[alertmanager.yml] --cluster.peer=[peer1:9094] --cluster.peer=[peer2:9094]```

用 amtool **验证配置文件**

```amtool check-config [alertmanager.yml]```

以**自定义 Web 监听地址**启动

```alertmanager --config.file=[alertmanager.yml] --web.listen-address=[0.0.0.0:9093]```

# SYNOPSIS

**alertmanager** [_options_]

# PARAMETERS

**--config.file** _path_
> Alertmanager 配置文件的路径。

**--storage.path** _path_
> 通知状态和静默数据存储的基础路径（默认：**data/**）。

**--data.retention** _duration_
> 通知和静默数据的保留时长（默认：**120h**）。

**--web.listen-address** _address_
> Web UI 和 API 的监听地址（默认：**:9093**）。

**--web.external-url** _url_
> 用于生成指回 Alertmanager 链接的外部 URL。

**--cluster.listen-address** _address_
> 集群通信地址（默认：**0.0.0.0:9094**）。

**--cluster.peer** _address_
> 组建集群时的初始 peer 地址（可重复）。

**--cluster.advertise-address** _address_
> 在集群中通告的地址。

**--log.level** _level_
> 日志级别：debug、info、warn、error。

**--log.format** _format_
> 日志格式：logfmt 或 json。

**--web.route-prefix** _prefix_
> Web 端点内部路由的前缀（默认取 **--web.external-url** 的路径）。

# DESCRIPTION

**Alertmanager** 处理由 Prometheus 和其他监控系统发送的告警。它负责告警的去重、分组、静默、抑制，并将告警路由到邮件、Slack、PagerDuty、webhook 等通知接收端。

当 Prometheus 检测到符合告警规则的条件时，它会向 Alertmanager 发送告警。Alertmanager 将相关告警分组，等待设定的间隔以批量发送通知，并根据标签匹配规则将其路由到合适的接收端。

关键特性包括：用于在维护期间屏蔽告警的 **silences（静默）**、在相关告警已触发时抑制其他告警的 **inhibition（抑制）**规则，以及基于 gossip 协议确保告警不会跨实例重复的**高可用**集群机制。

位于所配置监听地址上的 Web UI 提供告警管理、静默创建和集群状态可见性。

# CONFIGURATION

**/etc/alertmanager/alertmanager.yml**
> 主配置文件，定义路由、接收端、抑制规则和通知模板。

# CAVEATS

Alertmanager 要求正确配置的 YAML 文件；无效配置会导致无法启动。该二进制程序没有专门的配置检查标志；部署前请用 **amtool check-config** 验证配置。集群模式要求所有 peer 在集群端口上互相可达。通知状态存储在本地；存储丢失可能导致重复通知。如果分组间隔设置过长，可能延迟关键告警。

# HISTORY

**Alertmanager** 由 **SoundCloud** 开发，属于 Prometheus 生态系统，于 **2013** 年首次发布。**2018** 年它与 Prometheus 一同成为 **云原生计算基金会（CNCF）**的毕业项目。在现代云原生基础设施中，该工具已发展为支持众多通知集成和高可用部署。

# INSTALL

```dnf: sudo dnf install alertmanager```

```pacman: sudo pacman -S alertmanager```

```apk: sudo apk add alertmanager```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[prometheus](/man/prometheus)(1), [amtool](/man/amtool)(1), [grafana](/man/grafana)(1)

# RESOURCES

```[Source code](https://github.com/prometheus/alertmanager)```

```[Homepage](https://prometheus.io/)```

```[Documentation](https://prometheus.io/docs/alerting/latest/alertmanager/)```

<!-- verified: 2026-06-11 -->
