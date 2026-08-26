# TAGLINE

修改用户密码过期信息

# TLDR

列出用户的**密码信息**

```chage -l username```

设置密码 **10 天后过期**

```sudo chage -M 10 username```

**禁用**密码过期

```sudo chage -M -1 username```

设置**账户过期**日期

```sudo chage -E 2025-12-31 username```

强制用户下次登录时**更改密码**

```sudo chage -d 0 username```

**重新启用**已过期的账户

```sudo chage -E -1 username```

# SYNOPSIS

**chage** [_options_] _LOGIN_

# DESCRIPTION

**chage** 修改存储在 /etc/shadow 中的用户密码过期信息。它控制两次强制密码更改之间的天数、上次密码更改日期以及账户过期日期。

系统管理员使用 chage 来实施密码策略，例如要求用户定期更改密码、设置密码过期后的宽限期以及在特定日期禁用账户。-l 选项允许任何用户在没有 root 权限的情况下查看自己的账户时效信息。

通过 -d 将上次密码更改日期设为 0，会强制该用户下次登录时立即更改密码。这常用于创建新账户或发生安全事件之后。

# PARAMETERS

**-d, --lastday LAST_DAY**
> 设置上次密码更改日期（YYYY-MM-DD 或自 epoch 起的天数）

**-E, --expiredate EXPIRE_DATE**
> 设置账户过期日期；使用 -1 移除过期时间

**-i, --iso8601**
> 以 ISO 8601 格式输出日期

**-I, --inactive DAYS**
> 密码过期后到账户锁定前的非活动天数

**-l, --list**
> 显示账户时效信息

**-m, --mindays MIN_DAYS**
> 两次密码更改之间的最短天数

**-M, --maxdays MAX_DAYS**
> 强制密码更改前的最长天数

**-W, --warndays WARN_DAYS**
> 过期前多少天开始警告用户

# CONFIGURATION

**/etc/shadow**
> 每个用户账户的密码时效数据。

**/etc/login.defs**
> 密码时效策略的系统级默认值。

# CAVEATS

除使用 **-l** 列出自己的信息外，均需 root 权限。设置 **-d 0** 会强制用户下次登录时立即更改密码。

# HISTORY

**chage** 属于 **shadow-utils** 软件包。它按照 /etc/shadow 文件中的定义管理密码时效。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[passwd](/man/passwd)(1), [usermod](/man/usermod)(8), [chpasswd](/man/chpasswd)(8)
