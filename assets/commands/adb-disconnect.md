# TAGLINE

无线 Android 设备断开器

# TLDR

**断开**特定设备

```adb disconnect [192.168.1.100]:5555```

断开**所有**无线设备

```adb disconnect```

# SYNOPSIS

**adb disconnect** [_host_[:_port_]]

# DESCRIPTION

**adb disconnect** 终止无线 adb 连接。不带参数调用时，断开所有已连接的 TCP/IP 设备。指定主机和端口时，仅断开该设备。

此命令只影响无线连接；USB 连接的设备保持连接状态，直到物理拔除。

# PARAMETERS

**host**
> 要断开的设备的 IP 地址或主机名

**port**
> TCP 端口号（默认：5555）

# CAVEATS

不影响 USB 连接。断开后设备仍处于 TCP/IP 模式；无需重新配置即可用 **adb connect** 重新连接。

# HISTORY

**adb disconnect** 自 Android SDK 引入无线调试以来一直可用。它提供了一种干净地终止网络连接的方式，而无需杀死整个 adb 服务器。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-connect](/man/adb-connect)(1), [adb-pair](/man/adb-pair)(1), [adb-kill-server](/man/adb-kill-server)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
