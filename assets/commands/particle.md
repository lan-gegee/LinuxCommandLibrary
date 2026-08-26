# TAGLINE

控制 Particle IoT 设备

# TLDR

**登录 Particle**

```particle login```

**列出设备**

```particle list```

**向设备刷写固件**

```particle flash [device_name] [firmware.bin]```

**本地编译**

```particle compile [photon] [project_dir]```

**监视串口输出**

```particle serial monitor```

**调用设备函数**

```particle call [device_name] [function] [arg]```

**获取设备变量**

```particle get [device_name] [variable]```

**设置新设备**

```particle setup```

# SYNOPSIS

**particle** [_options_] _command_ [_args_]

# PARAMETERS

**login**
> 向 Particle Cloud 进行身份验证。

**list**
> 列出已认领的设备。

**flash**
> 向设备刷写固件。

**compile**
> 编译项目。

**serial**
> 串口相关命令。

**call**
> 调用设备函数。

**get**
> 获取设备变量。

**setup**
> 设置新设备。

**subscribe**
> 订阅事件。

**publish**
> 发布事件。

**webhook**
> 管理 webhook。

# DESCRIPTION

**particle** 用于控制 Particle IoT 设备。它管理设备固件、云函数和变量。

设备包括 Photon、Argon、Boron 和 Electron 开发板。借助云连接可以实现远程管理。

编译可以在本地完成，也可以在 Particle Cloud 完成。刷写可以通过 OTA 或 USB 发送固件。

函数和变量对外暴露设备能力。事件则支持设备之间的发布/订阅消息传递。

串口监视可以查看设备的调试输出。在开发和故障排查时很有用。

# CAVEATS

需要 Particle Cloud 账户。部分功能要求设备在线。OTA 刷写需要稳定的连接。

# HISTORY

**Particle**（前身为 Spark）于 **2012 年**通过 Kickstarter 众筹创立。该 CLI 为其 IoT 平台和设备生态提供开发者工具。

# SEE ALSO

[arduino-cli](/man/arduino-cli)(1), [platformio](/man/platformio)(1), [esptool](/man/esptool)(1)
