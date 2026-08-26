# TAGLINE

导出 OpenCode 会话数据

# TLDR

**以 JSON 格式导出**当前会话

```opencode export```

**按 ID 导出**特定会话

```opencode export [session_id]```

# SYNOPSIS

**opencode export** [_session_id_]

# DESCRIPTION

**opencode export** 将 OpenCode 的会话数据导出为 JSON。会话包含一次 AI 编程会话的完整对话历史、工具调用和上下文。如果未指定会话 ID，则导出当前或最近的会话。输出可以重定向到文件以便存档或分享。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-import](/man/opencode-import)(1), [opencode-session](/man/opencode-session)(1)
