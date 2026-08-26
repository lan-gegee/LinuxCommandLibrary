# TAGLINE

基于时间的任务调度守护进程

# TLDR

**编辑 crontab**

```crontab -e```

**列出 cron 任务**

```crontab -l```

**删除 crontab**

```crontab -r```

**编辑其他用户的 crontab**

```sudo crontab -u [user] -e```

**从文件安装 crontab**

```crontab [crontab.txt]```

# SYNOPSIS

**crontab** [_options_] [_file_]

**cron** [_options_]

# DESCRIPTION

**cron** 是负责执行计划任务的守护进程。**crontab** 用于管理各用户的 cron 表。二者配合提供基于时间的任务调度能力，可用于自动化系统维护、备份、日志轮转以及各种周期性任务。

cron 守护进程在系统启动时开始运行并常驻内存，每分钟唤醒一次，检查所有 crontab 文件中有无需要执行的任务。每个用户都可以拥有自己的 crontab 文件，同时系统也维护着用于全系统维护任务的 crontab。任务在后台无需用户交互即可运行，这使 cron 成为 Unix/Linux 系统管理不可或缺的工具。

# CRONTAB OPTIONS

**-e**
> 编辑 crontab

**-l**
> 列出 crontab

**-r**
> 删除 crontab

**-u** _user_
> 操作指定用户的 crontab（需要 root）

**-i**
> 删除前提示确认

# CRON DAEMON OPTIONS

**-n**
> 在前台运行

**-m** _command_
> 邮件命令（或用 "off" 禁用）

**-s**
> 记录日志到 syslog

**-p**
> 接受任意用户的 crontab

# CRONTAB SYNTAX

```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, Sun=0 or 7)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

# SPECIAL STRINGS

**@reboot**: 启动时运行

**@hourly**: 0 * * * *

**@daily**: 0 0 * * *

**@weekly**: 0 0 * * 0

**@monthly**: 0 0 1 * *

**@yearly**: 0 0 1 1 *

# CONFIGURATION

**/etc/crontab**
> 全系统的 crontab 文件，额外多出一个用户字段，可用于以特定用户身份运行任务。

**/etc/cron.d/**
> 存放系统 crontab 文件的目录，格式与 /etc/crontab 相同。

**/var/spool/cron/**
> 存放各用户 crontab 文件的目录，由 crontab 命令管理。

# CAVEATS

任务在受限的环境变量下运行。请在 crontab 中显式设置 PATH。除非重定向，输出会以邮件形式发给用户。使用 MAILTO="" 可禁用邮件通知。

# INSTALL

```apt: sudo apt install cron```

```zypper: sudo zypper install cron```

```nix: nix profile install nixpkgs#cron```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crontab](/man/crontab)(5), [at](/man/at)(1)
