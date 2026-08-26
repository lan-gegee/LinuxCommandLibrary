# TAGLINE

基于 WireGuard 的网状 VPN

# TLDR

**连接网络**

```tailscale up```

**断开连接**

```tailscale down```

**查看状态**

```tailscale status```

**显示 IP 地址**

```tailscale ip```

**Ping 节点**

```tailscale ping [hostname]```

**SSH 到节点**

```tailscale ssh [user@hostname]```

**共享文件**

```tailscale file cp [file] [hostname:]```

**接收文件**

```tailscale file get [download_dir]```

# SYNOPSIS

**tailscale** [_up_] [_down_] [_status_] [_ip_] [_ping_] [_ssh_] [_file_] [_options_]

# PARAMETERS

**up**
> 连接到 Tailscale。

**down**
> 断开连接。

**status**
> 显示网络状态。

**ip** [_-4_] [_-6_]
> 显示 IP 地址。

**ping** _HOST_
> Ping 一个 Tailscale 节点。

**ssh** _TARGET_
> SSH 到节点。

**file cp** _FILES_ _TARGET:_
> 复制文件。

**file get** [_DIR_]
> 接收文件。

**cert** _DOMAIN_
> 获取 TLS 证书。

**funnel**
> 暴露到互联网。

**serve**
> 对外提供内容服务。

**logout**
> 登出。

**--accept-routes**
> 接受子网路由。

**--advertise-routes** _ROUTES_
> 通告路由。

**--exit-node** _NODE_
> 使用出口节点。

# DESCRIPTION

**tailscale** 创建加密的网状网络。设备使用 WireGuard 直接互连，没有中央服务器转发流量。

认证通过 SSO 提供商完成。登录后，设备加入你的 tailnet（Tailscale 网络）。每台设备都会获得一个稳定的 IP。

MagicDNS 为设备提供主机名。SSH 集成让身份认证无需管理密钥。

文件共享在设备之间直接传输，不涉及云存储——文件点对点直达。

出口节点让流量经由特定设备路由，从而通过可信位置安全地上网。

Funnel 将服务暴露到互联网。Serve 提供快捷的 HTTP/HTTPS 服务，并自动管理证书。

# CAVEATS

需要 Tailscale 账户。控制平面基于云端。部分功能需要付费方案。网络的可用性依赖协调服务器。

# HISTORY

**Tailscale** 由 **Brad Fitzpatrick** 等人于 **2019 年**创立。它构建在 WireGuard 之上，提供易用的网状 VPN，专注于零配置的互联互通。

# INSTALL

```dnf: sudo dnf install tailscale```

```pacman: sudo pacman -S tailscale```

```apk: sudo apk add tailscale```

```zypper: sudo zypper install tailscale```

```brew: brew install tailscale```

```nix: nix profile install nixpkgs#tailscale```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wg](/man/wg)(8), [ssh](/man/ssh)(1), [openvpn](/man/openvpn)(8)
