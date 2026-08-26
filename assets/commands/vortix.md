# TAGLINE

带遥测的 WireGuard 和 OpenVPN 终端界面

# TLDR

**启动 VPN 管理 TUI**

```sudo vortix```

**导入 VPN 配置**

```vortix import [tunnel.conf]```

**显示版本和配置信息**

```vortix info```

# SYNOPSIS

**vortix** [_command_]

# DESCRIPTION

**vortix** 是一个用于管理 WireGuard 和 OpenVPN 连接的终端 UI，具备实时遥测和泄露防护。它会自动检测 VPN 配置文件，并提供吞吐量、延迟、抖动、丢包率和地理位置数据等实时指标。VPN 操作需要 root 权限。

# HISTORY

**vortix** 由 **Harry-kp** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S vortix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wg](/man/wg)(1), [openvpn](/man/openvpn)(1), [wg-cmd](/man/wg-cmd)(1)
