# TAGLINE

从命令行控制 KDE Connect

# TLDR

**列出设备**

```kdeconnect-cli --list-available```

**与设备配对**

```kdeconnect-cli --pair -d [device-id]```

**发送文件**

```kdeconnect-cli --share [file] -d [device-id]```

**让设备响铃**

```kdeconnect-cli --ring -d [device-id]```

**发送短信**

```kdeconnect-cli --send-sms "[message]" --destination [number] -d [device-id]```

**获取电量状态**

```kdeconnect-cli --battery -d [device-id]```

# SYNOPSIS

**kdeconnect-cli** [_options_]

# PARAMETERS

**--list-available**
> 列出可用设备。

**--pair**
> 与设备配对。

**--unpair**
> 取消与设备的配对。

**-d** _DEVICE_
> 目标设备 ID。

**--share** _FILE_
> 向设备发送文件。

**--ring**
> 让设备响铃。

**--send-sms** _MSG_
> 发送短信。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kdeconnect-cli** 从命令行控制 KDE Connect。它将 Linux 桌面与移动设备连接起来。

该工具可以发送文件和通知，并控制媒体播放。它让你可以在终端中实现手机集成。

# CAVEATS

需要 KDE Connect 守护进程。设备必须在同一网络中。手机端需要安装对应应用。

# HISTORY

kdeconnect-cli 是 **KDE Connect** 的一部分，实现 Linux 桌面与 Android 设备之间的无缝集成。

# INSTALL

```apt: sudo apt install kdeconnect```

```pacman: sudo pacman -S kdeconnect```

```apk: sudo apk add kdeconnect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[adb-connect](/man/adb-connect)(1), [nmcli-connection](/man/nmcli-connection)(1)
