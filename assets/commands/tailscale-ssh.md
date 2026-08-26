# TAGLINE

通过 Tailscale 网络进行基于身份认证的 SSH

# TLDR

**SSH 连接到 Tailscale 设备**

```tailscale ssh [user]@[device]```

使用设备的 Tailscale 主机名 **SSH 连接**

```tailscale ssh [user]@[hostname]```

**SSH 连接并执行远程命令**

```tailscale ssh [user]@[device] [command]```

带详细输出进行 **SSH 连接**

```tailscale ssh -v [user]@[device]```

# SYNOPSIS

**tailscale** **ssh** [_ssh_options_] [_user_@]_target_ [_command_]

# PARAMETERS

_target_
> 要连接的 Tailscale 设备名、主机名或 IP 地址。

_user_
> 远程用户名。若省略，则使用当前本地用户名。

_command_
> 可选，要在远程主机上执行的命令。

标准 SSH 标志（例如 **-v**、**-p**、**-L**）会原样传递给底层的 SSH 连接。

# DESCRIPTION

**tailscale ssh** 使用 SSH 连接到你的 Tailscale 网络中的其他机器，其认证由 Tailscale 的身份系统处理，而不依赖传统的 SSH 密钥或密码。

当目标机器启用了 Tailscale SSH 时，连接将使用连接用户的 Tailscale 身份进行认证。访问控制由管理控制台中的 Tailscale SSH ACL 管理，可以精细地规定哪些用户能以哪些系统用户身份访问哪些机器。

连接在 Tailscale 在节点之间建立的 WireGuard 隧道上端到端加密。这意味着无需向公共互联网暴露 22 端口、无需管理 SSH 密钥分发即可实现 SSH 访问。

# CAVEATS

目标设备必须启用 Tailscale SSH（通过 **tailscale up --ssh** 或管理控制台）。两台机器必须位于同一 Tailnet，或通过 Tailscale 共享功能获得访问权限。必须在 Tailscale 管理控制台中配置 SSH ACL 以允许该连接。目标机器必须运行 Tailscale SSH 服务器（内置于 Tailscale 客户端中）。

# INSTALL

```dnf: sudo dnf install tailscale```

```pacman: sudo pacman -S tailscale```

```apk: sudo apk add tailscale```

```zypper: sudo zypper install tailscale```

```brew: brew install tailscale```

```nix: nix profile install nixpkgs#tailscale```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tailscale](/man/tailscale)(1), [tailscale-up](/man/tailscale-up)(1), [ssh](/man/ssh)(1)
