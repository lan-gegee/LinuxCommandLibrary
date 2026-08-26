# TAGLINE

从 DynamoDB 表读取变更数据捕获记录。

# TLDR

**列出与 DynamoDB 表关联的所有流**

```aws dynamodbstreams list-streams --table-name [table_name]```

**查看流的详情和分片**

```aws dynamodbstreams describe-stream --stream-arn [arn:aws:dynamodb:region:account:table/name/stream/timestamp]```

**获取分片迭代器以开始读取记录**

```aws dynamodbstreams get-shard-iterator --stream-arn [stream_arn] --shard-id [shard_id] --shard-iterator-type [TRIM_HORIZON|LATEST|AT_SEQUENCE_NUMBER]```

**从分片读取记录**

```aws dynamodbstreams get-records --shard-iterator [iterator_string]```

**获取特定序列号处的分片迭代器**

```aws dynamodbstreams get-shard-iterator --stream-arn [stream_arn] --shard-id [shard_id] --shard-iterator-type AT_SEQUENCE_NUMBER --sequence-number [seq_num]```

# SYNOPSIS

**aws dynamodbstreams** _subcommand_ [_options_]

# DESCRIPTION

**aws dynamodbstreams** 是 AWS CLI 的子命令，用于读取 DynamoDB Streams 的变更数据捕获（change data capture）记录。当在 DynamoDB 表上启用流后，每一次修改（插入、更新、删除）都会被捕获为一条流记录。

流将记录组织到分片（shard）中，分片是有序记录的容器。要读取流数据，需先获取一个分片迭代器，再用它检索记录。每个分片迭代器在不活动 15 分钟后过期。

根据表上配置的流视图类型，流记录可以包含旧的项目映像、新的项目映像或两者兼有。这使得复制、数据分析以及触发下游工作流等用例成为可能。

# PARAMETERS

**list-streams**
> 列出某个表或所有表的流 ARN。

**describe-stream**
> 获取流的元数据，包括分片信息。

**get-shard-iterator**
> 获取用于从分片读取记录的迭代器。

**get-records**
> 使用分片迭代器读取流记录。

**--stream-arn** _arn_
> 流的 Amazon 资源名称（ARN）。

**--table-name** _name_
> 按表名筛选流。

**--shard-id** _id_
> 要读取的分片的标识符。

**--shard-iterator** _string_
> 由 get-shard-iterator 返回的迭代器。

**--shard-iterator-type** _type_
> 开始读取的位置：TRIM_HORIZON（最旧）、LATEST（最新）、AT_SEQUENCE_NUMBER 或 AFTER_SEQUENCE_NUMBER。

**--sequence-number** _number_
> 从该序列号开始读取（需要 AT/AFTER_SEQUENCE_NUMBER 类型）。

**--limit** _number_
> 返回记录的最大数量。

# CAVEATS

分片迭代器会在 15 分钟后过期。流记录仅保留 24 小时。高吞吐量下分片可能分裂，需要编写逻辑来处理子分片。由于分片的内部机制，即使存在数据，get-records 调用也可能返回空结果；应持续轮询直到分片关闭。

# HISTORY

DynamoDB Streams 在 **AWS re:Invent 2014** 上发布，并于 **2015 年 7 月** 正式可用。其设计目标是实时处理 DynamoDB 的变更，与同期推出的面向 DynamoDB 的 AWS Lambda 触发器相辅相成。该功能可通过全局表支持跨区域复制。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-dynamodb](/man/aws-dynamodb)(1), [aws-lambda](/man/aws-lambda)(1), [aws-kinesis](/man/aws-kinesis)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/dynamodbstreams/index.html)```

<!-- verified: 2026-06-18 -->
