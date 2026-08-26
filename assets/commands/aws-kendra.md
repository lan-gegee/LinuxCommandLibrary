# TAGLINE

管理由机器学习驱动的企业搜索索引和数据源。

# TLDR

**创建新的 Kendra 索引**

```aws kendra create-index --name [my-index] --role-arn [arn:aws:iam::account:role/kendra-role]```

**列出账户中的所有索引**

```aws kendra list-indices```

**提交搜索查询**

```aws kendra query --index-id [index-id] --query-text "[search terms]"```

**向索引添加文档**

```aws kendra batch-put-document --index-id [index-id] --documents file://[documents.json]```

**创建数据源连接器**

```aws kendra create-data-source --index-id [index-id] --name [s3-source] --type S3 --configuration file://[s3-config.json] --role-arn [arn:aws:iam::account:role/kendra-role]```

**启动数据源同步**

```aws kendra start-data-source-sync-job --index-id [index-id] --id [data-source-id]```

**创建 FAQ 以直接回答问题**

```aws kendra create-faq --index-id [index-id] --name [my-faq] --s3-path Bucket=[bucket],Key=[faq.csv] --role-arn [arn:aws:iam::account:role/kendra-role]```

# SYNOPSIS

**aws kendra** _command_ [_options_]

# DESCRIPTION

**aws kendra** 是 Amazon Kendra 的 AWS CLI 接口。Kendra 是一项由机器学习驱动的智能企业搜索服务，可跨文档、FAQ 和其他内容源提供自然语言搜索能力。

Kendra 可为 S3、SharePoint、Salesforce、ServiceNow 和数据库等多种数据源中的文档建立索引。它能理解自然语言查询，返回带高亮答案的相关段落，支持超越关键词匹配的语义搜索。

# COMMANDS

**create-index**
> 创建新的搜索索引

**delete-index**
> 删除索引

**list-indices**
> 列出所有索引

**query**
> 提交搜索查询

**batch-put-document**
> 向索引添加文档

**batch-delete-document**
> 从索引中移除文档

**create-data-source**
> 创建连接外部内容的连接器

**start-data-source-sync-job**
> 触发文档同步

**create-faq**
> 添加 FAQ 内容以直接回答问题

**get-query-suggestions**
> 获取自动补全建议

# CAVEATS

创建索引需要 15-30 分钟。文档摄取按扫描的文档数量计费。查询容量单位（QCU）决定并发查询上限。大文档处理可能较慢；批量内容应使用数据源。高级功能需要企业版。

# HISTORY

Amazon Kendra 于 **2019 年 12 月** 作为由机器学习驱动的企业搜索服务推出。查询建议于 **2021 年** 加入，推广内容的精选结果于 **2022 年** 加入。该服务的连接器已扩展至支持超过 14 种内容存储库。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-opensearch](/man/aws-opensearch)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/kendra/index.html)```

<!-- verified: 2026-06-18 -->
