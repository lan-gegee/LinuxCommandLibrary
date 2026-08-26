# TAGLINE

跟踪登录尝试次数

# TLDR

**启用登录尝试跟踪**

```auth required pam_tally2.so deny=5 unlock_time=900```

**查看用户的计数**

```pam_tally2 --user=[username]```

**重置用户的计数**

```pam_tally2 --user=[username] --reset```

**重置所有计数**

```pam_tally2 --reset```

# SYNOPSIS

**pam_tally2** [_options_]

# PARAMETERS

**deny=**_N_
> 连续失败 N 次后锁定账户。

**unlock_time=**_SECONDS_
> 锁定的账户在此秒数后自动解锁。

**magic_root**
> 对 uid 0 发起的尝试不增加计数器。

**even_deny_root**
> 对 root 也应用拒绝策略。

**root_unlock_time=**_SECONDS_
> root 的解锁时间（隐含 **even_deny_root**）。

**no_lock_time**
> 不对反复快速尝试施加默认锁定时长。

**lock_time=**_SECONDS_
> 失败后到下一次提示之间暂停这么多秒。

**file=**_PATH_
> 计数数据库的路径（默认 `/var/log/tallylog`）。

**audit**
> 将每个操作的详细信息写入审计子系统。

**silent**, **no_log_info**
> 降低 syslog 详细程度。

**--user** _NAME_
> 将 CLI 操作限定为单个用户。

**--reset**[=_N_]
> 重置计数器（可选重置为 _N_ 而不是零）。

**--quiet**
> 用户没有计数记录时不输出内容。

# DESCRIPTION

**pam_tally2** 跟踪登录尝试次数。失败次数达到阈值后锁定账户。

该模块用于防范暴力破解攻击。是 pam_tally 的后继者。

# CAVEATS

**已弃用**：已在 Linux-PAM 1.5.0（2020 年）中移除。现代发行版（RHEL 9+、Fedora 33+、Debian 12+）只附带 **pam_faillock**。计数数据库 `/var/log/tallylog` 与旧的 `pam_tally` 共享，与 pam_faillock 在 `/var/run/faillock/` 下按用户存储的文件不兼容。

# HISTORY

pam_tally2 取代了 pam_tally，提供了**改进的登录跟踪**与锁定功能。

# SEE ALSO

[pam](/man/pam)(8), [pam_faillock](/man/pam_faillock)(8)
