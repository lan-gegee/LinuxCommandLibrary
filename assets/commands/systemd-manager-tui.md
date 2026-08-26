# TAGLINE

通过 D-Bus 管理 systemd 服务的 TUI

# TLDR

**启动服务管理器 TUI**

```systemd-manager-tui```

# SYNOPSIS

**systemd-manager-tui**

# DESCRIPTION

**systemd-manager-tui** 是一个用于管理 systemd 服务的终端用户界面。它借助 D-Bus API 支持查看日志、列出服务、查看属性、编辑单元文件以及控制服务的生命周期（启动、停止、重启、屏蔽、取消屏蔽、启用、禁用）。

支持类似 Vim 的键盘导航，并可在系统/用户单元之间切换。该界面专为纯键盘操作而设计。

# CAVEATS

需要正在运行 systemd 的系统以及 D-Bus。使用 Rust 编写。

# HISTORY

**systemd-manager-tui** 由 **matheus-git** 创建，采用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#systemd-manager-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-tui](/man/systemctl-tui)(1), [journalctl](/man/journalctl)(1)
