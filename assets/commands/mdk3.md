# TAGLINE

无线安全测试工具

# TLDR

**Beacon 洪泛攻击**

```mdk3 [wlan0] b```

**认证 DoS**

```mdk3 [wlan0] a -a [BSSID]```

**去认证攻击**

```mdk3 [wlan0] d```

**Michael 关闭攻击**

```mdk3 [wlan0] m -t [BSSID]```

**探测请求洪泛**

```mdk3 [wlan0] p```

# SYNOPSIS

**mdk3** _interface_ _mode_ [_options_]

# PARAMETERS

_INTERFACE_
> 处于监视模式的无线接口。

_MODE_
> 攻击模式（b、a、d、m、p）。

**b**
> Beacon 洪泛。

**a**
> 认证洪泛。

**d**
> 去认证。

**-t** _BSSID_
> 目标 BSSID。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mdk3** 是一个无线安全测试工具。它测试 802.11 网络的抗攻击能力。

该工具执行各种攻击模拟用于安全审计。需要获得授权。

# CAVEATS

安全工具。仅在获得授权的情况下合法使用。需要监视模式。

# HISTORY

mdk3 为 **802.11 网络**的无线安全测试与渗透测试而创建。

# INSTALL

```apt: sudo apt install mdk3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdk4](/man/mdk4)(1), [aircrack-ng](/man/aircrack-ng)(1), [aireplay-ng](/man/aireplay-ng)(1)
