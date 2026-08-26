# TAGLINE

使用 LLM 解释上一条终端命令输出的 CLI

# TLDR

**解释上一条命令的输出**

```wut```

# SYNOPSIS

**wut**

# DESCRIPTION

**wut** 是一个终端助手，它利用大语言模型（LLM）解释最近打印到你终端上的内容。它可以解读堆栈跟踪、错误代码、陌生的日志行和出乎意料的命令输出，返回通俗的解释，通常还会给出建议的下一步操作。

该工具通过宿主终端复用器读取当前窗格中可见的回滚缓冲区，因此必须在 **tmux** 或 **screen** 会话内调用。它将捕获的文本发送给已配置的 LLM 提供商（如 OpenAI 或 Anthropic），凭据以环境变量形式存储。

# CONFIGURATION

**OPENAI_API_KEY**
> 当 wut 配置为调用 OpenAI 模型时使用的 API 密钥。

**ANTHROPIC_API_KEY**
> 当 wut 配置为调用 Anthropic 模型时使用的 API 密钥。

# CAVEATS

必须在 **tmux** 或 **screen** 会话中运行——wut 需要终端复用器来捕获窗格内容。每次调用都会把终端输出发送给第三方 LLM，因此不要对包含机密、令牌或个人身份信息（PII）的输出使用。需要网络访问权限和有效的 API 密钥。

# HISTORY

**wut** 由 **Jonathan Shobrook**（shobrook）创建，使用 Python 编写。它针对的问题域与 **thefuck** 相同，但只解释错误而不是尝试自动纠正。

# SEE ALSO

[tldr](/man/tldr)(1), [tmux](/man/tmux)(1), [screen](/man/screen)(1)
