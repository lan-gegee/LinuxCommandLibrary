# TAGLINE

管理 OpenCode 凭据

# TLDR

**登录** AI 提供商

```opencode auth login```

**显示**当前身份验证状态

```opencode auth status```

# SYNOPSIS

**opencode auth** _subcommand_ [_options_]

# DESCRIPTION

**opencode auth** 管理 OpenCode 所用 AI 提供商的凭据和登录会话。凭据存储在 **~/.local/share/opencode/auth.json** 中。支持向 OpenAI、Anthropic、Google、AWS Bedrock 和 GitHub Copilot 等提供商进行身份验证。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-models](/man/opencode-models)(1)
