# TAGLINE

报告所有用户或指定用户最近一次的登录情况

# TLDR

显示所有用户最近一次**登录情况**

```lastlog```

显示**特定用户**的 lastlog

```lastlog --user [username]```

显示**早于** N 天的记录

```lastlog --before [7]```

显示**晚于** N 天的记录

```lastlog --time [3]```

# SYNOPSIS

**lastlog** [_options_]

# PARAMETERS

**-u**, **--user** _LOGIN|RANGE_
> 显示指定用户的 lastlog 记录。可以是登录名、数字 UID 或 UID 范围（UID_MIN-UID_MAX）

**-b**, **--before** _DAYS_
> 显示早于 DAYS 天的记录

**-t**, **--time** _DAYS_
> 显示晚于 DAYS 天的记录

**-C**, **--clear**
> 清除某用户的 lastlog 记录（需要 -u）

**-S**, **--set**
> 将某用户的 lastlog 记录设为当前时间（需要 -u）

**-R**, **--root** _CHROOT\_DIR_
> 在 CHROOT_DIR 目录中应用更改并使用其中的配置文件

**-h**, **--help**
> 显示帮助信息并退出

# DESCRIPTION

**lastlog** 通过读取 /var/log/lastlog 来报告所有用户或指定用户最近一次的登录情况。与 last 不同，它每个用户只显示一条记录，即该用户最近一次的登录。

lastlog 文件是按 UID 索引的稀疏文件，因此看起来可能很大，但并不会占用太多磁盘空间。从未登录过的用户显示为 "Never logged in"。

# CAVEATS

lastlog 文件以 UID 为索引；非常大的 UID 可能让该文件显得很大。某些系统可能不维护 lastlog。系统账户通常显示为从未登录。

# HISTORY

lastlog 在类 Unix 系统中已存在数十年，提供了一种快速审计哪些用户近期登录过并找出休眠账户的方法。

# INSTALL

```apk: sudo apk add shadow-login```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[last](/man/last)(1), [lastb](/man/lastb)(1), [faillog](/man/faillog)(8), [who](/man/who)(1), [login](/man/login)(1)
