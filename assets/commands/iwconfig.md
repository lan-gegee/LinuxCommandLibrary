# TAGLINE

配置和显示无线网络接口参数

# TLDR

**显示所有无线接口及其设置**

```iwconfig```

**显示指定的无线接口**

```iwconfig [wlan0]```

**设置网络名称（ESSID）**

```iwconfig [wlan0] essid [network_name]```

**设置工作模式**

```iwconfig [wlan0] mode [Managed]```

**设置信道**

```iwconfig [wlan0] channel [6]```

**以 dBm 为单位设置发射功率**

```iwconfig [wlan0] txpower [20]```

**设置比特率**

```iwconfig [wlan0] rate [54M]```

**在接口上启用监听模式**

```iwconfig [wlan0] mode Monitor```

# SYNOPSIS

**iwconfig** [_interface_] [_parameter_ _value_...]

# PARAMETERS

**essid** _name_
> 设置网络名称（SSID）。使用 **essid off** 或 **essid any** 可禁用 ESSID 检查。

**mode** _mode_
> 设置工作模式：Ad-Hoc、Managed、Master、Repeater、Secondary、Monitor 或 Auto。

**freq** _frequency_
> 设置工作频率（如 2.46G 表示 2.46 GHz）。可加 k、M 或 G 后缀。

**channel** _channel_
> 设置工作信道编号。使用 **iwlist** 可查看可用信道。

**ap** _address_
> 按 MAC 地址强制关联到指定接入点。使用 **ap off** 重新启用自动选择。

**rate** _rate_
> 设置比特率（如 11M、54M）。使用 **rate auto** 进行自动选择。

**txpower** _power_
> 以 dBm 为单位设置发射功率，也可加 mW 后缀表示毫瓦。使用 **txpower off** 关闭射频。

**sens** _threshold_
> 设置用于漫游决策的灵敏度阈值。

**retry** _limit_
> 设置 MAC 重传的最大重试次数。

**rts** _threshold_
> 以字节为单位设置 RTS/CTS 握手阈值。使用 **rts off** 禁用。

**frag** _threshold_
> 以字节为单位设置最大分片大小。使用 **frag off** 禁用。

**power** _mode_
> 设置电源管理模式。使用 **power off** 禁用电源管理。

**key** _key_
> 设置 WEP 加密密钥（已废弃且不安全）。

# DESCRIPTION

**iwconfig** 与 **ifconfig** 类似，但专门用于无线网络接口。它用来设置无线操作特有的参数，例如 ESSID、频率、模式、加密密钥和电源管理。它还可以显示这些参数以及来自 /proc/net/wireless 的无线统计信息。

不带参数调用时，iwconfig 显示所有接口的无线参数。只带接口名调用时，则显示该接口的设置。

# CAVEATS

**iwconfig** 已被废弃，建议改用 **iw**。通过 **key** 配置的 WEP 加密并不安全，不应使用。对于 WPA/WPA2/WPA3，请改用 **wpa_supplicant**。只有超级用户才能更改无线参数。

# HISTORY

**iwconfig** 是 Jean Tourrilhes 在惠普工作时开发的 **wireless-tools** 软件包的一部分。在现代无线配置方面，它在很大程度上已被 **iw** 和 **wpa_supplicant** 取代。

# INSTALL

```apt: sudo apt install wireless-tools```

```apk: sudo apk add wireless-tools```

```zypper: sudo zypper install wireless-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iw](/man/iw)(8), [iwlist](/man/iwlist)(8), [ifconfig](/man/ifconfig)(8), [wpa_supplicant](/man/wpa_supplicant)(8)
