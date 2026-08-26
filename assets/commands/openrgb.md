# TAGLINE

开源 RGB 灯光控制

# TLDR

**启动 GUI**

```openrgb```

**列出设备**

```openrgb -l```

**设置设备颜色**

```openrgb -d [0] -c [FF0000]```

**设置模式**

```openrgb -d [0] -m [Static]```

**应用配置文件**

```openrgb -p [profile.orp]```

**设置特定分区的颜色**

```openrgb -d [0] -z [0] -c [00FF00]```

**启动 SDK 服务器**

```openrgb --server```

**在自定义端口上启动服务器**

```openrgb --server --server-port [1234]```

# SYNOPSIS

**openrgb** [_options_]

# PARAMETERS

**-l**, **--list-devices**
> 列出所有检测到的 RGB 设备及其索引号。

**-d** _INDEX_, **--device** _INDEX_
> 按索引号或名称选择设备。省略时作用于所有设备。

**-z** _INDEX_, **--zone** _INDEX_
> 选择设备上的分区。

**-c** _COLOR_, **--color** _COLOR_
> 以十六进制格式设置颜色（例如红色为 FF0000）。

**-m** _MODE_, **--mode** _MODE_
> 设置灯光模式（例如 Static、Breathing、Rainbow）。

**-s** _SIZE_, **--size** _SIZE_
> 设置分区大小（用于可调整大小的分区）。

**-p** _PROFILE_
> 加载已保存的配置文件。

**--server**
> 启动 SDK 服务器（默认端口 6742）。

**--server-port** _PORT_
> 设置 SDK 服务器端口（范围 1024-65535）。

**--client** _IP:PORT_
> 连接到某个 SDK 服务器。

**-v**, **--verbose**
> 将日志消息打印到 stdout。

**--startminimized**
> 启动 GUI 时最小化到系统托盘。

**--help**
> 显示帮助信息。

# DESCRIPTION

**OpenRGB** 是一款开源 RGB 灯光控制应用程序，为 ASUS、Corsair、Logitech、MSI、Razer 等众多硬件品牌提供统一的管理界面。

该工具同时提供 GUI 和 CLI，用于控制主板、内存、显卡、外设和其他设备上的 RGB LED。它可跨平台运行于 Linux、Windows 和 macOS，还带有 SDK 服务器，用于远程控制和与其他应用程序集成。

# CAVEATS

硬件支持程度不一。可能需要内核模块。部分设备需要 root 权限。

# HISTORY

OpenRGB 为实现跨不同品牌的**统一 RGB 灯光控制**而创建。

# INSTALL

```dnf: sudo dnf install openrgb```

```pacman: sudo pacman -S openrgb```

```apk: sudo apk add openrgb```

```nix: nix profile install nixpkgs#openrgb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[i2cdetect](/man/i2cdetect)(1)
