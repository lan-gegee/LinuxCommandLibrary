# TAGLINE

管理 WiFi 连接的终端界面工具

# TLDR

**启动交互式 WiFi 管理器**

```wifitui```

**扫描并列出可用的 WiFi 网络**

```wifitui scan```

**连接到特定网络**

```wifitui connect "[SSID]"```

**断开当前网络**

```wifitui disconnect```

**显示已知（已保存）的网络**

```wifitui known```

# SYNOPSIS

**wifitui** [_command_] [_options_]

# PARAMETERS

**scan**
> 扫描并显示可用的 WiFi 网络。

**connect** _SSID_
> 连接到指定的 WiFi 网络。

**disconnect**
> 断开当前的 WiFi 网络。

**known**
> 列出已保存/已知的 WiFi 网络。

# DESCRIPTION

**wifitui** 是一个面向 Linux 的终端 WiFi 管理器，提供交互式 TUI 用于扫描、连接和管理无线网络。它以 **NetworkManager** 或 **iwd** 作为后端，并提供模糊过滤以便选择网络。

功能包括生成二维码分享网络凭据，以及支持交互式和非交互式（命令行）两种操作模式。

# CAVEATS

需要 **NetworkManager** 或 **iwd** 作为无线后端正在运行。扫描和连接操作可能需要 root 权限或加入相应的用户组。

# HISTORY

**wifitui** 由 **shazow** 创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install wifitui```

```nix: nix profile install nixpkgs#wifitui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmtui](/man/nmtui)(1), [nmcli](/man/nmcli)(1), [iwctl](/man/iwctl)(1)
