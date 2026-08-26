# TAGLINE

点对点协议连接守护进程

# TLDR

**启动 PPP 连接**

```pppd [device] [speed]```

**使用选项文件连接**

```pppd call [provider]```

**调试模式**

```pppd debug [device] [speed]```

**指定认证信息**

```pppd user [username] password [password]```

# SYNOPSIS

**pppd** [_options_] [_device_] [_speed_]

# PARAMETERS

_DEVICE_
> 串行设备。

_SPEED_
> 波特率。

**call** _PROVIDER_
> 使用提供商配置。

**debug**
> 启用调试。

**user** _NAME_
> 用于认证的用户名。

**password** _PASS_
> 用于认证的密码。

**noauth**
> 不要求认证。

# DESCRIPTION

**pppd** 是点对点协议（Point-to-Point Protocol）守护进程，用于在串行链路、调制解调器和以太网上建立并管理 PPP 网络连接。它负责链路协商、认证（PAP、CHAP、EAP）、IP 地址分配和 DNS 配置。

该守护进程通常通过 **pon** 或 **pppoe-connect** 之类的辅助脚本调用，而不是直接运行。**/etc/ppp/peers/** 中的提供商配置文件为不同的 ISP 或 VPN 端点定义连接参数。插件则扩展了 PPPoE、RADIUS 认证等其他协议的功能。

# CONFIGURATION

**/etc/ppp/peers/**
> 提供商配置文件，为每个 ISP 或 VPN 端点定义连接参数。通过 `pppd call <provider>` 调用。

**/etc/ppp/pap-secrets**, **/etc/ppp/chap-secrets**
> PAP 和 CHAP 协议的认证凭据文件，包含用户名、服务器和密码条目。

**/etc/ppp/options**
> 应用于所有 PPP 连接的全局默认选项。针对特定设备的选项可放在 **/etc/ppp/options.<device>** 中。

**/etc/ppp/ip-up**, **/etc/ppp/ip-down**
> 在 PPP 链路建立或断开时执行的脚本，用于路由、防火墙和 DNS 更新。

# CAVEATS

需要 root 权限。配置较为复杂。

# HISTORY

pppd 是 Linux 网络中的**标准 PPP 守护进程**。

# INSTALL

```apt: sudo apt install ppp```

```dnf: sudo dnf install ppp```

```pacman: sudo pacman -S ppp```

```apk: sudo apk add ppp-daemon```

```zypper: sudo zypper install ppp```

```nix: nix profile install nixpkgs#ppp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pon](/man/pon)(1), [poff](/man/poff)(1), [pppconfig](/man/pppconfig)(8)
