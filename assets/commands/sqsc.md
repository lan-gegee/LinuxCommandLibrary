# TAGLINE

AWS SQS 队列管理 CLI

# TLDR

**列出队列**

```sqsc list```

**发送消息**

```sqsc send [queue-url] "[message]"```

**接收消息**

```sqsc receive [queue-url]```

**删除消息**

```sqsc delete [queue-url] [receipt-handle]```

**清空队列**

```sqsc purge [queue-url]```

**创建队列**

```sqsc create [queue-name]```

# SYNOPSIS

**sqsc** _command_ [_options_] [_args_]

# PARAMETERS

**list**
> 列出队列。

**send**
> 发送消息。

**receive**
> 接收消息。

**delete**
> 删除消息。

**purge**
> 清空队列。

**create**
> 创建队列。

**--region** _REGION_
> AWS 区域。

# DESCRIPTION

**sqsc** 是 Amazon Simple Queue Service（SQS）的命令行客户端。它提供队列管理操作，包括创建队列、发送和接收消息、删除已处理的消息以及清空队列。

该工具使用标准的 AWS 凭据配置进行身份验证。它支持常见的 SQS 工作流，例如向队列 URL 发送消息、批量接收消息进行处理，以及在成功处理后通过 receipt handle 删除消息。

# CAVEATS

需要 AWS 账户。需要凭据。结果因区域而异。

# HISTORY

**sqsc** 是 Amazon Simple Queue Service 的轻量级命令行客户端，旨在替代繁琐的 AWS CLI，覆盖列出、发送、接收和清空队列等常见 SQS 操作。

# SEE ALSO

[aws](/man/aws)(1)
