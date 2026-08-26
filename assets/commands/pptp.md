# TAGLINE

建立 PPTP VPN 隧道连接

# TLDR

**连接到 PPTP VPN 服务器**

```pptp [server] --nolaunchpppd```

**以调试输出连接**

```pptp [server] debug```

**以更高的日志详细程度连接**

```pptp [server] --loglevel [3]```

# SYNOPSIS

**pptp** _server_ [_options_] [_pppd-options_]

# PARAMETERS

_server_
> PPTP 服务器的 IP 地址或主机名。

**--nolaunchpppd**
> 不启动 pppd；在 pppd 被独立启动时使用。

**--phone** _number_
> 将电话号码传递给远程主机（某些服务器用它进行呼叫识别）。

**--loglevel** _N_
> 设置日志详细程度（0=最少，3=最多）。

**debug**
> 启用调试模式，输出额外的诊断信息。

**--quirks** _quirk_
> 解决特定 PPTP 实现中的缺陷（例如 BEZEQ_ISRAEL）。

**--timeout** _seconds_
> 等待服务器连接应答的时间。

# DESCRIPTION

**pptp** 使用点对点隧道协议（Point-to-Point Tunneling Protocol）建立 VPN 连接。它通过将 PPP 会话封装在 GRE（通用路由封装）数据包中，创建到远程 PPTP 服务器的隧道。

该客户端与 **pppd** 配合工作，后者处理隧道内的 PPP 协商和身份验证。pptp 无法识别的选项都会传递给 pppd。PPTP 被视为一种存在已知安全缺陷的过时协议，新部署建议使用 OpenVPN 或 WireGuard 等现代替代方案。

# CAVEATS

PPTP 存在已知的加密缺陷（MS-CHAPv2 和 MPPE 漏洞），不应用于安全敏感的连接。请改用 OpenVPN 或 WireGuard。需要加载 ip_gre 内核模块。

# HISTORY

PPTP 由 **Microsoft** 和其他几家公司于 20 世纪 90 年代为 VPN 连接而开发。Linux 客户端实现是 pptp-linux 项目的一部分。

# INSTALL

```apt: sudo apt install pptp-linux```

```dnf: sudo dnf install pptp```

```zypper: sudo zypper install pptp```

```nix: nix profile install nixpkgs#pptp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pptpsetup](/man/pptpsetup)(8), [pppd](/man/pppd)(8), [openvpn](/man/openvpn)(8), [ip](/man/ip)(8)
