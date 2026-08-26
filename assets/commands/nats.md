# TAGLINE

NATS 消息系统的 CLI

# TLDR

**发布消息**

```nats pub [subject] "[message]"```

**订阅主题**

```nats sub [subject]```

**请求/应答**

```nats req [subject] "[request]"```

**应答请求**

```nats reply [subject] "[response]"```

**列出流（JetStream）**

```nats stream ls```

**创建流**

```nats stream add [stream-name]```

**发布到流**

```nats pub [subject] "[message]"```

**查看服务器信息**

```nats server info```

# SYNOPSIS

**nats** _command_ [_options_] [_args_...]

# COMMANDS

**pub** _subject_ [_message_]
> 向主题发布消息。

**sub** _subject_
> 订阅主题。

**req** _subject_ [_payload_]
> 发送请求并等待应答。

**reply** _subject_ [_response_]
> 应答主题上的请求。

**stream** ls|add|info|rm|edit|purge
> 管理 JetStream 流。

**consumer** ls|add|info|rm|next
> 管理流的消费者。

**kv** add|get|put|del|ls
> 键值存储操作。

**object** add|get|put|del|ls
> 对象存储操作。

**server** info|list|ping|report
> 服务器信息。

**account** info
> 账户信息。

**context** add|select|ls|rm
> 管理连接上下文。

# PARAMETERS

**-s**, **--server** _url_
> NATS 服务器 URL。默认：nats://localhost:4222。

**--creds** _file_
> 用于认证的凭据文件。

**--user** _user_
> 用于认证的用户名。

**--password** _pass_
> 用于认证的密码。

**--nkey** _file_
> 用于认证的 NKey 文件。

**--tlscert** _file_
> TLS 客户端证书。

**--tlskey** _file_
> TLS 客户端密钥。

**--context** _name_
> 使用指定的命名上下文。

# DESCRIPTION

**nats** 是 NATS 消息系统的 CLI。它提供发布/订阅消息、请求/应答模式以及 JetStream 持久化操作。

Core NATS 提供至多一次（at-most-once）的消息传递。**pub** 发送消息，**sub** 接收消息。主题通配符：**\*** 匹配单个 token，**>** 匹配多个 token。

JetStream 通过流和消费者增加持久化能力。**stream add** 创建持久存储；消费者负责跟踪投递。键值存储和对象存储是 JetStream 之上的更高层抽象。

上下文保存多个环境的连接详情。使用 **context add** 创建，使用 **context select** 切换。

请求/应答支持 RPC 模式。**req** 发送并等待响应；服务端使用 **reply** 或自定义订阅者进行应答。

# CAVEATS

Core NATS 是发后即忘的；需要投递保证请使用 JetStream。主题命名使用点号分隔。大消息可能需要额外配置。上下文会将凭据保存在磁盘上。

# HISTORY

NATS 由 **Derek Collison** 创建，**2010 年**作为 Ruby gem 首次发布，**2012 年**用 Go 重写。它最初在 Apcera 使用，**2018 年**成为 CNCF 孵化项目，**2023 年**毕业。JetStream 在 NATS 2.2（2021 年）中加入持久化。该系统强调云原生消息传递的简洁性、性能和易运维性。

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(1), [mosquitto_pub](/man/mosquitto_pub)(1)
