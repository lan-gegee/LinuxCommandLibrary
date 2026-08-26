# TAGLINE

列出可用的 OpenCode AI 模型

# TLDR

**列出**已配置提供商提供的所有可用模型

```opencode models```

# SYNOPSIS

**opencode models**

# DESCRIPTION

**opencode models** 列出 OpenCode（一个开源 AI 编程助手）中已配置提供商提供的所有可用 AI 模型。它基于当前的 API 密钥配置显示模型名称、提供商和可用性。支持的提供商包括 OpenAI、Anthropic、Google Gemini、AWS Bedrock、Groq、Azure OpenAI、OpenRouter，以及通过 Ollama 提供的本地模型。

该子命令可用于在开始编程会话前确认哪些模型可以访问。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-auth](/man/opencode-auth)(1)
