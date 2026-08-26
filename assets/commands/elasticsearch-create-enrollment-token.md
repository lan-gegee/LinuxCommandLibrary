# TAGLINE

为节点和 Kibana 生成注册令牌

# TLDR

**为新节点创建令牌**

```elasticsearch-create-enrollment-token -s node```

**为 Kibana 创建令牌**

```elasticsearch-create-enrollment-token -s kibana```

**指定 URL**

```elasticsearch-create-enrollment-token -s node --url [https://localhost:9200]```

# SYNOPSIS

**elasticsearch-create-enrollment-token** **-s** _scope_ [_options_]

# PARAMETERS

**-s**, **--scope** _scope_
> 生成令牌的作用域：`node` 或 `kibana`。

**--url** _url_
> 用于提交 API 请求的基础 URL（主机名和端口）。默认取自 elasticsearch.yml 推导出的值。

**-f**, **--force**
> 强制命令在不健康的集群上运行。

**-E** _setting=value_
> 在命令运行期间配置指定的 Elasticsearch 设置。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**elasticsearch-create-enrollment-token** 生成注册令牌，用于将新的 Elasticsearch 节点加入现有集群，或用于配置 Kibana 实例与启用了安全的集群通信。

令牌有效期较短，生成 30 分钟后过期。该命令必须在 Elasticsearch 安装目录中运行（通常为 `bin/elasticsearch-create-enrollment-token`）。

# CAVEATS

仅适用于已自动配置安全特性的集群（Elasticsearch 8.0 及更高版本的默认行为）。生成的令牌 30 分钟后过期。除非给出 `--force`，否则要求存在正在运行且健康的节点。

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [elasticsearch-reset-password](/man/elasticsearch-reset-password)(1)
