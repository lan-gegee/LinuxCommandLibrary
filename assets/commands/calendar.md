# TAGLINE

显示日历文件中的提醒

# TLDR

**显示今天和明天的提醒**

```calendar```

**显示接下来 N 天的提醒**

```calendar -A [7]```

**回看 N 天内**的提醒

```calendar -B [3]```

**使用指定的日历文件**

```calendar -f [path/to/calendar]```

**假装今天是某个日期**

```calendar -t [1225]```

为系统上**所有人处理提醒**（需 root，会发送邮件）

```calendar -a```

**使用指定的日历目录**

```calendar -d [path/to/calendar_dir]```

# SYNOPSIS

**calendar** [_-A days_] [_-B days_] [_-a_] [_-f calendarfile_] [_-d calendardir_]

# PARAMETERS

**-A** _days_
> 向前查看指定的天数（默认：1，即今天和明天）。

**-B** _days_
> 向后查看指定的天数。

**-a**
> 为所有用户处理日历文件并发送邮件（仅 root）。

**-f** _file_
> 使用指定文件代替 ~/.calendar/calendar。

**-d** _dir_
> 使用指定目录存放日历文件。

**-t** _date_
> 假装今天是指定日期（格式：[[[cc]yy]mm]dd）。

**-w**
> 输出星期几的名称。

# DESCRIPTION

**calendar** 是一款传统 Unix 工具，用于显示日历文件中的提醒。它从 **~/.calendar/calendar**（或指定文件）读取条目，并显示与今天日期匹配的内容，也可选择显示即将到来的日期。

日历文件每行一条提醒，格式简单：日期后跟一个制表符和提醒文本。日期可用多种格式表示，如 "Jan 1"、"1/1"、"*/15"（每月）以及星期名称。程序还能理解节假日和特殊日期表达式。

该工具传统上用于系统级公告和个人提醒。root 用户以 **-a** 运行时，它会处理所有用户的日历文件并发送邮件通知。许多系统预装了包含历史日期、节假日和天文事件的日历文件。

常见日历文件位置包括 **/usr/share/calendar/** 下的系统日历，其中含有节假日、历史、音乐等类别的文件。用户可以在个人日历中用 **#include** 指令引用这些系统文件。

# CAVEATS

BSD 与其他实现之间的日期格式有所差异。-a 标志（向所有用户发邮件）需要 root 权限。某些实现的日期解析能力有限。邮件功能依赖可正常工作的邮件系统。

# HISTORY

**calendar** 命令起源于 1970 年代贝尔实验室的早期 Unix 系统。它是最早的一批基于时间的工具之一，在简单的提醒功能上早于 cron 出现。该程序自早期起就包含在 BSD 系统中，如今仍是许多类 Unix 操作系统的一部分，不过随着现代日历应用的普及，其使用已有所减少。

# INSTALL

```apt: sudo apt install calendar```

```dnf: sudo dnf install calendar```

```apk: sudo apk add outils-calendar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cal](/man/cal)(1), [date](/man/date)(1), [at](/man/at)(1), [cron](/man/cron)(8), [remind](/man/remind)(1)
