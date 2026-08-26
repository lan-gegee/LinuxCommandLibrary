# TAGLINE

控制系统时间和时区

# TLDR

显示当前的**日期和时间**设置

```timedatectl```

直接设置**本地时间**

```timedatectl set-time "2024-01-15 14:30:00"```

列出可用的**时区**

```timedatectl list-timezones```

设置系统**时区**

```timedatectl set-timezone America/New_York```

启用 **NTP 同步**

```timedatectl set-ntp on```

将硬件时钟设为**本地时间**

```timedatectl set-local-rtc 1```

# SYNOPSIS

**timedatectl** [_OPTIONS_] [_COMMAND_]

# DESCRIPTION

**timedatectl** 用于查询和修改系统时钟及其设置。它通过 systemd-timedated 控制系统时间、时区和网络时间同步。

# COMMANDS

**status**
> 显示当前的日期/时间设置（默认命令）

**show**
> 以机器可读格式显示属性

**set-time TIME**
> 设置系统时间（YYYY-MM-DD HH:MM:SS 格式）

**set-timezone ZONE**
> 设置系统时区

**list-timezones**
> 列出可用时区

**set-local-rtc BOOL**
> 控制 RTC 是否使用本地时间（0=UTC，1=本地）

**set-ntp BOOL**
> 启用或禁用 NTP 同步

**timesync-status**
> 显示 systemd-timesyncd 的状态

# PARAMETERS

**--no-pager**
> 不将输出送入分页器

**--no-ask-password**
> 不提示输入密码

**-H, --host**
> 在远程主机上执行操作

**-M, --machine**
> 在容器上执行操作

**-p, --property**
> 显示特定属性

**--value**
> 只显示属性值

# CAVEATS

手动设置时间（set-time）会禁用 NTP 同步。RTC 使用本地时间（set-local-rtc 1）在夏令时切换期间可能给双系统启动带来问题。

# HISTORY

**timedatectl** 是 **systemd** 的一部分，旨在提供统一的时间/日期管理接口，取代 hwclock 和 tzselect 等旧工具。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hwclock](/man/hwclock)(8), [date](/man/date)(1)
