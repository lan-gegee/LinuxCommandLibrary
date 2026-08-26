# TAGLINE

Proxmox 用户与权限管理

# TLDR

**列出**用户

```pveum user list```

**添加**用户

```pveum user add [username]@pve```

添加带**邮箱、描述和密码**的用户

```pveum user add [username]@pve --email [email] --comment [description] --password [password]```

**修改**用户密码

```pveum passwd [username]@pve```

**删除**用户

```pveum user delete [username]@pve```

以特定权限向用户**授予**虚拟机访问权

```pveum acl modify /vms/1000 --user [username]@pve --role PVEVMUser```

为用户**生成** API 令牌

```pveum user token add [username]@pve [tokenid]```

**列出**可用角色

```pveum role list```

# SYNOPSIS

**pveum** _command_ [_subcommand_] [_options_]

# PARAMETERS

**user** **list**, **u l**
> 列出所有用户

**user** **add**, **u a** _user_
> 添加新用户

**user** **delete**, **u d** _user_
> 删除用户

**passwd**, **pa** _user_
> 修改用户密码

**acl** **modify**, **a m** _path_
> 修改访问控制列表

**group** **list**
> 列出组

**role** **list**
> 列出角色

**realm** **list**
> 列出认证域

**realm** **add** _realm_
> 添加认证域（pam、pve、ldap、ad、openid）

**user** **token** **add** _user_ _tokenid_
> 为用户生成 API 令牌

**pool** **add** _poolid_
> 创建资源池

**pool** **list**
> 列出资源池

**--role** _role_
> 分配角色（PVEAdmin、PVEVMUser 等）

**--email** _email_
> 用户邮箱地址

**--comment** _text_
> 用户描述

# DESCRIPTION

**pveum** 管理 Proxmox VE 的用户、组、角色和访问控制列表。它配置认证域（PAM、PVE、LDAP、Active Directory）以及集群资源的权限分配。

权限系统采用基于路径的模型，在特定的资源路径（数据中心、节点、虚拟机、存储）上授予权限，由角色定义允许的操作。

# CAVEATS

用户认证域（@pve、@pam、@ldap）决定身份验证方式。权限更改立即生效。内置的 root@pam 无法删除。某些操作需要 PVEUserAdmin 角色。

# HISTORY

**Proxmox VE** 的组成部分，为多用户虚拟化环境提供细粒度访问控制。支持 LDAP/AD 集成和双因素认证等企业级功能。

# SEE ALSO

[pvesh](/man/pvesh)(1), [qm](/man/qm)(1), [pct](/man/pct)(1)
