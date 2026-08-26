# TAGLINE

登录失败跟踪与管理

# TLDR

**显示失败**记录

```faillog```

**查看某个用户的**失败记录

```faillog -u [username]```

**设置失败上限**

```faillog -m [5] -u [username]```

**重置失败计数**

```faillog -r -u [username]```

**设置锁定时长**

```faillog -l [600] -u [username]```

# SYNOPSIS

**faillog** [_options_]

# PARAMETERS

**-a**, **--all**
> 显示所有存在失败记录的用户。

**-u** _USER_, **--user** _USER_
> 指定要查询或修改的用户。

**-m** _MAX_, **--maximum** _MAX_
> 设置触发锁定前的最大失败次数。

**-r**, **--reset**
> 重置失败计数。

**-l** _SECONDS_, **--lock-time** _SECONDS_
> 设置锁定持续时间。

**-t** _DAYS_, **--time** _DAYS_
> 显示最近 N 天内的失败记录。

**--help**
> 显示帮助信息。

# CONFIGURATION

**/var/log/faillog**
> 登录失败记录的二进制数据库，跟踪失败尝试和锁定状态。

# DESCRIPTION

**faillog** 显示和管理来自 /var/log/faillog 的登录失败记录。它跟踪失败的登录尝试，可在达到阈值后强制锁定账户。

管理员使用 faillog 监控可疑的登录活动、设置账户锁定前的失败上限，并在合法用户被误锁后重置计数器。该数据库在重启后依然保留。

faillog 与 PAM 集成，可基于失败的身份验证尝试自动锁定账户。

# CAVEATS

修改操作需要 root 权限。依赖 PAM 配置。并非所有系统都使用 faillog 数据库。可能已被 pam_tally2 取代。

# HISTORY

faillog 是 **shadow-utils** 软件包的一部分，自早期 Linux 发行版起就提供登录失败跟踪功能。它比基于 PAM 的现代记账机制出现得更早，但出于兼容性考虑仍然可用。

# INSTALL

```apk: sudo apk add shadow-login```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lastlog](/man/lastlog)(1), [pam_tally2](/man/pam_tally2)(8), [login](/man/login)(1)

# RESOURCES

```[Source code](https://github.com/shadow-maint/shadow)```

<!-- verified: 2026-07-15 -->
