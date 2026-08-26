# TAGLINE

基于 xAI API 的 AI 终端编码智能体

# TLDR

在当前目录**启动交互式会话**

```grok```

**在特定目录中启动**

```grok -d [path/to/project]```

**执行一次性命令**后退出（无头模式）

```grok -p "[prompt]"```

**指定其他模型**

```grok -m [grok-4-latest]```

**使用自定义 API 密钥运行**

```grok -k [your_api_key]```

**添加 MCP 服务器**

```grok mcp add [server-name] --transport stdio --command bun --args [server.js]```

# SYNOPSIS

**grok** [_options_] [_prompt_]

**grok** **mcp** **add** _server-name_ [_--transport type_] [_--command cmd_] [_--args args_]

# PARAMETERS

**-V**, **--version**
> 显示版本信息。

**-d**, **--directory** _path_
> 设置会话的工作目录。

**-k**, **--api-key** _key_
> 提供 xAI Grok API 凭据。

**-u**, **--base-url** _url_
> 自定义 API 端点（默认：https://api.x.ai/v1）。

**-m**, **--model** _model_
> 指定 AI 模型（grok-4-latest、grok-3-latest、grok-3-fast、grok-3-mini-fast、grok-code-fast-1）。

**-p**, **--prompt** _text_
> 以无头模式执行单个提示词后退出。

**--max-tool-rounds** _n_
> 限制工具执行轮数。

**-h**, **--help**
> 显示帮助文档。

# DESCRIPTION

**Grok CLI** 是一款开源 AI 智能体，将 xAI 的 Grok 直接带入终端。它通过自然语言提供对话式界面，用于编程辅助、文件操作和 shell 命令执行。

该工具有两种模式：适用于持续对话长时间会话的交互模式，以及适用于脚本化自动化和一次性命令的无头模式（**-p**）。Grok 可以浏览代码库、查看和编辑文件、运行 bash 命令，并为请求的任务智能地选择合适的工具。

# CONFIGURATION

**~/.grok/user-settings.json**
> 用户级设置，包括 API 密钥、模型偏好和默认行为。

**.grok/settings.json**
> 项目级的工具权限和配置设置。

**.grok/GROK.md**
> 自动加载的项目级自定义指令。

# CAVEATS

需要从 xAI API 控制台获取 **xAI API 密钥**。该 CLI 默认使用 xAI API 端点，并要求 Node.js 18 或更高版本。API 用量受 xAI 的速率限制和计费约束。用于高速代码编辑的 Morph Fast Apply 功能需要额外配置。

# HISTORY

Grok CLI 作为开源项目于 **2024 年**问世，此前 xAI 公开发布了其 Grok API。它由 Superagent AI 社区构建，提供对 xAI Grok 模型的终端访问。**2025 年**，该工具作为专有编程助手的挑战者获得了显著关注；xAI 又于 **2026 年 1 月**宣布了官方的 **Grok Build** 编码智能体，以提供第一方的 CLI 支持。

# INSTALL

```brew: brew install grok```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grok-build](/man/grok-build)(1), [claude](/man/claude)(1), [copilot](/man/copilot)(1), [gh](/man/gh)(1)
