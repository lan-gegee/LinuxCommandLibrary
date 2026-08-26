# TAGLINE

在 Uncomplicated Firewall 中拦截流量

# TLDR

**拒绝**端口上的所有流量

```sudo ufw deny [port]```

拒绝端口上某个**协议**的流量

```sudo ufw deny [port]/[protocol]```

拒绝**来自**某源地址的所有流量

```sudo ufw deny from [source_address]```

拒绝来自某个**子网**的所有流量

```sudo ufw deny from 192.168.13.0/24```

拒绝 **UDP** 从一台主机到另一台主机某端口的流量

```sudo ufw deny from 192.168.1.12 to 192.168.1.100 port 8080 proto udp```

添加带**注释**的拒绝规则便于记录

```sudo ufw deny in 23/tcp comment "block telnet"```

按协议拒绝某接口上的**入站**流量

```sudo ufw deny in on eth0 to 192.168.1.100 proto igmp```

**模拟**拒绝规则而不实际应用

```sudo ufw --dry-run deny 80/tcp```

# SYNOPSIS

**ufw** [_--dry-run_] **deny** [_rule_]

# PARAMETERS

**deny**
> 丢弃匹配的流量（插入一条 deny/DROP 规则）

_port_[**/**_protocol_]
> 简单形式：端口号，可选 **/tcp** 或 **/udp**

**from** _address_
> 匹配源地址或网络（CIDR）

**to** _address_
> 匹配目标地址

**port** _port_
> 使用完整规则语法时的目标端口（或端口范围）

**proto** _protocol_
> 协议：**tcp**、**udp**、**igmp**、**gre** 等

**in** / **out**
> 流量方向

**on** _interface_
> 将规则限制在某个网络接口上

**comment** '_text_'
> 为规则附加人类可读的注释

**--dry-run**
> 显示将要发生的更改但不实际应用

# DESCRIPTION

**ufw deny** 向 Uncomplicated Firewall 添加一条拒绝规则，使匹配的数据包被丢弃（类似 iptables 的 DROP）。规则可以是简单的端口拒绝（`ufw deny 23/tcp`）、源地址或网络封锁（`ufw deny from 203.0.113.0/24`），也可以是包含源地址、目标地址、端口、协议和接口的完整五元组风格规则。

拒绝规则适合用来封锁已知的恶意主机、未使用的服务或整个子网，同时在其余部分保持默认放行策略。想要静默丢弃时优先使用 **deny**；希望对方收到明确拒绝时使用 **reject**（通过 `ufw reject`）。用 `ufw status numbered` 列出规则，用 `ufw delete` 按编号删除规则。

# CAVEATS

需要 root 或 sudo。与放行规则组合时规则顺序很重要——更具体的规则应谨慎排序（`ufw insert`）。如果数据包匹配先命中了更具体的较早放行规则，则拒绝规则不会覆盖它。应用配置名称必须与 `/etc/ufw/applications.d/` 下已安装的配置匹配。在管理远程主机时把自己 SSH 封锁掉会导致无法登录；建议先用 `--dry-run` 并确保有备用访问途径。

# HISTORY

属于 **ufw**（Uncomplicated Firewall）的一部分，这是源自 Ubuntu 的 iptables/nftables 前端。

# INSTALL

```dnf: sudo dnf install ufw```

```pacman: sudo pacman -S ufw```

```apk: sudo apk add ufw```

```zypper: sudo zypper install ufw```

<!-- packages: 2026-08-02 -->

# SEE ALSO

[ufw](/man/ufw)(8), [ufw-allow](/man/ufw-allow)(8), [ufw-enable](/man/ufw-enable)(8), [ufw-disable](/man/ufw-disable)(8), [iptables](/man/iptables)(8), [nftables](/man/nftables)(8)

# RESOURCES

```[Source code](https://git.launchpad.net/ufw)```

```[Documentation](https://help.ubuntu.com/community/UFW)```

<!-- verified: 2026-08-02 -->
