# TAGLINE

结合 traceroute 和 ping 的网络诊断工具

# TLDR

跟踪到主机的路由

```trip [example.com]```

使用 TCP 协议跟踪

```trip [example.com] -p tcp```

在特定端口使用 UDP 协议

```trip [example.com] -p udp --target-port [53]```

设置最大跳数 (TTL)

```trip [example.com] --max-ttl [30]```

同时跟踪多个目标

```trip [example.com] [example.org]```

# SYNOPSIS

**trip** [_options_] _target_ [_target_ ...]

# PARAMETERS

**-p**, **--protocol** _PROTOCOL_
> 跟踪协议：icmp（默认）、udp 或 tcp。

**--target-port** _PORT_
> UDP/TCP 跟踪的目标端口。

**--source-port** _PORT_
> UDP/TCP 跟踪的源端口。

**-i**, **--interface** _IFACE_
> 要使用的网络接口。

**--max-ttl** _N_
> 最大跳数。

**--first-ttl** _N_
> 起始 TTL 值。

**-a**, **--addr-family** _FAMILY_
> 地址族：ipv4、ipv6、ipv4-then-ipv6 或 ipv6-then-ipv4。

**-r**, **--dns-resolve-method** _METHOD_
> DNS 解析方式：system、resolv、google 或 cloudflare。

**--tui-preserve-screen**
> 退出时保留屏幕内容。

# DESCRIPTION

**trippy** 将 traceroute 与 ping 的功能合二为一，并提供实时 TUI 界面用于网络路径分析。它支持多种跟踪协议（ICMP、UDP、TCP）、IPv6、GeoIP 可视化和高级 ECMP 策略。可运行于 Linux、BSD、macOS 和 Windows。

# CAVEATS

ICMP 跟踪需要提升的权限（root 或 CAP_NET_RAW 能力）。某些防火墙可能拦截探测包。

# HISTORY

**trippy** 由 **fujiapple852** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S trippy```

```zypper: sudo zypper install trippy```

```brew: brew install trippy```

```nix: nix profile install nixpkgs#trippy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mtr](/man/mtr)(1), [traceroute](/man/traceroute)(1), [tracepath](/man/tracepath)(1), [ping](/man/ping)(1)
