# TAGLINE

AWS 出品的 AI 驱动终端助手

# TLDR

**启动交互式聊天会话**

```q chat```

**直接提问**

```q chat "[How do I list EC2 instances?]"```

**将自然语言翻译为 shell 命令**

```q translate "[find all Python files modified in the last week]"```

**以非交互模式运行并自动批准工具**

```q chat --no-interactive --trust-all-tools "[create a hello world script]"```

**恢复上一次聊天会话**

```q chat --resume```

**使用指定的智能体**

```q chat --agent [my-agent] "[help with AWS CLI]"```

**诊断并修复常见问题**

```q doctor```

**启用或禁用自动补全集成**

```q integrations install```

**查看当前版本**

```q version```

# SYNOPSIS

**q** [_command_] [_options_] [_prompt_]

# COMMANDS

**chat**
> 启动交互式聊天会话（默认命令）

**translate**
> 将自然语言转换为 shell 命令

**doctor**
> 诊断并修复常见问题

**integrations**
> 管理 shell 集成（自动补全、行内建议）

**version**
> 显示版本信息

# CHAT OPTIONS

**--no-interactive**
> 以非交互模式运行

**--trust-all-tools**
> 无需提示即信任所有工具执行

**--resume**
> 恢复上一次聊天会话

**--agent** _NAME_
> 使用指定的智能体配置

**--help**
> 显示帮助信息

# IN-SESSION COMMANDS

**/save**
> 保存当前聊天会话

**/load**
> 恢复之前的聊天历史

**/quit**
> 退出聊天（或使用 Ctrl+D）

# DESCRIPTION

**Amazon Q Developer CLI** 是 AWS 推出的 AI 驱动终端助手，提供智能体聊天、命令自动补全和自然语言代码生成。增强版 CLI 智能体由 Anthropic 的 Claude 驱动，可在本地读写文件、查询 AWS 资源、执行 bash 命令并协助调试问题。

该工具提供两种辅助功能：一是显示可用命令选项的自动补全下拉菜单，二是输入时以灰色幽灵文本出现的行内建议。它支持通过 **q translate** 将自然语言翻译为 shell 命令，以及通过 **q chat** 进行交互式编码会话。

支持 macOS 和 Linux，可与 macOS Terminal、iTerm2 以及 VS Code 内置终端等集成。

# CONFIGURATION

**~/.aws/credentials**
> AWS 凭据文件，与 Amazon Q Developer 服务进行身份验证时必需。

**Q_LOG_LEVEL**
> 控制日志详细程度的环境变量，排查问题时可设为 **debug**。

# CAVEATS

需要 AWS 身份验证和 Amazon Q Developer 订阅（Free 或 Pro 层级）。增强版 CLI 智能体在所有提供 Q Developer 的 AWS 区域可用。排查问题时可将 **Q_LOG_LEVEL** 环境变量设为 **debug**。

# HISTORY

Amazon Q Developer CLI 由 **AWS** 作为 Amazon Q Developer 套件的一部分发布。具备智能体编程能力的增强版 CLI 智能体于 **2025 年 3 月**公布，由 Anthropic 的 Claude 3.7 Sonnet 驱动。2025 年起，用户可升级到 Kiro CLI 获得更多功能，同时保留 Q Developer 的功能。

# INSTALL

```apk: sudo apk add dnsq```

```brew: brew install q```

```nix: nix profile install nixpkgs#q```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [claude](/man/claude)(1), [codex](/man/codex)(1), [gemini](/man/gemini)(1), [aichat](/man/aichat)(1)
