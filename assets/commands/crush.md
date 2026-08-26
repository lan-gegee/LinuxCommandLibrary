# TAGLINE

终端中炫酷的 AI 编程助手

# TLDR

**启动交互式会话**

```crush```

**切换到指定工作目录**

```crush --cwd [path/to/project]```

**跳过所有权限提示（谨慎使用）**

```crush --yolo```

**启用调试日志**

```crush --debug```

**使用自定义数据目录**

```crush --data-dir [path/to/data]```

**查看最近的日志**

```crush logs```

**实时跟踪日志**

```crush logs --follow```

**非交互式运行**

```crush run "[fix the bug in main.go]"```

# SYNOPSIS

**crush** [_options_] [_command_]

# PARAMETERS

**--cwd** _PATH_
> 启动前先切换到指定目录

**--data-dir** _PATH_
> 覆盖默认的数据目录位置

**--debug**
> 启用调试日志以便排查问题

**--yolo**
> 跳过所有权限提示（危险，谨慎使用）

**--help**
> 显示帮助信息

**--version**
> 显示版本号

# COMMANDS

**run** _PROMPT_
> 以非交互模式运行 Crush 并附带提示词

**logs**
> 打印最后 1000 行日志

**logs --tail** _N_
> 打印最后 N 行日志

**logs --follow**
> 实时跟踪日志

# DESCRIPTION

**Crush** 是由 Charmbracelet 开发的终端炫酷 AI 编程助手。它用 Go 编写以保证速度和效率，提供终端用户界面（TUI），可与多种 AI 模型交互，协助完成编码任务、调试和文件操作。

Crush 支持多个 AI 服务商，包括 OpenAI、Anthropic、Google Gemini、Groq、OpenRouter、AWS Bedrock，以及通过 Ollama 和 LM Studio 接入的本地模型。它利用语言服务器协议（LSP）增强代码上下文，并可通过 Model Context Protocol（MCP）服务器进行扩展，支持 stdio、http 和 sse 传输方式。

该工具具有出色的跨平台兼容性，支持 macOS、Linux、Windows（PowerShell 和 WSL）、FreeBSD、OpenBSD 和 NetBSD。配置保存在 JSON 文件中，包含服务商、LSP、MCP 服务器和权限等设置。

# CONFIGURATION

**~/.config/crush/crush.json**
> 主配置文件，包含 AI 服务商设置、API 密钥、LSP 配置、MCP 服务器定义和权限设置。

# CAVEATS

需要受支持服务商的 API 密钥，可通过环境变量（ANTHROPIC_API_KEY、OPENAI_API_KEY 等）设置或在 crush.json 中配置。**--yolo** 标志会绕过所有权限提示，必须极其谨慎地使用。配合 **--debug** 的调试模式会产生大量详细日志。

# HISTORY

Crush 由 **Charmbracelet** 开发，该公司以打造富有吸引力的终端应用而闻名。它源于 Kujtim Hoxha 的一个项目，该项目一度与 OpenCode 名称相关联；后来 Charmbracelet 将其自己的版本更名为 Crush，而 OpenCode 名称则作为独立的分支继续存在。项目以 FSL-1.1-MIT 许可证（与 MIT 兼容）发布，在 GitHub 上已获得超过 8900 颗星。0.4.0 版本于 2025 年 8 月发布。

# INSTALL

```nix: nix profile install nixpkgs#crush```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [opencode](/man/opencode)(1), [aider](/man/aider)(1), [codex](/man/codex)(1)
