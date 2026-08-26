# TAGLINE

用于任务调度的 cron 守护进程

# TLDR

在**后台**启动守护进程

```crond```

在**前台**启动守护进程

```crond -n```

将输出发送到 **syslog**

```crond -s```

接受**自定义 crontab**（绕过默认限制）

```crond -p```

从环境继承 **PATH**

```crond -P```

启用**集群**支持

```crond -c```

# SYNOPSIS

**crond** [_OPTIONS_]

# DESCRIPTION

**crond** 是一个守护进程，负责执行 crontab 文件中计划好的命令。它在系统启动时自动运行，并每分钟检查一次 crontab 文件中需要执行的任务。它监控 /var/spool/cron/（用户 crontab）、/etc/crontab（系统级 crontab）和 /etc/cron.d/（系统 cron 任务）。下述选项描述的是 **cronie** 实现，即大多数现代发行版附带的 crond；BusyBox 和 dcron 则提供各自版本的 crond，其选项有重叠但不完全相同。

# PARAMETERS

**-n**
> 在前台运行（对 init 系统有用）

**-s**
> 将任务输出发送到 syslog 而非电子邮件

**-m COMMAND**
> 指定自定义邮件命令，或用 "off" 禁用邮件

**-p**
> 绕过默认限制并接受自定义 crontab

**-P**
> 从环境继承 PATH，而不是设置默认值

**-c**
> 为共享 crontab 启用集群支持

**-h**
> 显示帮助信息

**-V**
> 显示版本号

# CONFIGURATION

**/etc/crontab**
> 由 crond 监控的系统级 crontab 文件。

**/etc/cron.d/**
> 存放其他系统级 crontab 文件的目录。

**/var/spool/cron/**
> 存放用户专属 crontab 文件的目录（每个用户一个）。Debian 的 cron 使用 /var/spool/cron/crontabs/ 代替。

# CAVEATS

任务输出会以电子邮件发送给 crontab 所有者，除非使用 -s 重定向到 syslog 或指定了自定义邮件命令。crontab 文件必须是普通文件、不可执行，且只有所有者可写。三小时以内的本地时间变化（如夏令时）会受到特殊处理。

# HISTORY

**crond** 是 cron 的守护进程组件。cron 是标准的 Unix 任务调度器，自 Version 7 Unix 起投入使用。现代实现包括 Vixie cron 和 cronie。

# INSTALL

```apt: sudo apt install cronie```

```dnf: sudo dnf install cronie```

```pacman: sudo pacman -S cronie```

```apk: sudo apk add cronie```

```zypper: sudo zypper install cronie```

```nix: nix profile install nixpkgs#cronie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crontab](/man/crontab)(1), [crontab](/man/crontab)(5), [anacron](/man/anacron)(8)

# RESOURCES

```[Source code](https://github.com/cronie-crond/cronie)```

<!-- verified: 2026-06-26 -->
