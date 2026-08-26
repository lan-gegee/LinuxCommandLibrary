# TAGLINE

简单、可自定义的终端番茄钟

# TLDR

**开始默认的 25 分钟工作时段**

```pomo```

**开始 30 分钟的工作时段**

```pomo 30m```

**以自定义休息时长开始工作时段**

```pomo 45m 15m```

**查看效率统计**

```pomo stats```

# SYNOPSIS

**pomo** [_duration_] [_break_duration_]

**pomo** _command_

# PARAMETERS

_duration_
> 工作时段长度（默认：25m）。支持 30m、1h 等格式。

_break_duration_
> 工作时段之后的休息长度（默认：5m）。

**stats**
> 显示效率统计，包括每周图表和热力图。

# DESCRIPTION

**pomo** 是一款基于终端的番茄钟，具有可自定义的工作与休息间隔、实时进度可视化、ASCII 艺术展示以及跨平台桌面通知。它通过每周图表和 GitHub 风格的活动热力图跟踪效率统计。

# HISTORY

**pomo** 由 **Bahaaio** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S pomo```

<!-- packages: 2026-07-22 -->
