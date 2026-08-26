# TAGLINE

快速、简洁的 systemd 服务 TUI

# TLDR

**启动交互式服务管理器**

```systemctl-tui```

按模式**限制显示的单元**

```systemctl-tui --limit-units "[pattern]"```

# SYNOPSIS

**systemctl-tui** [_options_]

# DESCRIPTION

**systemctl-tui** 让你通过交互式终端界面快速浏览 systemd 服务状态和日志，启动/停止/重启/重载服务，以及查看/编辑单元文件。

它力求把少量事情做好：查看服务状态、阅读日志和管理服务，无需记住 `systemctl` 和 `journalctl` 的各种子命令。

# PARAMETERS

**--limit-units** _pattern_
> 将视图限制为匹配给定模式的单元。

# CAVEATS

仅支持 Linux。WSL 需要启用 systemd。服务管理操作（start、stop、restart）需要相应权限。

# HISTORY

**systemctl-tui** 由 **Reilly Wood**（rgwood）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S systemctl-tui```

```nix: nix profile install nixpkgs#systemctl-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemd-manager-tui](/man/systemd-manager-tui)(1), [journalctl](/man/journalctl)(1)
