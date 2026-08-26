# TAGLINE

调试 OpenCode 连接与日志

# TLDR

**启用**调试日志

```opencode debug```

**调试** MCP 服务器的 OAuth 连接

```opencode debug mcp```

# SYNOPSIS

**opencode debug** [_options_]

# DESCRIPTION

**opencode debug** 启用调试日志，并为 OpenCode 提供诊断功能。它可以诊断与 MCP（Model Context Protocol，模型上下文协议）服务器之间的 OAuth 连接问题，并输出详细日志以便排查配置或连接问题。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-mcp](/man/opencode-mcp)(1)
