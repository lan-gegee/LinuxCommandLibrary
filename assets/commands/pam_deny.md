# TAGLINE

始终返回失败

# TLDR

**拒绝所有认证**

```auth required pam_deny.so```

**阻止账户访问**

```account required pam_deny.so```

**禁用密码更改**

```password required pam_deny.so```

# SYNOPSIS

**pam_deny.so**

# PARAMETERS

无参数。始终返回失败。

# DESCRIPTION

**pam_deny** 始终返回失败。用于阻止认证。

该模块无条件拒绝所有请求。是一个安全兜底模块。

# CAVEATS

没有配置选项。请谨慎使用，避免把用户锁在系统外。

# HISTORY

pam_deny 为 PAM 配置提供了一个**通用拒绝模块**。

# SEE ALSO

[pam](/man/pam)(8), [pam_permit](/man/pam_permit)(8)
