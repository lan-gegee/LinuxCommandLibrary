# TAGLINE

用于无线接入点和认证服务器的用户态守护进程

# TLDR

**启动接入点**

```sudo hostapd [/etc/hostapd/hostapd.conf]```

**以前台模式启动**并输出调试信息

```sudo hostapd -d [hostapd.conf]```

**以后台模式启动**

```sudo hostapd -B [hostapd.conf]```

**带调试信息和时间戳启动**

```sudo hostapd -dt [hostapd.conf]```

# SYNOPSIS

**hostapd** [_options_] _config_file_

# DESCRIPTION

**hostapd** 是用于无线接入点和认证服务器的用户态守护进程。它实现 IEEE 802.11 接入点管理、WPA/WPA2/WPA3 认证以及 IEEE 802.1X 认证器。

该工具将无线接口转变为接入点，处理客户端连接、加密和认证协议。

# PARAMETERS

**-B**
> 以后台（守护进程）方式运行。

**-d**
> 调试输出。

**-dd**
> 更详细的调试信息。

**-t**
> 在调试输出中包含时间戳。

**-v**
> 显示版本信息后退出。

**-K**
> 在调试输出中包含密钥数据。

**-g** _socket_
> 全局控制接口路径。

**-P** _pidfile_
> PID 文件路径。

**-f** _logfile_
> 将输出重定向到日志文件。

**-e** _entropy_file_
> 用于存储熵的文件（以加快重启）。

# CONFIG OPTIONS

**interface**: 无线接口（例如 wlan0）
**driver**: 驱动接口（nl80211、hostap 等）
**ssid**: 网络名称
**hw_mode**: 频段（a = 5GHz，b = 2.4GHz 11Mbps，g = 2.4GHz 54Mbps）
**channel**: 信道号（0 = ACS，若支持）
**ieee80211n**: 启用 802.11n（1 = 是）
**ieee80211ac**: 启用 802.11ac（1 = 是）
**wpa**: WPA 模式（1 = WPA，2 = WPA2，3 = 两者兼用）
**wpa_passphrase**: 密码（8-63 个字符）
**wpa_key_mgmt**: 密钥管理（WPA-PSK，WPA3 用 SAE）

# CAVEATS

需要支持 AP 模式的无线网卡。配置较复杂。驱动支持情况不一。可能与 NetworkManager 冲突。

# HISTORY

**hostapd** 由 **Jouni Malinen** 开发，是 Linux 无线协议栈的一部分。它成为在 Linux 上创建软件接入点的标准方式，支持不断演进的无线安全标准。

# INSTALL

```apt: sudo apt install hostapd```

```dnf: sudo dnf install hostapd```

```pacman: sudo pacman -S hostapd```

```apk: sudo apk add hostapd```

```zypper: sudo zypper install hostapd```

```nix: nix profile install nixpkgs#hostapd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iw](/man/iw)(1), [iwconfig](/man/iwconfig)(1), [wpa_supplicant](/man/wpa_supplicant)(1), [dnsmasq](/man/dnsmasq)(1)
