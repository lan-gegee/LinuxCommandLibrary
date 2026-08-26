# TAGLINE

兼容 Cisco 的 IPSec VPN 客户端

# TLDR

使用配置文件**连接**

```sudo vpnc [config_file]```

**断开** VPN

```sudo vpnc-disconnect```

# SYNOPSIS

**vpnc** [_OPTIONS_] [_CONFIG_FILE_]

# PARAMETERS

**--gateway** _HOST_
> VPN 网关地址

**--id** _ID_
> IPSec 组 ID

**--secret** _SECRET_
> IPSec 组密钥

**--username** _USER_
> 用于身份验证的用户名

# DESCRIPTION

**vpnc** 是一个面向 Cisco 3000 VPN 集中器、IOS 和 PIX 设备的 VPN 客户端。它建立的 IPSec 连接与 Cisco VPN 硬件兼容。

配置文件通常包含网关地址、组 ID、组密钥和用户凭据。

# CAVEATS

需要 root 权限。配置文件可能包含敏感凭据。某些功能可能无法在所有 Cisco VPN 设备上使用。

# INSTALL

```apt: sudo apt install vpnc```

```dnf: sudo dnf install vpnc```

```pacman: sudo pacman -S vpnc```

```apk: sudo apk add vpnc```

```zypper: sudo zypper install vpnc```

```nix: nix profile install nixpkgs#vpnc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openconnect](/man/openconnect)(8), [openvpn](/man/openvpn)(8)
