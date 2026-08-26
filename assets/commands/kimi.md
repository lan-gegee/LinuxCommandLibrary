# TAGLINE

Moonshot AI 的命令行智能体，用于 AI 驱动的编程和终端操作

# TLDR

**启动交互式会话**

```kimi```

**切换到智能体模式**

在交互式会话中按 **Ctrl+K**

**执行 shell 命令**

在交互式会话中按 **Ctrl+X**

**作为 ACP 服务器启动以集成 IDE**

```kimi acp```

**添加 HTTP MCP 服务器**

```kimi mcp add --transport http [name] [url]```

**添加 stdio MCP 服务器**

```kimi mcp add --transport stdio [name] -- [command] [args]```

**列出已配置的 MCP 服务器**

```kimi mcp list```

**移除 MCP 服务器**

```kimi mcp remove [name]```

# SYNOPSIS

**kimi** [_command_] [_options_]

# COMMANDS

**acp**
> 作为 Agent Client Protocol 服务器启动以集成 IDE

**mcp add**
> 添加新的 MCP（Model Context Protocol）服务器

**mcp list**
> 列出已配置的 MCP 服务器

**mcp remove**
> 移除 MCP 服务器

**mcp auth**
> 对 MCP 服务器进行身份验证

# MCP OPTIONS

**--transport** _TYPE_
> 传输类型：http 或 stdio

**--auth oauth**
> HTTP 传输使用 OAuth 身份验证

**--header** _"KEY: value"_
> 为 HTTP 传输添加自定义请求头

**--mcp-config-file** _PATH_
> 使用 JSON 配置文件连接 MCP 服务器

# KEYBOARD SHORTCUTS

**Ctrl+K**
> 切换到智能体模式

**Ctrl+X**
> 直接执行 shell 命令

# DESCRIPTION

**Kimi CLI** 是 Moonshot AI 推出的命令行智能体，用于 AI 驱动的编程和终端操作。它采用双模式交互设计，将传统的 shell 操作与智能代理能力结合在一起，只需一个按键即可切换。

该工具支持三种 UI 模式：交互式终端界面的 shell 模式、用于非交互式脚本的 print 模式，以及用于编辑器集成的 ACP 模式。它可以读取和编辑代码、执行 shell 命令、搜索并抓取网页，还能在执行过程中自主规划和调整行动。

Kimi CLI 基于 Python 3.13+ 和异步模式构建，默认使用 Moonshot AI 的 Kimi API，同时通过 kosong 框架支持任何 OpenAI 兼容端点。它集成了 MCP 服务器以扩展工具功能。

# CAVEATS

目前处于技术预览阶段。需要 Python 3.13+ 以及 Moonshot AI API 访问权限。MCP 服务器配置使用 JSON 格式。ACP 协议支持与 Zed 等编辑器集成，但需要先通过 **/setup** 命令进行初始配置。

# HISTORY

Kimi CLI 由 **Moonshot AI** 开发，以 Apache 2.0 许可证开源发布。它由 Kimi K2 模型驱动——这是一个先进的混合专家（MoE）模型，拥有 320 亿激活参数和 1 万亿总参数，专为智能体能力优化。

# SEE ALSO

[claude](/man/claude)(1), [gemini](/man/gemini)(1), [codex](/man/codex)(1), [qwen-code](/man/qwen-code)(1)
