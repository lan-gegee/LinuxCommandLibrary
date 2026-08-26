# TAGLINE

指标收集与监控工具包

# TLDR

**启动 Prometheus**

```prometheus --config.file=[prometheus.yml]```

**指定存储路径启动**

```prometheus --config.file=[prometheus.yml] --storage.tsdb.path=[/data]```

**指定数据保留期**

```prometheus --storage.tsdb.retention.time=[15d]```

**启用 Web 管理 API**

```prometheus --web.enable-admin-api```

# SYNOPSIS

**prometheus** [_options_]

# PARAMETERS

**--config.file** _file_
> 配置文件。

**--storage.tsdb.path** _path_
> 数据存储目录。

**--storage.tsdb.retention.time** _duration_
> 数据保留期。

**--web.listen-address** _addr_
> 监听地址。

**--web.enable-admin-api**
> 启用管理端点。

**--log.level** _level_
> 日志详细程度。

# DESCRIPTION

**Prometheus** 是一个监控和告警工具包，从配置的目标收集指标并存储，供查询和告警使用。

# EXAMPLES

```bash
# Start with config
prometheus --config.file=prometheus.yml

# Custom port
prometheus --web.listen-address=":9191" \
  --config.file=prometheus.yml

# With retention
prometheus --storage.tsdb.retention.time=30d \
  --config.file=prometheus.yml
```

# CONFIGURATION

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
```

# CAVEATS

需要配置文件。默认端口 9090。配合 Grafana 进行可视化。

# HISTORY

Prometheus 于 2012 年起在 **SoundCloud** 开发，2016 年作为第二个托管项目加入 **CNCF**。

# INSTALL

```apt: sudo apt install prometheus```

```dnf: sudo dnf install prometheus```

```pacman: sudo pacman -S prometheus```

```apk: sudo apk add prometheus```

```brew: brew install prometheus```

```nix: nix profile install nixpkgs#prometheus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grafana](/man/grafana)(1), [alertmanager](/man/alertmanager)(1)
