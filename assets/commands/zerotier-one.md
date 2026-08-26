# TAGLINE

ZeroTier 虚拟网络服务守护进程

# TLDR

**在前台启动服务**

```sudo zerotier-one```

**以自定义主目录启动**

```sudo zerotier-one [/var/lib/zerotier-one]```

**在后台运行（守护进程模式）**

```sudo zerotier-one -d```

# SYNOPSIS

**zerotier-one** [**-d**] [_home_directory_]

# PARAMETERS

**-d**
> 以守护进程方式在后台运行

_home_directory_
> ZeroTier 主目录（默认：/var/lib/zerotier-one）

# DESCRIPTION

**zerotier-one** 是 ZeroTier 网络虚拟化服务守护进程。它创建虚拟网络接口并管理加密的点对点连接，以构成软件定义网络。

服务运行时会：
- 维护与 ZeroTier 根服务器的连接
- 与其他节点建立点对点隧道
- 为已加入的网络创建虚拟网络接口（zt*）
- 为 zerotier-cli 提供本地 API
- 处理 NAT 穿透和连接优化

主目录包含身份文件、网络配置以及本地 API 的身份验证令牌。

在 systemd 系统上，zerotier-one 通常作为 systemd 服务（zerotier-one.service）管理，而不是直接运行。

# CAVEATS

需要 root 权限才能创建网络接口并绑定特权端口。

该服务默认绑定 UDP 端口 9993 用于对等通信。

主目录中的身份文件（identity.secret、identity.public）应当备份。丢失它们意味着必须生成具有不同地址的新身份。

防火墙规则必须允许对等连接的 UDP 流量。UDP 被阻断会迫使流量经由中继转发，降低性能。

# INSTALL

```pacman: sudo pacman -S zerotier-one```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zerotier-cli](/man/zerotier-cli)(1), [zerotier-idtool](/man/zerotier-idtool)(1), [systemctl](/man/systemctl)(1)
