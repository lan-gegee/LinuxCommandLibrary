# TAGLINE

HDMI-CEC 设备控制客户端

# TLDR

**列出**所有 CEC 适配器

```cec-client -l```

启动**交互式** CEC 会话

```sudo cec-client```

设置**屏幕显示（OSD）**名称

```sudo cec-client -o [name]```

**发送单条命令**

```echo [on 0] | sudo cec-client -s```

让设备进入**待机**状态（交互模式）

```standby [0]```

**打开**设备（交互模式）

```on [0]```

# SYNOPSIS

**cec-client** [_options_]

# DESCRIPTION

**cec-client** 基于 libCEC 库管理通过 HDMI 的 CEC（Consumer Electronics Control，消费电子控制）连接。CEC 是 HDMI 规范的一项功能，允许通过 HDMI 连接的设备相互控制，例如在媒体播放器启动时打开电视，或用单个遥控器控制多个设备的音量。

该工具既支持交互式控制，也支持脚本化控制 CEC 设备。在交互模式下，你可以向 HDMI 总线上的任意设备发送 `on`、`standby` 和 `tx`（原始 CEC 帧）等命令。对于自动化场景，`-s` 标志会处理来自 stdin 的单条命令然后退出，适合在脚本和家庭自动化方案中使用。

设备通过逻辑地址（0-15）寻址，其中 0 通常是电视，1 是录制设备，5 是音频系统。

# PARAMETERS

**-l, --list-devices**
> 列出可用的 CEC 适配器

**-o, --osd-name** _name_
> 设置屏幕显示（OSD）名称

**-s, --single-command**
> 执行来自 stdin 的单条命令后退出

**-d** _device_
> 使用指定的 CEC 设备

# INTERACTIVE COMMANDS

**on** _address_
> 打开位于指定地址的设备

**standby** _address_
> 让设备进入待机状态

**tx** _bytes_
> 发送原始 CEC 帧

**scan**
> 扫描 CEC 总线上的设备

# CAVEATS

需要 USB CEC 适配器（如 Pulse-Eight）。设备地址为 0-15，其中 0 通常是电视。访问设备需要 root 权限。

# INSTALL

```apt: sudo apt install cec-utils```

```apk: sudo apk add libcec-tools```

```zypper: sudo zypper install cec-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cec-ctl](/man/cec-ctl)(1)

# RESOURCES

```[Source code](https://github.com/Pulse-Eight/libcec)```

<!-- verified: 2026-06-22 -->
