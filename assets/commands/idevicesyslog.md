# TAGLINE

从 iOS 设备实时传输系统日志

# TLDR

从所连接设备**实时查看系统日志**

```idevicesyslog```

**仅包含**指定进程的消息（以竖线分隔）

```idevicesyslog -p [Safari|WebKit]```

按 UDID **指定目标设备**

```idevicesyslog -u [udid]```

**只打印**包含某模式的行

```idevicesyslog -m "[error]"```

**排除进程**（以竖线分隔）

```idevicesyslog -e "[SpringBoard|backboardd]"```

**通过网络**而非 USB 传输

```idevicesyslog -n```

将输出**保存到文件**

```idevicesyslog -o [device.log]```

# SYNOPSIS

**idevicesyslog** [_options_]

**idevicesyslog** **pidlist**

**idevicesyslog** **archive** _PATH_ [_options_]

# PARAMETERS

**-u**, **--udid** _UDID_
> 按 UDID 指定目标设备。

**-n**, **--network**
> 连接网络设备而非 USB 设备。

**-p**, **--process** _PROCESS_
> 只包含来自给定进程名的消息（以 **|** 分隔）。

**-e**, **--exclude** _PROCESS_
> 排除来自给定进程名的消息（以 **|** 分隔）。

**-m**, **--match** _STRING_
> 只打印包含 _STRING_ 的消息。

**-M**, **--unmatch** _STRING_
> 只打印**不**包含 _STRING_ 的消息。

**-t**, **--trigger** _STRING_
> 看到包含 _STRING_ 的消息时开始记录日志。

**-T**, **--untrigger** _STRING_
> 看到包含 _STRING_ 的消息时停止记录日志。

**-k**, **--kernel**, **-K**, **--no-kernel**
> 包含或排除内核消息。

**-o**, **--output** _FILE_
> 除终端外，还将日志流写入 _FILE_。

**-x**, **--exit**
> 设备断开连接时退出。

**--no-colors**, **--colors**
> 禁用或强制 ANSI 彩色输出。

**-q**, **--quiet**
> 抑制横幅/状态输出。

**-d**, **--debug**
> 启用调试输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**idevicesyslog** 实时传输 iOS 设备的系统日志。它提供对设备日志的实时访问，便于调试。

该工具可显示所有进程的消息或经过过滤的子集。它是 iOS 应用开发和调试的必备工具。

# CAVEATS

属于 libimobiledevice。持续输出流。iOS 16+ 可能需要开启开发者模式。

# HISTORY

idevicesyslog 是 **libimobiledevice** 的组成部分，用于 iOS 日志流式传输。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idevice_id](/man/idevice_id)(1), [ideviceinfo](/man/ideviceinfo)(1), [idevicepair](/man/idevicepair)(1), [adb](/man/adb)(1)
