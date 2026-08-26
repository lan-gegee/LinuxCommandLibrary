# TAGLINE

从终端检查 Kafka topic 中的消息

# TLDR

**启动 TUI** 检查 Kafka topic

```kplay tui [profile_name]```

**启动 Web 界面**浏览消息

```kplay serve [profile_name]```

**从指定偏移量开始消费**

```kplay tui [profile_name] -o [1000]```

**扫描消息并保存到本地**

```kplay scan [profile_name] -s -n [500]```

**将多个 profile 的消息转发到 S3**

```kplay forward [profile1],[profile2] [arn:aws:s3:::bucket/prefix]```

**使用自定义配置文件**

```kplay tui [profile_name] -c [path/to/config.yaml]```

# SYNOPSIS

**kplay** _command_ _profile_ [_flags_]

# PARAMETERS

**tui** _PROFILE_
> 启动终端用户界面，按需浏览消息。

**serve** _PROFILE_
> 启动一个用于浏览 topic 消息的 Web 界面。

**scan** _PROFILE_
> 扫描消息摘要，并可选择导出到本地。

**forward** _PROFILES_ _DESTINATION_
> 消费消息并转发到远程目的地（如 AWS S3）。

**-c**, **--config-path** _string_
> kplay 配置文件的位置（也可通过 $KPLAY_CONFIG_PATH 设置）。

**-o**, **--from-offset** _string_
> 从指定偏移量开始消费消息。

**-t**, **--from-timestamp** _string_
> 从指定时间戳开始消费（RFC3339 格式）。

**-n**, **--num-records** _uint_
> 要扫描的最大消息数（scan 子命令，默认 1000）。

**-O**, **--output-dir** _string_
> 持久化消息的目录（默认 $HOME/.kplay）。

**-s**, **--save-messages**
> 将消息导出到文件系统（scan 子命令）。

**-p**, **--persist-messages**
> 启动时启用消息持久化（tui 子命令）。

**--debug**
> 显示解析后的配置而不运行。

# DESCRIPTION

**kplay** (kafka-playground) 让你以简单而有节制的方式检查 Kafka topic 中的消息。它同时提供 TUI 和 Web 界面，可按需获取记录、以列表形式浏览、保存到本地，或转发到 S3。

消息可以按 **JSON**、**protobuf** 或 **raw** 格式解码。Profile 在 YAML 配置文件中定义，每个 profile 有自己的 broker、编码和身份验证细节。消息默认持久化到 **$HOME/.kplay**。

# CAVEATS

需要正在运行的 Kafka 集群和配置正确的 profile。使用前必须逐个 profile 设置好身份验证和编码。

# HISTORY

**kplay** 由 **dhth** 创建，使用 **Go** 编写。它的设计目标是简单、有节制地检查 Kafka 消息，避免全功能 Kafka 管理工具的开销。

# SEE ALSO

[kaskade](/man/kaskade)(1), [kcat](/man/kcat)(1)
