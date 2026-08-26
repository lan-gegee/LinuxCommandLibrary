# TAGLINE

启用和管理无线监听模式

# TLDR

**列出**无线接口

```sudo airmon-ng```

**启用**监听模式

```sudo airmon-ng start [wlan0]```

在**指定信道**上启用

```sudo airmon-ng start [wlan0] [6]```

**禁用**监听模式

```sudo airmon-ng stop [wlan0mon]```

**终止**干扰进程

```sudo airmon-ng check kill```

# SYNOPSIS

**airmon-ng** [_start_|_stop_|_check_] [_interface_] [_channel_]

# DESCRIPTION

**airmon-ng** 管理无线接口以进入监听模式。监听模式允许捕获范围内所有的无线数据包，而不仅仅是发往你设备的数据包，这是无线安全审计所必需的。

该工具可以识别并终止可能干扰监听模式运行的进程，例如 NetworkManager 和 wpa_supplicant。

# PARAMETERS

**start** _interface_
> 在接口上启用监听模式

**stop** _interface_
> 禁用监听模式

**check**
> 列出可能造成干扰的进程

**check kill**
> 终止干扰进程

**channel**
> 将接口锁定到特定信道

# OUTPUT

不带参数时，**airmon-ng** 会为每个检测到的无线设备列出 PHY 名称、接口名称、正在使用的驱动程序和芯片组。

# CAVEATS

启用监听模式会断开所有已连接的网络。有些驱动不支持监听模式。终止干扰进程可能导致正常 WiFi 连接受影响，直到这些进程重新启动。

# HISTORY

**airmon-ng** 是 aircrack-ng 套件的一部分，由早期的 airmon 脚本演化而来。"-ng" 版本于 **2006** 年发布，改进了驱动支持和进程管理。

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

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [aireplay-ng](/man/aireplay-ng)(1), [iw](/man/iw)(8), [iwconfig](/man/iwconfig)(8)

# RESOURCES

```[Source code](https://github.com/aircrack-ng/aircrack-ng)```

```[Homepage](https://www.aircrack-ng.org/)```

```[Documentation](https://www.aircrack-ng.org/documentation.html)```

<!-- verified: 2026-06-11 -->
