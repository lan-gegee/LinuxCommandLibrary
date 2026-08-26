# TAGLINE

管理 OpenCode 的 MCP 服务器

# TLDR

**添加** MCP 服务器

```opencode mcp add [name] [command]```

**列出**已配置的 MCP 服务器

```opencode mcp list```

**移除** MCP 服务器

```opencode mcp remove [name]```

**调试** MCP 服务器连接

```opencode mcp debug [name]```

# SYNOPSIS

**opencode mcp** _subcommand_ [_options_]

# DESCRIPTION

**opencode mcp** 管理 OpenCode 的 Model Context Protocol（MCP，模型上下文协议）服务器。MCP 服务器通过为 AI 智能体提供额外的工具、资源和上下文来扩展 OpenCode 的能力。你可以添加、列出、认证、移除和调试 MCP 服务器连接。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-debug](/man/opencode-debug)(1)
