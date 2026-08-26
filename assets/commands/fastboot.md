# TAGLINE

Android 引导加载程序刷写与修改工具

# TLDR

**列出已连接的设备**

```fastboot devices```

**刷写分区**

```fastboot flash [boot] [boot.img]```

**从出厂镜像刷写全部分区**

```fastboot flashall```

**解锁引导加载程序**

```fastboot flashing unlock```

**重启设备**

```fastboot reboot```

**重启到 recovery**

```fastboot reboot recovery```

**擦除分区**

```fastboot erase [cache]```

**引导临时镜像**

```fastboot boot [recovery.img]```

# SYNOPSIS

**fastboot** [_options_] _command_ [_args_]

# DESCRIPTION

**fastboot** 是一款用于刷写固件和修改设备分区的 Android 工具。它与处于 fastboot/bootloader 模式的设备通信，执行底层操作。

该工具可用于安装自定义 ROM、recovery 镜像，以及对 Android 设备进行维护。它是 Android SDK platform tools 的一部分。

# PARAMETERS

**devices**
> 列出已连接的设备。

**flash** _partition_ _image_
> 将镜像刷写到分区。

**flashall**
> 刷写所有分区。

**erase** _partition_
> 擦除分区。

**reboot** [_target_]
> 重启（bootloader、recovery）。

**boot** _image_
> 引导临时镜像。

**oem** _command_
> OEM 特定命令。

**getvar** _variable_
> 获取 bootloader 变量。

**-s** _serial_
> 指定目标设备。

**update** _zipfile_
> 从更新 zip 刷写所有分区。

**flashing unlock**
> 解锁 bootloader（较新设备）。

**-w**
> 清除 userdata。

# CAVEATS

设备必须处于 fastboot 模式。错误的镜像可能导致设备变砖。解锁 bootloader 可能使保修失效。Windows 上需要安装 USB 驱动。

# HISTORY

**fastboot** 是 Android SDK platform tools 的一部分，由 **Google** 开发。它随 Android 在 **2000 年代末**的开发而出现，成为刷写设备的标准方式。该协议允许厂商自定义行为，同时保持兼容性。

# INSTALL

```apt: sudo apt install fastboot```

```apk: sudo apk add android-tools-fastboot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[adb](/man/adb)(1)
