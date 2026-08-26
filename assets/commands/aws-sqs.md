# TAGLINE

管理 Simple Queue Service 队列和消息。

# TLDR

**创建新队列**

```aws sqs create-queue --queue-name [queue-name]```

**列出所有队列**

```aws sqs list-queues```

**获取队列的 URL**

```aws sqs get-queue-url --queue-name [queue-name]```

向队列**发送消息**

```aws sqs send-message --queue-url [queue-url] --message-body "[message content]"```

以长轮询方式**接收消息**（最多等待 20 秒）

```aws sqs receive-message --queue-url [queue-url] --max-number-of-messages [10] --wait-time-seconds [20]```

处理完成后**删除消息**

```aws sqs delete-message --queue-url [queue-url] --receipt-handle [handle]```

**清空**队列中的所有消息

```aws sqs purge-queue --queue-url [queue-url]```

**删除队列**

```aws sqs delete-queue --queue-url [queue-url]```

# SYNOPSIS

**aws sqs** _subcommand_ [_options_]

# DESCRIPTION

**aws sqs** 是 AWS CLI 中用于管理 Amazon Simple Queue Service（SQS）的接口。SQS 是一项全托管的消息队列服务，用于解耦和扩展分布式系统及无服务器应用。

SQS 提供两种队列类型：具有最大吞吐量和至少一次投递保证的标准队列，以及提供精确一次处理和有序投递的 FIFO 队列。消息最长可保留 14 天。

# SUBCOMMANDS

**Queue Management**
> create-queue, delete-queue, list-queues, get-queue-url, get-queue-attributes, set-queue-attributes, purge-queue

**Messaging**
> send-message, send-message-batch, receive-message, delete-message, delete-message-batch, change-message-visibility, change-message-visibility-batch

**Permissions**
> add-permission, remove-permission

**Tagging**
> tag-queue, untag-queue, list-queue-tags

**Dead-letter Queues**
> list-dead-letter-source-queues, start-message-move-task, cancel-message-move-task, list-message-move-tasks

# CAVEATS

消息在处理完成后必须显式删除；SQS 不会自动删除已消费的消息。可见性超时使正在处理的消息对其他消费者暂时不可见。标准队列可能重复投递消息；需要精确一次处理时请使用 FIFO 队列。单条消息最大为 256KB；更大的负载请使用 S3。

# HISTORY

Amazon SQS 于 **2006 年 7 月**上线，早于 S3，是 AWS 最早期服务之一。它于 **2014 年**重新设计，吞吐量和延迟得到显著改进。FIFO 队列于 **2016 年**加入，以支持有序的消息处理。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-sns](/man/aws-sns)(1), [aws-lambda](/man/aws-lambda)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/sqs/index.html)```

<!-- verified: 2026-06-18 -->
