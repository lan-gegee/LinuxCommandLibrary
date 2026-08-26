# TAGLINE

TUI 日历与任务管理器

# TLDR

**启动**日历 TUI

```calcure```

**从指定日期**开始

```calcure --date [2024-01-15]```

**导入** iCal 文件中的事件

```calcure --import [path/to/file.ics]```

# SYNOPSIS

**calcure** [_options_]

# PARAMETERS

**--date** _DATE_
> 从指定日期开始（YYYY-MM-DD）。

**--import** _FILE_
> 从 iCal（.ics）文件导入事件。

**--config** _FILE_
> 使用自定义配置文件。

**-p**, **--privacy**
> 以隐私模式启动（隐藏事件详情）。

# DESCRIPTION

**calcure** 是一款基于终端的现代 TUI 日历和任务管理器。它以月历视图展示日程并配带任务列表，支持创建事件、周期性事件，以及带有优先级和截止日期的任务管理。

界面提供类 vim 的导航键位，支持按颜色区分的类别、多个日历以及 iCal 导入/导出。事件和任务存储在本地，可通过兼容 iCal 的服务同步。

# CONFIGURATION

配置存储在 **~/.config/calcure/config.ini**。选项包括配色主题、键位、默认视图、日历数据路径和隐私设置。数据目录默认为 **~/.config/calcure/**。

# CAVEATS

不提供内置的日历同步——CalDAV 或 Google Calendar 集成需要借助外部工具。对周期性事件的支持可能无法覆盖所有 iCal 重复规则。

# HISTORY

**calcure** 的定位是 **calcurse** 等终端日历工具的现代、美观替代品。它用 **Python** 编写，注重简洁的用户界面和最少的依赖。

# INSTALL

```nix: nix profile install nixpkgs#calcure```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[calcurse](/man/calcurse)(1), [cal](/man/cal)(1), [taskwarrior](/man/taskwarrior)(1)
