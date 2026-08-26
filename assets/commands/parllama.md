# TAGLINE

面向 Ollama 及其他 LLM 提供方的 TUI

# TLDR

**启动 Ollama TUI**

```parllama```

# SYNOPSIS

**parllama** [_options_]

# DESCRIPTION

**parllama** 是一个终端用户界面，用于管理基于 Ollama 的 LLM 并与之对话，同时也支持 OpenAI、Anthropic、Groq 和 Google 等其他提供方。它支持带会话持久化的多标签页对话、面向图像聊天的视觉模型支持、跨对话的持久记忆系统，以及通过可配置命令白名单实现的安全模板执行。

# CAVEATS

要使用本地模型，需要一个正在运行的 Ollama 服务器。其他提供方则需提供 API 密钥。

# HISTORY

**parllama** 由 **Paul Robello**（paulrobello）开发，使用 **Python** 编写。

# SEE ALSO

[ollama](/man/ollama)(1), [oterm](/man/oterm)(1), [oatmeal](/man/oatmeal)(1)
