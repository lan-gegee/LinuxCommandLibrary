# TAGLINE

iwd（现代无线网络配置守护进程）的命令行界面

# TLDR

运行**交互式**模式

```iwctl```

显示 Wi-Fi **站点**

```iwctl station list```

**扫描**网络

```iwctl station [station] scan```

显示**发现的网络**

```iwctl station [station] get-networks```

**连接**到网络

```iwctl station [station] connect [network_name]```

显示**帮助**

```iwctl -h```

# SYNOPSIS

**iwctl** [_options_] [_command_]

# PARAMETERS

**station list**
> 列出无线站点（接口）

**station** _STATION_ **scan**
> 触发网络扫描

**station** _STATION_ **get-networks**
> 显示发现的网络

**station** _STATION_ **connect** _SSID_
> 连接到网络

**station** _STATION_ **disconnect**
> 断开当前网络的连接

**known-networks list**
> 列出已保存的网络配置

**-h**, **--help**
> 显示帮助

# DESCRIPTION

**iwctl** 是 iwd（iNet Wireless Daemon）的命令行界面。iwd 是一款现代的无线网络配置守护进程。它提供交互式和命令行两种模式来管理 Wi-Fi 连接。

iwd 的设计定位是 wpa_supplicant 的轻量级替代品，连接速度更快、配置更简单。凭据可以交互式输入，也可以预先配置好。

# CAVEATS

需要 iwd 守护进程正在运行。网络凭据存储在 /var/lib/iwd/ 中。如果与 NetworkManager 同时试图管理同一接口，可能发生冲突。

# HISTORY

iwd 由 Intel 开发，于 **2017 年**首次发布，作为 wpa_supplicant 的现代替代品。它的目标是提供更简单的配置和更快的连接速度，同时支持现代无线安全协议。

# INSTALL

```apt: sudo apt install iwd```

```dnf: sudo dnf install iwd```

```pacman: sudo pacman -S iwd```

```apk: sudo apk add iwd```

```zypper: sudo zypper install iwd```

```nix: nix profile install nixpkgs#iwd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iw](/man/iw)(8), [nmcli](/man/nmcli)(1), [wpa_supplicant](/man/wpa_supplicant)(8)
