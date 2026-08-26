# TAGLINE

管理 OpenCode 会话

# TLDR

**列出**所有会话

```opencode session list```

**恢复**之前的会话

```opencode session resume [session_id]```

**继续**最近一次会话

```opencode session continue```

# SYNOPSIS

**opencode session** _subcommand_ [_options_]

# DESCRIPTION

**opencode session** 管理 OpenCode 编程会话。会话将对话历史、工具调用和上下文持久化保存在本地 **SQLite** 数据库中。你可以列出过去的会话、按 ID 恢复特定会话，或继续最近一次会话。这样即使重启终端也能从上次中断的地方继续。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-export](/man/opencode-export)(1), [opencode-import](/man/opencode-import)(1)
