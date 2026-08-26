# TAGLINE

NetworkManager 系统托盘小程序

# TLDR

**启动网络管理器小程序**

```nm-applet```

**以指示器样式启动**

```nm-applet --indicator```

**带调试输出启动**

```nm-applet --debug```

# SYNOPSIS

**nm-applet** [_options_]

# PARAMETERS

**--indicator**
> 使用指示器（appindicator）样式。

**--debug**
> 启用调试输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nm-applet** 是 NetworkManager 的系统托盘小程序。为网络管理提供图形界面。

该工具显示网络状态。允许连接 WiFi 和 VPN。

# CAVEATS

需要 NetworkManager。依赖桌面环境。需要系统托盘。

# HISTORY

nm-applet 是 **NetworkManager** 的一部分，为 Linux 桌面提供图形化的网络管理。

# INSTALL

```apt: sudo apt install network-manager-applet```

```dnf: sudo dnf install network-manager-applet```

```pacman: sudo pacman -S network-manager-applet```

```apk: sudo apk add network-manager-applet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmtui](/man/nmtui)(1), [NetworkManager](/man/NetworkManager)(1)
