# TAGLINE

在不连续开机的系统上运行周期性任务

# TLDR

立即**运行** anacron 任务

```sudo anacron -n```

在**前台**运行

```sudo anacron -d```

**测试**运行（不实际执行任务）

```anacron -T```

无视**时间戳**强制运行

```sudo anacron -f```

使用**指定的配置**文件

```sudo anacron -t [/etc/anacrontab]```

# SYNOPSIS

**anacron** [_-s_] [_-f_] [_-n_] [_-d_] [_-t anacrontab_] [_-T_]

# DESCRIPTION

**anacron** 是一个类似 cron 的任务调度器，但它不假设计算机持续开机运行。它非常适合并非全天候开机的笔记本电脑和台式机，即使错过了计划时间也能保证周期性任务得到执行。

与在特定时刻运行任务的 cron 不同，anacron 按周期（每天、每周、每月）运行任务，并记录上次运行日期。如果自上次运行以来某个任务的周期已经过去，就会执行该任务。

# PARAMETERS

**-f**
> 忽略时间戳，强制执行

**-n**
> 立即运行任务，忽略延迟设置

**-d**
> 在前台运行（不作为守护进程）

**-s**
> 串行化任务执行（按顺序）

**-T**
> 仅测试配置文件语法

**-t** _file_
> 使用替代的 anacrontab 文件

**-S** _dir_
> 使用替代的 spool 目录

**-u**
> 仅更新时间戳，不运行任务

# CONFIGURATION

**/etc/anacrontab**
> 定义周期性任务，包括以天为单位的周期、以分钟为单位的延迟、标识符和要执行的命令。

**/var/spool/anacron/**
> 时间戳文件，记录每个任务上次执行的日期。

# CAVEATS

默认以 root 运行；用户级任务需要额外配置。任务的延迟设置会被随机化，以避免资源峰值。不适合对时间敏感的任务。

# HISTORY

**anacron** 由 Christian Schwarz 创建，于 **1998** 年首次发布，旨在解决 cron 不适合非持续开机机器的问题。如今大多数现代 Linux 发行版都将它与传统 cron 一同提供。

# INSTALL

```apt: sudo apt install anacron```

```dnf: sudo dnf install cronie```

```pacman: sudo pacman -S cronie```

```apk: sudo apk add cronie```

```zypper: sudo zypper install cronie```

```nix: nix profile install nixpkgs#cronie```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[cron](/man/cron)(8), [crontab](/man/crontab)(1)
