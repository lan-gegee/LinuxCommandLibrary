# TAGLINE

扫描网络并将 IP 映射到 mDNS 主机名的 TUI

# TLDR

**扫描本地网络**

```mdns-scanner```

# SYNOPSIS

**mdns-scanner** [_options_]

# DESCRIPTION

**mdns-scanner** 是一个终端 UI 应用，它扫描本地网络中的活动主机，并将其 IP 地址解析为 **组播 DNS** (mDNS) 主机名或 DNS-SD 服务实例。它枚举非环回网络接口，执行基于 ARP/ICMP 的主机发现，然后在 UDP 端口 **5353** 上向 **224.0.0.251** (IPv4) 和 **ff02::fb** (IPv6) 链路本地组播组发送 mDNS 查询。

TUI 以可导航列表的形式显示发现的主机及其 IP 地址和任何已解析的 **\*.local** 主机名或服务记录，非常适合在局域网中查找打印机、Chromecast、Apple 设备、HomeKit 配件以及其他支持 Bonjour/Avahi 的硬件。

# CAVEATS

只能发现响应 mDNS 查询的设备。没有 mDNS 应答程序（或 mDNS 被防火墙规则阻止）的设备无法被解析，不过它们可能仍会以 IP 形式出现。组播流量默认不会跨越路由网段，因此该工具只能看到直接相连的广播域。

# HISTORY

**mdns-scanner** 由 **CramBL** 创建，用 **Rust** 编写。它发布于 **crates.io**，通过 **cargo install mdns-scanner** 分发。

# INSTALL

```nix: nix profile install nixpkgs#mdns-scanner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[avahi-browse](/man/avahi-browse)(1), [nmap](/man/nmap)(1), [arp-scan](/man/arp-scan)(1)
