# TAGLINE

管理 Samba 用户数据库，允许管理员添加

# TLDR

**列出**所有 Samba 用户及其设置

```sudo pdbedit --list --verbose```

将现有 Unix 用户**添加**到 Samba

```sudo pdbedit --user [username] --create```

**移除** Samba 用户

```sudo pdbedit --user [username] --delete```

**重置** Samba 用户的密码失败计数器

```sudo pdbedit --user [username] --bad-password-count-reset```

# SYNOPSIS

**pdbedit** [_options_]

# PARAMETERS

**-L**, **--list**
> 列出所有 Samba 用户账户

**-v**, **--verbose**
> 启用详细列表模式

**-u**, **--user** _username_
> 指定要操作的用户

**-a**, **--create**
> 添加新用户账户（提示输入密码）

**-x**, **--delete**
> 删除指定的用户账户

**-z**, **--bad-password-count-reset**
> 重置用户的密码错误计数

**-t**, **--password-from-stdin**
> 从 stdin 读取密码

**-w**, **--smbpasswd-style**
> 使用 smbpasswd 风格的输出

**-e**, **--export**
> 将用户数据库导出到 stdout

**-i**, **--import**
> 从 stdin 导入用户数据库

**-b**, **--backend** _name_
> 使用指定的 passdb 后端

**-P**, **--account-policy**
> 显示或更改账户策略

**--policies-reset**
> 将账户策略重置为默认值

# DESCRIPTION

**pdbedit** 管理 Samba 用户数据库（SAM 数据库），允许管理员添加、修改和删除 Samba 用户账户。它比 smbpasswd 提供更细致的控制，包括访问用户标志、密码策略以及数据库导入/导出。

用户必须先存在于 Unix 系统中，才能被添加到 Samba。该工具可在不同的 passdb 后端上运行，包括 tdbsam（默认）和用于 LDAP 集成的 ldapsam。

# CAVEATS

需要 root 权限。用户必须先存在于 Unix passwd 数据库中才能添加到 Samba。对于简单的用户管理，smbpasswd 可能更方便。后端配置取决于 smb.conf 设置。

# HISTORY

自 Samba 3.0 起成为 **Samba** 套件的一部分，取代了较旧的密码数据库工具。随着 Samba 弃用旧的 smbpasswd 文件格式，它为管理各种 Samba passdb 后端提供了统一接口。

# INSTALL

```apt: sudo apt install samba```

```dnf: sudo dnf install samba```

```pacman: sudo pacman -S samba```

```apk: sudo apk add samba-common-tools```

```zypper: sudo zypper install samba```

```brew: brew install samba```

```nix: nix profile install nixpkgs#samba```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbpasswd](/man/smbpasswd)(8), [samba](/man/samba)(7)
