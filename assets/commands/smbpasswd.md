# TAGLINE

管理 Samba 用户密码和账户

# TLDR

**修改**当前用户的 SMB 密码

```smbpasswd```

**添加**用户到 Samba 并设置密码

```sudo smbpasswd -a [username]```

**修改**已有 Samba 用户的密码

```sudo smbpasswd [username]```

**删除**一个 Samba 用户

```sudo smbpasswd -x [username]```

**启用**一个 Samba 用户

```sudo smbpasswd -e [username]```

**禁用**一个 Samba 用户

```sudo smbpasswd -d [username]```

# SYNOPSIS

**smbpasswd** [_options_] [_username_]

# PARAMETERS

**-a**
> 添加新的 Samba 用户

**-x**
> 删除一个 Samba 用户

**-d**
> 禁用一个 Samba 用户账户

**-e**
> 启用先前被禁用的账户

**-n**
> 设置空密码（需要启用 null passwords）

**-r _machine_**
> 在远程机器上修改密码

**-U _username_**
> 在远程机器上使用指定的用户名

**-s**
> 从标准输入读取密码（静默模式）

# DESCRIPTION

**smbpasswd** 管理 Samba 用户密码。它允许用户修改自己的 SMB 密码，也允许管理员添加、删除或修改 Samba 用户账户。

Samba 用户在被添加之前必须已存在对应的本地 Unix 账户。Samba 密码数据库与系统密码是相互独立的。

# CAVEATS

用户必须先存在于 Unix 系统中才能被添加到 Samba。如果 Unix 账户先于 Samba 账户被删除，请改用 **pdbedit** 来移除 Samba 条目。

# INSTALL

```apt: sudo apt install samba-common-bin```

```dnf: sudo dnf install samba-common-tools```

```apk: sudo apk add samba-common-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdbedit](/man/pdbedit)(8), [samba](/man/samba)(7)
