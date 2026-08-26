# TAGLINE

Elastic Stack 的轻量级日志采集器

# TLDR

**以默认配置启动 filebeat**

```filebeat```

**以指定的配置文件启动**

```filebeat -c [path/to/filebeat.yml]```

**测试配置文件**语法

```filebeat test config```

**测试输出连通性**（Elasticsearch、Logstash 等）

```filebeat test output```

**启用一个模块**

```filebeat modules enable [nginx]```

**列出可用模块**

```filebeat modules list```

**设置仪表盘和索引模板**

```filebeat setup```

**运行一次后退出**（处理已有文件）

```filebeat --once```

# SYNOPSIS

**filebeat** [_COMMAND_] [_FLAGS_]

# COMMANDS

**run**
> 运行 Filebeat（未指定命令时的默认命令）。

**test config**
> 测试配置文件语法。

**test output**
> 测试与已配置输出的连通性。

**modules enable** _MODULE_...
> 启用一个或多个模块。

**modules disable** _MODULE_...
> 禁用一个或多个模块。

**modules list**
> 列出可用及已启用的模块。

**setup**
> 设置索引模板、仪表盘和管道。

**export config**
> 将当前配置导出到标准输出。

**export template**
> 将索引模板导出到标准输出。

**export dashboard**
> 将一个 Kibana 仪表盘导出到标准输出。

# PARAMETERS

**-c** _FILE_
> 指定配置文件（默认：filebeat.yml）。

**-e**
> 把日志记录到 stderr 而不是 syslog/文件。

**--modules** _MODULES_
> 要运行的模块列表，以逗号分隔。

**--once**
> 采集器只运行一轮，完成后退出。

**--path.config** _PATH_
> 配置文件的路径。

**--path.data** _PATH_
> 数据目录的路径。

**--path.logs** _PATH_
> 日志文件的路径。

**--strict.perms**
> 对配置文件强制执行严格权限检查（默认：true）。

**-v**
> 启用详细日志输出。

**-d** _SELECTOR_
> 为特定组件启用调试输出。

# CONFIGURATION

**filebeat.yml**
> 主配置文件，定义输入、输出、模块和处理选项。

**/etc/filebeat/modules.d/*.yml**
> 各模块专属的配置文件，对应内置的日志解析器。

# DESCRIPTION

**Filebeat** 是来自 Elastic Stack（ELK）的轻量级日志采集器。它监控日志文件、收集日志事件，并将其转发给 Elasticsearch、Logstash 或其他输出进行索引和分析。

Filebeat 使用采集器（harvester）逐行读取日志文件，再把数据发送到配置好的输出端。它会维护状态信息来跟踪读取位置，即使重启之后也能保证可靠送达。模块则为 nginx、Apache、MySQL 和系统日志等常见应用提供预置配置。

配置在 filebeat.yml 中定义，内容包括输入（日志路径）、输出（Elasticsearch/Logstash 端点）以及处理选项。

# CAVEATS

配置文件默认要求严格权限（仅所有者可读写）。通过 systemd 运行时，-e 标志可能覆盖日志相关设置。模块必须先启用才能使用。设置索引模板和仪表盘时需要能够连接 Elasticsearch 与 Kibana。

# HISTORY

Filebeat 是 **Elastic** 开发的 **Beats** 轻量级数据采集器家族的一员。它由 Logstash Forwarder（Lumberjack）演化而来，提供了资源占用更低的日志收集方案。Beats 平台在 **2015 年**前后推出，此后 Filebeat 成为 Elastic Stack 中日志采集的首选。

# INSTALL

```brew: brew install filebeat```

```nix: nix profile install nixpkgs#filebeat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[logstash](/man/logstash)(1), [elasticsearch](/man/elasticsearch)(1), [journalctl](/man/journalctl)(1)
