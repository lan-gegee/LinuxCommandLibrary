# TAGLINE

日历与提醒系统

# TLDR

**显示提醒**

```remind [~/.reminders]```

**显示日历**

```remind -c [~/.reminders]```

**显示接下来 N 天**

```remind -c+[7] [~/.reminders]```

**运行守护进程**

```remind -z [~/.reminders]```

**简易日历**

```remind -s [~/.reminders]```

# SYNOPSIS

**remind** [_options_] _filename_ [_date_]

# PARAMETERS

**-c** [_+n_]
> 日历模式（提前 n 天）。

**-s**
> 简易日历。

**-z**
> 守护进程模式。

**-q**
> 安静模式。

**-n**
> 仅显示下一次出现。

**@** _time_
> 在指定时间触发。

# DESCRIPTION

**Remind** 是一个功能完善的日历与提醒程序。它使用脚本语言处理复杂的周期性事件，支持日历输出和守护进程模式。

# REMINDER FILE

```
# ~/.reminders

# Simple reminder
REM Jan 1 MSG Happy New Year!

# Weekly
REM Mon MSG Weekly meeting

# With time
REM Mon AT 9:00 MSG Standup

# Monthly
REM 15 MSG Pay rent

# Advance warning
REM Apr 15 +7 MSG Tax deadline approaching
```

# EXAMPLES

```bash
# Show today's reminders
remind ~/.reminders

# Calendar view
remind -c ~/.reminders

# Next 30 days
remind -c+30 ~/.reminders

# Run in background
remind -z ~/.reminders &

# HTML calendar
remind -pp ~/.reminders | rem2html > cal.html
```

# CONFIGURATION

**~/.reminders**
> 默认的提醒文件，包含使用 Remind 脚本语言编写的 REM 语句，用于定义事件、周期性计划和定时提醒。

# CAVEATS

功能强大的脚本语言有一定学习曲线。通过提醒文件进行配置。可与 wyrd 配合提供 TUI。

# HISTORY

Remind 由 **David F. Skoll** 自 1990 年起编写，是一个灵活的日历/提醒系统。

# INSTALL

```apt: sudo apt install remind```

```dnf: sudo dnf install remind```

```pacman: sudo pacman -S remind```

```apk: sudo apk add remind```

```zypper: sudo zypper install remind```

```brew: brew install remind```

```nix: nix profile install nixpkgs#remind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[calcurse](/man/calcurse)(1), [cal](/man/cal)(1)
