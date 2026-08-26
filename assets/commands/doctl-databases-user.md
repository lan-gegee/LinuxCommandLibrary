# TAGLINE

管理数据库集群的用户

# TLDR

**列出数据库用户**

```doctl databases user list [cluster_id]```

**创建一个用户**

```doctl databases user create [cluster_id] [username]```

**获取用户信息**

```doctl databases user get [cluster_id] [username]```

**重置用户认证**密码或 MySQL 认证插件

```doctl databases user reset [cluster_id] [username] [new_auth_mode]```

**创建使用指定 MySQL 认证插件的**用户

```doctl databases user create [cluster_id] [username] --mysql-auth-plugin [caching_sha2_password]```

**以自定义输出格式列出用户**

```doctl databases user list [cluster_id] --format Name,Role```

**删除一个用户**

```doctl databases user delete [cluster_id] [username]```

# SYNOPSIS

**doctl** **databases** **user** _command_ [_options_]

# SUBCOMMANDS

**list**
> 获取数据库用户的列表。

**create**
> 创建一个数据库用户。新用户的角色为 normal，并自动生成密码。

**get**
> 获取某个数据库用户的详情。

**delete**
> 删除一个数据库用户。

**reset**
> 重置指定用户的认证密码或 MySQL 授权插件，并返回新凭据。

# PARAMETERS

**--mysql-auth-plugin** _PLUGIN_
> 设置 MySQL 授权插件（caching_sha2_password 或 mysql_native_password）。与 create 一起使用。

**--acl** _RULES_
> 以逗号分隔的 Kafka ACL 规则，格式为 topic:permission。与 create 一起使用。

**--opensearch-acl** _RULES_
> 以逗号分隔的 OpenSearch ACL 规则，格式为 index:permission。与 create 一起使用。

**--format** _COLUMNS_
> 输出列（例如 Name,Role）。

**--no-header**
> 输出中省略表头行。

**--output** _FORMAT_
> 输出格式：text 或 json（默认：text）。

# DESCRIPTION

**doctl databases user** 管理 DigitalOcean 托管数据库集群的用户。用户代表应用和管理员连接数据库时使用的身份验证凭据。

每个用户都有关联的凭据（用户名和密码），并根据数据库引擎拥有不同的权限。用户管理包括为不同的应用或服务创建用户、通过密码重置轮换凭据，以及在不再需要访问时删除用户。

正确的用户管理应遵循安全最佳实践：为每个应用创建专用用户、定期轮换凭据，以及删除不再使用的账户以尽量减少安全暴露面。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl-databases](/man/doctl-databases)(1), [doctl-databases-pool](/man/doctl-databases-pool)(1), [doctl-databases-db](/man/doctl-databases-db)(1), [doctl-databases-firewalls](/man/doctl-databases-firewalls)(1)
