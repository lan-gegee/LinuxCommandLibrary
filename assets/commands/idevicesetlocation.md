# TAGLINE

设置或重置 iOS 设备的模拟 GPS 位置

# TLDR

**设置设备位置**

```idevicesetlocation -- [latitude] [longitude]```

**重置为真实位置**

```idevicesetlocation reset```

**指定目标设备**

```idevicesetlocation -u [device-udid] -- [37.7749] [-122.4194]```

# SYNOPSIS

**idevicesetlocation** [_options_] [**--** _lat_ _lon_ | **reset**]

# PARAMETERS

**-u** _udid_, **--udid** _udid_
> 按设备的 UDID 指定目标设备。

**-n**, **--network**
> 通过网络而非 USB 连接设备。

**-d**, **--debug**
> 启用详细调试输出。

**-h**, **--help**
> 显示帮助信息。

**--**
> 位置参数坐标前的分隔符（当经度为负数时必须使用，以免开头的负号被解析成选项）。

# DESCRIPTION

**idevicesetlocation** 设置或重置 iOS 设备上报的模拟 GPS 位置，适合测试位置感知类应用。它是 **libimobiledevice** 套件的一部分，与设备的开发者服务通信。

传入 `reset` 而不是坐标即可清除模拟位置并恢复真实的 GPS 上报。坐标采用十进制度表示：北纬/东经为正，南纬/西经为负。

# CAVEATS

要求目标设备上已挂载开发者磁盘镜像（iOS 17+ 则需要开发者模式隧道）——通常通过 **ideviceimagemounter** 完成。模拟位置会一直保持，直到设备重启或执行 reset。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ideviceimagemounter](/man/ideviceimagemounter)(1), [ideviceinfo](/man/ideviceinfo)(1)

