# TAGLINE

与 Android 设备配对以进行无线调试

# TLDR

使用配对码与设备**配对**

```adb pair [192.168.1.100]:[port]```

# SYNOPSIS

**adb pair** _host_:_port_ [_pairing_code_]

# DESCRIPTION

**adb pair** 使用配对码与 Android 11 及以上版本的设备建立安全的无线调试连接。这样无需先进行 USB 连接即可启用无线调试。

要使用此功能，请在设备的开发者选项中启用"无线调试"，然后点按"使用配对码配对设备"以获取配对端口和配对码。配对完成后，使用无线调试设置中显示的连接端口执行 **adb connect**。

# PARAMETERS

**host**
> Android 设备的 IP 地址

**port**
> 设备上显示的配对端口（不同于连接端口）

**pairing_code**
> 设备上显示的六位配对码（未提供时会提示输入）

# CAVEATS

仅适用于 Android 11（API 30）及更高版本。配对端口不同于 **adb connect** 使用的连接端口。配对码很快就会过期。两台设备必须处于同一网络。

# HISTORY

带配对的无线调试随 **2020** 年发布的 Android 11 引入。该功能旨在取消先进行 USB 连接的要求，改善开发者体验。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-connect](/man/adb-connect)(1), [adb-disconnect](/man/adb-disconnect)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/packages/modules/adb/)```

```[Documentation](https://developer.android.com/tools/adb)```

<!-- verified: 2026-06-11 -->
