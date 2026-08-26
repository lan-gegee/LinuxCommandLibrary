# TAGLINE

802.11 WiFi 攻击与渗透测试工具

# TLDR

在无线接口上**开始扫描**

```sudo angryoxide -i [wlan0]```

**扫描特定信道**

```sudo angryoxide -i [wlan0] -c [1,6,11]```

**针对特定网络**

```sudo angryoxide -i [wlan0] -t [AA:BB:CC:DD:EE:FF]```

**以被动模式运行**，不发送攻击帧

```sudo angryoxide -i [wlan0] --notransmit```

配合自动猎取**扫描整个频段**

```sudo angryoxide -i [wlan0] -b [5] --autohunt```

**无界面运行**并自定义输出

```sudo angryoxide -i [wlan0] --headless -o [output_prefix]```

# SYNOPSIS

**sudo angryoxide** **-i** _interface_ [_options_]

# PARAMETERS

**-i**, **--interface** _interface_
> 要使用的无线接口（必需）

**-c**, **--channel** _channels_
> 要扫描的特定信道（默认：1,6,11）

**-b**, **--band** _band_
> 扫描整个频段（2、5、6 或 60）

**-t** _target_
> 针对特定 MAC 或 SSID（可重复使用）

**-w** _target_
> 将某个 MAC 或 SSID 列入白名单以免受攻击（可重复使用）

**--targetlist** _file_
> 从文件加载目标列表

**--whitelist** _file_
> 从文件加载白名单

**-o**, **--output** _prefix_
> 自定义输出文件名前缀

**-r**, **--rate** _level_
> 攻击强度：1（低）、2（默认）、3（高）

**--notransmit**
> 仅被动收集，不发送攻击帧

**--autohunt**
> 自动发现目标信道，然后聚焦于这些信道

**--headless**
> 无终端 UI 运行

**--autoexit**
> 当所有目标都有有效 hashline 时退出

**--combine**
> 将所有 .hc22000 文件合并为单个输出

**--gpsd** _ip:port_
> 连接 GPS 守护进程以进行 wardriving

**-h**, **--help**
> 显示帮助

# DESCRIPTION

**angryoxide** 是一款用 Rust 编写的 802.11 WiFi 攻击工具，能够自主收集 WPA/WPA2/WPA3 哈希素材（EAPOL 握手和 PMKID），供 Hashcat 离线破解使用。它具有基于 Ratatui 构建的实时 TUI，可以显示发现的网络、捕获的握手和攻击状态。

攻击引擎支持 PMKID 收集、隐藏 SSID 获取、匿名重关联（绕过 MFP）、信道切换通告攻击、RSN 降级以及 WiFi 6e 解除关联。输出文件包括与 Hashcat 兼容的 .hc22000 hashline、.pcapng 抓包文件和 Kismet 兼容的 .kismetdb 数据库。

# CAVEATS

需要 root/sudo 权限以及支持监听模式和包注入的无线适配器。严格用于授权的安全测试和研究。速率受限的传输方式可以降低但无法完全避免被无线 IDS 检测到。

# HISTORY

**angryoxide** 由 **Ragnt**（rage）创建，其灵感来自 hcxdumptool。项目使用 Rust 编写，采用 GPL-3.0 许可证，正处于高强度活跃开发中。

# INSTALL

```aur: yay -S angryoxide```

```nix: nix profile install nixpkgs#angryoxide```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [hashcat](/man/hashcat)(1), [tcpdump](/man/tcpdump)(1), [iwconfig](/man/iwconfig)(8)
