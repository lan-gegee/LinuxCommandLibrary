# TAGLINE

动态防火墙管理接口

# TLDR

**检查** firewalld 守护进程状态

```firewall-cmd --state```

**列出**所有活动区域及其绑定的接口

```firewall-cmd --get-active-zones```

**列出**默认区域中的全部规则

```firewall-cmd --list-all```

**永久添加**服务到某个区域

```firewall-cmd --permanent --zone public --add-service https```

**永久添加**端口到某个区域

```firewall-cmd --permanent --zone public --add-port 8080/tcp```

**永久移除**服务

```firewall-cmd --permanent --zone public --remove-service http```

**重载**配置（使永久性更改在运行时生效）

```firewall-cmd --reload```

**保存**运行时配置为永久配置

```firewall-cmd --runtime-to-permanent```

在区域上**启用地址伪装**（NAT）

```firewall-cmd --permanent --zone public --add-masquerade```

# SYNOPSIS

**firewall-cmd** [_OPTIONS_]

# DESCRIPTION

**firewall-cmd** 是 firewalld 的命令行接口，用于动态管理 Linux 防火墙。它支持区域、服务、端口转发、地址伪装和富规则，同时提供运行时和永久两种配置方式。

# PARAMETERS

**--state**
> 检查 firewalld 守护进程是否在运行（运行中则返回退出码 0）。

**--reload**
> 在保留状态信息的前提下重新加载防火墙规则。会把永久规则应用到运行时配置。

**--complete-reload**
> 彻底重载防火墙，包括 netfilter 内核模块。可能会终止现有连接。

**--runtime-to-permanent**
> 把当前运行时配置保存为永久配置。

**--get-zones**
> 列出所有预定义的区域。

**--get-default-zone**
> 打印连接和接口所用的默认区域。

**--set-default-zone** _zone_
> 设置默认区域。

**--get-active-zones**
> 打印当前活动的区域及其绑定的接口和来源。

**--list-all-zones**
> 列出所有可用区域及其完整设置。

**--list-all**
> 列出当前或指定区域内添加或启用的一切条目。

**--zone** _zone_
> 指定要操作的区域。

**--get-services**
> 列出所有预定义的服务。

**--add-service** _service_
> 向区域添加服务。

**--remove-service** _service_
> 从区域移除服务。

**--add-port** _port/protocol_
> 向区域添加端口或端口范围（例如 `8080/tcp` 或 `5000-5100/tcp`）。

**--remove-port** _port/protocol_
> 从区域移除先前添加的端口。

**--add-masquerade**
> 在区域上启用 IPv4 地址伪装（NAT）。机器作为路由器使用时很有用。

**--remove-masquerade**
> 在区域上禁用 IPv4 地址伪装。

**--query-masquerade**
> 查询该区域是否启用了 IPv4 地址伪装。

**--add-rich-rule** _rule_
> 添加一条富语言（rich language）防火墙规则。

**--remove-rich-rule** _rule_
> 移除一条富语言防火墙规则。

**--permanent**
> 使更改永久生效（重启后依然保留）。需要执行 `--reload` 才能在运行时生效。

**--panic-on** / **--panic-off**
> 启用/禁用恐慌模式（丢弃所有出入站流量）。

**--change-interface** _interface_
> 更改网络接口所绑定的区域。

# CONFIGURATION

**/etc/firewalld/zones/*.xml**
> 区域定义，包括允许的服务、端口和富规则。

**/etc/firewalld/services/*.xml**
> 服务定义，把服务名映射到端口和协议。

# CAVEATS

不带 --permanent 的更改会在重载或重启后丢失。做完永久性更改后，需要用 --reload 使其在运行时生效。修改区域可能导致活动会话被断开。

# HISTORY

**firewall-cmd** 是 **firewalld** 的客户端；firewalld 是 Red Hat 推出的动态防火墙管理守护进程，常见于 RHEL、CentOS 和 Fedora。

# INSTALL

```dnf: sudo dnf install firewalld```

```pacman: sudo pacman -S firewalld```

```apk: sudo apk add firewalld```

```zypper: sudo zypper install firewalld```

```nix: nix profile install nixpkgs#firewalld```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firewalld](/man/firewalld)(1), [iptables](/man/iptables)(8), [nft](/man/nft)(8)
