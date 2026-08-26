# TAGLINE

让语言模型在本地执行代码的自然语言界面

# TLDR

**启动交互式会话**

```interpreter```

**无需确认自动运行代码**

```interpreter -y```

**使用指定模型**

```interpreter --model [gpt-4o]```

**使用本地模型**

```interpreter --local```

**启用小模型的快速模式**

```interpreter --fast```

**设置上下文窗口和最大 token 数**

```interpreter --local --max_tokens [1000] --context_window [3000]```

**加载已保存的 profile**

```interpreter --profile [my_profile.yaml]```

**从 stdin 管道输入**

```echo "[What OS am I using?]" | interpreter --stdin -y```

# SYNOPSIS

**interpreter** [_options_]

# PARAMETERS

**-y**, **--auto-run**
> 无需每步手动确认即可运行代码

**--model** _MODEL_
> 指定要使用的模型（如 gpt-4o、claude-3-sonnet）

**--local**
> 使用本地模型进行代码解释（通过 Ollama、LM Studio、jan.ai 等）

**--fast**
> 使用更快、更小的模型以加快响应速度

**--verbose**
> 启用详细输出模式

**--os**
> 启用 OS 模式以控制你的计算机（鼠标、键盘、屏幕）

**--max_tokens** _N_
> 模型输出的最大 token 数

**--context_window** _N_
> 上下文窗口大小（必须大于 max_tokens）

**--profile** _FILE_
> 从 YAML profile 加载配置

**--save-profile** _NAME_
> 将当前配置保存为命名的 profile

**--tools** _LIST_
> 启用特定工具（默认：interpreter,editor）

**--stdin**
> 接受来自 stdin 的输入，支持 Unix 风格管道

**--custom_instructions** _TEXT_
> 向系统消息追加自定义指令（如系统信息、偏好的编程语言）。

**--api_base** _URL_
> 模型提供商的自定义 API 基础 URL。

**--api_key** _KEY_
> 用于身份验证的 API 密钥。

# IN-SESSION COMMANDS

**%reset**
> 重置当前会话的对话

**%undo**
> 删除上一条消息及 AI 回复

**%tokens** _[prompt]_
> 计算下一个提示的 token 数并估算费用

**%verbose true|false**
> 在聊天过程中切换详细输出模式

# DESCRIPTION

**Open Interpreter** 为计算机提供自然语言接口，允许语言模型在你的机器上本地执行代码（Python、JavaScript、Shell 等）。它的作用类似于 ChatGPT 的 Code Interpreter，但运行在你的终端中，可以完全访问本地环境。

该工具为支持函数调用的语言模型提供一个 exec() 函数，接受编程语言和要运行的代码。由于代码在本地环境中执行，它可以与文件交互、安装软件包、浏览网页以及控制系统设置。默认情况下，interpreter 在执行代码前会请求确认。

Open Interpreter 支持多种模型提供商，包括 OpenAI、Anthropic 以及通过 Ollama、LM Studio 或 jan.ai 提供的本地模型。配置可保存为 YAML profile，便于在不同设置间切换。

# CAVEATS

生成的代码对本地环境拥有完全访问权限，可能导致数据丢失或安全风险。确认执行前务必检查代码。**-y** 标志会跳过确认，应谨慎使用。本地模型的能力可能弱于云端 API。

# HISTORY

Open Interpreter 由 **Killian Lucas** 创建，于 **2023 年 9 月 5 日**发布。它在第一周内就成为 GitHub 趋势榜第一，获得了超过 20,000 颗星。该项目位于华盛顿州西雅图，作为开源 Agent-Computer-Interface 项目已增长至超过 50,000 GitHub 星标。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [aider](/man/aider)(1), [python](/man/python)(1)
