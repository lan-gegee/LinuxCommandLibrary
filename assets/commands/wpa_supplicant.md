# TAGLINE

WPA/WPA2 无线网络身份验证

# TLDR

**带配置启动**

```wpa_supplicant -i [wlan0] -c [/etc/wpa_supplicant.conf]```

**在前台运行**

```wpa_supplicant -i [wlan0] -c [config.conf] -d```

**后台守护进程**

```wpa_supplicant -i [wlan0] -c [config.conf] -B```

**使用指定驱动**

```wpa_supplicant -i [wlan0] -c [config.conf] -D [nl80211]```

# SYNOPSIS

**wpa_supplicant** [_-i interface_] [_-c config_] [_-B_] [_-D driver_]

# PARAMETERS

**-i** _IFACE_
> 接口名称。

**-c** _FILE_
> 配置文件。

**-B**
> 后台模式。

**-D** _DRIVER_
> 驱动后端。

**-d**
> 调试输出。

**-P** _FILE_
> PID 文件。

# CONFIGURATION

**/etc/wpa_supplicant/wpa_supplicant.conf**
> 主配置文件，包含网络定义、全局设置和凭据。可用 **wpa_passphrase** 生成。

# DESCRIPTION

**wpa_supplicant** 是 Linux 系统标准的无线网络身份验证守护进程。它实现了 WPA、WPA2 和 WPA3 安全协议，处理连接受保护无线网络所需的密钥协商和身份验证过程。

该守护进程同时支持个人（PSK）和企业（802.1X/EAP）认证方式，可以管理多个已配置的网络，并根据信号强度和优先级自动选择。网络 SSID、安全设置和凭据都在配置文件中定义。

在大多数桌面 Linux 系统上，wpa_supplicant 作为由 NetworkManager 或 systemd-networkd 管理的后端服务运行，而不是由用户直接调用。

# CAVEATS

需要 root 权限。配置文件包含明文密码，应设置受限权限（600）。在大多数桌面系统上，wpa_supplicant 由 NetworkManager 或 systemd-networkd 管理，而非直接运行。在同一接口上运行多个实例会产生冲突。

# HISTORY

**wpa_supplicant** 由 **Jouni Malinen** 创建，用于 Linux 上的无线网络身份验证。

# INSTALL

```apt: sudo apt install wpasupplicant```

```dnf: sudo dnf install wpa_supplicant```

```pacman: sudo pacman -S wpa_supplicant```

```apk: sudo apk add wpa_supplicant```

```zypper: sudo zypper install wpa_supplicant```

```nix: nix profile install nixpkgs#wpa_supplicant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wpa_cli](/man/wpa_cli)(1), [iwconfig](/man/iwconfig)(8), [NetworkManager](/man/NetworkManager)(8)
