# TAGLINE

比 ss 和 netstat 更友好的替代品

# TLDR

**启动交互式 TUI，实时刷新连接**

```snitch```

**以样式化表格列出 TCP 已建立的连接**

```snitch ls -t -e```

**以 JSON 格式输出所有连接**

```snitch json```

# SYNOPSIS

**snitch** [_command_] [_flags_]

# DESCRIPTION

**snitch** 是用于检查 Linux 和 macOS 上 TCP 和 UDP 网络连接的 TUI 与 CLI 工具。它是 **ss** 和 **netstat** 的现代化、人性化的替代品，显示实时刷新的连接表，支持 DNS 解析、过滤以及多种输出格式（样式化表格、JSON、CSV）。

# HISTORY

**snitch** 由 **Karol Broda** 创建，使用 **Go** 编写。

# INSTALL

```brew: brew install snitch```

```nix: nix profile install nixpkgs#snitch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ss](/man/ss)(1), [netstat](/man/netstat)(1), [nethogs](/man/nethogs)(1)
