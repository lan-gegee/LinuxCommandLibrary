# TAGLINE

用于摄取、转换和传输数据的服务端数据处理管道

# TLDR

**使用配置文件启动 Logstash**

```logstash -f [/path/to/config.conf]```

**测试配置语法**

```logstash -t -f [/path/to/config.conf]```

**以内联配置启动**

```logstash -e 'input { stdin {} } output { stdout {} }'```

**以配置目录启动**

```logstash -f [/etc/logstash/conf.d/]```

**以指定的流水线设置启动**

```logstash -f [config.conf] --pipeline.workers [4]```

**自动重新加载配置**

```logstash -f [config.conf] --config.reload.automatic```

**列出已安装的插件**

```logstash-plugin list```

**安装插件**

```logstash-plugin install [logstash-filter-json]```

# SYNOPSIS

**logstash** [_-f config_] [_-e string_] [_-t_] [_--pipeline.workers num_] [_options_]

# PARAMETERS

**-f**, **--path.config** _PATH_
> 配置文件或目录的路径。

**-e**, **--config.string** _CONFIG_
> 内联配置字符串。

**-t**, **--config.test_and_exit**
> 测试配置后退出。

**-r**, **--config.reload.automatic**
> 配置更改时自动重新加载。

**--config.reload.interval** _SECONDS_
> 配置重载检查间隔。

**-w**, **--pipeline.workers** _NUM_
> 流水线工作线程数。

**-b**, **--pipeline.batch.size** _NUM_
> 每个批次的事件数。

**-u**, **--pipeline.batch.delay** _MS_
> 批次延迟（毫秒）。

**-l**, **--path.logs** _PATH_
> 日志文件目录。

**--log.level** _LEVEL_
> 日志级别：fatal、error、warn、info、debug、trace。

**--path.data** _PATH_
> 数据目录路径。

**--path.plugins** _PATH_
> 自定义插件目录。

**-n**, **--node.name** _NAME_
> 用于集群标识的节点名称。

**--api.http.host** _HOST_
> 监控 API 主机（默认：127.0.0.1）。

**--api.http.port** _PORT_
> 监控 API 端口（默认：9600）。

**--path.settings** _DIR_
> 包含 logstash.yml 的目录。

**-V**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**Logstash** 是一个服务端数据处理管道，从多个来源摄取数据、进行转换并发送到各种目的地。它是 Elastic Stack（ELK：Elasticsearch、Logstash、Kibana）的一部分。

配置分为三个部分：**input**（文件、beats、syslog 等数据来源）、**filter**（grok、mutate、geoip 等转换）和 **output**（Elasticsearch、file、stdout 等目的地）。配置采用类 Ruby 的 DSL。

grok 过滤器尤为强大，可以通过模式匹配把非结构化日志数据解析为结构化字段。它内置了 Web 日志、syslog 等常见格式的常用模式。

多个流水线可以同时在 `pipelines.yml` 中以独立配置的方式运行。流水线之间的通信支持复杂的路由。持久化队列可在重启后保证数据的持久性。

插件扩展了功能：通过 `logstash-plugin` 可以获得数百个 input、filter 和 output 插件。编解码器（codec）系统负责数据序列化（JSON、multiline 等）。

# CAVEATS

基于 JVM，内存需求较大（通常需要 1GB 以上堆内存）。启动较慢。复杂的 grok 模式可能占用大量 CPU。配置错误只在启动或重载时才会暴露。插件的兼容性随 Logstash 版本而异。

# HISTORY

**Logstash** 由 **Jordan Sissel** 于 **2009 年**创建，最初是一个管理日志和事件的工具。它原本是独立项目，**2013 年**被 **Elastic**（当时的 Elasticsearch）收购，成为 ELK Stack 的核心组成部分。该项目从一个简单的日志传送器演变为完整的数据处理管道，期间经历了多次重大重构，包括转向持久化队列架构。

# INSTALL

```brew: brew install logstash```

```nix: nix profile install nixpkgs#logstash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[filebeat](/man/filebeat)(1), [elasticsearch](/man/elasticsearch)(1)
