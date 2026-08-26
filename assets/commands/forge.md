# TAGLINE

面向终端的开源 AI 编程助手

# TLDR

**启动交互式会话**

```forge```

**不进入交互模式直接执行提示词**

```forge -p "[fix the bug in main.rs]"```

**从文件执行命令**

```forge -c [commands.txt]```

**运行工作流**

```forge -w [workflow.yaml]```

**在沙箱化的 git worktree 中启动**

```forge --sandbox```

**配置 AI 提供商凭证**

```forge provider login```

**列出已配置的 MCP 服务器**

```forge mcp list```

# SYNOPSIS

**forge** [_options_]

# PARAMETERS

**-p**, **--prompt** _PROMPT_
> 直接处理的提示词，不进入交互模式

**-c**, **--command** _FILE_
> 包含待执行初始命令的文件路径

**-w**, **--workflow** _FILE_
> 包含待执行工作流的文件路径

**-e**, **--event** _EVENT_
> 向工作流派发一个事件

**--conversation-id** _ID_
> 按标识符恢复已有会话

**-C**, **--directory** _DIR_
> 在启动前设置工作目录

**--sandbox**
> 创建隔离的 git worktree 以便安全实验

**--agent** _AGENT_
> 指定本次会话使用的智能体

**-r**, **--restricted**
> 使用受限 Shell（rbash）以增强安全性

**--verbose**
> 启用详细输出模式

**-h**, **--help**
> 打印帮助信息

**-V**, **--version**
> 打印版本号

# CONFIGURATION

**forge.yaml**
> 项目级的 forge 设置与偏好配置。

**.mcp.json**
> Model Context Protocol（MCP）服务器配置。

**~/.forge/config.yaml**
> 全局用户配置，存放 API 密钥和默认设置。

# COMMANDS

**provider login**
> 交互式配置 AI 提供商凭证

**provider logout**
> 移除提供商凭证

**provider list**
> 显示受支持的 AI 提供商

**mcp list**
> 列出所有已配置的 MCP 服务器

**mcp add**
> 交互式添加新的 MCP 服务器

**mcp add-json**
> 用 JSON 格式添加 MCP 服务器

**mcp get**
> 查看特定 MCP 服务器的详情

**mcp remove**
> 移除 MCP 服务器

# DESCRIPTION

**Forge** 是一个在你的终端中原生工作的开源 AI 编程助手。它用 Rust 编写，与你现有的 shell（bash、zsh、fish）无缝集成，提供 AI 驱动的代码辅助，无需单独的 IDE 或图形界面。

Forge 支持 300 多种 AI 模型，包括 Claude、GPT、Gemini、Grok 和 DeepSeek。它采用多智能体架构，包含专门的智能体：负责实现的 **Forge**、负责规划的 **Muse**、负责文档审查的 **Prime**、负责技术写作的 **Parker**，以及负责代码库探索的 **Sage**。

该工具分析项目文件、依赖项和 Git 历史，以低于 50ms 的启动时间提供上下文感知的建议。所有操作都在本地运行，代码保留在你自己的机器上，兼顾隐私和安全。

# CAVEATS

需要来自受支持 AI 提供商的 API 密钥，通过 **forge provider login** 配置。**--restricted** 标志会限制 Shell 访问以增强安全性，但会降低功能性。

# HISTORY

Forge 由 **Antinomy** 开发，作为 Cursor 和 Claude Code 等专有 AI 编程工具的开源替代品。它以 Rust 编写以保证性能，并以开源许可证发布。项目托管于 github.com/antinomyhq/forge。

# INSTALL

```apt: sudo apt install snap```

```pacman: sudo pacman -S forge```

```zypper: sudo zypper install forge```

```brew: brew install snap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [aider](/man/aider)(1), [codex](/man/codex)(1), [opencode](/man/opencode)(1)
