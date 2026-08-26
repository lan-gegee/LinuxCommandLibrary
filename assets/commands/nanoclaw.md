# TAGLINE

带 WhatsApp 集成的容器化个人 AI 助手

# TLDR

**启动 nanoclaw 并运行初始设置**

```claude```

```/setup```

**通过 WhatsApp 触发词发送消息**

```@Andy [message]```

**安排周期性简报**

```@Andy schedule a daily news briefing at 8am```

**在群聊中提问**

```@Andy what's the weather forecast for today?```

# SYNOPSIS

**nanoclaw** (runs as a Claude agent via **claude** command, then **/setup**)

# PARAMETERS

**/setup**
> Claude 会话中的交互式设置向导，用于配置 WhatsApp 集成、定时任务和容器设置。

**@**_TRIGGER_ _MESSAGE_
> 使用配置的触发词（默认：@Andy）通过 WhatsApp 向 nanoclaw 发送消息。

# DESCRIPTION

**nanoclaw** 是一个由 Claude 驱动的轻量级个人 AI 助手，运行在隔离的容器环境中。它集成 WhatsApp，支持自然的消息式交互，让用户可以从任何设备与自己的 AI 助手交流。

每个群聊都拥有独立的隔离上下文，包括各自的记忆和沙盒化的文件系统，确保对话和数据相互分离。该助手支持定时任务自动化，可用于每日简报、新闻摘要和提醒等周期性任务。

nanoclaw 以单个 Node.js 进程运行，使用 SQLite 作为存储。它使用 Apple Container 或 Docker 实现隔离，并使用 Claude Agent SDK 提供 AI 能力。设置通过 **claude** 命令加 **/setup** 斜杠命令交互式完成。

# CAVEATS

需要 Claude API 密钥和 WhatsApp Business API 访问权限。容器隔离依赖于 Apple Container（macOS）或 Docker 的可用性。定时任务只在进程运行期间执行。WhatsApp 集成需要一个电话号码和企业账号设置。

# HISTORY

nanoclaw 由 **Gavriel Cohen** 创建，是一个专注于 WhatsApp 集成和容器化隔离的极简个人 AI 助手。其设计目标是在保持对话上下文之间严格安全边界的同时，提供比重量级助手框架更轻量的选择。

# SEE ALSO

[openclaw](/man/openclaw)(1), [nanobot](/man/nanobot)(1), [claude](/man/claude)(1), [leon](/man/leon)(1)
