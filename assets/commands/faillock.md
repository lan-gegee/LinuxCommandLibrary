# TAGLINE

认证失败跟踪与锁定管理工具

# TLDR

列出当前用户的**登录失败**记录

```faillock```

重置当前用户的失败记录

```faillock --reset```

列出**所有**用户的登录失败记录

```sudo faillock```

列出**指定**用户的失败记录

```sudo faillock --user [user]```

重置**指定**用户的失败记录

```sudo faillock --user [user] --reset```

# SYNOPSIS

**faillock** [_options_]

# DESCRIPTION

**faillock** 显示和修改身份验证失败记录文件。它是 PAM pam_faillock 模块的一部分，跟踪失败的登录尝试，并可在失败次数过多后锁定账户。

用于安全监控和账户锁定管理。

# PARAMETERS

**--user** _user_
> 操作指定用户

**--reset**
> 重置失败记录

**--dir** _dir_
> 使用备用计数目录

# CONFIGURATION

**/etc/security/faillock.conf**
> pam_faillock 模块的配置，包括锁定阈值和持续时间。

# CAVEATS

属于 Linux-PAM 软件包的一部分。记录默认存储在 /var/run/faillock/ 中。查看其他用户的记录需要 root 权限。

# INSTALL

```apt: sudo apt install libpam-modules-bin```

```apk: sudo apk add linux-pam```

```brew: brew install linux-pam```

```nix: nix profile install nixpkgs#linux-pam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pam_faillock](/man/pam_faillock)(8), [pam](/man/pam)(8)

# RESOURCES

```[Source code](https://github.com/linux-pam/linux-pam)```

```[Homepage](http://www.linux-pam.org/)```

<!-- verified: 2026-07-15 -->
