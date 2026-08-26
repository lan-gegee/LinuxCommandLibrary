# TAGLINE

提供匿名 FTP 认证

# TLDR

**启用匿名 FTP 认证**

```auth sufficient pam_ftp.so```

**使用自定义用户名**

```auth sufficient pam_ftp.so users=ftp,anonymous```

**忽略非匿名用户**

```auth sufficient pam_ftp.so ignore```

# SYNOPSIS

**pam_ftp.so** [_options_]

# PARAMETERS

**users=**_LIST_
> 以逗号分隔的用户列表。

**ignore**
> 对非匿名用户忽略此模块。

# DESCRIPTION

**pam_ftp** 提供匿名 FTP 认证。以邮箱地址作为密码。

该模块验证邮箱格式的密码。面向 FTP 服务。

# CAVEATS

仅适用于 FTP。只验证邮箱格式。需注意安全问题。

# HISTORY

pam_ftp 通过邮箱验证实现了**匿名 FTP 认证**。

# SEE ALSO

[pam](/man/pam)(8), [pam_unix](/man/pam_unix)(8), [vsftpd](/man/vsftpd)(8)
