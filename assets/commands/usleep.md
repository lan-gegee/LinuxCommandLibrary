# TAGLINE

按微秒暂停执行

# TLDR

**休眠若干微秒**

```usleep [1000000]```

**休眠 100ms**

```usleep [100000]```

**休眠 1ms**

```usleep [1000]```

# SYNOPSIS

**usleep** _microseconds_

# PARAMETERS

_microseconds_
> 要休眠的时间。

# DESCRIPTION

**usleep** 让程序暂停指定的微秒数（百万分之一秒）。它的计时粒度比标准 **sleep** 命令更细——后者传统上只接受整数秒。

该命令只接受一个参数，表示要暂停的微秒数。例如 usleep 500000 暂停半秒钟，usleep 1000 暂停一毫秒。

在现代 Linux 系统上，usleep 已经基本过时，因为 GNU **sleep** 支持小数形式的秒数（例如 sleep 0.5）。usleep 命令历史上由 initscripts 软件包提供，并不是在所有发行版上都可用。

# CAVEATS

在许多系统上已被弃用。请改用 sleep。并非所有发行版都有这个命令。

# HISTORY

**usleep** 由 initscripts 软件包提供，用于实现微秒级休眠。现代的 sleep 已支持小数秒。

# INSTALL

```pacman: sudo pacman -S usleep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sleep](/man/sleep)(1), [nanosleep](/man/nanosleep)(2)
