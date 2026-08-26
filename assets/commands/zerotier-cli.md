# TAGLINE

管理 ZeroTier 虚拟网络连接

# TLDR

**显示节点状态**

```sudo zerotier-cli status```

**加入网络**

```sudo zerotier-cli join [network_id]```

**离开网络**

```sudo zerotier-cli leave [network_id]```

**列出已加入的网络**

```sudo zerotier-cli listnetworks```

**列出已连接的对等节点**

```sudo zerotier-cli listpeers```

**显示节点信息**

```sudo zerotier-cli info```

# SYNOPSIS

**zerotier-cli** [_options_] _command_ [_args_]

# PARAMETERS

**-D** _path_
> ZeroTier 主目录

**-p** _port_
> 本地 API 端口

**-T** _token_
> 身份验证令牌

# SUBCOMMANDS

**status**
> 显示节点状态和地址

**info**
> 显示节点信息

**join** _network_
> 加入 ZeroTier 网络

**leave** _network_
> 离开 ZeroTier 网络

**listnetworks**
> 列出已加入的网络

**listpeers**
> 列出已连接的对等节点

**listmoons**
> 列出已加入的 moon（自定义根服务器）

**orbit** _world_id_ _seed_
> 加入 moon

**deorbit** _world_id_
> 离开 moon

**set** _network_ _setting_ _value_
> 配置网络设置

# DESCRIPTION

**zerotier-cli** 是管理 ZeroTier One 的命令行界面，ZeroTier One 是一种创建安全虚拟网络的软件定义网络（SDN）服务。它与本地 zerotier-one 服务通信。

ZeroTier 在节点之间建立加密的点对点连接，跨越互联网组成虚拟局域网。每个节点获得一个唯一的 10 位地址。网络由 16 位网络 ID 标识。

加入网络后，节点可以像在同一局域网内一样通信，从而实现远程访问、游戏联机以及连接分布式系统。网络成员资格通过 ZeroTier Central 或自托管控制器进行管理。

# CAVEATS

大多数命令需要 root/sudo 权限才能与 zerotier-one 服务通信。

加入网络需要网络控制器的授权（公共网络自动授权，私有网络需手动操作）。

可能需要调整防火墙规则以放行 ZeroTier 流量（默认 UDP 端口 9993）。

网络性能取决于能否建立直接的对等连接，还是必须经由中继转发。

# SEE ALSO

[zerotier-one](/man/zerotier-one)(8), [zerotier-idtool](/man/zerotier-idtool)(1), [ip](/man/ip)(8), [wg](/man/wg)(8)
