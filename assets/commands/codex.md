# TAGLINE

OpenAI 基于终端的编码代理

# TLDR

**启动交互式终端界面**

```codex```

**附带初始提示启动**

```codex "[fix the authentication bug]"```

**以非交互方式运行并输出结果**

```codex exec "[refactor this function]"```

**使用指定的模型**

```codex --model [gpt-5.2-codex]```

**启用完全自动模式以进行无人值守的工作**

```codex --full-auto```

**继续上一次会话**

```codex resume --last```

**附加图片作为上下文**

```codex -i [screenshot.png] "[fix this UI bug]"```

# SYNOPSIS

**codex** [_options_] [_prompt_]

# PARAMETERS

**--model**, **-m** _MODEL_
> 覆盖默认模型（例如 gpt-5.2-codex、codex-mini-latest）

**--sandbox**, **-s** _POLICY_
> 沙箱策略：read-only、workspace-write 或 danger-full-access

**--ask-for-approval**, **-a** _MODE_
> 控制审批时机：untrusted、on-failure、on-request 或 never

**--full-auto**
> 启用低干预模式：按请求审批并使用 workspace-write 沙箱

**--yolo**
> 禁用审批和沙箱（仅在强隔离环境中使用）

**--cd**, **-C** _PATH_
> 在处理前设置工作目录

**--add-dir** _PATH_
> 授予额外目录的写权限

**--image**, **-i** _PATH_
> 将图片文件附加到初始提示

**--oss**
> 通过 Ollama 使用本地开源模型

**--search**
> 启用网络搜索能力

**--profile**, **-p** _NAME_
> 从 config.toml 加载配置档案

**--help**
> 显示帮助信息

# COMMANDS

**exec**, **e**
> 以非交互方式运行；支持 --json、--output-last-message

**resume**
> 按 ID 继续之前的会话，或使用 --last

**fork**
> 将之前的会话分支为新线程

**apply**, **a**
> 将 Codex Cloud 任务的最新 diff 应用到本地仓库

**cloud**
> 浏览或执行云端任务

**login**
> 通过 ChatGPT OAuth 或 API 密钥进行身份验证

**logout**
> 移除已存储的凭据

**mcp**
> 管理 Model Context Protocol 服务器（添加、列出、移除）

**sandbox**
> 在 macOS seatbelt 或 Linux Landlock 沙箱下运行命令

**completion**
> 生成 Shell 补全脚本（bash、zsh、fish、powershell）

# DESCRIPTION

**Codex** 是 OpenAI 官方的基于终端的编码代理。它会启动一个全屏终端界面，能够读取你的仓库、建议并实现代码修改，还能在你以对话方式迭代的同时执行命令。

该工具通过操作系统级沙箱保障安全，提供三种安全模式：**read-only**（仅供参考，不做修改）、**workspace-write**（默认，改动工作区之外的文件前会先询问）以及 **danger-full-access**（不受限制，需谨慎使用）。由模型生成的命令在隔离环境中运行，使用 macOS seatbelt 或 Linux Landlock 实现。

Codex 可与 ChatGPT Plus、Pro、Business 和 Enterprise 订阅配合使用，也可以使用 API 额度。它支持云端任务以分流复杂工作，并提供 MCP 集成以扩展能力。

# CAVEATS

需要通过 ChatGPT 账户或 OpenAI API 密钥进行身份验证。**--yolo** 标志会绕过所有安全措施，只能在隔离环境中使用。网络访问默认受限；可通过 **--search** 或完全访问沙箱模式启用。

# HISTORY

OpenAI 最初于 **2021 年 8 月**将 Codex 作为代码自动补全 API 发布，它曾为 GitHub Copilot 提供支持。**Codex CLI** 终端代理于 **2025 年 4 月 16 日**以 Apache 2.0 许可证发布，版本 1.0.0 于 **2025 年 5 月**发布。Codex Cloud 于 **2025 年 6 月**面向 ChatGPT Plus 用户推出。GPT-5.2-Codex 模型于 **2025 年 12 月**发布，具备更强的智能体编码能力。

# INSTALL

```nix: nix profile install nixpkgs#codex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [gemini](/man/gemini)(1), [opencode](/man/opencode)(1), [copilot](/man/copilot)(1)
