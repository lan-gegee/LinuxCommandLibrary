# TAGLINE

Name Service Switch 数据库查询工具

# TLDR

按 UID 查找 **passwd** 条目

```getent passwd [1000]```

列出 **group** 数据库中的所有条目

```getent group```

显示某个**组名**的成员

```getent group [group_name]```

通过 **hosts**（NSS）解析主机名

```getent hosts [hostname]```

列出 services 数据库中已知的**服务**

```getent services```

# SYNOPSIS

**getent** _database_ [_key_...]

# PARAMETERS

**passwd**
> 用户账户数据库（/etc/passwd 及 NSS 来源）

**group**
> 组数据库（/etc/group 及 NSS 来源）

**hosts**
> 主机名/IP 解析（如 /etc/hosts、DNS）

**services**
> 网络服务（/etc/services）

**protocols**
> 网络协议（/etc/protocols）

**networks**
> 网络名称与地址

**shadow**
> 影子密码条目（需要 root 权限）

**aliases**
> 邮件别名

# CONFIGURATION

**/etc/nsswitch.conf**
> Name Service Switch 配置，决定每种数据库类型查询哪些来源。

# DESCRIPTION

**getent** 从 Name Service Switch（NSS）配置的管理数据库中查询条目，这些数据库包括本地文件、LDAP、NIS 和其他来源。它提供一个统一接口来查找用户、组、主机和其他系统信息，而无需关心数据实际存储在哪里。

与直接读取 /etc/passwd 等文件不同，getent 会返回所有已配置 NSS 来源的结果，因此对使用集中式认证（LDAP、Active Directory 等）的系统至关重要。

不带键时，getent 列出数据库中的所有条目；带键时，只返回匹配的条目。

# CAVEATS

shadow 数据库需要 root 权限。某些数据库可能不支持枚举（列出所有条目）。结果取决于 /etc/nsswitch.conf 中的 NSS 配置。

# HISTORY

自 20 世纪 90 年代初实现 Name Service Switch 以来，getent 一直是 GNU C Library（glibc）的一部分，为查询可能来自多个来源的系统数据库提供了标准方式。

# INSTALL

```apt: sudo apt install libc-bin```

```apk: sudo apk add musl-utils```

```nix: nix profile install nixpkgs#getent```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[id](/man/id)(1), [groups](/man/groups)(1), [host](/man/host)(1)
