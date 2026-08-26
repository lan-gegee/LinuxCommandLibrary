# TAGLINE

Ollama 本地 LLM 运行器的终端客户端

# TLDR

**启动 Ollama TUI**

```oterm```

# SYNOPSIS

**oterm** [_options_]

# DESCRIPTION

**oterm** 是 Ollama（本地 LLM 运行器）的终端客户端。它提供存储在 SQLite 中的持久化聊天会话、模型参数自定义、系统提示词配置、MCP（Model Context Protocol，模型上下文协议）工具和提示词支持，以及多种主题。

你可以在 TUI 中管理对话、切换模型并自定义生成参数。

# CAVEATS

需要正在运行的 Ollama 服务器，且至少已下载一个模型。

# HISTORY

**oterm** 由 **ggozad** 创建，使用 **Python** 编写。

# INSTALL

```brew: brew install oterm```

```nix: nix profile install nixpkgs#oterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ollama](/man/ollama)(1), [oatmeal](/man/oatmeal)(1)
