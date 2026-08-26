# TAGLINE

暴力破解 WPS PIN 以恢复 WPA/WPA2 密码短语

# TLDR

对接入点**暴力破解**其 WPS PIN

```bully -b [mac] -c [channel] [interface]```

显示**帮助**

```bully -h```

# SYNOPSIS

**bully** [_options_] _interface_

# DESCRIPTION

**bully** 是一个 WPS（Wi-Fi Protected Setup）暴力破解攻击工具，利用 WPS 协议中的漏洞恢复 WPA/WPA2 密码短语。它通过系统性猜测来破解 8 位数字的 WPS PIN。

使用 bully 之前，需要先用 **airmon-ng** 和 **airodump-ng** 等工具收集网络信息，以确定目标的 MAC 地址和信道。

# PARAMETERS

**-b, --bssid** _mac_
> 目标接入点的 MAC 地址

**-c, --channel** _channel_
> 目标无线信道

**-B, --bruteforce**
> 启用暴力破解模式

**-h, --help**
> 显示帮助信息

# CAVEATS

只能在你拥有所有权或获得明确授权的网络测试中使用。WPS 攻击可被检测到，并可能触发路由器锁定。许多现代路由器带有 WPS 防护机制，会限制攻击效果。未经授权的使用属于违法行为。

# INSTALL

```apt: sudo apt install bully```

```pacman: sudo pacman -S bully```

```nix: nix profile install nixpkgs#bully```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[reaver](/man/reaver)(1), [airmon-ng](/man/airmon-ng)(8), [airodump-ng](/man/airodump-ng)(8)
