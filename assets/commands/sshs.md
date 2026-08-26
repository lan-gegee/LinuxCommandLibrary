# TAGLINE

用于浏览和连接 SSH 主机的交互式 TUI

# TLDR

**启动交互式 SSH 主机选择器**

```sshs```

**使用自定义的 SSH 配置文件**

```sshs --config [~/.ssh/custom_config]```

# SYNOPSIS

**sshs** [**--config** _path_]

# DESCRIPTION

**sshs** 是一个面向 SSH 的终端用户界面，它读取你的 ~/.ssh/config 文件来列出并连接主机。它提供支持模糊搜索的交互式界面，可快速选择并连接到已配置的 SSH 目标。

# HISTORY

**sshs** 由 **quantumsheep** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S sshs```

```brew: brew install sshs```

```nix: nix profile install nixpkgs#sshs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [sshclick](/man/sshclick)(1), [ssh-list](/man/ssh-list)(1)
