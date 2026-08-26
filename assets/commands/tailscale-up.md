# TAGLINE

将设备接入 Tailscale 网络

# TLDR

**连接到 Tailscale**

```tailscale up```

通过出口节点**连接**

```tailscale up --exit-node=[node]```

接受路由并**连接**

```tailscale up --accept-routes```

启用 SSH 后**连接**

```tailscale up --ssh```

**通告为出口节点**

```tailscale up --advertise-exit-node```

# SYNOPSIS

**tailscale** **up** [_options_]

# PARAMETERS

**--accept-routes**
> 接受通告的路由。

**--advertise-exit-node**
> 将本机提供为出口节点。

**--exit-node** _node_
> 让流量经由 node 路由。

**--hostname** _name_
> 设备主机名。

**--shields-up**
> 阻止入站连接。

**--ssh**
> 启用 Tailscale SSH。

**--login-server** _url_
> 自定义控制服务器。

**--authkey** _key_
> 预授权密钥。

**--accept-dns**
> 接受来自管理控制台的 DNS 配置。

**--advertise-routes** _CIDR_
> 将物理子网路由暴露给 tailnet。

**--advertise-tags** _TAGS_
> 为本设备赋予基于标签的权限。

**--force-reauth**
> 强制重新认证。

**--reset**
> 将未指定的设置重置为默认值。

**--qr**
> 为登录 URL 生成二维码。

**--exit-node-allow-lan-access**
> 使用出口节点时仍允许访问局域网。

**--operator** _USER_
> 无需 sudo 即可操作 tailscaled 的 Unix 用户名。

**--timeout** _DURATION_
> 服务初始化的最长等待时间。

# DESCRIPTION

**tailscale up** 将设备连接到 Tailscale 网络，完成认证并加入 tailnet。首次运行时会打开浏览器进行认证，除非提供了 authkey。

要修改已连接设备的设置，优先使用 **tailscale set**——它只更新指定的标志；而 **tailscale up** 会把所有未指定的标志应用为操作系统默认值。

# INSTALL

```dnf: sudo dnf install tailscale```

```pacman: sudo pacman -S tailscale```

```apk: sudo apk add tailscale```

```zypper: sudo zypper install tailscale```

```brew: brew install tailscale```

```nix: nix profile install nixpkgs#tailscale```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tailscale](/man/tailscale)(1), [tailscale-set](/man/tailscale-set)(1)
