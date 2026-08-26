# TAGLINE

管理基于文件的 Elasticsearch 用户

# TLDR

**列出用户**

```elasticsearch-users list```

**添加用户**

```elasticsearch-users useradd [username] -p [password] -r [roles]```

**删除用户**

```elasticsearch-users userdel [username]```

**更改密码**

```elasticsearch-users passwd [username]```

**为用户添加角色**

```elasticsearch-users roles [username] -a [role]```

**从用户移除角色**

```elasticsearch-users roles [username] -r [role]```

# SYNOPSIS

**elasticsearch-users** _command_ [_options_]

# SUBCOMMANDS

**useradd**
> 添加用户。

**userdel**
> 删除用户。

**passwd**
> 更改密码。

**roles**
> 管理用户角色。

**list**
> 列出用户。

# PARAMETERS

**-p** _pass_
> 用户密码（必须至少 6 个字符）。省略时交互式提示输入。

**-r** _roles_
> 以逗号分隔的角色列表。在 **useradd** 中用于分配角色；在 **roles** 中用于移除角色。

**-a** _roles_
> 添加以逗号分隔的角色（与 **roles** 子命令配合使用）。

# DESCRIPTION

**elasticsearch-users** 管理 Elasticsearch native realm 的基于文件的用户。这些用户存储在节点的配置目录中，不需要外部身份验证系统。该工具是 Elasticsearch 安全特性的一部分。

列出用户时，只显示在本地节点上注册的用户。在多节点集群中，基于文件的用户必须在每个节点上分别管理。

# CAVEATS

用户存储在 **config/users**，角色存储在 **config/users_roles**。变更只对本地节点生效；需要在集群节点之间手动同步这些文件。要求启用 X-Pack 安全特性。

# HISTORY

**elasticsearch-users** 随 Elasticsearch 安全特性一起提供（最初属于商业 **X-Pack** 插件，在 Elasticsearch **6.8/7.1** 中随 Basic 许可证免费开放）。它提供轻量级身份验证，无需 LDAP、Active Directory 或其他外部 realm。

# INSTALL

```nix: nix profile install nixpkgs#elasticsearch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [elasticsearch-reset-password](/man/elasticsearch-reset-password)(1)
