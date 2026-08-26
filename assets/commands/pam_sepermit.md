# TAGLINE

根据 SELinux 用户状态允许或拒绝登录的 PAM 模块

# TLDR

**在 PAM auth 栈中启用**

```auth required pam_sepermit.so```

**启用并强制独占登录**

```auth required pam_sepermit.so exclusive```

**使用自定义配置文件**

```auth required pam_sepermit.so conf=/etc/security/custom_sepermit.conf```

**向配置添加用户放行规则**

```echo "%wheel" >> /etc/security/sepermit.conf```

# SYNOPSIS

**pam_sepermit.so** [**conf=**_file_] [**exclusive**]

# PARAMETERS

**exclusive**
> 对 SELinux 用户同一时间只允许一个登录会话。如果已有另一个会话处于活动状态，则拒绝登录。

**conf=**_FILE_
> 使用替代的配置文件，而不是默认的 /etc/security/sepermit.conf。

# CONFIGURATION

**/etc/security/sepermit.conf**
> 配置文件，列出允许或拒绝登录的 SELinux 用户、UNIX 用户或 UNIX 组（以 % 为前缀）。以 # 开头的行是注释。每行指定一个用户或组，并可带有 exclusive 或 ignore 等可选修饰符。

# DESCRIPTION

**pam_sepermit** 是一个 PAM 模块，根据 SELinux 用户状态允许或拒绝登录。它检查 SELinux 是否处于 enforcing 模式，以及用户的 SELinux 上下文是否匹配配置文件中的条目。当 SELinux 处于 permissive 模式或已禁用时，该模块默认允许访问。

该模块通常放在 auth 栈中，用于在启用了 SELinux 的系统上基于用户映射的 SELinux 身份来限制哪些用户可以登录。

# CAVEATS

要求系统已启用并配置 SELinux。SELinux 被禁用时，该模块允许所有访问。模块必须放在 PAM 栈的正确位置。配置错误可能把用户锁在外面。

# HISTORY

**pam_sepermit** 是 Linux-PAM 项目的一部分，引入它是为了在启用了 SELinux 的系统上提供细粒度的登录控制，作为更通用的 pam_selinux 模块的补充。

# SEE ALSO

[pam](/man/pam)(8), [pam_selinux](/man/pam_selinux)(8), [getenforce](/man/getenforce)(8), [sestatus](/man/sestatus)(8)
