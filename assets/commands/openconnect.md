# TAGLINE

SSL VPN 客户端

# TLDR

**连接到 VPN**

```openconnect [vpn.example.com]```

**使用用户名连接**

```openconnect -u [username] [vpn.example.com]```

**使用证书**

```openconnect -c [cert.pem] [vpn.example.com]```

**指定协议**

```openconnect --protocol=[anyconnect|nc|gp] [vpn.example.com]```

**后台模式**

```openconnect -b [vpn.example.com]```

# SYNOPSIS

**openconnect** [_options_] _server_

# PARAMETERS

_SERVER_
> VPN 服务器地址。

**-u** _USER_
> 用户名。

**-c** _CERT_
> 客户端证书。

**--protocol** _PROTO_
> VPN 协议。

**-b**
> 在后台运行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**openconnect** 是一个 SSL VPN 客户端。与 Cisco AnyConnect 兼容。

该工具用于建立 VPN 连接。支持多种协议。

# CAVEATS

tun 设备需要 root/sudo 权限。支持多种协议。

# HISTORY

openconnect 作为 Cisco AnyConnect 客户端的**开源替代品**而创建。

# INSTALL

```apt: sudo apt install openconnect```

```dnf: sudo dnf install openconnect```

```pacman: sudo pacman -S openconnect```

```apk: sudo apk add openconnect```

```zypper: sudo zypper install openconnect```

```brew: brew install openconnect```

```nix: nix profile install nixpkgs#openconnect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openvpn](/man/openvpn)(1), [vpnc](/man/vpnc)(1)
