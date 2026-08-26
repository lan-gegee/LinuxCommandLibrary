# TAGLINE

导入 OpenCode 会话数据

# TLDR

**从 JSON 文件导入**会话

```opencode import [path/to/session.json]```

# SYNOPSIS

**opencode import** _file_

# DESCRIPTION

**opencode import** 从先前用 **opencode export** 创建的 JSON 文件将会话数据导入 OpenCode。这样可以在不同的 OpenCode 安装之间或不同用户之间恢复或共享对话会话。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-export](/man/opencode-export)(1), [opencode-session](/man/opencode-session)(1)
