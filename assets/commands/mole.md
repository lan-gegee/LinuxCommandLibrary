# TAGLINE

轻松创建 SSH 隧道的 CLI 应用

# TLDR

**创建本地 SSH 隧道**

```mole start local --source :[local_port] --destination [host]:[port] --server [user]@[ssh_server]```

**创建隧道并显示详细输出**

```mole start local --verbose --source :[local_port] --destination [host]:[port] --server [user]@[ssh_server]```

**使用特定 SSH 密钥创建隧道**

```mole start local --source :[local_port] --destination [host]:[port] --server [user]@[ssh_server] --key [~/.ssh/id_rsa]```

**将隧道保存为别名以便复用**

```mole add alias local [name] --source :[local_port] --destination [host]:[port] --server [user]@[ssh_server]```

**启动已保存的隧道别名**

```mole start alias [name]```

**显示所有已保存的别名**

```mole show alias```

# SYNOPSIS

**mole** _command_ [_subcommand_] [_options_]

# PARAMETERS

**--source** _[HOST:]PORT_
> 本地监听的地址和端口。未指定时自动选择。

**--destination** _HOST:PORT_
> 要转发到的远程目标。

**--server** _USER@HOST[:PORT]_
> 用作隧道的 SSH 服务器。

**--key** _path_
> SSH 私钥文件的路径。

**--verbose**
> 启用详细日志输出。

**--detach**
> 在后台运行 mole。

**--insecure**
> 跳过 SSH 主机密钥校验。

**--connection-retries** _N_
> SSH 连接断开时的重连尝试次数。

**--retry-wait** _duration_
> 重连尝试之间的等待时间。

# DESCRIPTION

**mole** 是一个专注于可靠性和用户体验的创建 SSH 隧道的 CLI 应用。它通过 SSH 服务器把本地端口转发到远程地址，支持在单条连接上承载多个隧道，并能利用 SSH 配置文件的设置。

子命令包括 **start**（启动隧道或别名）、**add**（保存隧道别名）、**delete**（删除别名）、**show**（显示别名详情）、**stop**（停止正在运行的隧道）和 **version**。

Mole 通过合成保活包维持空闲连接，并在 SSH 连接断开时自动重连。隧道配置可保存为别名以便快速复用。

# CAVEATS

需要对隧道服务器的 SSH 访问权限。认证使用系统的 SSH 配置和密钥。

# HISTORY

**mole** 由 **davrodpin** 创建，使用 **Go** 编写。

# INSTALL

```brew: brew install mole```

```nix: nix profile install nixpkgs#mole```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [autossh](/man/autossh)(1)
