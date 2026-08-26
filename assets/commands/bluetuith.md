# TAGLINE

跨平台 TUI 蓝牙管理器

# TLDR

**启动蓝牙管理器**

```bluetuith```

**连接到指定适配器**

```bluetuith --adapter [hci0]```

# SYNOPSIS

**bluetuith** [_options_]

# PARAMETERS

**--adapter** _name_
> 指定要使用的蓝牙适配器。

**--no-warning**
> 不显示警告消息。

**--confirm-on-quit**
> 退出前请求确认。

# DESCRIPTION

**bluetuith** 是一个用于管理蓝牙设备的终端用户界面。它通过交互式 TUI 提供设备扫描、配对、连接以及基于 OBEX 的文件传输功能。该界面显示附近的设备、已配对的设备和适配器属性，使得在没有图形桌面环境的情况下也能管理蓝牙。

它使用 Go 编写，旨在成为 blueman 等大多数蓝牙管理器的替代品。支持 Linux、macOS 和 Windows。

# CAVEATS

目前处于 alpha 阶段。需要特定平台的蓝牙支持（Linux 上为 BlueZ，macOS/Windows 上为原生协议栈）。功能取决于蓝牙适配器硬件的能力。

# INSTALL

```apk: sudo apk add bluetuith```

```zypper: sudo zypper install bluetuith```

```nix: nix profile install nixpkgs#bluetuith```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bluetoothctl](/man/bluetoothctl)(1), [hcitool](/man/hcitool)(1)
