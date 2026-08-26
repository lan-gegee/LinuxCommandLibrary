# TAGLINE

支持多提供商 LLM 的语义化 AI 编程智能体

# TLDR

在当前目录**启动**交互式编程智能体

```vtcode```

向智能体**提出**一次性问题后退出

```vtcode ask "[explain the project structure]"```

通过智能体的安全执行器**运行** Shell 命令

```vtcode exec "[cargo test]"```

**使用**指定的模型提供商和模型

```vtcode --provider [anthropic] --model [claude-sonnet-4-5]```

**针对**另一个工作区目录**运行**

```vtcode --workspace [path/to/repo]```

**打开**配置文件进行编辑

```vtcode config edit```

**打印**解析后的配置

```vtcode config show```

通过 OAuth 向提供商**进行身份验证**

```vtcode /login```

# SYNOPSIS

**vtcode** [_global-flags_] [_subcommand_] [_args_]

# PARAMETERS

**ask** _prompt_
> 向所配置的模型发送单条提示词并打印响应。

**exec** _command_
> 通过智能体具备策略感知的 Shell 执行器运行 _command_，并经 **tree-sitter-bash** 校验。

**config** [**show**|**edit**|**path**]
> 查看或编辑 **vtcode.toml** 配置。

**--provider** _name_
> 覆盖默认的 LLM 提供商（例如 **openai**、**anthropic**、**deepseek**、**gemini**、**ollama**、**lmstudio**）。

**--model** _id_
> 为所选提供商覆盖默认的模型 ID。

**--workspace** _path_
> 设置智能体工作的目录（默认为 **$PWD**）。

**--config** _file_
> 使用 _file_ 而不是默认的 **vtcode.toml**。

**--no-tools**
> 禁用工具执行；智能体只输出文本。

**--yes**
> 自动批准工具调用，而不是每个操作都提示。

**-v**, **--verbose**
> 提高日志详细程度。

**--version**
> 打印版本后退出。

**-h**, **--help**
> 显示用法信息。

# SLASH COMMANDS

**/login**
> 运行 OAuth 流程，向当前激活的提供商进行身份验证。

**/agent**
> 查看当前会话中受托管的子智能体。

**/agents active**
> 列出当前正在运行的子智能体。

**/subprocesses**
> 打开本地智能体抽屉（也绑定到 **Alt+S**）。

# DESCRIPTION

**vtcode** 是一个用 **Rust** 编写的开源语义化编程智能体。它连接一个或多个 LLM 提供商，提供一个可以使用工具的助手，能够在工作区内读取、编辑和执行代码。基于 Tree-sitter 的解析器让智能体对多种语言的源文件具有结构性理解，从而实现有针对性的编辑，而不是盲目的文本重写。

工具执行由可配置的策略控制：每个工具可设为 **allow**、**deny** 或 **prompt**，并且 Shell 命令在运行前会经过 **tree-sitter-bash** 静态校验。沙箱机制将文件操作限制在配置的工作区边界之内。

多提供商支持——**OpenAI**、**Anthropic**、**DeepSeek**、**Gemini**、**Z.AI**、**Moonshot**、**OpenRouter**、**MiniMax**、**Ollama**、**LM Studio**——通过单一配置文件接入，并提供自动故障转移、提示词缓存和上下文窗口感知的截断。

# CONFIGURATION

用户配置位于 **vtcode.toml**（项目级）或 **~/.config/vtcode/vtcode.toml**（全局）。常用键：

> **[providers.<name>]** — 各提供商的 API 基础 URL 和凭据来源。
> **[oauth]** — OAuth 客户端设置；令牌存储在操作系统密钥链中。
> **[tools]** — 每个工具的 allow/deny/prompt 策略。
> **[workspace]** — 根路径和忽略通配规则。
> **[security]** — Shell 沙箱、命令允许/拒绝列表、最大输出大小。
> **[context]** — 上下文窗口预算和截断策略。
> **[hooks]** — 在生命周期事件（会话启动、工具调用等）时运行的 Shell 命令。

密钥通常从环境变量（例如 **OPENAI_API_KEY**、**ANTHROPIC_API_KEY**、**GEMINI_API_KEY**）或操作系统原生的凭据存储中读取。

# KEYBOARD SHORTCUTS

```
Ctrl+B   Toggle background subagent
Alt+S    Open Local Agents drawer
Ctrl+C   Cancel current request
```

# CAVEATS

vtcode 处于 **pre-1.0** 阶段——选项、配置键和斜杠命令在各个版本之间可能变化。LLM 提供商可能按 token 收费；在真实代码库上启用自动批准（**--yes**）之前，请先检查 **[security]** 策略。某些功能（Zed 编辑器集成、A2A 协议、沙箱隔离）需要在默认安装之外进行额外设置。

# HISTORY

**vtcode** 由 **Vinh Nguyen**（**vinhnx**）开发，发布于 **github.com/vinhnx/vtcode**。它可通过 **Cargo**（**cargo install vtcode**）、**Homebrew**（**brew install vtcode**） 和安装脚本分发。各版本以开源许可证发布在 GitHub 上。

# INSTALL

```brew: brew install vtcode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [aider](/man/aider)(1), [gh](/man/gh)(1), [cargo](/man/cargo)(1)
