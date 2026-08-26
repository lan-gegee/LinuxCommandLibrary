# TAGLINE

基于文本的日历与日程安排应用

# TLDR

以**交互模式**启动 calcurse

```calcurse```

输出今天的**约会与事件**

```calcurse -a```

输出**待办清单**

```calcurse -t```

输出**下一个即将到来的约会**

```calcurse -n```

输出**指定日期**的约会

```calcurse -d [MM/DD/YYYY]```

输出**接下来 N 天**的约会

```calcurse -r [7]```

**导入** iCal 文件

```calcurse -i [calendar.ics]```

将数据**导出**为 iCal 格式

```calcurse -x ical > [calendar.ics]```

# SYNOPSIS

**calcurse** [_options_]

# DESCRIPTION

**calcurse** 是一款基于文本的日历和日程应用。它提供基于 curses 的界面来管理约会、待办事项和笔记，并支持 CalDAV 同步。

交互式界面同时显示月历、约会列表和待办列表。

# PARAMETERS

**-a, --appointment**
> 输出今天的约会与事件后退出

**-t, --todo**
> 输出待办清单后退出

**-d** _date_
> 输出指定日期的约会

**-n, --next**
> 输出下一个约会

**-r, --range** _days_
> 输出指定天数范围内的约会

**-i** _file_
> 从文件导入 iCal（.ics）数据

**-x** _format_
> 导出数据（ical 或 pcal 格式）

**-c** _file_
> 使用备用的日历文件

**-D, --directory** _dir_
> 使用备用的数据目录

# SUBCOMMANDS

**calcurse-caldav**
> 与 CalDAV 服务器同步

# CONFIGURATION

**~/.calcurse/conf**
> 主配置文件，包含显示设置、键位绑定和常规选项

# CAVEATS

CalDAV 同步需要在 ~/.calcurse/caldav/config 中进行配置。首次同步应指定初始化模式以解决冲突。

# INSTALL

```apt: sudo apt install calcurse```

```dnf: sudo dnf install calcurse```

```pacman: sudo pacman -S calcurse```

```apk: sudo apk add calcurse```

```zypper: sudo zypper install calcurse```

```brew: brew install calcurse```

```nix: nix profile install nixpkgs#calcurse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cal](/man/cal)(1), [task](/man/task)(1), [remind](/man/remind)(1)
