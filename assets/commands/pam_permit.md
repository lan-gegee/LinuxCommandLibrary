# TAGLINE

始终返回成功

# TLDR

**允许所有认证**

```auth sufficient pam_permit.so```

**会话始终成功**

```session optional pam_permit.so```

# SYNOPSIS

**pam_permit.so**

# PARAMETERS

无参数。始终返回成功。

# DESCRIPTION

**pam_permit** 始终返回成功。无条件允许所有访问。

该模块批准所有请求。是一个绕过安全检查的模块。

# CAVEATS

存在安全风险。仅在合适时使用。不执行任何认证。

# HISTORY

pam_permit 为 PAM 配置提供了一个**通用放行模块**。

# SEE ALSO

[pam](/man/pam)(8), [pam_deny](/man/pam_deny)(8)
