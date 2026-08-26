# TAGLINE

通知用户新邮件

# TLDR

**检查新邮件**

```session optional pam_mail.so```

**显示标准邮件路径**

```session optional pam_mail.so standard```

**自定义邮件目录**

```session optional pam_mail.so dir=~/Maildir```

**邮箱为空时保持安静**

```session optional pam_mail.so quiet```

**跳过新邮件检查（仅登录 MOTD 时显示）**

```session optional pam_mail.so nopen```

# SYNOPSIS

**pam_mail.so** [_options_]

# PARAMETERS

**dir=**_PATH_
> 邮件目录（覆盖 MAIL 环境变量）。

**standard**
> 使用标准的邮件 spool 位置。

**close**
> 会话关闭时若收到新邮件也打印提示。

**empty**
> 即使邮箱为空也进行报告。

**hash=**_N_
> 在 `dir` 下的 N 层哈希子目录中查找（适用于采用哈希 spool 的站点）。

**nopen**
> 登录时不检查任何邮箱（抑制状态消息）。

**noenv**
> 不导出 `MAIL` 环境变量。

**quiet**
> 只在有新邮件时报告（不显示"没有邮件"的消息）。

# DESCRIPTION

**pam_mail** 通知用户新邮件。在登录时检查邮件 spool。

该模块显示邮件通知。属于会话登录功能。

# CAVEATS

session 模块。依赖邮件 spool。可选的通知功能。

# HISTORY

pam_mail 为 Unix 邮件 spool 提供登录时的**邮件通知**。

# SEE ALSO

[pam](/man/pam)(8), [mail](/man/mail)(1)
