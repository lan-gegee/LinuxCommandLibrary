# TAGLINE

终端日历应用

# TLDR

**显示日历**

```khal```

**列出事件**

```khal list```

**添加事件**（START END SUMMARY）

```khal new [2024-01-15] [10:00] [11:00] [Meeting]```

**交互式添加事件**

```khal new -i```

**搜索事件**

```khal search [keyword]```

**交互式 TUI**

```khal interactive```

**导入 ICS 文件**

```khal import [event.ics]```

**显示某个日期范围内的事件**

```khal list [2024-01-15] [7d]```

# SYNOPSIS

**khal** [_options_] _command_

# PARAMETERS

**list** [_START_] [_END_|_DELTA_]
> 列出日期范围内的事件。

**at** _DATETIME_
> 显示特定日期时间的事件。

**calendar** [_START_] [_END_]
> 显示带事件的类 cal 日历视图。

**new** _START_ [_END_|_DELTA_] [_TIMEZONE_] _SUMMARY_ [:: _DESCRIPTION_]
> 创建新事件。使用 **-i** 进行交互式输入。

**search** _STRING_
> 搜索与给定字符串匹配的事件。

**edit** _STRING_
> 交互式编辑或删除匹配的事件。

**import** _FILE_
> 导入 ICS 文件。

**printcalendars**
> 列出已配置的日历。

**printformats**
> 显示日期/时间格式示例。

**configure**
> 运行初始配置向导。

**-a** _CALENDAR_ / **-d** _CALENDAR_
> 包含（**-a**）或排除（**-d**）某个日历。

**--help**
> 显示帮助信息。

# DESCRIPTION

**khal** 是一款终端日历应用。它通过 vdirsyncer 读写 CalDAV 日历。

该工具同时提供命令行和交互式界面，支持多个日历和重复事件。

# CAVEATS

同步依赖 vdirsyncer。基于 Python 实现。需要配置文件。

# HISTORY

khal 的设计目标是通过 vdirsyncer 生态系统实现兼容 CalDAV 的终端日历客户端。

# INSTALL

```dnf: sudo dnf install khal```

```pacman: sudo pacman -S khal```

```apk: sudo apk add khal```

```brew: brew install khal```

```nix: nix profile install nixpkgs#khal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vdirsyncer](/man/vdirsyncer)(1), [todoman](/man/todoman)(1), [calcurse](/man/calcurse)(1)
