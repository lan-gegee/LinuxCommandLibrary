# TAGLINE

管理 DigitalOcean 上的 PostgreSQL 连接池

# TLDR

**列出数据库集群的所有连接池**

```doctl databases pool list [cluster_id]```

**创建一个连接池**

```doctl databases pool create [cluster_id] [pool_name] --db [database] --user [user] --size [10] --mode [transaction]```

**获取指定连接池的详情**

```doctl databases pool get [cluster_id] [pool_name]```

**更新一个连接池**

```doctl databases pool update [cluster_id] [pool_name] --size [20]```

**删除一个连接池**

```doctl databases pool delete [cluster_id] [pool_name]```

# SYNOPSIS

**doctl** **databases** **pool** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出数据库集群的所有连接池。

**create**
> 创建一个连接池（需要名称、数据库、用户和大小）。

**get**
> 获取指定连接池的详情。

**update**
> 更新现有连接池的设置。

**delete**
> 删除一个连接池。

# PARAMETERS

**--db** _string_
> 连接池的目标数据库名称。

**--user** _string_
> 用于连接池认证的数据库用户名。

**--size** _int_
> 池大小（要维持的连接数）。

**--mode** _string_
> 池模式：transaction（默认，最快）、session（保留会话状态）或 statement。

**--format** _string_
> 自定义输出列。

# DESCRIPTION

**doctl databases pool** 管理 DigitalOcean 托管 PostgreSQL 数据库的连接池。连接池使用 PgBouncer 提供连接复用，可显著改善拥有大量并发客户端的应用的性能。

连接池充当应用与数据库之间的中间层，维护一定数量的可复用数据库连接，从而减少反复建立和关闭连接的开销。池模式决定连接的行为：**transaction** 模式在每个事务结束后释放连接（对无状态查询最快），**session** 模式在整个客户端会话期间保持连接，**statement** 模式则在每条语句结束后释放连接。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl-databases](/man/doctl-databases)(1), [doctl-databases-db](/man/doctl-databases-db)(1), [doctl-databases-user](/man/doctl-databases-user)(1)
