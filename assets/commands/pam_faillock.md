# TAGLINE

在多次认证失败后拒绝访问的 PAM 模块

# TLDR

**显示失败的登录尝试**

```faillock --user [username]```

**重置失败计数**

```faillock --user [username] --reset```

**显示所有用户的状态**

```faillock```

**配置锁定策略（在 pam 文件中）**

```auth required pam_faillock.so deny=5 unlock_time=900```

# SYNOPSIS

**faillock** [_options_]

# PARAMETERS

**--user** _name_
> 指定用户。

**--reset**
> 重置失败计数。

**--dir** _path_
> 计数记录目录。

# DESCRIPTION

**pam_faillock** 是一个 PAM 模块，在多次认证失败后拒绝访问。它通过临时锁定账户提供暴力破解防护。

faillock 命令可查询和重置失败记录。

# PAM CONFIGURATION

```
# /etc/pam.d/system-auth
auth     required  pam_faillock.so preauth silent deny=5 unlock_time=900
auth     required  pam_unix.so
auth     required  pam_faillock.so authfail deny=5 unlock_time=900

account  required  pam_faillock.so
```

# PARAMETERS

```
deny=N        - Lock after N failures
unlock_time=S - Unlock after S seconds
fail_interval - Time window for failures
even_deny_root - Also lock root
```

# CAVEATS

可能把正当用户锁在外面。锁定 root 很危险。请仔细测试配置。

# HISTORY

在现代 Linux 发行版中，pam_faillock 取代了 pam_tally2，用于跟踪和执行登录失败策略。

# SEE ALSO

[pam](/man/pam)(8), [faillock](/man/faillock)(8), [pam.d](/man/pam.d)(5)
