# TAGLINE

使用 Kinesis Data Streams 管理实时数据流。

# TLDR

**创建新的数据流**

```aws kinesis create-stream --stream-name [my-stream] --shard-count 1```

**列出账户中的所有流**

```aws kinesis list-streams```

**向流写入记录**

```aws kinesis put-record --stream-name [my-stream] --partition-key [key1] --data "[message data]"```

**获取用于读取的分片迭代器**

```aws kinesis get-shard-iterator --stream-name [my-stream] --shard-id [shardId-000000000000] --shard-iterator-type TRIM_HORIZON```

**从分片读取记录**

```aws kinesis get-records --shard-iterator [shard-iterator-value]```

**查看流的详情**

```aws kinesis describe-stream --stream-name [my-stream]```

**将流保留期延长至 7 天**

```aws kinesis increase-stream-retention-period --stream-name [my-stream] --retention-period-hours 168```

**删除流**

```aws kinesis delete-stream --stream-name [my-stream]```

# SYNOPSIS

**aws kinesis** _command_ [_options_]

# DESCRIPTION

**aws kinesis** 是 Amazon Kinesis Data Streams 的 AWS CLI 接口。这是一项用于实时数据流的无服务器服务，可实时摄取和处理来自网站点击流、IoT 遥测和应用程序日志等来源的海量数据。

数据流由提供吞吐能力的分片组成。每个分片支持每秒 1 MB 写入和每秒 2 MB 读取。Kinesis 默认将数据保留 24 小时，针对回放场景最长可延长至 365 天。

# COMMANDS

**create-stream**
> 创建新的数据流

**delete-stream**
> 删除流

**describe-stream**
> 获取流的配置和状态

**list-streams**
> 列出所有流

**put-record**
> 写入单条记录

**put-records**
> 批量写入多条记录

**get-shard-iterator**
> 获取用于从分片读取数据的迭代器

**get-records**
> 使用迭代器检索记录

**update-shard-count**
> 扩缩流容量

**start-stream-encryption**
> 启用服务器端加密

**register-stream-consumer**
> 注册增强扇出（enhanced fan-out）消费者

**merge-shards**
> 合并两个相邻分片

**split-shard**
> 将一个分片拆分为两个

**list-tags-for-stream**
> 列出流的标签

# CAVEATS

分片迭代器会在 5 分钟后过期。每个分片都有吞吐限制；超限会导致限流。单条记录大小上限为 1 MB。GetRecords 每次调用最多返回 10 MB 或 10,000 条记录。增强扇出消费者会产生额外费用，但可获得专用吞吐量。

# HISTORY

Amazon Kinesis 于 **2013 年 11 月** 作为实时数据流服务推出。增强扇出于 **2018 年** 加入，为消费者提供专用吞吐量。按需容量模式于 **2021 年** 推出，免去了手动管理分片数量的负担。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-firehose](/man/aws-firehose)(1), [aws-kafka](/man/aws-kafka)(1)
