# TAGLINE

用户 cron 表编辑器

# TLDR

**编辑** crontab

```crontab -e```

**列出** cron 任务

```crontab -l```

**删除** crontab

```crontab -r```

**编辑**指定用户的 crontab

```sudo crontab -e -u [username]```

# SYNOPSIS

**crontab** [_options_]

# DESCRIPTION

**crontab** 为用户管理计划任务。它提供编辑、列出和删除 cron 表的接口；cron 表包含要在指定日期和时间执行的命令。cron 守护进程读取这些表，并在计划的时间点执行任务。

每个用户都可以拥有自己的 crontab 文件，从而无需 root 权限即可进行用户级的任务调度。crontab 命令提供了编辑这些文件的安全途径，会进行语法校验并通知 cron 守护进程发生变更。任务可以安排在特定时间、固定间隔或特殊事件（如系统启动时）运行。

# PARAMETERS

**-e**
> 编辑 crontab

**-l**
> 列出 crontab

**-r**
> 删除 crontab

**-u** _user_
> 指定用户

**-i**
> 交互模式（删除前提示确认）

# CRONTAB FORMAT

```
* * * * * command
│ │ │ │ │
│ │ │ │ └── Day of week (0-7, Sunday = 0 or 7)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
```

# SPECIAL CHARACTERS

***** - 任意值
**,** - 列表（如 1,3,5）
**-** - 范围（如 1-5）
**/** - 步长（如 */5 = 每 5 个单位）

# SPECIAL STRINGS

**@reboot** - 启动时运行
**@yearly** / **@annually** - 每年一次（0 0 1 1 *）
**@monthly** - 每月一次（0 0 1 * *）
**@weekly** - 每周一次（0 0 * * 0）
**@daily** / **@midnight** - 每天一次（0 0 * * *）
**@hourly** - 每小时一次（0 * * * *）

# CONFIGURATION

**/var/spool/cron/crontabs/[username]**
> 用户的 crontab 文件（位置因系统而异）。应通过 crontab -e 编辑，不要直接修改。

# CAVEATS

环境变量有限。除非重定向输出或发送邮件，否则没有任何输出。时间采用服务器时区。需要 cron 守护进程处于运行状态。系统关机期间任务不会运行。语法错误会被静默忽略。请使用绝对路径。可检查 /var/log/cron 或 /var/log/syslog 排查错误。

# HISTORY

**cron** 随 **Version 7 Unix**（1979 年）发布。**crontab** 接口随后被引入，使用户无需直接编辑文件即可进行任务调度。

# INSTALL

```apt: sudo apt install cron```

```dnf: sudo dnf install cronie```

```pacman: sudo pacman -S cronie```

```apk: sudo apk add cronie```

```zypper: sudo zypper install cron```

```nix: nix profile install nixpkgs#cron```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cron](/man/cron)(8), [at](/man/at)(1)
