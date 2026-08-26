# TAGLINE

从命令行控制 Private Internet Access VPN

# TLDR

**连接** VPN

```piactl connect```

**断开** VPN

```piactl disconnect```

**显示连接状态**

```piactl get connectionstate```

**设置区域**

```piactl set region [us-east]```

**列出区域**

```piactl get regions```

**获取当前区域**

```piactl get region```

**启用终止开关**

```piactl set killswitch on```

**显示公网 IP**

```piactl get vpnip```

# SYNOPSIS

**piactl** _command_ [_args_]

# PARAMETERS

**connect**
> 连接 VPN。

**disconnect**
> 断开 VPN。

**get** _PROPERTY_
> 获取设置或状态。

**set** _PROPERTY_ _VALUE_
> 设置配置。

**login**
> 进行身份验证。

**logout**
> 登出。

**reset**
> 重置为默认值。

# PROPERTIES

**connectionstate**
> 连接状态。

**region**
> VPN 区域。

**regions**
> 可用区域。

**vpnip**
> VPN IP 地址。

**publicip**
> 当前公网 IP。

**killswitch**
> 终止开关状态。

**protocol**
> VPN 协议。

# DESCRIPTION

**piactl** 从命令行控制 Private Internet Access VPN。它管理连接和设置。

连接命令处理 VPN 状态。快速连接使用上次的区域或自动选择。

区域选择决定出口位置。列出可用区域即可查看选项。

终止开关在断开连接时阻止流量，防止连接故障期间的 IP 泄漏。

设置项可配置协议、端口和功能。DNS 和分流（split tunneling）均可配置。

# CAVEATS

需要 PIA 守护进程正在运行。需要订阅。某些功能需要先在 GUI 中配置。

# HISTORY

**piactl** 是 **Private Internet Access** VPN 服务的命令行界面。它为 PIA 客户端提供可脚本化的控制，适合自动化和无头系统。

# SEE ALSO

[openvpn](/man/openvpn)(1), [wg](/man/wg)(1), [nmcli](/man/nmcli)(1)
