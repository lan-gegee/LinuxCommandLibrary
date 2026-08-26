# TAGLINE

管理 Thunderbolt 设备授权

# TLDR

列出**已连接且已授权**的设备

```boltctl```

列出已连接设备，包括**未授权**的设备

```boltctl list```

临时**授权**一台设备

```boltctl authorize [device_uuid]```

**授权并记住**一台设备

```boltctl enroll [device_uuid]```

**注册**一台设备，每次连接时自动授权

```boltctl enroll --policy auto [device_uuid]```

**撤销**先前授权过的设备

```boltctl forget [device_uuid]```

显示设备的**详细信息**

```boltctl info [device_uuid]```

**监视**守护进程的设备变化

```boltctl monitor```

# SYNOPSIS

**boltctl** [_command_] [_options_] [_device_uuid_]

# DESCRIPTION

**boltctl** 用于管理 Thunderbolt 设备及其安全级别。它控制哪些 Thunderbolt 设备被授权连接到系统，从而防范恶意设备（Thunderclap 攻击）。

该工具与 boltd 守护进程协作，为 Thunderbolt/USB4 端口实施安全策略。

# SUBCOMMANDS

**list**
> 列出所有已连接的设备。

**authorize**
> 仅为当前会话临时授权一台设备。

**enroll**
> 授权并记住一台设备，以便后续连接。可使用 **--policy**（_default_、_auto_ 或 _manual_）控制设备在后续连接时如何被授权，并可用 **--chain** 在必要时同时授权父设备。

**forget**
> 将设备从授权列表中移除（撤销存储的密钥）。

**info**
> 显示详细的设备信息。

**monitor**
> 监听并打印设备和守护进程的状态变化。

**config**
> 获取或设置设备及守护进程的全局配置值。

**domains**
> 列出守护进程已知的 Thunderbolt 域（控制器）。

**power**
> 控制强制供电状态。

# CAVEATS

Thunderbolt 安全级别在 BIOS/UEFI 中设置。并非所有系统都支持所有安全级别。未授权设备的功能可能受限或完全不可用。

# HISTORY

随着通过 Thunderbolt 端口发起 DMA 攻击的手段被发现，Thunderbolt 安全变得日益重要。bolt 项目正是为了给 Linux 系统提供用户态安全控制而开发的。

# INSTALL

```apt: sudo apt install bolt```

```dnf: sudo dnf install bolt```

```pacman: sudo pacman -S bolt```

```apk: sudo apk add bolt```

```zypper: sudo zypper install bolt```

```nix: nix profile install nixpkgs#bolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[boltd](/man/boltd)(8), [udevadm](/man/udevadm)(8)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/bolt/bolt)```

```[Documentation](https://man.archlinux.org/man/boltctl.1)```

<!-- verified: 2026-06-19 -->
