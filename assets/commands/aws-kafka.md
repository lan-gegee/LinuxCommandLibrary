# TAGLINE

管理 Amazon Managed Streaming for Apache Kafka 集群。

# TLDR

**创建新的 MSK 集群**

```aws kafka create-cluster --cluster-name [my-cluster] --kafka-version [3.5.1] --number-of-broker-nodes 3 --broker-node-group-info file://[broker-config.json]```

**列出所有 MSK 集群**

```aws kafka list-clusters```

**获取集群及其详情**

```aws kafka describe-cluster --cluster-arn [arn:aws:kafka:region:account:cluster/name/id]```

**获取用于客户端连接的引导代理端点**

```aws kafka get-bootstrap-brokers --cluster-arn [arn:aws:kafka:region:account:cluster/name/id]```

**更新代理数量**

```aws kafka update-broker-count --cluster-arn [arn:aws:kafka:region:account:cluster/name/id] --current-version [K1234] --target-number-of-broker-nodes 6```

**列出**所有 MSK 配置

```aws kafka list-configurations```

**列出可用于升级的兼容 Kafka 版本**

```aws kafka get-compatible-kafka-versions --cluster-arn [arn:aws:kafka:region:account:cluster/name/id]```

**删除集群**

```aws kafka delete-cluster --cluster-arn [arn:aws:kafka:region:account:cluster/name/id]```

# SYNOPSIS

**aws kafka** _command_ [_options_]

# DESCRIPTION

**aws kafka** 是 Amazon Managed Streaming for Apache Kafka（MSK）的 AWS CLI 接口。MSK 是一项运行 Apache Kafka 的全托管服务，负责集群预置、配置、修补和监控，同时保持与开源 Kafka 的兼容性。

MSK 支持预置和无服务器两种部署模式、SASL/SCRAM 与 IAM 认证、静态及传输中加密，并可与 Lambda、Kinesis Data Firehose 和 Glue 等 AWS 服务集成。

# COMMANDS

**create-cluster**
> 创建新的 MSK 集群

**delete-cluster**
> 删除 MSK 集群

**describe-cluster**
> 获取集群配置和状态

**list-clusters**
> 列出账户中的所有集群

**get-bootstrap-brokers**
> 获取用于客户端连接的代理端点

**update-broker-count**
> 扩缩代理数量

**update-broker-storage**
> 增加代理存储容量

**update-cluster-kafka-version**
> 升级 Kafka 版本

**create-configuration**
> 创建自定义代理配置

**reboot-broker**
> 重启特定代理

**update-cluster-configuration**
> 更新集群的代理配置

**list-cluster-operations**
> 列出集群操作

**list-configurations**
> 列出所有 MSK 配置

# CAVEATS

代理数量只能增加，不能减少。存储只能扩大。Kafka 版本升级是单向的，无法回滚。创建集群需要 15-20 分钟。MSK Serverless 的配额与预置集群不同。

# HISTORY

Amazon MSK 于 **2018 年 12 月** 作为托管 Kafka 服务推出。用于托管连接器的 MSK Connect 于 **2021 年** 加入；无需容量规划即可自动扩缩的 MSK Serverless 于 **2022 年** 推出。用于成本优化的分层存储于 **2023 年** 推出。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-kinesis](/man/aws-kinesis)(1), [kafka-topics](/man/kafka-topics)(1)
