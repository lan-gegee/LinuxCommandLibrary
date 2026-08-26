# TAGLINE

在终端、桌面或 IDE 中运行的开源 AI 编程智能体

# TLDR

**启动交互式 TUI**

```opencode```

**打开特定项目目录**

```opencode [path/to/project]```

**非交互式运行提示词**

```opencode run "[fix the bug in main.go]"```

**使用指定模型**

```opencode --model [anthropic/claude-sonnet-4]```

**继续最近一次会话**

```opencode --continue```

**恢复特定会话**

```opencode --session [session_id]```

**启动 Web 界面**

```opencode web```

**列出可用模型**

```opencode models```

# SYNOPSIS

**opencode** [_command_] [_options_] [_project_]

# PARAMETERS

**--model**, **-m** _PROVIDER/MODEL_
> 指定要使用的 AI 模型（例如 anthropic/claude-sonnet-4、openai/gpt-4o）

**--continue**, **-c**
> 恢复最近一次会话

**--session**, **-s** _ID_
> 按 ID 继续特定会话

**--prompt** _TEXT_
> 启动时提供初始提示词

**--agent** _NAME_
> 选择特定智能体（build、plan 或自定义）

**--port** _NUMBER_
> web 或 serve 命令使用的服务器端口

**--help**, **-h**
> 显示帮助信息

**--version**, **-v**
> 显示版本号

# COMMANDS

**run**
> 非交互式执行一个提示词后退出

**serve**
> 启动无头服务器以供 API 访问

**web**
> 启动带 HTTP 服务器的 Web 界面

**attach**
> 将 TUI 连接到远程 OpenCode 服务器

**auth login**
> 配置提供商的 API 密钥

**models**
> 显示已配置提供商的所有可用模型

**session list**
> 显示所有已保存的会话

**stats**
> 查看 token 用量与费用分析

**mcp add**
> 注册 MCP（Model Context Protocol）服务器

# DESCRIPTION

**OpenCode** 是一个开源的 AI 编程智能体，可以在终端、桌面或 IDE 中运行。它提供与 Claude Code 相当的能力，且不会将你锁定在单一模型或平台上，支持超过 75 种 AI 模型，包括 Claude、GPT、Gemini 和本地模型。

默认的 TUI 模式提供交互式聊天界面，内置两种智能体：**build**（拥有完整开发权限）和 **plan**（只读分析）。用 Tab 键即可在两者间切换。OpenCode 与 Language Server Protocol 集成提供代码智能，并可接入你的 GitHub 工作流实现 CI/CD 自动化。

与云端助手不同，OpenCode 让你掌控自己的数据。由你选择模型提供商以及共享哪些内容。运行本地模型可以让整个工作流程完全私密。

# CAVEATS

使用云模型提供商需要 API 密钥（通过 **opencode auth login** 配置）。对大型代码库而言，token 用量可能相当可观。该工具默认启动 TUI，需要兼容的终端模拟器。

# HISTORY

OpenCode 由 SST（Serverless Stack）团队的 **Jay V**、**Frank Wang**、**Dax Raad** 和 **Adam Elmore** 创建，于 **2024 年 6 月 19 日**发布，以回应专有 AI 编程助手的兴起。该项目在五个月内增长到每月 **65 万用户**，GitHub 星标超过 **7 万**。它采用 MIT 许可证发布。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aider](/man/aider)(1), [claude](/man/claude)(1), [copilot](/man/copilot)(1)
