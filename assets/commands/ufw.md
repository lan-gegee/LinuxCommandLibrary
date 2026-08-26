# TAGLINE

Uncomplicated Firewall 管理界面

# TLDR

**启用** ufw

```sudo ufw enable```

**禁用** ufw

```sudo ufw disable```

显示带编号的**规则**

```sudo ufw status numbered```

**放行**端口上的入站流量

```sudo ufw allow 5432 comment "Service"```

放行来自特定 IP 的 **TCP 流量**

```sudo ufw allow proto tcp from 192.168.0.4 to any port 22```

**拒绝**端口上的流量

```sudo ufw deny 80```

拒绝端口范围内的 **UDP 流量**

```sudo ufw deny proto udp from any to any port 8412:8500```

将默认入站策略**设为** deny

```sudo ufw default deny incoming```

**放行**已知的应用配置

```sudo ufw allow OpenSSH```

按编号**删除**规则

```sudo ufw delete [rule_number]```

放行接口之间的**路由转发**流量

```sudo ufw route allow in on [eth0] out on [eth1]```

# SYNOPSIS

**ufw** [_--dry-run_] _command_ [_rule_]

# DESCRIPTION

**ufw**（Uncomplicated Firewall）是 iptables/nftables 的前端，旨在让防火墙配置更简单。它提供友好的界面来管理 netfilter 防火墙规则，同时支持简单和复杂的规则写法。

# PARAMETERS

**enable**
> 启用防火墙并在开机时加载规则

**disable**
> 禁用防火墙并卸载规则

**reload**
> 重载防火墙配置

**reset**
> 重置为安装时的默认值

**status**
> 显示防火墙状态和规则

**status verbose**
> 显示详细状态，包括日志级别和默认策略

**status numbered**
> 显示带行号的规则以便删除

**--dry-run**
> 显示将要进行的更改但不实际应用

**--force**
> 不弹出确认提示直接执行

# RULE COMMANDS

**allow**
> 放行匹配的流量

**deny**
> 静默拦截匹配的流量

**reject**
> 拦截匹配的流量并通知发送方

**limit**
> 对连接限速（30 秒内尝试 6 次以上则封锁）

**delete**
> 按规格或编号移除规则

**insert NUM**
> 在指定位置插入规则

**prepend**
> 将规则添加到同 IP 类型的所有其他规则之前

**route** _allow|deny|reject|limit_
> 为路由/转发的流量添加规则

# DEFAULT POLICY

**default allow|deny|reject incoming**
> 设置入站流量的默认策略

**default allow|deny|reject outgoing**
> 设置出站流量的默认策略

**default allow|deny|reject routed**
> 设置转发流量的默认策略

# APPLICATION PROFILES

**app list**
> 列出可用的应用配置

**app info** _PROFILE_
> 显示某个应用配置的信息

**app default allow|deny|reject|skip**
> 设置默认的应用策略

# REPORTS

**show raw**
> 显示原始 iptables 规则

**show added**
> 显示命令行上添加的规则原样

**show listening**
> 显示监听端口及关联的规则

**show builtins**
> 显示默认的内建规则

# RULE SYNTAX

**简单形式**: ufw allow 22/tcp
**带注释**: ufw allow 80 comment 'HTTP'
**端口范围**: ufw allow 6000:6007/tcp
**多端口**: ufw allow 80,443/tcp
**指定来源地址**: ufw allow from 192.168.1.0/24
**完整语法**: ufw allow proto tcp from any to any port 80

# LOGGING

**logging off**
> 禁用日志

**logging on**
> 启用日志（低级别）

**logging low|medium|high|full**
> 设置日志详细程度

# CONFIGURATION

**/etc/ufw/ufw.conf**
> 主配置文件，控制启用/禁用状态、日志级别和 IPv6 支持。

**/etc/ufw/before.rules**
> 在 ufw 管理的规则之前应用的自定义 iptables 规则。

**/etc/ufw/after.rules**
> 在 ufw 管理的规则之后应用的自定义 iptables 规则。

**/etc/default/ufw**
> 默认策略设置以及 input/output/forward 策略配置。

# CAVEATS

默认策略为：拒绝入站、允许出站、拒绝转发。如果未先配置规则就启用 ufw，可能会中断现有连接。应用更改前可用 **--dry-run** 预览。

# HISTORY

**ufw** 由 Canonical 为 Ubuntu 开发，用于简化 iptables 防火墙管理。它首次发布于 Ubuntu 8.04（2008 年），如今已成为众多 Linux 发行版上流行的防火墙工具。

# INSTALL

```dnf: sudo dnf install ufw```

```pacman: sudo pacman -S ufw```

```apk: sudo apk add ufw```

```zypper: sudo zypper install ufw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [ip6tables](/man/ip6tables)(8), [nft](/man/nft)(8), [firewall-cmd](/man/firewall-cmd)(1)
