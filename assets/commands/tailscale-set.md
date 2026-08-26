# TAGLINE

配置持久的 Tailscale 选项

# TLDR

**接受**其他 tailnet 节点通告的**路由**

```tailscale set --accept-routes```

**将本设备通告为出口节点**

```tailscale set --advertise-exit-node```

**设置设备主机名**

```tailscale set --hostname [name]```

允许非 root 用户控制 tailscaled

```tailscale set --operator=[$USER]```

让本设备的流量经由出口节点**路由**

```tailscale set --exit-node [node-name-or-ip]```

# SYNOPSIS

**tailscale** **set** [_options_]

# PARAMETERS

**--accept-routes**
> 接受其他节点通告的子网路由。

**--accept-dns**
> 接受来自管理控制台的 DNS 配置。

**--advertise-routes** _CIDRS_
> 将物理子网路由暴露给 tailnet。

**--advertise-exit-node**
> 将本节点提供为出口节点。

**--advertise-tags** _TAGS_
> 为本设备应用 ACL 标签。

**--exit-node** _NODE_
> 让流量经由指定的出口节点路由（空字符串表示清除）。

**--exit-node-allow-lan-access**
> 连接到出口节点时仍允许访问局域网。

**--hostname** _NAME_
> 覆盖设备主机名。

**--shields-up**
> 阻止所有入站连接。

**--ssh**
> 在本设备上启用 Tailscale SSH。

**--operator** _USER_
> 允许指定的本地用户无需 sudo 即可操作 **tailscaled**。

**--auto-update**
> 启用 Tailscale 客户端自动更新（在支持的平台上）。

# DESCRIPTION

**tailscale set** 在不打断现有连接的情况下修改每个节点的 Tailscale 选项。**tailscale up** 会把所有未指定的标志重置回默认值，而 **set** 只修改你传入的标志——因此更适合做增量修改，也更安全。

# INSTALL

```dnf: sudo dnf install tailscale```

```pacman: sudo pacman -S tailscale```

```apk: sudo apk add tailscale```

```zypper: sudo zypper install tailscale```

```brew: brew install tailscale```

```nix: nix profile install nixpkgs#tailscale```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tailscale](/man/tailscale)(1), [tailscale-up](/man/tailscale-up)(1)
