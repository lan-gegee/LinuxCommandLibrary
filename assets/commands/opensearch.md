# TAGLINE

源自 Elasticsearch 7 的开源搜索与分析引擎

# TLDR

**启动 OpenSearch**

```opensearch```

**使用指定配置启动**

```opensearch -E path.data=[/data] -E path.logs=[/logs]```

**以守护进程方式运行**（后台）

```opensearch -d```

**检查集群健康状态**

```curl -XGET "http://localhost:9200/_cluster/health?pretty"```

**索引文档**

```curl -XPOST "http://localhost:9200/[index]/_doc" -H 'Content-Type: application/json' -d '{"field":"value"}'```

# SYNOPSIS

**opensearch** [_options_]

# PARAMETERS

**-d**
> 以守护进程方式（在后台）运行。

**-p** _file_
> 将进程 ID 写入文件。

**-E** _setting=value_
> 设置配置项（例如 -E cluster.name=myCluster）。

**-q**, **--quiet**
> 抑制输出到 stdout 的常规输出。

**-v**, **--verbose**
> 启用详细输出。

# DESCRIPTION

**OpenSearch** 是从 Elasticsearch 7.10.2 衍生而来的开源搜索与分析引擎。它提供全文搜索、日志和分析功能。

OpenSearch 包含用于可视化的 OpenSearch Dashboards（从 Kibana 分叉而来）。

# REST API

```bash
# Create index
curl -XPUT "localhost:9200/myindex"

# Search
curl -XGET "localhost:9200/myindex/_search?q=field:value"

# Delete index
curl -XDELETE "localhost:9200/myindex"
```

# CONFIGURATION

```
/etc/opensearch/opensearch.yml
/etc/opensearch/jvm.options
```

# CAVEATS

需要 Java。内存占用高；请配置堆大小。安全插件默认启用。

# HISTORY

在 Elastic 更改许可证之后，**Amazon Web Services** 于 **2021 年**创建了 OpenSearch，作为 Elasticsearch 的开源分支。

# INSTALL

```pacman: sudo pacman -S opensearch```

```brew: brew install opensearch```

```nix: nix profile install nixpkgs#opensearch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [logstash](/man/logstash)(1), [curl](/man/curl)(1)
