# TAGLINE

显示已连接 iOS 设备的信息（libimobiledevice）

# TLDR

**显示第一台已连接设备的所有可用属性**

```ideviceinfo```

**按 UDID 指定目标设备**

```ideviceinfo -u [device-udid]```

**只查询特定键**

```ideviceinfo -k [ProductVersion]```

**查询特定的 Lockdown 域**

```ideviceinfo -q [com.apple.disk_usage]```

**以 XML 属性列表输出**

```ideviceinfo -x```

**通过网络连接设备**（Wi-Fi 配对）

```ideviceinfo -n```

**简单/未配对连接**（跳过自动配对）

```ideviceinfo -s```

# SYNOPSIS

**ideviceinfo** [_options_]

# PARAMETERS

**-u**, **--udid** _UDID_
> 按设备的 UDID 指定目标设备。连接多台设备时必须提供。

**-q**, **--domain** _NAME_
> 将查询限制在给定的 Lockdown 域（如 `com.apple.disk_usage`、`com.apple.mobile.battery`、`com.apple.mobile.wireless_lockdown`）。

**-k**, **--key** _NAME_
> 只打印给定键的值。直接输出原始值，不带键名前缀。

**-x**, **--xml**
> 以 Apple XML plist 格式而非 `key: value` 行输出。适合脚本处理。

**-s**, **--simple**
> 使用不与设备配对的简单 Lockdown 连接。可用的键会少一些。

**-n**, **--network**
> 连接通过 Wi-Fi（而非 USB）配对的设备。

**-d**, **--debug**
> 输出 libimobiledevice 的详细调试信息。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**ideviceinfo** 查询已连接 iOS（iPhone、iPad、iPod、Apple TV）设备上的 Lockdown 服务并打印其属性。不指定键或域时，它会转储公开的根级键——`DeviceName`、`ProductType`、`ProductVersion`、`BuildVersion`、`SerialNumber`、`UniqueDeviceID`、`WiFiAddress`、`BluetoothAddress` 等等。

按域查询（`-q`）可以访问受保护的命名空间，例如 `com.apple.disk_usage`（存储统计）或 `com.apple.mobile.battery`（电池信息）。大多数域要求设备已完成配对并处于解锁状态。

# CAVEATS

属于 **libimobiledevice**。设备必须在主机上被**信任**——即在解锁状态下插入过一次，并在"信任这台电脑？"提示中点击同意。在 macOS 上，Apple 自带的 `usbmuxd` 会替代 libimobiledevice 的版本；两者混用可能导致配对冲突。网络连接方式（`-n`）只有在 iTunes/Finder 中启用 Wi-Fi 同步后才能使用。

# HISTORY

**ideviceinfo** 随 **libimobiledevice** 项目一同发布——该项目是 Apple iTunes/Finder 设备协议的跨平台重新实现。它由 **Jonathan Beck** 于 **2008 年**前后创建，目前由 **Nikias Bassen** 及众多贡献者维护。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevice_id](/man/idevice_id)(1), [idevicebackup2](/man/idevicebackup2)(1), [idevicepair](/man/idevicepair)(1), [idevicesyslog](/man/idevicesyslog)(1)
