# TAGLINE

Google Calendar 的命令行界面

# TLDR

**显示未来 5 天的日程**

```gcalcli agenda```

**列出日历**

```gcalcli list```

**显示周视图**

```gcalcli calw```

**显示月视图**

```gcalcli calm```

添加带详细信息的**日程**

```gcalcli add --title "[title]" --when "[tomorrow 2pm]" --duration [60] --where "[location]"```

用自然语言**快速添加日程**

```gcalcli quick "[Meeting tomorrow at 3pm]"```

**搜索日程**

```gcalcli search "[query]"```

从 ICS 文件**导入日程**

```gcalcli import [path/to/events.ics]```

**删除日程**

```gcalcli delete "[event title]"```

# SYNOPSIS

**gcalcli** [_options_] _command_ [_args_]

# SUBCOMMANDS

**agenda**
> 显示即将到来的日程。

**list**
> 列出日历。

**calw**
> 周视图。

**calm**
> 月视图。

**add**
> 添加日程。

**quick**
> 快速添加日程。

**search**
> 搜索日程。

**delete**
> 删除日程。

**edit**
> 编辑日程。

**import**
> 从 ics/vcal 文件导入日程。

**remind**
> 若日程在指定时间内发生则执行命令。

# PARAMETERS

**--calendar** _name_
> 指定日历。

**--title** _text_
> 日程标题。

**--when** _time_
> 日程开始时间。

**--duration** _minutes_
> 日程持续时间。

**--where** _location_
> 日程地点。

**--lineart** _type_
> 线框风格：fancy、unicode 或 ascii。

**--nocache**
> 执行命令时不使用缓存。

**--locale** _LOCALE_
> 设置日期/时间输出的区域设置。

**--refresh**
> 删除并刷新缓存数据。

# CONFIGURATION

**~/.gcalclirc**
> 配置文件，每行写一条常用 CLI 选项。也可用 @file 语法从任意文件加载选项。

**~/.gcalcli_oauth**
> 访问 Google Calendar API 所需的 OAuth 2.0 凭据。

# DESCRIPTION

**gcalcli** 是 Google Calendar 的命令行界面，无需打开浏览器即可在终端管理日历。它通过 OAuth 2.0 进行身份验证，提供对 Google Calendar 数据的完整访问。

该工具既支持日程和日历显示等查看操作，也支持创建、编辑和删除日程等修改操作。快速添加功能允许用自然语言创建日程，而结构化的 add 命令则能精确控制日程细节。

gcalcli 特别适合以终端为核心的工作流、自动化脚本以及与其他命令行工具集成。它可以多种格式显示日历数据，并同时操作多个日历。

# INSTALL

```zypper: sudo zypper install gcalcli```

```brew: brew install gcalcli```

```nix: nix profile install nixpkgs#gcalcli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcal](/man/gcal)(1), [calcurse](/man/calcurse)(1)
