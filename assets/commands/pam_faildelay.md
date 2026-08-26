# TAGLINE

设置认证失败后的延迟

# TLDR

**设置认证延迟**

```auth optional pam_faildelay.so delay=3000000```

**较短延迟**

```auth optional pam_faildelay.so delay=1000000```

# SYNOPSIS

**pam_faildelay.so** [_options_]

# PARAMETERS

**delay=**_MICROSECONDS_
> 延迟时间（微秒）（1000000 = 1 秒）。

# DESCRIPTION

**pam_faildelay** 是一个 PAM 模块，用于设置认证失败后施加的延迟。它会覆盖 `/etc/login.defs` 中的 **FAIL_DELAY** 设置。延迟以微秒为单位指定（1,000,000 = 1 秒）。

该模块在 PAM 服务文件（例如 `/etc/pam.d/login`）中配置，通过拖慢反复的认证尝试来帮助缓解暴力破解攻击。

# CAVEATS

延迟以微秒而非秒为单位。设置过长的延迟可能让输错密码的正当用户感到沮丧。该模块只影响由 PAM 栈处理的失败，不影响应用层的认证。

# HISTORY

pam_faildelay 的设计目的是通过可配置的延迟来**拖慢暴力破解攻击**。

# SEE ALSO

[pam](/man/pam)(8), [pam_tally2](/man/pam_tally2)(8)
