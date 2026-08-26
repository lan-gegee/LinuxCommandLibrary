# TAGLINE

大语言模型的 TUI 界面

# TLDR

**启动 LLM 聊天 TUI**

```tenere```

**使用指定的配置文件**

```tenere --config [~/.config/tenere/config.toml]```

# SYNOPSIS

**tenere** [_options_]

# DESCRIPTION

**tenere** 是一个用于与 ChatGPT、llama.cpp、Ollama 等 LLM 交互的终端用户界面。它具有类 Vim 的模式（Normal、Visual、Insert）、语法高亮、聊天历史和文件保存功能。配置通过 TOML 文件完成。

# HISTORY

**tenere** 由 **Badr**（pythops）创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install tenere```

```nix: nix profile install nixpkgs#tenere```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aichat](/man/aichat)(1), [ollama](/man/ollama)(1), [oterm](/man/oterm)(1)
