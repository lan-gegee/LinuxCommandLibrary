# TAGLINE

管理用于搜索和分析的 OpenSearch Service 域。

# TLDR

**列出所有 OpenSearch 域**

```aws opensearch list-domain-names```

**描述域**

```aws opensearch describe-domain --domain-name [domain_name]```

**获取域配置**

```aws opensearch describe-domain-config --domain-name [domain_name]```

**创建新域**

```aws opensearch create-domain --domain-name [domain_name] --engine-version OpenSearch_2.11 --cluster-config InstanceType=t3.small.search,InstanceCount=1```

**更新域配置**

```aws opensearch update-domain-config --domain-name [domain_name] --cluster-config InstanceType=r6g.large.search```

**删除域**

```aws opensearch delete-domain --domain-name [domain_name]```

**列出可用的引擎版本**

```aws opensearch list-versions```

**获取升级历史**

```aws opensearch get-upgrade-history --domain-name [domain_name]```

# SYNOPSIS

**aws opensearch** _subcommand_ [_options_]

# DESCRIPTION

**aws opensearch** 是 AWS CLI 的一个子命令，用于管理 Amazon OpenSearch Service。这是一项托管的搜索与分析引擎服务，是 Amazon Elasticsearch Service 的后继者，兼容 OpenSearch 及旧版 Elasticsearch API。

OpenSearch 域是运行 OpenSearch 引擎的集群。每个域都有集群配置（实例类型、数量）、存储设置（EBS 卷）、访问策略，以及细粒度访问控制和加密等可选功能。

该服务支持的用例包括日志分析、全文搜索、应用监控和 SIEM。OpenSearch Dashboards 提供可视化功能。

# PARAMETERS

**list-domain-names**
> 列出账户中的所有域。

**describe-domain**
> 获取域的状态和配置。

**describe-domain-config**
> 获取详细的配置设置。

**create-domain**
> 创建新的 OpenSearch 域。

**update-domain-config**
> 修改域的设置。

**delete-domain**
> 删除域。

**list-versions**
> 列出可用的 OpenSearch 和 Elasticsearch 版本。

**upgrade-domain**
> 启动版本升级。

**get-upgrade-status**
> 检查升级进度。

**--domain-name** _name_
> 域的名称。

**--engine-version** _version_
> OpenSearch 或 Elasticsearch 版本。

**--cluster-config** _config_
> 实例类型、数量和可用区感知设置。

**--ebs-options** _options_
> EBS 卷配置。

**--access-policies** _json_
> 基于资源的访问策略。

**--vpc-options** _options_
> 私有域的 VPC 配置。

**--encryption-at-rest-options** _options_
> 启用静态加密。

# CAVEATS

域名必须为小写且在一个区域内唯一。配置更改可能需要 15-30 分钟才能生效。位于 VPC 中的域之后无法改为公开访问。版本升级可能需要蓝/绿部署。细粒度访问控制要求启用 HTTPS 和节点间加密。删除域会永久移除所有数据。

# HISTORY

**Amazon Elasticsearch Service** 于 **2015 年 10 月**上线，是一项托管的 Elasticsearch 服务。在 Elasticsearch 更改许可证后，AWS 分叉了该项目，并于 **2021 年 9 月**将该服务更名为 **Amazon OpenSearch Service**，基于开源的 OpenSearch 项目。此后该服务陆续增加了 UltraWarm 存储层、无服务器集合以及面向 AI 应用的向量搜索等功能。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [curl](/man/curl)(1), [aws-logs](/man/aws-logs)(1), [aws-firehose](/man/aws-firehose)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/opensearch/index.html)```

<!-- verified: 2026-06-18 -->
