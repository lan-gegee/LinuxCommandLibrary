# TAGLINE

将本地服务暴露到互联网

# TLDR

**将 8080 端口上的本地服务**暴露到互联网

```tailscale funnel [8080]```

**将本地 HTTPS 代理**目标暴露到互联网

```tailscale funnel https+insecure://localhost:[8443]```

在特定端口上**暴露**（443、8443 或 10000）

```tailscale funnel --serve-port [8443] [3000]```

关闭 funnel

```tailscale funnel off```

查看 funnel 状态

```tailscale funnel status```

以后台模式运行

```tailscale funnel --bg [8080]```

# SYNOPSIS

**tailscale** **funnel** [_options_] _target_

# PARAMETERS

**--bg**
> 在后台运行。

**--serve-port** _port_
> 面向公众的端口（443、8443 或 10000；默认 443）。

**--set-path** _path_
> 将服务挂载到特定的 URL 路径。

**off**
> 禁用 funnel。

**status**
> 显示当前 funnel 配置。

**reset**
> 重置所有 funnel 配置。

# DESCRIPTION

**tailscale funnel** 通过你的 Tailscale 节点将本地服务暴露到公共互联网。与只能在 tailnet 内部访问服务的 **tailscale serve** 不同，Funnel 会创建一个互联网上任何人都能访问的公开 HTTPS 端点。

Tailscale 会自动为端点申请和管理 TLS 证书，因此无需手动配置证书即可实现流量加密。服务可以通过 **--set-path** 映射到特定的 URL 路径，从而让多个本地服务以不同的路由对外提供。**off** 子命令禁用 funnel，**status** 则显示当前的配置。

# CAVEATS

会将服务暴露到公共互联网——请谨慎使用。必须先在 Tailscale 管理控制台的 ACL 策略中启用 Funnel。面向公众的端点只支持 443、8443 和 10000 端口。

# INSTALL

```dnf: sudo dnf install tailscale```

```pacman: sudo pacman -S tailscale```

```apk: sudo apk add tailscale```

```zypper: sudo zypper install tailscale```

```brew: brew install tailscale```

```nix: nix profile install nixpkgs#tailscale```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tailscale](/man/tailscale)(1), [tailscale-up](/man/tailscale-up)(1), [ngrok](/man/ngrok)(1)
