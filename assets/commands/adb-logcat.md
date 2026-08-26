# TAGLINE

Android 系统日志查看器

# TLDR

**查看**设备日志

```adb logcat```

按优先级**过滤**（Verbose、Debug、Info、Warn、Error、Fatal）

```adb logcat *:[E]```

按**标签**和优先级过滤

```adb logcat [ActivityManager]:I *:S```

**清空**日志缓冲区

```adb logcat -c```

查看来自**特定缓冲区**的日志

```adb logcat -b [main|system|crash|events]```

将日志保存到**文件**

```adb logcat -f [logfile.txt]```

# SYNOPSIS

**adb logcat** [_-v format_] [_-b buffer_] [_-c_] [_-f file_] [_filter-spec_]

# DESCRIPTION

**adb logcat** 实时显示 Android 系统日志。它显示来自系统、应用和各种 Android 组件的日志消息。输出包含时间戳、进程 ID、线程 ID、优先级、标签和消息。

过滤表达式允许你根据标签名和最低优先级选择要显示的日志消息。多个过滤器可以组合成复杂的过滤规则。

# PARAMETERS

**-v** _format_
> 输出格式：brief、process、tag、thread、raw、time、threadtime（默认）、long

**-b** _buffer_
> 日志缓冲区：main、system、radio、events、crash、all

**-c**
> 清空日志缓冲区并退出

**-d**
> 转储日志后退出（不阻塞）

**-f** _file_
> 将输出写入文件

**-g**
> 打印指定日志缓冲区的大小并退出

**-n** _count_
> 设置轮转日志的最大数量（默认 4，需配合 -r）

**-r** _kbytes_
> 每输出 kbytes KB 就轮转一次日志（默认 16，需配合 -f）

**-s**
> 将默认过滤器设为静默（等价于 *:S）

**-e** _regex_
> 只打印匹配正则表达式的行

**--pid=**_pid_
> 只显示指定进程 ID 的日志

# FILTER FORMAT

```tag:priority``` 其中 priority 为：
- **V**：Verbose
- **D**：Debug
- **I**：Info
- **W**：Warning
- **E**：Error
- **F**：Fatal
- **S**：Silent（抑制输出）

# CAVEATS

日志缓冲区大小有限；旧消息会被覆盖。某些系统日志可能需要 root 权限。过量的日志记录会拖慢设备。请使用过滤器减少输出量。

# HISTORY

Logcat 自 **2008** 年 Android SDK 首次发布起就是其一部分。它基于 Linux 内核的 printk 日志系统，但针对 Android 的需求做了调整，增加了基于标签的过滤。

# INSTALL

```apt: sudo apt install adb```

```dnf: sudo dnf install android-tools```

```pacman: sudo pacman -S android-tools```

```apk: sudo apk add android-tools-adb```

```zypper: sudo zypper install android-tools```

```nix: nix profile install nixpkgs#android-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [dmesg](/man/dmesg)(1), [journalctl](/man/journalctl)(1)
