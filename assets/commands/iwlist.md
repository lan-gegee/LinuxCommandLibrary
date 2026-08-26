# TAGLINE

从网络接口获取详细的无线信息

# TLDR

**扫描**网络

```iwlist wlan0 scanning```

列出**频率**

```iwlist wlan0 frequency```

列出**比特率**

```iwlist wlan0 rate```

显示 **WPA** 认证

```iwlist wlan0 auth```

显示 **WPA 密钥**

```iwlist wlan0 wpakeys```

显示**加密**密钥

```iwlist wlan0 keys```

显示**电源**管理

```iwlist wlan0 power```

# SYNOPSIS

**iwlist** _interface_ _action_

# DESCRIPTION

**iwlist** 从无线网络接口获取详细信息，包括可用网络、支持的频率、比特率和加密能力。

# PARAMETERS

**scan**[**ning**]
> 列出范围内的接入点和 ad-hoc 小区及其详细信息

**frequency**
> 显示可用频率和信道

**rate**
> 显示支持的比特率

**keys**
> 显示 WEP 加密密钥及密钥长度

**auth**
> 显示 WPA 认证参数

**wpakeys**
> 显示 WPA 加密密钥

**genie**
> 显示通用信息元素（Generic Information Elements，用于 WPA）

**power**
> 显示电源管理设置

**txpower**
> 显示发射功率设置

**retry**
> 显示发送重试限制和重试生存期

**event**
> 列出设备支持的无线事件

**modulation**
> 列出受支持和已启用的调制方式

# CAVEATS

iwlist 已被废弃，建议改用 iw。扫描可能会短暂中断连接。部分信息需要 root 权限才能显示。

# HISTORY

**iwlist** 是 **wireless-tools** 软件包的一部分，为 Linux 提供无线网络信息。

# INSTALL

```apt: sudo apt install wireless-tools```

```apk: sudo apk add wireless-tools```

```zypper: sudo zypper install wireless-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iw](/man/iw)(8), [iwconfig](/man/iwconfig)(8), [nmcli](/man/nmcli)(1)
