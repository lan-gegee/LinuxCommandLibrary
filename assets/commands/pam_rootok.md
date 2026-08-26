# TAGLINE

对 UID 0 恒定成功的 PAM 模块

# TLDR

在 /etc/pam.d/su 中**让 root 无需密码即可切换**

```auth sufficient pam_rootok.so```

为模块**启用调试日志**

```auth sufficient pam_rootok.so debug```

# SYNOPSIS

**pam_rootok.so** [_debug_]

# DESCRIPTION

**pam_rootok** 是一个 PAM 认证模块，当调用用户的 UID 为 0（root）时返回成功。它最常见的用途是在 **/etc/pam.d/su** 中，让 root 用户无需输入密码即可切换到任何其他账户。

它通常与 **sufficient** 控制标志搭配：root 立即通过认证，其他用户则继续沿栈向下由后续模块正常认证（例如 **pam_unix** 或 **pam_wheel**）。

该模块只提供 **auth** 管理组；没有 session、password 或 account 语义。

# PARAMETERS

**debug**
> 向 syslog（auth 设施）记录一条描述所执行操作的消息。

# EXAMPLES

```
# /etc/pam.d/su — let root su to anyone without a password
auth   sufficient   pam_rootok.so
auth   required     pam_unix.so
```

# CAVEATS

只在 **auth** 栈中有用。该模块检查的是真实 UID，因此依赖调用进程确实以 root 身份运行。若把该模块错误地放入其他服务的配置文件中，可能导致意外的权限提升。

# HISTORY

**pam_rootok** 是 **Linux-PAM** 发行版的一部分，自 20 世纪 90 年代末 Linux-PAM 的早期版本起就已包含。

# SEE ALSO

[pam](/man/pam)(8), [su](/man/su)(1), [pam_wheel](/man/pam_wheel)(8), [pam_unix](/man/pam_unix)(8)
