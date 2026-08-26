# TAGLINE

Cloudflare WARP VPN 客户端命令行工具

# TLDR

**连接**

```warp-cli connect```

**断开连接**

```warp-cli disconnect```

**检查状态**

```warp-cli status```

**注册**

```warp-cli register```

**设置模式**

```warp-cli set-mode warp```

**显示设置**

```warp-cli settings```

# SYNOPSIS

**warp-cli** _command_ [_options_]

# PARAMETERS

**connect**
> 连接到 WARP。

**disconnect**
> 断开连接。

**status**
> 显示状态。

**register**
> 注册设备。

**set-mode** _MODE_
> 设置连接模式。

**settings**
> 显示设置。

# DESCRIPTION

**warp-cli** 是用于管理 Cloudflare WARP 的命令行界面。WARP 是一项 VPN 和安全 DNS 服务，对设备与 Cloudflare 网络之间的流量进行加密。它提供连接、断开、检查状态和配置 WARP 客户端的命令。

客户端支持多种连接模式，包括将所有流量路由经过 Cloudflare 网络的完整 WARP VPN 模式，以及只加密 DNS 查询以进行私密域名解析的 DNS-over-HTTPS 模式。WARP+ 付费档位通过 Cloudflare 的 Argo 网络优化路由，以获得更好的性能。

首次使用前需要注册设备，且必须运行 warp-svc 守护进程 CLI 才能工作。该工具可在 Linux、macOS 和 Windows 上使用。

# CAVEATS

Cloudflare 服务。需要注册。守护进程必须运行。

# HISTORY

**warp-cli** 是 **Cloudflare WARP**（Cloudflare 出品的 VPN 和 DNS 服务）的命令行工具。

# INSTALL

```apt: sudo apt install libghc-wai-app-static-dev```

```pacman: sudo pacman -S warp```

```apk: sudo apk add warp```

```zypper: sudo zypper install warp```

```nix: nix profile install nixpkgs#warp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cloudflared](/man/cloudflared)(1)
