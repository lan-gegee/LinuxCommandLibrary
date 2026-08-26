# TAGLINE

管理网络连接的守护进程

# TLDR

**查看连接状态**

```nmcli general status```

**列出连接**

```nmcli connection show```

**连接 WiFi**

```nmcli device wifi connect "[SSID]" password "[password]"```

**显示 WiFi 网络**

```nmcli device wifi list```

**启用连接**

```nmcli connection up [connection_name]```

**创建静态连接**

```nmcli connection add type ethernet con-name [myeth] ifname [eth0] ip4 [192.168.1.10/24] gw4 [192.168.1.1]```

# SYNOPSIS

**NetworkManager** [_options_]

# PARAMETERS

**--debug**
> 调试模式。

**--log-level** _level_
> 日志级别。

**--log-domains** _domains_
> 日志域。

**--pid-file** _file_
> PID 文件位置。

# DESCRIPTION

**NetworkManager** 是一个管理网络连接的守护进程。它提供自动的网络检测和配置，处理有线、无线、移动宽带以及 VPN 连接。

NetworkManager 通过 nmcli、nmtui 或 GUI 小程序进行控制。

# CLI TOOL (nmcli)

```bash
nmcli device                    # List devices
nmcli connection                # List connections
nmcli connection modify ...     # Modify connection
nmcli networking off            # Disable networking
```

# CONFIGURATION

```
/etc/NetworkManager/
├── NetworkManager.conf
├── system-connections/
└── conf.d/
```

# CAVEATS

可能与其他网络工具冲突。连接保存在 /etc/NetworkManager/ 中。部分系统使用其他替代方案。

# HISTORY

NetworkManager 由 **Red Hat** 自 **2004 年**起开发，旨在简化 Linux 桌面上的网络配置。

# INSTALL

```apt: sudo apt install network-manager```

```dnf: sudo dnf install NetworkManager```

```pacman: sudo pacman -S networkmanager```

```apk: sudo apk add networkmanager```

```zypper: sudo zypper install NetworkManager```

```nix: nix profile install nixpkgs#networkmanager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmtui](/man/nmtui)(1), [netctl](/man/netctl)(1)
