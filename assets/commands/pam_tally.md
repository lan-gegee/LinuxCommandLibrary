# TAGLINE

统计登录尝试次数

# TLDR

**启用登录计数（已弃用）**

```auth required pam_tally.so```

**失败若干次后锁定**

```auth required pam_tally.so deny=5```

**重置计数**

```pam_tally --user=[username] --reset```

**查看计数**

```pam_tally --user=[username]```

# SYNOPSIS

**pam_tally.so** [_options_]

# PARAMETERS

**deny=**_N_
> 失败 N 次后锁定。

**unlock_time=**_SECONDS_
> 自动解锁时间。

**per_user**
> 按用户设置。

**--user** _NAME_
> 指定用户。

**--reset**
> 重置计数器。

# DESCRIPTION

**pam_tally** 统计登录尝试次数。失败后锁定账户。

该模块跟踪失败的登录。已弃用，请使用 pam_tally2。

# CAVEATS

已弃用。请改用 pam_tally2。仅存在于旧系统中。

# HISTORY

pam_tally 在 pam_tally2 出现之前提供**登录尝试计数**功能。

# SEE ALSO

[pam](/man/pam)(8), [pam_tally2](/man/pam_tally2)(8), [pam_faillock](/man/pam_faillock)(8)
