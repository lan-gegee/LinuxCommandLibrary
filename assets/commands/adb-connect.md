# TAGLINE

无线 Android 设备连接器

# TLDR

通过 Wi-Fi **连接**设备

```adb connect [192.168.1.100]:5555```

使用**默认端口**（5555）连接

```adb connect [192.168.1.100]```

连接**模拟器**

```adb connect [localhost]:5554```

# SYNOPSIS

**adb connect** _host_[:_port_]

# DESCRIPTION

**adb connect** 建立到 Android 设备的 TCP/IP 连接，用于无线调试。连接建立后，所有 adb 命令都可以通过网络执行，而不必使用 USB。

在无线连接之前，通常需要先通过 USB 用 **adb tcpip 5555** 配置设备以启用 TCP/IP 模式。Android 11 及以上版本支持直接无线配对，无需先进行 USB 连接。

# PARAMETERS

**host**
> Android 设备的 IP 地址或主机名

**port**
> TCP 端口号（默认：5555）

# CAVEATS

电脑和设备必须处于同一网络。设备重启后会恢复为 USB 模式，需要重新配置。无线连接不如 USB 安全；请只在可信网络中使用。与 USB 相比，连接速度可能较慢。

# HISTORY

无线 ADB 调试自早期 Android 版本起就已可用，但需要先通过 USB 设置。Android 11（发布于 **2020** 年）引入了带配对码的无线调试，不再需要 USB。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-disconnect](/man/adb-disconnect)(1), [adb-pair](/man/adb-pair)(1), [adb-devices](/man/adb-devices)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
