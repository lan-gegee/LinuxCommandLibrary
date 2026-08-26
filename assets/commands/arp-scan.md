# TAGLINE

通过 ARP 请求发现本地网络中的主机。

# TLDR

**扫描**本地网络

```sudo arp-scan -l```

扫描**指定子网**

```sudo arp-scan [192.168.1.0/24]```

使用**指定接口**扫描

```sudo arp-scan -I [eth0] -l```

扫描指定的 **IP 范围**

```sudo arp-scan [192.168.1.1-192.168.1.50]```

**安静**输出（仅显示响应的主机）

```sudo arp-scan -l -q```

使用**自定义源** MAC 地址扫描

```sudo arp-scan -l --srcaddr=[00:11:22:33:44:55]```

# SYNOPSIS

**arp-scan** [_-l_] [_-I interface_] [_options_] [_targets_]

# DESCRIPTION

**arp-scan** 通过发送 ARP 请求来发现本地网络中的主机。它比基于 ping 的扫描更快，因为 ARP 工作在第 2 层，主机难以对其隐藏。

该工具会显示 IP 地址、MAC 地址，以及可选的来自 IEEE OUI 数据库的厂商名称。

# PARAMETERS

**-l**, **--localnet**
> 扫描本地网络上的所有地址

**-I** _interface_
> 要使用的网络接口

**-q**, **--quiet**
> 安静模式（仅显示响应的主机）

**-r** _n_, **--retry**=_n_
> 每台主机的重试次数（默认 2）。

**-t** _ms_, **--timeout**=_ms_
> 每台主机的超时时间，单位毫秒（默认 500）。

**-B**, **--bandwidth**=_bps_
> 限制出站带宽（例如 256000）。

**-x**, **--ignoredups**
> 忽略重复的 ARP 响应。

**--srcaddr**=_mac_
> 设置发出数据包中的源 MAC 地址。

**-D**, **--destaddr**=_mac_
> 设置目标 MAC 地址（默认 ff:ff:ff:ff:ff:ff）。

# CONFIGURATION

**/etc/arp-scan/mac-vendor.txt**
> 用于 OUI 解析的 MAC 地址到厂商名称映射数据库。

# CAVEATS

需要 root/sudo 权限以访问原始套接字。只能在本网段内工作（无法跨路由器扫描）。部分主机可能会对 ARP 响应进行速率限制。

# HISTORY

**arp-scan** 由 Roy Hills 编写，自 **2000** 年代初以来一直作为可靠的网络发现工具维护至今。

# INSTALL

```apt: sudo apt install arp-scan```

```dnf: sudo dnf install arp-scan```

```pacman: sudo pacman -S arp-scan```

```apk: sudo apk add arp-scan```

```zypper: sudo zypper install arp-scan```

```brew: brew install arp-scan```

```nix: nix profile install nixpkgs#arp-scan```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arp](/man/arp)(8), [arping](/man/arping)(8), [nmap](/man/nmap)(1)
