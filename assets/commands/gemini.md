# TAGLINE

来自 Google 的 AI 驱动智能体编程助手

# TLDR

**启动交互式会话**

```gemini```

**以非交互方式运行提示词**（无头模式）

```gemini -p "[explain this code]"```

**使用特定模型**

```gemini -m [gemini-2.5-flash]```

**带初始提示词启动交互式会话**

```gemini -i "[explain this code]"```

**获取 JSON 输出以便脚本处理**

```gemini -p "[prompt]" --output-format json```

**启用沙箱模式运行**

```gemini --sandbox```

**在对话中包含文件**

```gemini``` 然后 ```@[path/to/file.py] [explain this code]```

# SYNOPSIS

**gemini** [_options_] [_prompt_]

# PARAMETERS

**-p**, **--prompt** _PROMPT_
> 使用给定的提示词以无头（非交互）模式运行。

**-i**, **--prompt-interactive** _PROMPT_
> 以提供的提示词作为初始输入启动交互式会话。

**-m**, **--model** _MODEL_
> 指定模型变体（例如 gemini-2.5-pro、gemini-2.5-flash）。

**--output-format** _FORMAT_
> 输出格式：text、json 或 stream-json。

**--sandbox**, **-s**
> 在沙箱化的 Docker 环境中运行以确保安全。

**--yolo**
> 自动批准所有工具操作，无需确认。

**--debug**
> 启用调试模式和详细输出。

**--help**
> 显示帮助信息。

**--version**
> 显示版本号。

# IN-CHAT COMMANDS

**/model**
> 选择其他 Gemini 模型

**/clear**
> 清空终端屏幕和回滚缓冲区

**/resume**
> 浏览并恢复之前的对话

**/stats**
> 显示令牌使用量和会话时长

**/compress**
> 总结对话上下文以节省令牌

**/memory add** _text_
> 将文本加入 AI 的指令记忆

**/tools**
> 列出可用工具

**/mcp list**
> 显示已连接的 MCP 服务器

**/quit**
> 退出 CLI

**@**_path_
> 将文件或目录内容包含到提示词中

**!**_command_
> 执行 Shell 命令

# CONFIGURATION

**GEMINI.md**
> 从工作目录加载的项目专属指令和上下文。

**~/.config/gemini/config.json**
> 用户配置，包括 API 密钥、默认模型和偏好设置。

# DESCRIPTION

**Gemini CLI** 是 Google 的开源 AI 智能体，将 Gemini 的能力直接带入你的终端。它让开发者能够用自然语言编写、重构和调试代码，执行命令，以及分析整个代码仓库。

该 CLI 采用"推理与行动"（ReAct）循环，内置多种工具，包括 Google Search grounding、文件操作、Shell 命令和网页抓取。它支持 MCP（Model Context Protocol）以实现自定义集成，还可以通过 GEMINI.md 文件配置项目专属指令。

免费层用户使用个人 Google 账户可获得每分钟 60 次请求和每天 1000 次请求的额度，访问具有 100 万令牌上下文窗口的模型。该工具可在 macOS、Linux 和 Windows 上运行。

# CAVEATS

需要通过 Google 账户或 API 密钥进行身份验证（通过 **GEMINI_API_KEY** 环境变量设置）。Shell 命令和文件修改可能有危险；对不可信的操作请使用 **--sandbox** 模式。处理大型代码库时令牌消耗可能很大。

# HISTORY

Gemini CLI 由 **Google** 于 **2025 年 6 月 25 日**发布，是以 Apache 2.0 许可证开源的工具。它构建于 Gemini 2.5 Pro 模型之上，与全新的 Gemini 标志一同推出。到 2025 年 12 月，免费层用户已可访问 Gemini 3 Pro 和 Flash 模型。

# SEE ALSO

[claude](/man/claude)(1), [opencode](/man/opencode)(1), [aider](/man/aider)(1), [gcloud](/man/gcloud)(1)
