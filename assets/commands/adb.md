# TAGLINE

Android Debug Bridge 客户端-服务器工具

# TLDR

**列出**已连接的设备

```adb devices```

**安装** APK

```adb install [app.apk]```

将文件从设备**复制到电脑**

```adb pull [/sdcard/file.txt] [./local/]```

将文件从电脑**复制到设备**

```adb push [local_file] [/sdcard/]```

在设备上打开 **shell**

```adb shell```

与设备**配对**以进行无线调试（Android 11+）

```adb pair [host]:[port]```

无线**连接**设备

```adb connect [host]:[port]```

# SYNOPSIS

**adb** [_-d|-e|-s serial_] _command_ [_options_]

# DESCRIPTION

**adb**（Android Debug Bridge）是一款多用途命令行工具，用于与 Android 设备通信。它提供 Unix shell 以执行命令、安装/卸载应用、传输文件和调试应用程序。

该工具采用客户端-服务器架构：adb 服务器运行在你的电脑上，与所连设备上的 adb 守护进程（adbd）通信。连接可以通过 USB 建立，也可以通过 TCP/IP 无线建立。

# PARAMETERS

**-d**
> 将命令定向到唯一连接的 USB 设备

**-e**
> 将命令定向到唯一运行的模拟器

**-s** _serial_
> 将命令定向到具有指定序列号的设备

**-t** _transport_id_
> 将命令定向到具有给定 transport ID 的设备

**devices**
> 列出所有已连接设备及其状态

**install** [**-r**] [**-g**] _apk_
> 安装 APK 文件。-r 表示重装并保留数据，-g 表示授予所有运行时权限。

**uninstall** [**-k**] _package_
> 按包名移除应用。-k 保留数据目录和缓存目录。

**pair** _host_:_port_ [_pairing_code_]
> 与设备配对以进行无线调试（Android 11+）。

**connect** _host_:_port_
> 通过 TCP/IP 连接设备。

**push** _local_ _remote_
> 将文件从电脑复制到设备

**pull** _remote_ _local_
> 将文件从设备复制到电脑

**shell**
> 打开交互式 shell 或在设备上执行命令

**logcat**
> 查看设备日志输出

**forward** _local_ _remote_
> 设置端口转发

**reverse** _remote_ _local_
> 设置反向端口转发

**reboot**
> 重启设备（可选 bootloader、recovery 模式）

**start-server**
> 启动 adb 服务器

**kill-server**
> 停止 adb 服务器

**sideload** _otapackage_
> 在 recovery 模式下侧载 OTA 更新包

**bugreport** [_path_]
> 生成错误报告并保存到 path

# CONFIGURATION

**~/.android/adb_usb.ini**
> 用于设备检测的 USB 厂商 ID 列表，每行一个。

**~/.android/adbkey**
> 用于设备身份验证的 RSA 私钥。对应的公钥（adbkey.pub）会被推送到已授权的设备上。

**ANDROID_ADB_SERVER_PORT**
> 覆盖 adb 服务器默认端口（5037）的环境变量。

**ADB_VENDOR_KEYS**
> 指定冒号分隔的其他 RSA 密钥文件路径的环境变量，用于设备授权。

# CAVEATS

必须在设备上启用 USB 调试。首次连接需要在设备上授权这台电脑。部分命令需要 root 权限。无线调试需要先进行 USB 设置或配对（Android 11+）。

# HISTORY

**adb** 由 Google 作为 Android SDK 的一部分开发，随 **2008** 年 Android 1.0 首次发布。此后它不断演进，增加了无线调试、分区存储访问等特性，并通过 RSA 密钥认证提升了安全性。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[fastboot](/man/fastboot)(1), [aapt](/man/aapt)(1), [logcat](/man/logcat)(1), [scrcpy](/man/scrcpy)(1)
