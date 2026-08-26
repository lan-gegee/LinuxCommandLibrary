# TAGLINE

Tailscale 控制服务器的自托管实现

# TLDR

**启动服务器**

```headscale serve```

**创建用户**

```headscale users create [username]```

**列出用户**

```headscale users list```

**创建认证密钥**

```headscale authkeys create --user [username]```

**列出节点**

```headscale nodes list```

**注册节点**

```headscale nodes register --user [username] --key [nodekey:abc123]```

**删除节点**

```headscale nodes delete --id [1]```

**为节点启用路由**

```headscale routes enable --route [10.0.0.0/24]```

# SYNOPSIS

**headscale** _command_ [_subcommand_] [_options_]

# COMMANDS

**serve**
> 启动 Headscale 服务器。

**users** create|list|rename|destroy
> 管理用户（命名空间）。

**nodes** list|register|delete|expire|rename|move|tag
> 管理节点。

**authkeys** create|list|expire
> 管理预认证密钥。

**routes** list|enable|disable
> 管理子网路由。

**preauthkeys** create|list|expire
> authkeys 的别名。

**apikeys** create|list|expire
> 管理 API 密钥。

**debug**
> 调试命令。

**completion**
> 生成 shell 补全脚本。

# PARAMETERS

**--user**, **-u** _name_
> 用户（命名空间）名称。

**--key** _nodekey_
> 用于注册的节点密钥。

**--id** _id_
> 节点或路由 ID。

**--expiration** _duration_
> 密钥过期时间。

**--reusable**
> 创建可重复使用的认证密钥。

**--ephemeral**
> 创建临时认证密钥。

**--tags** _list_
> 认证密钥的 ACL 标签。

**--output** _format_
> 输出格式：human、json、yaml。

# DESCRIPTION

**headscale** 是 Tailscale 控制服务器的自托管实现，用于协调 Tailscale 客户端之间的 WireGuard 连接。

**serve** 启动协调服务器。客户端连接后交换密钥并发现对等节点。配置文件位于 **/etc/headscale/config.yaml**。

用户（命名空间）用来组织节点。除非 ACL 策略允许跨用户通信，否则各用户的节点相互隔离。注册节点之前必须先创建用户。

**authkeys** 创建预认证密钥，用于无人值守的注册。客户端用它们代替交互式登录。密钥可以是可重复使用的或一次性的。

节点通告的子网路由必须通过 **routes enable** 显式启用。由此控制哪些网络可以通过 mesh 网络访问。

配置中定义的 ACL 策略基于用户、组和标签来控制节点之间的流量。

# CAVEATS

生产环境需要 TLS 证书。NAT 穿透需要 DERP 服务器。并非所有 Tailscale 功能都受支持。Tailscale 客户端需要进行 HEADSCALE_URL 配置。

# HISTORY

Headscale 由 **Juan Font** 创建，首次发布于 **2020 年**。它在复用相同的 WireGuard 客户端的基础上，提供了 Tailscale 协调服务的自托管替代方案。该项目源于人们对摆脱厂商控制的自主托管 mesh VPN 的需求。对于希望兼得 Tailscale 兼容性与基础设施完全掌控权的组织而言，Headscale 颇受欢迎。

# INSTALL

```dnf: sudo dnf install headscale```

```pacman: sudo pacman -S headscale```

```apk: sudo apk add headscale```

```zypper: sudo zypper install headscale```

```nix: nix profile install nixpkgs#headscale```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tailscale](/man/tailscale)(1), [nebula](/man/nebula)(1)
