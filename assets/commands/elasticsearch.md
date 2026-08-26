# TAGLINE

分布式搜索与分析引擎

# TLDR

**启动 Elasticsearch**

```elasticsearch```

**使用指定配置启动**

```elasticsearch -Epath.conf=[/etc/elasticsearch]```

**以后台守护进程方式启动**

```elasticsearch -d -p [/var/run/elasticsearch.pid]```

**检查集群健康状况**

```curl -X GET "localhost:9200/_cluster/health?pretty"```

**列出索引**

```curl -X GET "localhost:9200/_cat/indices?v"```

**创建索引**

```curl -X PUT "localhost:9200/[index_name]"```

# SYNOPSIS

**elasticsearch** [_options_]

# PARAMETERS

**-d**, **--daemonize**
> 以守护进程运行。

**-p** _pidfile_
> 将 PID 写入文件。

**-E** _setting=value_
> 配置设置项。

**-q**, **--quiet**
> 安静输出。

**-s**, **--silent**
> 静默输出。

**-v**, **--verbose**
> 详细输出。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**Elasticsearch** 是一个构建于 Apache Lucene 之上的分布式搜索与分析引擎。它通过 RESTful API 提供全文搜索、结构化搜索和分析能力。

数据以 JSON 文档的形式存储在索引中（类似于数据库）。Elasticsearch 自动将数据分布到多个节点上，以实现可扩展性和副本冗余。它通常与 Kibana 配合进行可视化，并作为 ELK 技术栈（Elasticsearch、Logstash、Kibana）的一部分使用。

# CONFIGURATION

**/etc/elasticsearch/elasticsearch.yml**
> 主配置文件，包含集群设置、网络配置和路径。

**/etc/elasticsearch/jvm.options**
> JVM 堆大小和垃圾回收设置。

**config/elasticsearch.keystore**
> 密码等敏感设置的安全存储。

# CAVEATS

需要 Java 运行时。内存占用大；应合理配置堆大小。旧版本默认关闭安全特性。单节点开发模式与生产集群不同。索引映射应在大量写入之前定义好。

# HISTORY

Elasticsearch 由 **Shay Banon** 创建，于 **2010 年**首次发布。它源自他早期开发的 Compass。Elastic 公司成立于 **2012 年**，该产品成为用于可观测性和安全分析的 Elastic Stack 的基础。

# INSTALL

```nix: nix profile install nixpkgs#elasticsearch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opensearch](/man/opensearch)(1), [logstash](/man/logstash)(1), [curl](/man/curl)(1)
