# TAGLINE

管理 NetworkManager 连接配置文件

# TLDR

列出所有 **NetworkManager 连接**

```nmcli connection```

**激活**一个连接

```nmcli connection up uuid```

**停用**一个连接

```nmcli connection down uuid```

创建一个**自动配置**的连接

```nmcli connection add ifname eth0 type ethernet ipv4.method auto ipv6.method auto```

创建一个**静态 IPv4** 连接

```nmcli connection add ifname eth0 type ethernet ip4 10.0.0.7/8 gw4 10.0.0.1 ipv4.dns 10.0.0.1```

创建一个**静态 IPv6** 连接

```nmcli connection add ifname eth0 type ethernet ip6 2001:db8::2/64 gw6 2001:db8::1```

从文件导入 **VPN** 连接

```nmcli connection import type openvpn file vpn_config.ovpn```

# SYNOPSIS

**nmcli connection** {_show_|_up_|_down_|_add_|_edit_|_modify_|_clone_|_delete_|_monitor_|_reload_|_load_|_migrate_|_import_|_export_} [_ARGUMENTS_]

# DESCRIPTION

**nmcli connection** 管理 NetworkManager 连接配置文件。它可以列出、激活、停用、创建、修改和删除网络连接配置，包括以太网、Wi-Fi、VPN 及其他连接类型。

# COMMANDS

**show [id]**
> 列出连接，或显示特定连接的详情

**up id|uuid**
> 激活一个连接

**down id|uuid**
> 停用一个连接

**add**
> 创建新的连接配置文件

**edit [id|uuid]**
> 启动交互式连接编辑器

**modify id|uuid**
> 修改连接属性。属性值支持 `+`/`-` 前缀来追加或移除列表项

**clone id|uuid NEW_NAME**
> 以新名称复制现有的配置文件

**delete id|uuid**
> 移除一个连接配置文件

**monitor [id|uuid]**
> 实时监视所有或特定配置文件的活动变化

**reload**
> 从磁盘重新加载所有连接文件

**load filename**
> 将磁盘上的单个连接文件加载进 NetworkManager

**migrate**
> 将旧式 keyfile/ifcfg 位置的配置文件迁移到默认存储位置

**import type TYPE file FILE**
> 导入外部连接（例如 VPN）

**export id**
> 导出连接配置文件

# COMMON ADD OPTIONS

**ifname**: 绑定连接的接口名
**type**: 连接类型（ethernet、wifi、vpn、bridge 等）
**con-name**: 自定义连接名称
**ip4**: 带前缀长度的 IPv4 地址
**gw4**: IPv4 网关地址
**ip6**: 带前缀长度的 IPv6 地址
**gw6**: IPv6 网关地址
**ipv4.method**: auto、manual 或 disabled
**ipv6.method**: auto、manual 或 ignore
**ipv4.dns**: DNS 服务器地址

# COMMON GLOBAL OPTIONS

**--ask**
> 对任何必需但缺失的参数进行交互式询问。不适合脚本使用。

**--wait** _seconds_
> 覆盖等待操作（如 **up**）完成时的默认超时时间。

**--active**
> 在 **show** 时只列出当前处于活动状态的连接。

**--offline**
> 在不经过正在运行的 NetworkManager 守护进程的情况下编辑连接文件。

**--temporary**
> 在 **modify** 时仅将更改保留在内存中——守护进程重启后即被丢弃。

# CAVEATS

包含空格的连接名称需要加引号。当多个连接同名时请使用 UUID。除非使用 **--temporary**，否则 **modify** 所做的更改会在下一次激活时生效。

# HISTORY

是 **NetworkManager** 的 **nmcli** 命令行界面的一部分。提供可脚本化的网络配置管理。

# INSTALL

```apt: sudo apt install network-manager```

```apk: sudo apk add networkmanager-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmcli-device](/man/nmcli)(1), [nmtui](/man/nmtui)(1)
