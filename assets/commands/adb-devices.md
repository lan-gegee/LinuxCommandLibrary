# TAGLINE

列出已连接的 Android 设备

# TLDR

**列出**所有已连接的设备

```adb devices```

以**扩展信息**列出设备

```adb devices -l```

# SYNOPSIS

**adb devices** [_-l_]

# DESCRIPTION

**adb devices** 列出当前连接到电脑的所有 Android 设备，无论是通过 USB 还是无线连接。输出显示设备的序列号及其连接状态。

设备状态包括：**device**（已连接且就绪）、**offline**（无响应）、**unauthorized**（USB 调试未授权）、**no permissions**（Linux udev 规则问题）和 **bootloader**（处于 fastboot 模式）。

# PARAMETERS

**-l**
> 长格式输出，显示额外的设备信息（product、model、device、transport_id）

# OUTPUT FORMAT

```
List of devices attached
[serial]    [state]
```

使用 -l 标志时：
```
[serial]    [state] product:[name] model:[name] device:[name] transport_id:[id]
```

# CAVEATS

显示 "unauthorized" 的设备需要你在设备上确认 RSA 密钥提示。Linux 上的 "no permissions" 错误通常需要为你的设备添加 udev 规则。模拟器显示为 emulator-5554 或类似名称。

# HISTORY

**adb devices** 命令自 **2008** 年 Android SDK 首次发布起就是 adb 的一部分。用于扩展信息的 -l 标志是后来加入的，帮助区分多台同型号设备。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-connect](/man/adb-connect)(1), [fastboot](/man/fastboot)(1)
