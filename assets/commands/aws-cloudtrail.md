# TAGLINE

跟踪并审计跨云服务的 API 活动。

# TLDR

**按用户名查找近期事件**

```aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=[user@example.com]```

**按事件名称查找事件**

```aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=[RunInstances]```

**在时间范围内查找事件**

```aws cloudtrail lookup-events --start-time [2024-01-01T00:00:00Z] --end-time [2024-01-02T00:00:00Z]```

**创建多区域跟踪**

```aws cloudtrail create-trail --name [my-trail] --s3-bucket-name [my-bucket] --is-multi-region-trail```

**为跟踪启动日志记录**

```aws cloudtrail start-logging --name [my-trail]```

**列出所有跟踪**

```aws cloudtrail describe-trails```

**获取跟踪状态**

```aws cloudtrail get-trail-status --name [my-trail]```

# SYNOPSIS

**aws cloudtrail** _command_ [_options_]

# PARAMETERS

**lookup-events**
> 搜索最近 90 天的管理事件

**create-trail**
> 创建用于记录 API 活动的新跟踪

**describe-trails**
> 列出跟踪及其配置

**get-trail-status**
> 获取跟踪的日志记录状态

**start-logging**
> 开始向跟踪记录事件

**stop-logging**
> 暂停向跟踪记录事件

**update-trail**
> 修改跟踪配置

**delete-trail**
> 删除跟踪（日志仍保留在 S3 中）

**put-event-selectors**
> 配置要记录哪些事件

**put-insight-selectors**
> 启用 CloudTrail Insights

**--name** _trail-name_
> 跟踪名称或 ARN

**--s3-bucket-name** _bucket_
> 用于存储日志的 S3 存储桶

**--is-multi-region-trail**
> 记录所有区域的事件

**--is-organization-trail**
> 记录组织中所有账户的事件

**--kms-key-id** _key_
> 用于日志加密的 KMS 密钥

**--lookup-attributes** _attr_
> 筛选事件（AttributeKey=Type,AttributeValue=Value）

**--start-time** _timestamp_
> 查找时间范围的起点

**--end-time** _timestamp_
> 查找时间范围的终点

# LOOKUP ATTRIBUTES

**EventId** - 唯一的事件标识符

**EventName** - API 操作（RunInstances、CreateBucket）

**Username** - IAM 用户或角色名称

**ResourceType** - AWS 资源类型

**ResourceName** - 资源标识符

**EventSource** - 服务（ec2.amazonaws.com）

**AccessKeyId** - 所使用的访问密钥

# DESCRIPTION

**aws cloudtrail** 管理 AWS CloudTrail。CloudTrail 会记录跨 AWS 服务的 API 活动和事件，用于审计、合规与安全分析。

**lookup-events** 可搜索最近 90 天的管理事件，无需预先配置跟踪。每个区域的限速为每秒 2 个请求。

**跟踪（Trail）** 将日志传送到 S3 存储桶进行长期保存。多区域跟踪会捕获所有区域的活动。组织跟踪会为 AWS Organizations 中的所有账户记录事件。

**事件选择器** 用于筛选要记录的事件（管理事件、S3/Lambda 的数据事件，或用于异常检测的 Insights 事件）。

日志内容包括请求发起者、所用的服务、执行的操作、参数以及响应元素。

# CAVEATS

lookup-events 只能搜索最近 90 天的事件；更早的事件需配合 Athena 查询 S3 日志。限速为每秒 2 个请求。每次查询只能使用一个查找属性。创建跟踪需要先配置 S3 存储桶及存储桶策略。日志传送会有数分钟延迟。

# HISTORY

**AWS CloudTrail** 于 **2013 年 11 月** 推出，是 AWS 的审计日志服务。它已成为安全、合规与治理的关键组件。用于异常检测的 CloudTrail Insights 于 **2019 年** 加入。支持基于 SQL 的事件查询的 CloudTrail Lake 于 **2022 年** 推出。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-s3](/man/aws-s3)(1), [aws-athena](/man/aws-athena)(1)
