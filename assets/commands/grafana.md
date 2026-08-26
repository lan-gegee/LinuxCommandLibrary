# TAGLINE

分析与监控可视化平台

# TLDR

**启动 Grafana 服务器**（新版二进制）

```grafana server```

**启动 Grafana 服务器**（旧版二进制）

```grafana-server```

**使用配置文件启动**

```grafana server --config [/etc/grafana/grafana.ini]```

**检查版本**

```grafana server -v```

**运行管理 CLI**

```grafana cli admin reset-admin-password [newpass]```

**访问 Web 界面**

```http://localhost:3000```

# SYNOPSIS

**grafana-server** [_options_]

# PARAMETERS

**--config** _file_
> 配置文件路径。

**--homepath** _path_
> Grafana 主目录。

**--pidfile** _file_
> PID 文件路径。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**Grafana** 是一个开源的分析与可视化平台。它创建仪表盘，用于监控来自 Prometheus、InfluxDB、Elasticsearch 等众多数据源的指标。

Grafana 提供丰富的可视化选项，包括图表、表格、热力图和告警。它常用于基础设施监控、应用指标和业务分析。

# DEFAULT CREDENTIALS

```
URL: http://localhost:3000
Username: admin
Password: admin (change on first login)
```

# KEY FEATURES

- 多数据源仪表盘
- 带通知的告警
- 用户身份验证与团队
- 插件生态
- 仪表盘模板化

# CONFIGURATION

**/etc/grafana/grafana.ini**
> 主服务器配置文件，控制端口、身份验证、数据库和数据源。

**/etc/grafana/provisioning/**
> 用于通过 YAML 文件预配置（provisioning）仪表盘、数据源和告警的目录。

# CAVEATS

以服务方式运行；需要 systemd 或 init 配置。数据源需要单独安装。复杂的仪表盘可能影响性能。暴露到互联网时请注意安全。

# HISTORY

Grafana 由 **Torkel Odegaard** 于 **2014 年**创建，最初是用于 Graphite 可视化的 Kibana 分支。它逐步成长为领先的可视化平台，**2015 年**成立的 Grafana Labs 支持其商业化开发。

# INSTALL

```dnf: sudo dnf install grafana```

```pacman: sudo pacman -S grafana```

```apk: sudo apk add grafana```

```zypper: sudo zypper install grafana```

```brew: brew install grafana```

```nix: nix profile install nixpkgs#grafana```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prometheus](/man/prometheus)(1)
