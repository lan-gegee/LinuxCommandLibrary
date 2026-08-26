# TAGLINE

超轻量级个人 AI 助手

# TLDR

**初始化**配置并设置凭据

```nanobot onboard```

与 AI 智能体**开始交互式** CLI 聊天会话

```nanobot agent```

**启动多通道网关**以集成聊天平台

```nanobot gateway```

**发送单条消息**后退出

```nanobot agent [-m|--message] "[Hello!]"```

向聊天平台**进行认证**（如 WhatsApp 二维码配对）

```nanobot channels login```

**显示当前配置**和提供商状态

```nanobot status```

# SYNOPSIS

**nanobot** [_command_] [_options_]

# PARAMETERS

**onboard**
> 初始化配置并为首次使用准备环境。在 **~/.nanobot/config.json** 创建配置文件。

**agent** [_options_]
> 与 AI 智能体开始交互式 CLI 聊天会话。使用 **-m** 进入单条消息模式。

**gateway** [_options_]
> 运行多通道网关，连接 Telegram、Discord、WhatsApp、Slack 等聊天平台。使用 **-p** 指定自定义端口。

**status**
> 显示当前配置路径、工作区位置、所选模型和 API 密钥状态。

**channels login**
> 向聊天平台认证，主要用于 WhatsApp 二维码配对。

**channels status**
> 显示所有受支持平台的启用/禁用状态。

**cron list** [_options_]
> 列出已调度的任务。使用 **-a** 包含已禁用的任务。

**cron add** [_options_]
> 创建定时任务，使用 **-n** 指定名称、**-m** 指定消息，以及调度选项。

**provider login** _provider_
> 为支持的提供商进行 OAuth 认证（openai-codex、github-copilot）。

# DESCRIPTION

**nanobot** 是一个超轻量级的个人 AI 助手，用约 4000 行 Python 代码实现核心智能体功能。它将闭源和开源 LLM 连接到本地编码智能体，后者可以在你的机器上运行命令、读取日志、执行脚本和搜索文件。

Nanobot 支持多种 LLM 提供商，包括 OpenRouter、Anthropic（Claude）、OpenAI（GPT）、DeepSeek、Google Gemini、Groq 以及自定义的 OpenAI 兼容端点。它集成了 Telegram、Discord、WhatsApp、飞书、Slack、电子邮件、QQ、钉钉和 Mochat 等聊天平台，可通过 gateway 命令让智能体从各种消息服务中访问。

该工具使用 MCP（Model Context Protocol，模型上下文协议）通过外部工具和服务扩展能力。

# CONFIGURATION

配置保存在 **~/.nanobot/config.json**。运行 **nanobot onboard** 进行交互式设置。

最小配置需要提供商 API 密钥和模型选择：

```
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  },
  "agents": {
    "defaults": {
      "model": "anthropic/claude-sonnet-4"
    }
  }
}
```

支持的提供商：**openrouter**、**anthropic**、**openai**、**deepseek**、**groq**、**gemini**、**minimax** 和 **custom**（任何 OpenAI 兼容端点）。

# CAVEATS

Nanobot 会以你的用户权限在本地机器上执行命令。授予广泛的工具访问权限之前，务必审查智能体的操作。该工具需要网络访问以调用 LLM API 和集成聊天平台。提供商 API 密钥以明文形式存储在配置文件中。

# HISTORY

Nanobot 由 **HKUDS**（香港大学数据科学实验室）开发，是大型 AI 编程助手的超轻量替代品。它于 **2025 年**首次发布，旨在用极小的代码库提供核心智能体功能，强调研究可用性和简洁、可修改的架构。该项目作为开发者探索智能体 AI 工作流的易入门选择而获得关注。

# INSTALL

```brew: brew install nanobot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[picoclaw](/man/picoclaw)(1), [claude](/man/claude)(1)
