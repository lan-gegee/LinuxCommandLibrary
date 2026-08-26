# TAGLINE

管理 Amazon Data Firehose 传输流

# TLDR

**列出所有传输流**

```aws firehose list-delivery-streams```

**查看传输流**

```aws firehose describe-delivery-stream --delivery-stream-name [stream_name]```

**创建到 S3 的传输流**

```aws firehose create-delivery-stream --delivery-stream-name [stream_name] --s3-destination-configuration RoleARN=[role_arn],BucketARN=[bucket_arn]```

**向传输流写入单条记录**

```aws firehose put-record --delivery-stream-name [stream_name] --record Data=[base64_encoded_data]```

**批量写入多条记录**

```aws firehose put-record-batch --delivery-stream-name [stream_name] --records Data=[data1] Data=[data2]```

**更新传输流目标**

```aws firehose update-destination --delivery-stream-name [stream_name] --current-delivery-stream-version-id [version] --destination-id [dest_id] --s3-destination-update BucketARN=[new_bucket_arn]```

**删除传输流**

```aws firehose delete-delivery-stream --delivery-stream-name [stream_name]```

# SYNOPSIS

**aws firehose** _subcommand_ [_options_]

# DESCRIPTION

**aws firehose** 是 AWS CLI 的子命令，用于管理 Amazon Data Firehose（前身为 Kinesis Data Firehose）——一项将流式数据加载到数据存储和分析服务中的服务。

Firehose 在把数据传送到 S3、Redshift、OpenSearch、Splunk 或 HTTP 端点等目的地之前，会自动进行批处理、压缩、转换和加密。它无需预置资源即可自动扩缩。

数据可通过 put-record API 直接发送，也可从 Kinesis Data Streams 摄取。Firehose 在传送之前按大小（1-128 MB）或时间（60-900 秒）缓冲记录。

# PARAMETERS

**list-delivery-streams**
> 列出账户中的所有传输流。

**describe-delivery-stream**
> 获取流的详细配置。

**create-delivery-stream**
> 创建新的传输流。

**delete-delivery-stream**
> 删除传输流。

**put-record**
> 发送单条数据记录。

**put-record-batch**
> 在一个请求中发送多条记录。

**update-destination**
> 修改目标配置。

**start-delivery-stream-encryption**
> 启用服务器端加密。

**stop-delivery-stream-encryption**
> 禁用加密。

**--delivery-stream-name** _name_
> 传输流名称。

**--record** _data_
> 带 Data 字段（base64）的单条记录。

**--records** _records_
> 用于批量写入的记录数组。

**--s3-destination-configuration** _config_
> S3 目标设置。

**--redshift-destination-configuration** _config_
> Redshift 目标设置。

**--extended-s3-destination-configuration** _config_
> 带数据转换设置的 S3 目标配置。

# CAVEATS

使用 CLI 时记录数据必须经过 base64 编码。单条记录最大为 1 MB。批量写入每次请求最多接受 500 条记录或 4 MB。传输流无法重命名；只能另建新的。缓冲间隔会造成传送延迟。发往 Redshift 失败的记录会作为备份写入 S3。

# HISTORY

**Amazon Kinesis Firehose** 于 **2015 年 10 月** 推出，是将流式数据加载到 AWS 的最简单方式。为了体现其已超越 Kinesis 集成的更广定位，于 **2024 年 2 月** 更名为 **Amazon Data Firehose**。其目的地也从最初的 S3 和 Redshift 逐步扩展到 OpenSearch、Splunk 和自定义 HTTP 端点。动态分区功能于 **2021 年** 加入，支持高效的数据湖模式。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-kinesis](/man/aws-kinesis)(1), [aws-s3](/man/aws-s3)(1), [aws-redshift](/man/aws-redshift)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/firehose/index.html)```

<!-- verified: 2026-06-18 -->
