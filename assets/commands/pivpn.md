# TAGLINE

简洁的 OpenVPN 和 WireGuard 服务器管理工具

# TLDR

**添加**新的客户端设备

```sudo pivpn add```

**列出**所有客户端

```sudo pivpn list```

显示**已连接**的客户端及统计信息

```sudo pivpn clients```

**吊销**某个客户端

```sudo pivpn revoke```

**卸载** PiVPN

```sudo pivpn uninstall```

# SYNOPSIS

**pivpn** [**add**|**list**|**clients**|**revoke**|**uninstall**|**-d**|**-u**]

# COMMANDS

**add**
> 创建新的客户端配置

**list**
> 列出所有客户端配置

**clients**
> 显示已连接客户端及统计信息

**revoke**
> 吊销客户端证书

**uninstall**
> 移除 PiVPN 安装

**debug, -d**
> 生成用于故障排查的调试输出。

**update, -u**
> 检查 PiVPN 更新。

**off**
> 禁用 PiVPN 服务器。

**backup**
> 创建服务器/客户端配置的备份。

# DESCRIPTION

**pivpn** 简化了 Linux（尤其是 Raspberry Pi）上 OpenVPN 或 WireGuard 服务器的管理。它通过交互式菜单系统处理证书生成、客户端配置和连接管理。

它最初为 Raspberry Pi 设计，但可在任何基于 Debian 的系统上运行。它能以安全加固的配置自动完成 VPN 服务器的复杂设置。

# CONFIGURATION

**/etc/pivpn/**
> PiVPN 配置目录，包含安装变量和协议设置。

**/etc/openvpn/** 或 **/etc/wireguard/**
> 由 PiVPN 管理的 VPN 服务器配置文件，取决于所选协议。

**/home/\<user\>/ovpns/** 或 **/home/\<user\>/configs/**
> 生成的待分发客户端配置文件。

# CAVEATS

安装脚本需要 curl。初始设置需要联网。外部访问需要在路由器上做端口转发。WireGuard 模式需要内核 5.6+ 或 DKMS 模块。

# HISTORY

**PiVPN** 的诞生是为了让家庭用户（尤其是使用 Raspberry Pi 的用户）也能轻松搭建 VPN 服务器。它逐步演进为同时支持 OpenVPN 和 WireGuard 协议，并提供以安全为重的默认配置。

# SEE ALSO

[openvpn](/man/openvpn)(8), [wg](/man/wg)(8), [wg-quick](/man/wg-quick)(8)
