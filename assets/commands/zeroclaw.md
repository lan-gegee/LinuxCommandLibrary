# TAGLINE

用 Rust 构建的自主式 AI 智能体运行时

# TLDR

**初始化**配置，使用交互式设置向导

```zeroclaw onboard --interactive```

**启动交互式** CLI 智能体会话

```zeroclaw agent```

**发送单条消息**，不进入交互模式

```zeroclaw agent -m "[message]"```

**启动完整的自主守护进程**，包含通道与调度器

```zeroclaw daemon```

**检查系统健康状态**并运行诊断

```zeroclaw doctor```

**列出所有支持的** LLM 提供商

```zeroclaw providers```

# SYNOPSIS

**zeroclaw** [_command_] [_subcommand_] [_options_]

# PARAMETERS

**onboard**
> 初始化或重新配置工作区。会创建 **~/.zeroclaw/config.toml** 和脚手架文件。

**onboard --interactive**
> 运行完整的 9 步配置向导。

**onboard --api-key** _KEY_ **--provider** _PROVIDER_ [**--model** _MODEL_]
> 一条命令内以 API 密钥和提供商完成非交互式设置。

**onboard --channels-only**
> 仅修复或重新配置通道与允许列表。

**agent** [**-m** _MESSAGE_]
> 运行交互式 CLI 智能体，或用 **-m** 发送单条消息。

**agent --provider** _PROVIDER_
> 为本次会话覆盖默认提供商。

**gateway** [**--port** _PORT_]
> 启动供外部集成使用的 HTTP/WebSocket 服务器。默认端口：42617。

**daemon**
> 启动包含 gateway、通道、心跳和调度器的完整自主运行时。

**status**
> 显示全面的系统状态，包括提供商、内存、通道和安全。

**doctor** [**models** | **traces**]
> 运行系统诊断。可选检查模型目录或查看运行时追踪。

**service install** | **start** | **stop** | **status** | **restart**
> 将 zeroclaw 作为后台系统服务管理（systemd 或 OpenRC）。

**channel list** | **doctor** | **start**
> 列出、健康检查或启动已配置的消息通道。

**channel add** _TYPE_ _JSON_CONFIG_
> 添加新的消息通道配置。

**channel bind-telegram** _USER_ID_
> 将 Telegram 用户加入允许列表。

**auth login** _PROVIDER_ [_PROFILE_]
> 通过 OAuth 或设备码流程进行身份验证。

**auth status** | **logout** _PROFILE_ID_
> 显示或移除身份验证配置档案。

**memory stats** | **list** | **search** _QUERY_ | **delete** _KEY_ | **prune**
> 管理内置的记忆系统。

**cron add** _NAME_ _SCHEDULE_ _MESSAGE_ [**--tz** _TIMEZONE_]
> 使用 cron 表达式安排周期性任务。

**cron list** | **remove** _NAME_
> 列出或移除计划任务。

**skills list** | **install** _NAME_ | **remove** _NAME_
> 管理智能体技能和扩展。

**migrate openclaw** [**--dry-run**]
> 从 OpenClaw 运行时导入记忆。

**completions** _SHELL_
> 为 bash、zsh、fish、powershell 或 nushell 生成 Shell 补全。

**providers**
> 列出所有支持的 LLM 提供商及别名。

**estop** [**--resume**]
> 触发紧急停止或从中恢复。

# DESCRIPTION

**zeroclaw** 是一个轻量级、安全优先的自主式 AI 智能体运行时，完全用 Rust 构建。它是智能体工作流的基础设施，将模型、工具、记忆和执行抽象为一个二进制文件，可部署于 ARM、x86 和 RISC-V 架构。

该运行时编译后约为 9MB 的二进制文件，冷启动低于 10 毫秒，空闲时内存占用不足 5MB。它采用 trait 驱动的架构，提供商、通道、记忆后端和工具都可以通过配置更换而无需修改代码。

ZeroClaw 内置混合搜索记忆系统，将向量嵌入与关键词搜索相结合（基于 SQLite），无需外部依赖。它支持 28 个以上的 LLM 提供商，包括 OpenRouter、Anthropic、OpenAI、Gemini、Ollama 以及任何 OpenAI 兼容端点。消息集成覆盖 70 多个通道，包括 Telegram、Discord、Slack、iMessage、Matrix、Signal 和 WhatsApp。

该智能体支持保留上下文的多轮对话、工具执行（shell、文件、git、浏览器）、基于 cron 表达式的定时任务，以及面向 IoT 设备的硬件外设控制。

# CONFIGURATION

配置存储在 **~/.zeroclaw/config.toml** 中。运行 **zeroclaw onboard --interactive** 进行引导式设置。

```
[providers]
default = "openrouter"

[providers.openrouter]
api_key = "sk-or-v1-xxx"
model = "anthropic/claude-opus-4-5"

[memory]
backend = "sqlite"

[runtime]
kind = "native"

[channels.telegram]
bot_token = "123:ABC..."
allowed_users = ["123456789"]
```

支持的记忆后端：**sqlite**（默认，混合搜索）、**postgres**、**markdown** 和 **none**（无状态）。

环境变量可覆盖配置值：**ZEROCLAW_API_KEY**、**ZEROCLAW_PROVIDER**、**ZEROCLAW_MODEL**、**ZEROCLAW_WORKSPACE**。

# CAVEATS

ZeroClaw 会以你的用户权限执行 shell 命令和文件操作。启用工具使用时，智能体可以修改文件并运行任意命令。API 密钥存储在 **config.toml** 和 **auth-profiles.json** 中（若启用了密钥加密则静态加密存储）。通道集成要求守护进程处于运行状态。由于需要 Rust 工具链，从源码编译至少需要 2GB 内存和 6GB 磁盘空间。

# HISTORY

ZeroClaw 由 **ZeroClaw Labs** 创建，于 **2025 年**首次发布，作为现有 AI 智能体运行时的 Rust 替代方案。它围绕零开销和零锁定的原则设计，目标是部署在资源受限的硬件上，同时保持生产级的可扩展性。该项目引入了 trait 驱动的架构，使提供商、通道和工具可以在不改动代码的情况下替换，并以低于 10 毫秒的冷启动时间和单二进制部署模型受到关注。

# INSTALL

```brew: brew install zeroclaw```

```nix: nix profile install nixpkgs#zeroclaw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nanobot](/man/nanobot)(1), [picoclaw](/man/picoclaw)(1), [claude](/man/claude)(1), [openclaw](/man/openclaw)(1)
