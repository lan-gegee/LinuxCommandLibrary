# TAGLINE

显示 Android 系统和应用日志

# TLDR

**查看所有日志**

```adb logcat```

**按标签过滤**

```adb logcat -s [TAG]```

**按优先级过滤**

```adb logcat "*:[E]"```

**清空日志缓冲区**

```adb logcat -c```

**输出到文件**

```adb logcat > [logfile.txt]```

**显示特定缓冲区**

```adb logcat -b [main,system,crash]```

**设置输出格式**

```adb logcat -v [time]```

# SYNOPSIS

**logcat** [_options_] [_filter_...]

# DESCRIPTION

**logcat** 显示 Android 系统和应用日志。它通过 adb 连接 Android 设备或模拟器，流式输出日志消息以便调试和分析。

该工具支持按标签、优先级级别和缓冲区类型过滤，是 Android 开发与故障排查的必备工具。

# PARAMETERS

**-s** _tag_
> 过滤到指定的标签。

**-b** _buffer_
> 日志缓冲区（main、system、radio、events、crash）。

**-c**
> 清空日志缓冲区。

**-d**
> 转储日志后退出。

**-f** _file_
> 写入文件。

**-v** _format_
> 输出格式（brief、time、long、color）。

**-t** _count_
> 打印最后 N 行。

**-g**
> 获取缓冲区大小。

**--pid** _pid_
> 按进程 ID 过滤。

# PRIORITY LEVELS

**V**: Verbose（详细）
**D**: Debug（调试）
**I**: Info（信息）
**W**: Warning（警告）
**E**: Error（错误）
**F**: Fatal（致命）

# CAVEATS

需要 adb 连接。缓冲区大小有限。旧日志在重启后被清除。部分日志需要 root 权限。

# HISTORY

**logcat** 是 **Google** 开发的 **Android SDK** 的组成部分。自 **2008 年** Android 发布以来，它一直是主要的 Android 日志工具，并逐步支持更多缓冲区和过滤选项。

# SEE ALSO

[adb](/man/adb)(1), [dmesg](/man/dmesg)(1), [journalctl](/man/journalctl)(1)
