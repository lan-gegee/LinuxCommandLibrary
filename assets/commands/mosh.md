# TAGLINE

远程终端应用

# TLDR

**连接远程主机**

```mosh [user@host]```

**在指定端口连接**

```mosh --ssh="ssh -p [2222]" [user@host]```

**使用指定的服务器程序连接**

```mosh --server=[/usr/bin/mosh-server] [user@host]```

**在本地预测键入内容**

```mosh --predict=always [user@host]```

**禁用预测**

```mosh --predict=never [user@host]```

**使用指定的区域设置**

```mosh --client="LANG=en_US.UTF-8 mosh-client" [user@host]```

# SYNOPSIS

**mosh** [_options_] [_user@host_] [_command_]

# PARAMETERS

_USER@HOST_
> 远程主机连接。

**--ssh** _CMD_
> 要使用的 SSH 命令。

**--server** _PATH_
> mosh-server 的路径。

**--predict** _MODE_
> 预测模式（always、adaptive、never）。

**--port** _PORT_
> 使用指定的 UDP 端口。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mosh**（Mobile Shell）是一个远程终端应用。它能够应对间歇性的网络连接。

该工具使用 UDP 建立连接，提供本地回显和漫游支持，比单纯的 SSH 更具韧性。

# CAVEATS

远程端需要安装 mosh-server。使用 UDP 端口范围。初始连接依赖 SSH。

# HISTORY

mosh 由 **MIT** 开发，旨在提供更好的移动 Shell 体验，于 2012 年发布。

# INSTALL

```apt: sudo apt install mosh```

```dnf: sudo dnf install mosh```

```pacman: sudo pacman -S mosh```

```apk: sudo apk add mosh```

```zypper: sudo zypper install mosh```

```brew: brew install mosh```

```nix: nix profile install nixpkgs#mosh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [screen](/man/screen)(1), [tmux](/man/tmux)(1)
