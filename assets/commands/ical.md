# TAGLINE

处理 iCalendar 文件的命令行工具

# TLDR

**显示日历**

```ical [calendar.ics]```

**列出事件**

```ical -l [calendar.ics]```

**显示今天的事件**

```ical -t [calendar.ics]```

**导出为其他格式**

```ical -o [output.txt] [calendar.ics]```

# SYNOPSIS

**ical** [_options_] [_file_]

# PARAMETERS

**-l**
> 列出事件。

**-t**
> 显示今天的事件。

**-o** _file_
> 输出到文件。

# DESCRIPTION

**ical** 是一款处理 iCalendar（.ics）文件的命令行工具。它可以显示、解析和操作大多数日历应用所使用的标准 iCalendar 格式的日历数据。

# INSTALL

```apt: sudo apt install itools```

```nix: nix profile install nixpkgs#itools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[calcurse](/man/calcurse)(1), [khal](/man/khal)(1), [remind](/man/remind)(1)
