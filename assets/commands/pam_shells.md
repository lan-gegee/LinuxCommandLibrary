# TAGLINE

验证用户登录 Shell 的 PAM 模块

# TLDR

**要求有效 Shell 才能认证**

```auth required pam_shells.so```

**要求有效 Shell 才能访问账户**

```account required pam_shells.so```

# SYNOPSIS

**pam_shells.so**

# PARAMETERS

该模块不接受任何参数。

# DESCRIPTION

**pam_shells** 是一个 PAM 模块，只有当用户的 Shell 列在 **/etc/shells** 中时才允许访问系统。它还会检查 /etc/shells 是否为普通文件且非全局可写。

该模块同时提供 **auth** 和 **account** 模块类型。Shell 未被列出时返回 PAM_AUTH_ERR；Shell 有效时返回 PAM_SUCCESS；无法确定用户名时返回 PAM_SERVICE_ERR。

# CAVEATS

要求 **/etc/shells** 存在且包含有效的 Shell 路径（每行一个绝对路径）。Shell 不在 /etc/shells 中的用户将被拒绝访问。/etc/shells 中的空行和以 # 开头的行会被忽略。

# HISTORY

**pam_shells** 是 Linux-PAM（可插拔认证模块）框架的一部分，提供了一种简单机制，可根据用户是否拥有合法登录 Shell 来限制访问。

# SEE ALSO

[pam](/man/pam)(8), [pam_unix](/man/pam_unix)(8), [pam_deny](/man/pam_deny)(8), [chsh](/man/chsh)(1), [getent](/man/getent)(1), [login](/man/login)(1)
