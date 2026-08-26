# TAGLINE

重启已连接的 Android 设备

# TLDR

正常**重启**设备

```adb reboot```

重启进入 **bootloader/fastboot** 模式

```adb reboot bootloader```

重启进入 **recovery** 模式

```adb reboot recovery```

重启进入 **sideload** 模式

```adb reboot sideload```

重启进入 sideload 模式并在完成后**自动重启**

```adb reboot sideload-auto-reboot```

# SYNOPSIS

**adb reboot** [_bootloader_|_recovery_|_sideload_|_sideload-auto-reboot_]

# DESCRIPTION

**adb reboot** 重启已连接的 Android 设备。不带参数时执行常规重启。带模式参数时可重启进入特殊模式，如 bootloader（fastboot）、recovery 或 sideload，用于刷写固件或安装更新。

# PARAMETERS

**bootloader**
> 重启进入 bootloader/fastboot 模式，用于底层刷机

**recovery**
> 重启进入 recovery 模式，用于系统恢复或更新

**sideload**
> 重启进入 sideload 模式，用于 ADB 侧载

**sideload-auto-reboot**
> 重启进入 sideload 模式，并在侧载完成后自动重启

# CAVEATS

Bootloader 和 recovery 模式可能要求已解锁的引导加载程序或特定的设备状态。某些设备使用厂商专有的启动模式。重启到 bootloader 会终止 adb 连接；之后请改用 **fastboot** 命令。

# HISTORY

**adb reboot** 自 **2008** 年 Android SDK 首次发布起即可用。启动模式选项是为方便 ROM 开发和设备恢复操作而加入的。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [adb-shell](/man/adb-shell)(1), [fastboot](/man/fastboot)(1)
