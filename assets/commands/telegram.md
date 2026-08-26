# TAGLINE

从 Shell 发送 Telegram 消息和文件

# TLDR

**发送文本消息**

```telegram "Hello, World."```

**显式指定 token 和 chat id 发送**

```telegram -t [BOT_TOKEN] -c [CHAT_ID] "Hello, World."```

**通过 stdin 发送多行文本**（等宽字体）

```ls -l | telegram -```

**发送 Markdown**

```telegram -M "To *boldly* go, where _no man_ has gone before."```

**带说明文字发送文件**

```telegram -f [results.txt] "Here are the results."```

**发送图片**

```telegram -i [photo.png]```

**发送视频**

```telegram -V [video.mp4]```

**列出已知的聊天**（美化输出需要 **jq**）

```telegram -t [BOT_TOKEN] -l```

**读取最后收到的消息**

```telegram -m```

# SYNOPSIS

**telegram** [**-t** *token*] [**-c** *chat_id*]... [**-f** *file* | **-i** *image* | **-V** *video*] [**-M** | **-H**] [*message* | **-**]

# DESCRIPTION

**telegram**（来自 **telegram.sh** 项目的脚本）使用 **bash** 和 **curl** 通过 Telegram Bot API 发送消息、文件、图片和视频。典型用途包括 cron 通知、把服务器上的小文件绕过棘手的网络路径传送出去，以及把命令输出管道发给自己。

先用 **@BotFather** 创建一个机器人，在你的客户端中给它发一条消息，然后用 **telegram -t** *token* **-l** 找到你的 **chat_id**。token 和 chat id 可以通过标志、环境变量（**TELEGRAM_TOKEN**、**TELEGRAM_CHAT**）或配置文件提供（见 CONFIGURATION）。多个 **-c** 值可以发送到多个聊天。

# PARAMETERS

**-t** *token*

> 来自 BotFather 的 Bot API token。

**-c** *chat_id*

> 目标聊天 ID；可重复使用以发送到多个聊天。

**-f** *file*

> 发送文档/文件。

**-i** *image*

> 发送带预览的图片。

**-V** *video*

> 发送视频文件。

**-M**

> 将消息按 Markdown 解析。

**-H**

> 将消息按 HTML 解析（需要你的脚本版本支持）。

**-l**

> 列出该机器人已知的聊天（**jq** 可改善格式化）。

**-m**

> 打印最后收到的消息：消息 ID、发送者 ID、聊天 ID、文本。

**-**

> 从 stdin 读取消息正文（管道输入时以等宽字体发送）。

*message*

> 要发送的文本；可以包含 shell 换行符。

代理：设置 **HTTPS_PROXY**（或写入配置文件），即可使用 curl 支持的代理，例如 **socks5://127.0.0.1:1234**。

# CONFIGURATION

设置按顺序加载（后者优先）：

1. **/etc/telegram.sh.conf**
2. **~/.telegram.sh**
3. **~/.telegram.sh.conf**
4. **./telegram.sh.conf**（与脚本同目录）
5. 环境变量 **TELEGRAM_TOKEN** / **TELEGRAM_CHAT**
6. 命令行标志

配置文件示例：

```
TELEGRAM_TOKEN="123456:AbcDefGhi-JlkMno"
TELEGRAM_CHAT="12345678"
```

多个聊天可以用 bash 数组 **CHATS=(...)** 定义。请妥善保管 bot token。

# CAVEATS

只需要 **bash** 和 **curl**；**-l** 的美化输出需要 **jq**。消息大小和媒体类型受 Telegram Bot API 限制。token 或 chat id 配置错误会在 API 层面失败。这不是官方的 Telegram Desktop 客户端（**telegram-desktop**）。

# SEE ALSO

[curl](/man/curl)(1), [jq](/man/jq)(1), [notify-send](/man/notify-send)(1)

# RESOURCES

```[Source code](https://github.com/fabianonline/telegram.sh)```

<!-- verified: 2026-07-19 -->
