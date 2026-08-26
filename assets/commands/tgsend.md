# TAGLINE

通过 Bot API 发送 Telegram 消息

# TLDR

**发送消息**

```tgsend "[message]"```

**发送到特定聊天**

```tgsend -c [chat_id] "[message]"```

**发送文件**

```tgsend -f [document.pdf]```

**发送图片**

```tgsend -p [image.jpg]```

**带说明文字发送**

```tgsend -p [image.jpg] -m "[caption]"```

**静默消息**

```tgsend -s "[message]"```

# SYNOPSIS

**tgsend** [_-c chat_id_] [_-f file_] [_-p photo_] [_options_] [_message_]

# PARAMETERS

**-c** _ID_
> 聊天 ID。

**-f** _FILE_
> 发送文件。

**-p** _FILE_
> 发送图片。

**-m** _TEXT_
> 说明文字。

**-s**
> 静默模式。

**-t** _TOKEN_
> Bot 令牌。

# DESCRIPTION

**tgsend** 使用 Telegram Bot API 向 Telegram 聊天发送消息、文件和图片。它专为自动化和脚本化场景设计，可以从命令行或 cron 任务发送通知、警报和文件。

消息可以通过聊天 ID 发送到指定聊天，媒体附件可通过 **-m** 标志附带说明文字。**-s** 标志以静默方式发送消息，不会在接收方设备上触发通知。需要 bot 令牌，可通过 **-t** 标志或环境配置传入。

# CAVEATS

需要 bot 令牌。需要聊天 ID。受速率限制约束。

# HISTORY

**tgsend** 是一款通过 Telegram Bot API 发送消息的轻量级 CLI 工具，常用于 DevOps 工作流中的告警和自动化。

# SEE ALSO

[telegram-desktop](/man/telegram-desktop)(1), [curl](/man/curl)(1)
