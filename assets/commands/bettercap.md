# TAGLINE

网络攻击与监控框架

# TLDR

**启动**交互会话

```bettercap -iface [eth0]```

**运行** caplet 脚本

```bettercap -caplet [script.cap]```

**ARP 欺骗**

```bettercap -iface [eth0] -eval ["set arp.spoof.targets 192.168.1.10; arp.spoof on"]```

**启动** web UI

```bettercap -caplet http-ui```

# SYNOPSIS

**bettercap** [_options_]

# DESCRIPTION

**bettercap** 是一款面向 WiFi、蓝牙低功耗（BLE）、无线 HID 劫持、CAN 总线以及 IPv4/IPv6 网络侦察和中间人（MITM）攻击的瑞士军刀。它使用 Go 编写，通过模块化架构提供中间人攻击、网络侦察、数据包嗅探、凭据收集，以及 REST API 和 web UI。

该工具面向安全研究、渗透测试和网络分析而设计，必须以 root 身份运行。

# PARAMETERS

**-iface** _name_
> 要绑定的网络接口；为空时自动选择默认接口

**-caplet** _file_
> 从该文件读取命令并在交互会话中运行

**-eval** _code_
> 在交互会话中运行一条或多条命令（以 ; 分隔）

**-autostart** _modules_
> 要自动启动的模块列表，以逗号分隔

**-script** _file_
> 加载会话脚本

**-gateway-override** _ip_
> 使用给定的 IP 地址而不是检测到的默认网关

**-env-file** _file_
> 从该文件加载环境变量

**-caplets-path** _dir_
> caplet 的备用基础路径

**-no-history**
> 禁用交互会话历史文件

**-no-colors**
> 禁用输出色彩效果

**-debug**
> 打印调试消息

**-silent**
> 抑制所有非错误日志

**-version**
> 打印版本并退出

# MODULES

**net.recon**
> 网络侦察

**net.probe**
> 主动主机发现

**arp.spoof**
> ARP 欺骗攻击

**dns.spoof**
> DNS 欺骗

**http.proxy**
> HTTP 透明代理

**https.proxy**
> HTTPS 透明代理

**wifi**
> WiFi 攻击与监控

**ble**
> 蓝牙低功耗（BLE）攻击

**packet.proxy**
> 原始数据包操作

# INTERACTIVE COMMANDS

```
# Enable ARP spoofing
> set arp.spoof.targets 192.168.1.0/24
> arp.spoof on

# HTTP proxy with SSL stripping
> set http.proxy.sslstrip true
> http.proxy on

# Network scan
> net.probe on
> net.show
```

# CAPLETS

用于自动化任务的脚本：
```
# quick-recon.cap
net.probe on
sleep 10
net.show
```

# CAVEATS

需要 root 权限。未经授权使用即属违法。可能干扰网络流量。可能被 IDS/IPS 系统检测到。WiFi 攻击需要支持监听模式的适配器。仅限在获授权的安全评估中使用。

# HISTORY

**bettercap** 由 Simone Margaritelli（evilsocket）于 **2016 年**创建，作为 ettercap 的现代替代品，为获得更好性能而用 Go 重写。

# INSTALL

```apt: sudo apt install bettercap```

```pacman: sudo pacman -S bettercap```

```zypper: sudo zypper install bettercap```

```brew: brew install bettercap```

```nix: nix profile install nixpkgs#bettercap```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ettercap](/man/ettercap)(8), [arpspoof](/man/arpspoof)(8), [nmap](/man/nmap)(1), [aircrack-ng](/man/aircrack-ng)(1), [wireshark](/man/wireshark)(1)

# RESOURCES

```[Source code](https://github.com/bettercap/bettercap)```

```[Homepage](https://www.bettercap.org/)```

<!-- verified: 2026-06-19 -->
