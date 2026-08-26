# TAGLINE

解析并显示块 I/O 跟踪数据

# TLDR

**解析并显示某设备的 blktrace 输出**

```blkparse [sda]```

**解析多个设备**

```blkparse [sda] [sdb]```

**从标准输入解析**（与 blktrace 配合的实时模式）

```blktrace -d [/dev/sda] -o - | blkparse -i -```

**输出到文件**

```blkparse [sda] -o [output.txt]```

**显示指定的输出字段**

```blkparse -f "%D %a %S %n\n" [sda]```

**以安静模式解析**（仅摘要）

```blkparse -q [sda]```

# SYNOPSIS

**blkparse** [_options_] [_device_...]

# DESCRIPTION

**blkparse** 对 **blktrace** 记录的事件流产生格式化输出。它合并来自多个 CPU 和设备的事件流，将机器可读的跟踪数据转换为人类可读的格式。

该工具对分析块 I/O 模式、排查存储性能问题以及理解 Linux I/O 调度器如何处理请求至关重要。

# PARAMETERS

**-i** _file_
> 输入文件的基本名（默认 device.blktrace.cpu）；使用 "-" 表示实时标准输入

**-o** _file_
> 输出文件（默认：stdout）

**-D** _dir_
> 将此目录添加到输入文件名之前

**-d** _file_
> 将合并后的二进制事件流转储到 _file_

**-f** _format_
> 适用于所有事件的自定义输出格式字符串

**-F** _typ,format_
> 针对特定事件类型的输出格式字符串

**-q**
> 安静模式；仅在最后打印摘要

**-s**
> 显示按程序（按进程）统计

**-t**
> 跟踪 I/O 计时；显示每个 I/O 的耗时差值

**-w** _span_
> 将输出限制在一个时间窗口内；_end_ 或 _start:end_，单位为纳秒

**-a** _mask_
> 将 _mask_ 加入当前的跟踪动作过滤器

**-A** _hexmask_
> 将跟踪动作过滤器设为 _hexmask_

**-v**
> 更详细的输出

# TRACE ACTIONS

**Q** - 排队（Queued）：已记录排队 I/O 的意图
**I** - 插入（Inserted）：请求已发送至 I/O 调度器
**D** - 下发（Issued）：请求已发送至驱动程序
**C** - 完成（Complete）：请求已完成
**M** - 后端合并（Back merge）：请求与已有请求在尾部合并
**F** - 前端合并（Front merge）：请求在头部合并
**P** - 塞住（Plug）：队列被塞住
**U** - 解塞（Unplug）：队列被解塞

# CAVEATS

需要 **blktrace** 的跟踪数据才能工作。繁忙系统上的跟踪文件可能非常大。运行 blktrace 需要 root 权限。输出可能过于庞杂；可使用格式选项限制字段。

# HISTORY

blkparse 由 **Jens Axboe**、**Alan D. Brunelle** 和 **Nathan Scott** 编写，是 blktrace 工具集的一部分。其开发目的是为 Linux 存储子系统的分析与调试提供详细的 I/O 跟踪能力。

# INSTALL

```apt: sudo apt install blktrace```

```dnf: sudo dnf install blktrace```

```zypper: sudo zypper install blktrace```

```nix: nix profile install nixpkgs#blktrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blktrace](/man/blktrace)(8), [btrace](/man/btrace)(8), [btt](/man/btt)(1), [iostat](/man/iostat)(1)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/linux/kernel/git/axboe/blktrace.git)```

<!-- verified: 2026-06-19 -->
