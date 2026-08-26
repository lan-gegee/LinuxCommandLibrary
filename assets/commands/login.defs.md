# TAGLINE

shadow 密码套件的配置文件

# TLDR

**设置密码最大有效期**（天）

```PASS_MAX_DAYS 90```

**设置两次密码更改之间的最小天数**

```PASS_MIN_DAYS 7```

**设置密码过期前的警告天数**

```PASS_WARN_AGE 14```

**设置普通用户的 UID 范围**

```UID_MIN 1000```

**设置密码哈希算法**

```ENCRYPT_METHOD SHA512```

**设置新用户的默认 umask**

```UMASK 077```

# SYNOPSIS

**/etc/login.defs**

# PARAMETERS

**PASS_MAX_DAYS**
> 密码有效的最大天数。

**PASS_MIN_DAYS**
> 两次密码更改之间的最小天数。

**PASS_MIN_LEN**
> 最小密码长度（使用 PAM 时被忽略；参见 pam_pwquality）。

**PASS_WARN_AGE**
> 过期前的警告天数。

**UID_MIN**, **UID_MAX**
> 用户的 UID 范围。

**GID_MIN**, **GID_MAX**
> 组的 GID 范围。

**UMASK**
> 默认 umask。

**ENCRYPT_METHOD**
> 密码哈希算法（DES、MD5、SHA256、SHA512、YESCRYPT）。

**CREATE_HOME**
> 默认创建主目录（yes/no）。

**USERGROUPS_ENAB**
> 启用用户私有组（yes/no）。

**LOGIN_RETRIES**
> 密码失败时登录重试的最大次数。

**LOGIN_TIMEOUT**
> 登录的最长时间（秒）。

# DESCRIPTION

**login.defs** 是 shadow 密码套件的配置文件，位于 **/etc/login.defs**。它定义用户账户创建、密码时效和登录行为的默认值。

其中的设置影响 useradd、usermod、passwd、groupadd 以及其他 shadow 工具。在使用 PAM 的系统上，某些设置（尤其是 PASS_MIN_LEN）可能被 PAM 模块覆盖。

# EXAMPLE CONFIG

```
# /etc/login.defs
PASS_MAX_DAYS   90
PASS_MIN_DAYS   7
PASS_WARN_AGE   14
UID_MIN         1000
UID_MAX         60000
ENCRYPT_METHOD  SHA512
UMASK           077
```

# CAVEATS

PAM 可能覆盖部分设置。更改不影响已有用户。部分取值与系统相关。需要 shadow 工具。

# SEE ALSO

[passwd](/man/passwd)(1), [useradd](/man/useradd)(8), [usermod](/man/usermod)(8), [groupadd](/man/groupadd)(8), [chage](/man/chage)(1), [login](/man/login)(1), [pam](/man/pam)(8)
