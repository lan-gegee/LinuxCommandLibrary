# TAGLINE

将 su 限制为 wheel 组成员

# TLDR

**要求 su 必须属于 wheel 组**

```auth required pam_wheel.so```

**切换为 root 时要求 wheel 组**

```auth required pam_wheel.so root_only```

**使用指定组**

```auth required pam_wheel.so group=admin```

**信任组成员**

```auth sufficient pam_wheel.so trust```

# SYNOPSIS

**pam_wheel.so** [_options_]

# PARAMETERS

**root_only**
> 仅对切换到 root 的 su 生效。

**group=**_NAME_
> 使用替代的组。

**trust**
> 信任组成员（无需密码）。

**deny**
> 拒绝组成员访问。

# DESCRIPTION

**pam_wheel** 将 su 限制为 wheel 组。控制 root 访问。

该模块要求组成员身份。属于传统 Unix 安全机制。

# CAVEATS

auth 模块。需要 wheel 组。BSD 风格的安全机制。

# HISTORY

pam_wheel 为 su 命令访问提供 **wheel 组限制**。

# SEE ALSO

[pam](/man/pam)(8), [su](/man/su)(1), [pam_rootok](/man/pam_rootok)(8)
