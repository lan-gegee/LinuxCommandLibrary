# TAGLINE

防止系统睡眠的跨平台实用工具

# TLDR

**交互式地让系统保持唤醒**

```keep-alive```

**在指定时长内保持系统唤醒**

```keep-alive -d [2h30m]```

**让系统保持唤醒到指定时间**

```keep-alive -c [22:00]```

**保持系统唤醒并为聊天应用模拟活动状态**

```keep-alive -a```

# SYNOPSIS

**keep-alive** [_options_]

# PARAMETERS

**-d**, **--duration** _duration_
> 保持系统唤醒的时长（如 "2h30m"，或以分钟计的 "150"）。

**-c**, **--clock** _time_
> 让系统保持唤醒到指定时间（如 "22:00" 或 "10:00PM"）。

**-a**, **--active**
> 模拟活动，让聊天应用（Slack/Teams）持续显示在线状态。

**-l**, **--log**
> 启用写入 debug.log 文件的日志。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**keep-alive** 是一个轻量级跨平台实用工具，可以阻止系统睡眠、调暗显示器或暂停后台进程。它确保下载、构建和其他长时间任务不被中断。

该工具可在 **Linux**、**macOS** 和 **Windows** 上工作，使用操作系统特定的 API 抑制睡眠。在 macOS 上使用 caffeinate，在 Linux 上使用 systemd-inhibit 或 xset，在 Windows 上使用 SetThreadExecutionState API。不带标志运行时，它会提供一个可选择时长的交互式 TUI。

# CAVEATS

根据操作系统的不同，可能需要相应的权限。无法阻止用户手动触发的睡眠。程序退出时会恢复电源设置。

# SEE ALSO

[caffeinate](/man/caffeinate)(8), [systemd-inhibit](/man/systemd-inhibit)(1), [xset](/man/xset)(1)
