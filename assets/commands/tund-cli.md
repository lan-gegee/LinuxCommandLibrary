# TAGLINE

基于 UDP 的虚拟局域网集线器与客户端

# TLDR

**生成**共享网络密钥

```openssl rand -base64 24 > tund.key```

**启动** TunD 服务器（集线器）

```sudo tund-cli server --key-file tund.key```

将客户端**连接**到服务器

```sudo tund-cli client -s [server_ip] --key-stdin```

使用显示名称和密钥文件**连接**

```sudo tund-cli client -s [server_ip] -n [name] --key-file tund.key```

**在不带终端 UI 的情况下运行服务器**

```sudo tund-cli server --key-file tund.key --no-tui```

连接后 **ping** 集线器的虚拟地址

```ping 10.9.0.1```

# SYNOPSIS

**tund-cli** **server**|_client_ [_options_]

# DESCRIPTION

**tund-cli** 是轻量级自托管虚拟局域网工具 **TunD** 的命令行核心。一台主机以 **server** 模式作为 UDP 集线器运行；其他机器以 **client** 模式运行，并在固定的虚拟子网 **10.9.0.0/24**（集线器为 **10.9.0.1**）中自动获得地址。流量通过服务器经 UDP 隧道转发，使各节点如同处于同一个 IPv4 局域网中——适用于局域网联机游戏派对、物理局域网不可靠的场景以及需要直连 IP 的游戏。

C 语言核心会创建 TUN 设备、配置路由，并对每个端点与服务器之间传输的数据报进行加密（共享密钥加密；服务器解密以便路由）。客户端只需向可达的集线器发送出站 UDP 流量（默认端口 **9909**）。可选的终端 UI 可显示各个节点，**--no-tui** 可将其禁用。另有独立的 Flutter 桌面 GUI 可以启动同一个二进制文件。

TunD 比 WireGuard、Tailscale 或 ZeroTier 更窄：它提供固定的虚拟 IPv4 子网、节点分配以及对兼容游戏的广播支持——并非通用的安全覆盖 VPN。

# PARAMETERS

**server**
> 作为虚拟局域网集线器运行。需要通过 **--key-file**、**--key-stdin** 或 **-k**/**--key** 提供共享密钥。

**client**
> 加入一个集线器。需要 **-s**/**--server** _host_ 以及与服务器相同的共享密钥。

**-s**, **--server** _ip_
> 服务器的 IP 或主机名（仅限 **client**）。

**-p**, **--port** _port_
> UDP 端口（默认 **9909**）。

**-n**, **--name** _name_
> 客户端显示名称（默认：主机名）。

**-k**, **--key** _key_
> 在命令行上提供共享网络密钥（会在进程列表中可见；建议改用文件或 stdin）。

**--key-file** _path_
> 从文件读取共享密钥。

**--key-stdin**
> 从 stdin 首行或交互提示读取密钥。

**-t**, **--no-tui**
> 禁用实时节点面板 TUI。

**-v**, **--verbose**
> 调试日志。

**--json-events**
> 在标准输出上输出机器可读的节点事件（**server** 模式）。

# CAVEATS

TUN 设置需要 root 或管理员权限。请使用足够长的随机共享密钥；流量加密到集线器为止，对服务器运营者而言**并非**端到端加密。它不是以太网网桥：不支持二层发现、IPv6 或组播发现——需要这些功能的游戏可能需要手动指定主机 IP，或者无法工作。如果 **10.9.0.0/24** 已在其他地方路由，请避免使用。对于一般的机密通信需求，建议选择 WireGuard/Tailscale/ZeroTier。

# SEE ALSO

[wireguard](/man/wireguard)(8), [tailscale](/man/tailscale)(1), [zerotier-cli](/man/zerotier-cli)(1), [ip](/man/ip)(8), [ping](/man/ping)(8)

# RESOURCES

```[Source code](https://github.com/danterolle/tund)```

```[Homepage](https://danterolle.github.io/tund/)```

```[Documentation](https://github.com/danterolle/tund/blob/main/docs/USAGE.md)```

<!-- verified: 2026-07-22 -->
