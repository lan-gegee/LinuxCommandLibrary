# TAGLINE

针对 Berkeley DB 进行认证

# TLDR

**针对数据库认证**

```auth required pam_userdb.so db=/path/to/userdb```

**不区分大小写**

```auth required pam_userdb.so db=/path/to/userdb icase```

**创建用户数据库**

```db_load -T -t hash -f users.txt /path/to/userdb.db```

# SYNOPSIS

**pam_userdb.so** [_options_]

# PARAMETERS

**db=**_PATH_
> 数据库文件路径（在某些系统上不带 .db 扩展名）。

**icase**
> 用户名匹配不区分大小写。

**crypt=**_TYPE_
> 密码加密类型：_none_（明文）或 _crypt_（经 crypt(3) 哈希）。

**try_first_pass**
> 在提示输入前先尝试先前输入的密码。

**use_first_pass**
> 只使用先前输入的密码；不再提示输入。

**dump**
> 将数据库内容转储到日志（调试用途，不安全）。

**unknown_ok**
> 对不在数据库中的用户不判定认证失败（跳过模块）。

**key_only**
> 仅根据用户名是否存在进行认证，忽略密码。

# DESCRIPTION

**pam_userdb** 使用存储在 Berkeley DB 数据库中的凭据对用户进行认证，独立于系统账户文件。该数据库将用户名（键）映射到密码（值），从而支持针对特定应用或服务的认证，而无需创建系统账户。

常用于为 FTP、VPN 或 Web 应用等提供单独的凭据。

# CAVEATS

需要 Berkeley DB。数据库格式有特定要求。用户管理需自行实现。

# HISTORY

pam_userdb 实现了独立于系统账户的**基于数据库的认证**。

# SEE ALSO

[pam](/man/pam)(8), [db_load](/man/db_load)(1)
