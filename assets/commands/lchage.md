# TAGLINE

在使用 libuser 的系统上显示或更改用户密码过期策略

# TLDR

显示**密码策略**

```sudo lchage --list [username]```

**禁用**密码过期

```sudo lchage --date -1 [username]```

设置**密码最小使用天数**

```sudo lchage --mindays [days] [username]```

设置**密码最大使用天数**

```sudo lchage --maxdays [days] [username]```

设置过期前的**警告天数**

```sudo lchage --warndays [days] [username]```

# SYNOPSIS

**lchage** [_options_] _username_

# DESCRIPTION

**lchage** 在使用 libuser 的系统上显示或更改用户密码过期策略。它提供与 chage 类似的功能，但使用 libuser 库访问用户数据库。

# PARAMETERS

**-l, --list**
> 显示用户的密码时效信息

**-d, --date DAYS**
> 设置上次密码更改日期（-1 表示禁用过期）

**-m, --mindays DAYS**
> 两次密码更改之间的最小天数

**-M, --maxdays DAYS**
> 要求更改密码前的最大天数

**-W, --warndays DAYS**
> 密码过期前发出警告的天数

**-I, --inactive DAYS**
> 密码过期后到账户被禁用之间的天数

**-E, --expiredate DATE**
> 设置账户过期日期

# CAVEATS

需要 root 权限。仅在安装了 libuser 库的系统上可用（主要是 Fedora/RHEL 系发行版）。某些选项可能因认证后端配置（如 LDAP）而不可用。

# INSTALL

```apt: sudo apt install libuser```

```dnf: sudo dnf install libuser```

```apk: sudo apk add libuser```

```zypper: sudo zypper install libuser```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chage](/man/chage)(1), [passwd](/man/passwd)(1), [usermod](/man/usermod)(8)
