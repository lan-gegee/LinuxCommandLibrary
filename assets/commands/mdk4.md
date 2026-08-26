# TAGLINE

无线安全测试工具

# TLDR

**Beacon 洪泛攻击**

```mdk4 [wlan0] b```

**认证 DoS**

```mdk4 [wlan0] a -a [BSSID]```

**去认证攻击**

```mdk4 [wlan0] d```

**WDS 混淆攻击**

```mdk4 [wlan0] w```

**模糊测试**

```mdk4 [wlan0] f -t [BSSID]```

# SYNOPSIS

**mdk4** _interface_ _mode_ [_options_]

# PARAMETERS

_INTERFACE_
> 处于监视模式的无线接口。

_MODE_
> 攻击模式（b、a、d、w、f）。

**b**
> Beacon 洪泛 —— 广播伪造的 AP beacon。

**a**
> 认证 DoS —— 用认证帧淹没目标 AP。

**p**
> SSID 探测/暴力破解（包括隐藏 SSID）。

**d**
> 将客户端与 AP 去认证并解除关联。

**m**
> Michael（TKIP 对策）漏洞利用。

**e**
> EAPOL start 和 logoff 数据包注入。

**s**
> 针对 mesh 网络链路和路由的攻击。

**w**
> 通过伪造客户端混淆无线 IDS/IPS。

**f**
> 可配置来源和修改器的数据包模糊测试器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mdk4** 是一个无线安全测试工具。它是 mdk3 的后继者，具有更多功能。

该工具测试 802.11 网络安全性并进行漏洞评估。

# CAVEATS

安全工具。仅在合法情况下使用。需要监视模式。仅限授权测试。

# HISTORY

mdk4 是 **mdk3** 的后继者，提供了更新的无线安全测试能力。

# INSTALL

```apt: sudo apt install mdk4```

```pacman: sudo pacman -S mdk4```

```nix: nix profile install nixpkgs#mdk4```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdk3](/man/mdk3)(1), [aircrack-ng](/man/aircrack-ng)(1), [wifite](/man/wifite)(1)
