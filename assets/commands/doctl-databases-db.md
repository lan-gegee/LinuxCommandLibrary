# TAGLINE

管理集群内的各个数据库

# TLDR

**列出集群中的数据库**

```doctl databases db list [cluster_id]```

**创建一个数据库**

```doctl databases db create [cluster_id] [db_name]```

**删除一个数据库**

```doctl databases db delete [cluster_id] [db_name]```

**获取数据库详情**

```doctl databases db get [cluster_id] [db_name]```

**以 JSON 输出列出数据库**

```doctl databases db list [cluster_id] --output json```

# SYNOPSIS

**doctl** **databases** **db** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出集群中的数据库。

**create**
> 创建一个数据库。

**delete**
> 删除一个数据库。

**get**
> 获取数据库信息。

# DESCRIPTION

**doctl databases db** 管理 DigitalOcean 托管数据库集群中的各个数据库。

在单个数据库集群中，你可以创建多个相互隔离的数据库，从而在同一套集群基础设施上托管不同的应用或环境（开发、预发布、生产）。每个数据库可以拥有自己的用户和权限集，同时共享集群的计算和存储资源。

该命令负责集群内数据库的创建、列出和删除。它与管理集群本身不同，后者由父命令 doctl databases 处理。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl-databases](/man/doctl-databases)(1), [doctl-databases-user](/man/doctl-databases-user)(1), [doctl-databases-pool](/man/doctl-databases-pool)(1), [doctl](/man/doctl)(1)
