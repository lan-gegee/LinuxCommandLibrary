# TAGLINE

Exoscale 托管数据库服务操作

# TLDR

**列出数据库服务**

```exo dbaas list```

**创建 PostgreSQL 数据库**

```exo dbaas create pg [name] --zone [ch-gva-2] --plan [hobbyist-2]```

**显示数据库详情**

```exo dbaas show [name] --zone [ch-gva-2]```

**显示数据库连接 URI**

```exo dbaas show [name] --zone [ch-gva-2] --uri```

**列出可用的数据库类型和套餐**

```exo dbaas type list [--zone ch-gva-2]```

**删除数据库**

```exo dbaas delete [name] --zone [ch-gva-2]```

**更新数据库设置**

```exo dbaas update [name] --zone [ch-gva-2] --plan [business-4]```

# SYNOPSIS

**exo** **dbaas** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出数据库服务。

**create**
> 创建数据库服务。

**show**
> 显示数据库详情。

**update**
> 更新数据库设置。

**delete**
> 删除数据库。

**type**
> 列出并查看可用的数据库类型和套餐。

# PARAMETERS

**--zone** _zone_
> Exoscale 可用区（如 ch-gva-2、de-fra-1、at-vie-1）。

**--plan** _plan_
> 服务套餐（如 hobbyist-2、startup-4、business-4）。

**--uri**
> 显示数据库服务的连接 URI。

**-O**, **--output-format** _FORMAT_
> 输出格式：table、json、text。

# DESCRIPTION

**exo dbaas** 用于管理 Exoscale 的数据库即服务（DBaaS）。支持 PostgreSQL、MySQL、Redis、OpenSearch、Kafka 以及其他托管数据库引擎。

DBaaS 提供完全托管的数据库实例，具备自动备份、监控、更新和高可用性。服务运行在专用基础设施上，并提供可配置的性能套餐。

该工具处理开通、配置更新和访问凭据管理，无需手动管理数据库服务器。

# INSTALL

```dnf: sudo dnf install exo```

```pacman: sudo pacman -S exo```

```apk: sudo apk add exoscale```

```nix: nix profile install nixpkgs#exo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exo](/man/exo)(1), [exo-compute](/man/exo-compute)(1), [exo-storage](/man/exo-storage)(1)
