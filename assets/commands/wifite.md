# TAGLINE

自动化无线网络安全审计

# TLDR

以交互模式**启动 wifite**

```sudo wifite```

**只针对 WPA 网络**

```sudo wifite --wpa```

**只针对启用 WPS 的网络**

```sudo wifite --wps```

**指定无线网卡接口**

```sudo wifite -i [wlan0]```

**攻击信号强度不低于阈值的网络**

```sudo wifite --power [50]```

按 ESSID **指定目标网络**

```sudo wifite --essid "[NetworkName]"```

破解时**使用指定的字典文件**

```sudo wifite --dict [/path/to/wordlist.txt]```

**扫描 5GHz 信道**

```sudo wifite --5ghz```

# SYNOPSIS

**wifite** [_options_]

# PARAMETERS

**-i** _INTERFACE_
> 要使用的无线网卡接口

**-c** _CHANNEL_
> 要扫描的信道（如 1,3-6）

**-5**, **--5ghz**
> 包含 5GHz 信道

**-p** _POWER_, **--power** _POWER_
> 最小信号强度（dBm）

**--essid** _NAME_
> 按名称指定目标网络

**--bssid** _MAC_
> 按 MAC 地址指定目标网络

**--wpa**
> 只针对 WPA 加密的网络

**--wps**
> 只针对启用 WPS 的网络

**--wep**
> 只针对 WEP 加密的网络

**--dict** _FILE_
> 用于密码破解的字典文件

**--pmkid**
> 使用 PMKID 捕获攻击

**--new-hs**
> 捕获新的握手包，忽略已有的

**--pixie**
> 对 WPS 使用 Pixie Dust 攻击

**--bully**
> 使用 Bully 进行 WPS 攻击

**--reaver**
> 使用 Reaver 进行 WPS 攻击

**--clients-only**
> 仅显示有客户端的网络

**--nodeauths**
> 被动模式；不进行去认证攻击

**--daemon**
> 退出时将网卡恢复为管理模式

**--infinite**
> 启用无限攻击模式

**-v**, **--verbose**
> 显示更多输出和命令

**-h**, **--help**
> 显示帮助

# DESCRIPTION

**wifite** 是一款自动化无线网络审计工具，简化了 Wi-Fi 安全测试。它自动完成网络扫描、握手包捕获，并尝试使用多种攻击方法破解密码。

该工具支持多种攻击向量：WPA 握手捕获配合字典攻击、WPS PIN 暴力破解、针对存在漏洞的 WPS 实现的 Pixie Dust 攻击，以及传统的 WEP 攻击。它与 Aircrack-ng、Reaver、Bully 和 Hashcat 等工具集成。

Wifite 负责将无线网卡置于监听模式、扫描目标，并依次尝试攻击。结果通过交互式界面展示，显示网络详情和攻击进度。

# CAVEATS

需要支持监听模式和包注入的无线网卡。需要 root 权限。只应测试你拥有或有明确授权审计的网络——未经授权的访问是违法的。某些攻击（去认证）会影响合法的网络用户。成功率取决于网络配置和密码复杂度。

# HISTORY

Wifite 最初由 **derv82** 创建，旨在自动完成以前需要手动使用多个工具的常见 Wi-Fi 审计任务。完全重写的 Wifite2 增加了 Python 3 支持、改进了攻击方法，并更好地应对现代无线安全机制。该工具因渗透测试而在安全社区广受欢迎，并默认包含在 Kali Linux 中。

# INSTALL

```pacman: sudo pacman -S wifite```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [reaver](/man/reaver)(1), [bully](/man/bully)(1), [kismet](/man/kismet)(1)
