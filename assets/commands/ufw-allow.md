# TAGLINE

在 Uncomplicated Firewall 中放行流量

# TLDR

**放行**端口上的所有流量

```sudo ufw allow [port]```

放行端口上某个**协议**的流量

```sudo ufw allow [port]/[protocol]```

放行已知的**应用配置**

```sudo ufw allow OpenSSH```

放行**来自**某源地址的所有流量

```sudo ufw allow from [source_address]```

允许 **TCP** 从一台主机到另一台主机的 443 端口

```sudo ufw allow from 192.168.1.12 to 192.168.1.100 port 443 proto tcp```

添加带**注释**的放行规则便于记录

```sudo ufw allow 5432 comment "PostgreSQL"```

**模拟**放行规则而不实际应用

```sudo ufw --dry-run allow 80/tcp```

# SYNOPSIS

**ufw** [_--dry-run_] **allow** [_rule_]

# PARAMETERS

**allow**
> 放行匹配的流量（插入一条 allow 规则）

_port_[**/**_protocol_]
> 简单形式：端口号，可选 **/tcp** 或 **/udp**

**from** _address_
> 匹配源地址或网络（CIDR）

**to** _address_
> 匹配目标地址

**port** _port_
> 使用完整规则语法时的目标端口（或端口范围）

**proto** _protocol_
> 协议：**tcp**、**udp**、**gre** 等

**in** / **out**
> 流量方向

**on** _interface_
> 将规则限制在某个网络接口上

**comment** '_text_'
> 为规则附加人类可读的注释

**--dry-run**
> 显示将要发生的更改但不实际应用

# DESCRIPTION

**ufw allow** 向 Uncomplicated Firewall 添加一条放行规则，使匹配的数据包被接受。规则可以是简单的端口放行（`ufw allow 22/tcp`）、服务或应用配置（`ufw allow OpenSSH`），也可以是包含源地址、目标地址、端口、协议和接口的完整五元组风格规则。

在远程主机上，放行规则通常应在 `ufw enable` **之前**配置好，以保证 SSH 和其他管理访问不被切断。用 `ufw status numbered` 列出规则，用 `ufw delete` 按编号删除规则。

# CAVEATS

需要 root 或 sudo。规则的顺序和默认策略（`ufw default deny incoming`）很重要——只有当默认策略原本会拦截该流量时，放行规则才起作用。应用配置名称必须与 `/etc/ufw/applications.d/` 下已安装的配置匹配。

# HISTORY

属于 **ufw**（Uncomplicated Firewall）的一部分，这是源自 Ubuntu 的 iptables/nftables 前端。

# INSTALL

```dnf: sudo dnf install ufw```

```pacman: sudo pacman -S ufw```

```apk: sudo apk add ufw```

```zypper: sudo zypper install ufw```

<!-- packages: 2026-07-29 -->

# SEE ALSO

[ufw](/man/ufw)(8), [ufw-enable](/man/ufw-enable)(8), [ufw-disable](/man/ufw-disable)(8), [iptables](/man/iptables)(8), [nftables](/man/nftables)(8)

# RESOURCES

```[Source code](https://git.launchpad.net/ufw)```

```[Documentation](https://help.ubuntu.com/community/UFW)```

<!-- verified: 2026-07-29 -->
