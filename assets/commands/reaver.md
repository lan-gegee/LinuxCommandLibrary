# TAGLINE

针对 WiFi 网络的 WPS 暴力破解工具

# TLDR

使用 wash **扫描启用了 WPS 的接入点**

```wash -i [wlan0mon]```

**发起 WPS 暴力破解攻击**

```reaver -i [wlan0mon] -b [AA:BB:CC:DD:EE:FF] -c [channel] -vv```

**使用 Pixie Dust 攻击**（离线攻击）

```reaver -i [wlan0mon] -b [AA:BB:CC:DD:EE:FF] -c [channel] -K -vv```

**恢复之前的会话**

```reaver -i [wlan0mon] -b [AA:BB:CC:DD:EE:FF] -s [session_file]```

**以自定义间隔**发起攻击

```reaver -i [wlan0mon] -b [AA:BB:CC:DD:EE:FF] -d [5] -vv```

# SYNOPSIS

**reaver** **-i** _interface_ **-b** _bssid_ [**-c** _channel_] [**-K**] [**-vv**] [_options_]

# PARAMETERS

**-i** _interface_
> 处于监听模式的无线接口

**-b** _bssid_
> 目标接入点的 MAC 地址

**-c** _channel_
> 目标接入点所在的信道

**-K**
> 执行 Pixie Dust 离线攻击

**-vv**
> 详细输出（多个 v 表示更详细）

**-d** _seconds_
> 两次 PIN 尝试之间的延迟（默认：1）

**-l** _seconds_
> 检测到 WPS 锁定后的等待时间（默认：60）

**-s** _file_
> 将会话保存到文件或从中恢复

**-p** _pin_
> 使用指定的 4 位或 8 位 WPS PIN 码

**-N**
> 出错时不发送 NACK 数据包

**-T** _seconds_
> M5/M7 超时时间（默认：0.20）

**-t** _seconds_
> 接收超时时间（默认：5）

# DESCRIPTION

**reaver** 对 Wi-Fi Protected Setup（WPS）执行暴力破解攻击，以恢复 WPA/WPA2 密码短语。WPS 使用 8 位 PIN 码，该 PIN 可分两半进行攻击，将最大尝试次数降低到约 11,000 种组合。

这种攻击利用了 WPS 的一个设计缺陷：接入点分两个阶段校验 PIN，攻击者可以在尝试后半部分之前判断前半部分是否正确。

**Pixie Dust** 攻击（**-K**）是一种离线攻击，利用某些芯片组（Ralink、Broadcom、Realtek）中薄弱的随机数生成机制，可能在数秒内恢复 PIN 而无需暴力破解。

配套工具 **wash** 用于扫描启用了 WPS 的接入点并识别潜在目标，包括易受 Pixie Dust 攻击的目标。

# CAVEATS

**需要授权**：只能对你拥有或获得明确书面许可测试的网络使用。未经授权的访问属于违法行为。

运行 reaver 之前接口必须处于监听模式。可使用 **airmon-ng start wlan0** 启用监听模式。

许多现代接入点会在多次失败尝试后实施 WPS 锁定，从而显著拖慢攻击速度。有些可能会永久锁定或完全禁用 WPS。

速率限制和锁定检测（**-l** 选项）对于避免永久锁定至关重要。某些接入点可能需要重启设备才能清除 WPS 锁定。

# HISTORY

安全研究员 **Stefan Viehböck** 于 **2011 年** 12 月发表论文 "Brute forcing Wi-Fi Protected Setup"，揭示了 WPS 设计中的根本性缺陷，Reaver 随之开发。该工具迅速成为无线安全测试工具包的标准组件。Pixie Dust 攻击是后来加入的，用于利用特定芯片组的实现缺陷。

# INSTALL

```apt: sudo apt install reaver```

```dnf: sudo dnf install reaver```

```pacman: sudo pacman -S reaver```

```brew: brew install reaver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [wash](/man/wash)(1), [airmon-ng](/man/airmon-ng)(8), [wifite](/man/wifite)(1)
