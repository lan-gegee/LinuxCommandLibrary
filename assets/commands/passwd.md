# TAGLINE

更改用户密码

# TLDR

**修改自己的密码**

```passwd```

**修改其他用户的密码**（root）

```passwd [username]```

**锁定用户账户**

```passwd -l [username]```

**解锁用户账户**

```passwd -u [username]```

强制在下次登录时**修改密码**

```passwd -e [username]```

设置密码在指定天数后**过期**

```passwd -x [90] [username]```

**显示密码状态**

```passwd -S [username]```

**删除用户密码**（免密登录）

```passwd -d [username]```

# SYNOPSIS

**passwd** [_options_] [_username_]

# DESCRIPTION

**passwd** 用于更改用户密码。普通用户不带参数运行时，它会先提示输入当前密码，然后允许设置新密码。root 无需知道旧密码即可更改任何用户的密码。

该工具会执行密码策略，包括最小长度、复杂度要求和历史限制。这些策略在 /etc/login.defs 和 PAM 配置中设定。

passwd 还管理密码时效，允许管理员强制定期修改密码、使密码过期以及锁定/解锁账户。

# PARAMETERS

**-l**, **--lock**
> 锁定账户密码。

**-u**, **--unlock**
> 解锁账户密码。

**-d**, **--delete**
> 删除密码（免密码登录）。

**-e**, **--expire**
> 强制下次登录时修改密码。

**-n** _days_, **--mindays** _days_
> 两次修改之间的最短天数。

**-x** _days_, **--maxdays** _days_
> 超过该天数则必须修改密码。

**-w** _days_, **--warndays** _days_
> 过期前提前警告用户的天数。

**-i** _days_, **--inactive** _days_
> 密码过期后到账户被禁用的天数。

**-S**, **--status**
> 显示密码状态信息。

**-a**, **--all**
> 与 -S 配合使用，显示所有用户的状态。

**--stdin**
> 从 stdin 读取密码（非交互式）。

# CAVEATS

更改其他用户的密码需要 root 权限。PAM 模块可能强制额外的密码要求。被锁定的账户仍可通过 SSH 密钥访问。密码策略因系统配置而异。

# HISTORY

**passwd** 自最早的 Unix 版本起就已存在，可追溯到 **1971 年** **贝尔实验室**的 **Version 1 Unix**。密码文件最初直接存储哈希后的密码，但现代系统出于安全考虑使用影子密码（/etc/shadow），该机制于 **20 世纪 80 年代**在 **SunOS** 中引入。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chage](/man/chage)(1), [usermod](/man/usermod)(8), [login.defs](/man/login.defs)(5)
