# TAGLINE

面向 OpenAI 兼容 LLM API 的 Bash 优先 CLI 封装

# TLDR

向默认的 Groq 提供方**发送提示词**

```bash4llm "[prompt]"```

**运行**文件中的提示词

```bash4llm -f [prompt.txt]```

单次请求**使用特定模型**

```bash4llm -m [llama-3.3-70b-versatile] "[prompt]"```

**启动交互式聊天**模式

```bash4llm --chat```

从提供方 API **刷新模型列表**

```bash4llm --refresh-models```

在命名会话中跨轮次**启用上下文记忆**

```bash4llm --session [chat1] "[prompt]"```

# SYNOPSIS

**bash4llm** [_options_] [_prompt_]

# PARAMETERS

**-f** _file_
> 从 _file_ 读取提示词文本。

**-m**, **--model** _model_
> 仅本次运行使用 _model_。

**--provider** _name_
> 选择已安装的提供方（例如 **groq** 或 **gemini**）。

**--system** _text_
> 设置系统提示词。

**--temperature**, **--ture** _n_
> 设置采样温度，范围 **0.0** 到 **2.0**。

**--max** _n_
> 限制最大输出 token 数。

**--session** _id_
> 启用会话记忆，用于有上下文衔接的后续提问。

**--session-window** [_n_]
> 限制纳入的先前会话轮次数（默认 **10**）。

**--stream**, **--no-stream**
> 启用或禁用流式输出。

**--chat**
> 启动交互式 REPL 聊天会话。

**--dry-run**
> 只校验配置，不调用 API。

**--json**, **--pretty**, **--text**, **--raw**
> 控制响应输出格式。

**--save**, **--nosave**, **--out** _path_, **--threshold** _bytes_
> 控制长响应的自动保存行为。

**--refresh-models**, **--list-models**, **--list-providers**
> 管理和查看提供方模型列表。

**--set-default** _model_
> 持久保存当前提供方的默认模型。

**--install-extras** [_dir_]
> 安装可选的提供方扩展包、模板和工具。

**--show-config**, **--diagnostics**
> 打印生效配置或运行系统检查。

**-h**, **--help**
> 显示帮助。

**--version**
> 打印版本并退出。

# DESCRIPTION

**bash4llm** (Bash4LLM⁺) 是一个自包含的单文件 Bash 脚本，封装了 OpenAI 兼容的 chat completion API，默认提供方为 Groq。它的设计目标是可读、可审计，并且可在 Linux、macOS、WSL、Cygwin、Termux 和 BSD 系统间移植。

该脚本从提供方 API 动态获取模型列表而不是硬编码，支持流式与非流式响应，并可以从文件或标准输入管道读取内容。可选 extras 增加了 Gemini、Hugging Face、Mistral 等更多提供方。使用 **--session** 时，会话支持将轮次历史存储在 NDJSON 文件中，从而提供短期上下文记忆；默认情况下不保留任何状态。

安全是核心设计目标：脚本避免使用 **eval**，从不执行模型输出，不使用共享的 **/tmp** 目录，并以严格权限隔离临时文件。提供方模块被视为受信代码，应存放在用户拥有的目录中。

# CONFIGURATION

**$BASH4LLM_CONFIG_DIR/config**
> 本地设置，如模型、温度、最大 token 数、输出格式和保存阈值。

**$BASH4LLM_CONFIG_DIR/model.$PROVIDER**
> 提供方的持久化默认模型。

**$BASH4LLM_CONFIG_DIR/ui_state/**
> 供外部工具和可选 GUI 集成使用的原子 JSON 元数据。

**$BASH4LLM_HISTORY_DIR/sessions/<id>.ndjson**
> 启用 **--session** 时的会话对话历史。

**GROQ_API_KEY**
> 默认 Groq 提供方的 API 密钥。

**BASH4LLM_TMPDIR**
> 替代系统 **/tmp** 使用的私有临时目录。

模型选择优先级为：**-m/--model**，其次 **model.$PROVIDER**，然后是提供方自动选择，再后是白名单中的第一个模型，最后是旧版全局配置文件。

# CAVEATS

需要 **PATH** 上存在 **bash**、**curl**、**jq**、**gawk** 及常用 coreutils 工具。只有每次相关调用都带上 **--session** 时，上下文记忆才存在。提供方 extras 是可执行的 Shell 代码，必须保存在可信目录中。在 Termux 上，由于 **flock** 通常不可靠，文件锁会退回到原子目录锁。

# EXIT CODES

**0**
> 成功。

**10**
> 缺少 API 密钥。

**11**
> 模型无效或不在白名单内。

**12**
> 网络或 curl 失败。

**14**
> 未提供提示词。

**15**
> 文件系统或临时文件错误。

**16**
> 提供方 HTTP 或 API 错误。

# SEE ALSO

[groq](/man/groq)(1), [curl](/man/curl)(1), [jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/kamaludu/bash4llm)```

<!-- verified: 2026-06-28 -->
