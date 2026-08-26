# TAGLINE

带 TUI 的可视化网络路由跟踪工具

# TLDR

跟踪路由

```trip [example.com]```

使用 ICMP

```trip -p icmp [example.com]```

使用 UDP

```trip -p udp [example.com]```

使用 TCP

```trip -p tcp [example.com]```

启用 DNS 解析

```trip -r [example.com]```

图表视图

```trip --tui-chart [example.com]```

# SYNOPSIS

**trip** [_-p protocol_] [_-r_] [_options_] _target_

# PARAMETERS

**-p** _PROTOCOL_
> 协议 (icmp, udp, tcp)。

**-r**
> 反向 DNS 解析。

**--tui-chart**
> 图表显示。

**-m** _HOPS_
> 最大跳数。

**-i** _INTERVAL_
> 探测间隔。

# DESCRIPTION

**trip** 是一款现代网络诊断工具，将 traceroute 功能与文本用户界面相结合以实现实时可视化。它持续追踪到目标主机的网络路径，并在交互式终端界面中逐跳显示延迟统计信息。

该工具支持多种协议，包括 ICMP、UDP 和 TCP，可以穿越不同的网络路径和防火墙配置进行探测。图表视图提供延迟随时间变化的可视化，便于发现间歇性连接问题和抖动模式。

可以启用反向 DNS 解析以显示每一跳的主机名。持续追踪模式会不断运行并更新统计数据，适合长期网络监控和故障排查。

# CAVEATS

访问原始套接字（ICMP/UDP 探测）需要 root 权限或相应的能力。TCP 探测在有状态防火墙后的表现可能不同。某些跳点可能不响应探测，在输出中显示为 `*`。

# HISTORY

**trip** 作为一款带文本用户界面的现代 traceroute 网络诊断工具而创建。

# INSTALL

```apt: sudo apt install trippy```

```pacman: sudo pacman -S trippy```

```zypper: sudo zypper install trippy```

```brew: brew install trippy```

```nix: nix profile install nixpkgs#trippy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[traceroute](/man/traceroute)(1), [mtr](/man/mtr)(1), [ping](/man/ping)(1)
