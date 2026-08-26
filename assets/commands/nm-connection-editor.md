# TAGLINE

NetworkManager 连接的图形化编辑器

# TLDR

**打开连接编辑器**

```nm-connection-editor```

**编辑特定连接**

```nm-connection-editor -e [connection_uuid]```

**创建新连接**

```nm-connection-editor -c```

**创建特定类型**

```nm-connection-editor -t [wifi]```

# SYNOPSIS

**nm-connection-editor** [_options_]

# PARAMETERS

**-e**, **--edit** _uuid_
> 按 UUID 编辑连接。

**-c**, **--create**
> 创建新连接。

**-t**, **--type** _type_
> 新连接的类型。

**-s**, **--show**
> 显示编辑器窗口。

# DESCRIPTION

**nm-connection-editor** 是 NetworkManager 连接的图形化编辑器。它提供用于创建、编辑和管理网络连接的 GUI。

该编辑器支持有线、无线、VPN、移动宽带以及其他连接类型。

# CONNECTION TYPES

```
ethernet  - Wired connections
wifi      - Wireless networks
vpn       - VPN connections
bond      - Bonded interfaces
bridge    - Network bridges
vlan      - VLAN configurations
```

# CONFIGURATION STORAGE

**/etc/NetworkManager/system-connections/**
> 以单独文件形式存储连接配置文件的目录。

# CAVEATS

需要 X11/Wayland 显示服务器。命令行替代方案是 nmcli。更改会保存到 system-connections。

# HISTORY

nm-connection-editor 是由 **Red Hat** 开发的 **NetworkManager** 项目的一部分，提供基于 GTK 的网络配置界面。

# INSTALL

```apt: sudo apt install nm-connection-editor```

```dnf: sudo dnf install nm-connection-editor```

```pacman: sudo pacman -S nm-connection-editor```

```apk: sudo apk add network-manager-applet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmtui](/man/nmtui)(1), [NetworkManager](/man/NetworkManager)(1)
