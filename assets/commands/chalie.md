# TAGLINE

带持久记忆的本地个人 AI 伴侣

# TLDR

使用官方安装脚本**安装**

```curl -fsSL https://chalie.ai/install | bash```

在默认端口（31025）上**启动**

```chalie```

在自定义端口上**启动**

```chalie --port=[9000]```

**停止**守护进程

```chalie stop```

**重启**守护进程

```chalie restart```

**更新**到最新版本

```chalie update```

**检查**是否正在运行

```chalie status```

**跟踪**日志文件

```chalie logs```

# SYNOPSIS

**chalie** [**--port=**_N_] [**--host=**_H_] [_command_]

# DESCRIPTION

**chalie** 是一款运行在你机器上的开源个人 AI。它在后台持续运行，具备持久记忆（带衰减机制的情节、概念与抽象）、目标追踪和主动调研能力。所有操作都遵循 Allow / Ask / Deny 策略，未经同意不会擅自行动。

它是单个 Python 进程（Flask + WebSocket），使用 SQLite 存储（含向量搜索和 FTS 全文搜索）。可选的本地语音功能基于 ONNX STT/TTS。特性包括视觉能力（照片/截图）、受控浏览器、MCP 客户端与工具、邮件/日历/联系人（IMAP、CalDAV、CardDAV）、自然语言日程安排、受保护的 shell 和沙箱化代码执行，以及整实例加密备份。模型可以是云服务商（OpenAI、Anthropic、Gemini），也可以通过 **ollama** 本地运行。默认 Web UI：**http://localhost:31025**。

# PARAMETERS

**start**

> 在后台启动守护进程（未给出命令时的默认行为）。将 PID 写入 **~/.chalie/chalie.pid**，日志写入 **~/.chalie/chalie.log**。

**stop**

> 停止运行中的实例并删除 PID 文件。

**restart**

> 先停止，再以相同的 port/host 选项重新启动。

**update**

> 停止，重新运行安装程序获取最新版本，然后再次启动。

**status**

> 打印 Chalie 是否在运行及其 PID。

**logs**

> 当 stdout 是终端时跟踪 **~/.chalie/chalie.log**；否则打印最后 50 行。

**version**, **-V**, **--version**

> 打印已安装的版本号。

**--port=**_N_, **--port** _N_

> 监听端口（默认：**31025**）。

**--host=**_H_, **--host** _H_

> 绑定地址（默认：**0.0.0.0**）。若希望 UI 仅限本机访问，请使用 **127.0.0.1**。

# CONFIGURATION

**~/.chalie/**

> 安装主目录：虚拟环境（**venv/**）、应用源码（**app/**）、PID 和日志文件。

**~/.chalie/app/data/**

> 持久化的实例数据（SQLite 及相关状态）。升级时不会被覆盖。

**CHALIE_HOME**

> 覆盖安装主目录（默认 **$HOME/.chalie**）。

**CHALIE_VENV**

> **run.sh** 所用 Python 虚拟环境的路径（由安装器 CLI 设置）。

首次启动会打开引导向导以选择模型提供商。完全本地化的方案：安装 **ollama** 并拉取一个受支持的模型，然后在设置过程中让 Chalie 指向它。

# CAVEATS

需要 Python 3.11+。软件处于 Beta 阶段：难免有粗糙之处。首次启动可能下载较大的嵌入模型（约 400 MB）。绑定 **0.0.0.0** 会把 UI 暴露到网络——如果机器是共享的，请用 **--host=127.0.0.1** 或防火墙加以限制。确保 **~/.local/bin** 位于 **PATH** 中，以便安装后能找到 **chalie** 包装脚本。

# HISTORY

**Chalie** 是一款开源的个人 AI 伴侣，专注于长期运行的本地自主行为和克制的行动策略，而不是单次会话聊天。它以 Apache 2.0 许可证发布。

# SEE ALSO

[ollama](/man/ollama)(1), [llm](/man/llm)(1), [aichat](/man/aichat)(1), [sgpt](/man/sgpt)(1)

# RESOURCES

```[Source code](https://github.com/chalie-ai/chalie)```

```[Homepage](https://chalie.ai)```

```[Documentation](https://chalie.ai/docs)```

<!-- verified: 2026-07-20 -->
