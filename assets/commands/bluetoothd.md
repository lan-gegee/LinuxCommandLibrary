# TAGLINE

蓝牙系统守护进程

# TLDR

**启动**守护进程

```bluetoothd```

启动守护进程并**将日志输出到 stdout**

```bluetoothd -n```

以**指定的配置**文件启动

```bluetoothd -f [path/to/file]```

以**详细的调试**输出启动

```bluetoothd -d```

仅输出来自**指定源文件**的调试信息

```bluetoothd -d=[path/to/file1:path/to/file2]```

# SYNOPSIS

**bluetoothd** [_options_]

# DESCRIPTION

**bluetoothd** 是蓝牙系统守护进程，负责管理蓝牙设备、连接和服务。它处理系统上所有蓝牙功能的设备发现、配对和连接管理。

该守护进程通常由 systemd 自动启动。它从 **/etc/bluetooth/main.conf** 读取配置，并管理蓝牙适配器和已连接的设备。

# PARAMETERS

**-n, --nodetach**
> 在前台运行；不分离为守护进程。日志输出到 stdout。

**-f, --configfile** _file_
> 使用备用配置文件代替 /etc/bluetooth/main.conf。

**-d, --debug** [_files_]
> 启用调试输出，可选地限定为冒号分隔的源文件列表。

**-E, --experimental**
> 启用实验性的 D-Bus 接口和特性。

**-p, --plugin** _name_
> 指定要加载的插件。

**-P, --noplugin** _name_
> 指定要排除的插件。

# CONFIGURATION

**/etc/bluetooth/main.conf**
> 主配置文件，控制设备类别、名称、配对超时、可发现模式以及适配器默认值。

# CAVEATS

通常由 systemd 管理，很少需要手动调用。需要 root 权限。配置更改需要重启守护进程。调试模式会产生大量输出。

# HISTORY

**bluetoothd** 是 **BlueZ** 的一部分，BlueZ 是自 **2000 年代初**以来一直维护的 Linux 官方蓝牙协议栈。在 BlueZ 5（**2012 年**）中，它取代了 BlueZ 4 中旧的按配置文件划分的守护进程，成为单一的基于插件的守护进程，并通过 D-Bus 暴露其功能。

# INSTALL

```apt: sudo apt install bluez```

```dnf: sudo dnf install bluez```

```pacman: sudo pacman -S bluez```

```zypper: sudo zypper install bluez```

```brew: brew install bluez```

```nix: nix profile install nixpkgs#bluez```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bluetoothctl](/man/bluetoothctl)(1), [hciconfig](/man/hciconfig)(1), [hcitool](/man/hcitool)(1)

# RESOURCES

```[Homepage](http://www.bluez.org/)```

```[Source code](https://github.com/bluez/bluez)```

<!-- verified: 2026-06-19 -->
