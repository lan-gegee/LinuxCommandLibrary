# TAGLINE

将 Git 对象和引用存储在 PostgreSQL 中

# TLDR

在数据库中**初始化**新仓库

```gitgres-backend init "[dbname=gitgres]" [repo_name]```

**将本地 Git 仓库推送**进 PostgreSQL

```gitgres-backend push "[dbname=gitgres]" [repo_name] [path/to/repo]```

把数据库中的仓库**克隆**回磁盘

```gitgres-backend clone "[dbname=gitgres]" [repo_name] [path/to/dest]```

**列出数据库中存储的引用**

```gitgres-backend ls-refs "[dbname=gitgres]" [repo_name]```

无需编译后端即可**导入现有仓库**

```./import/gitgres-import.sh [path/to/repo] "[dbname=gitgres]" [repo_name]```

# SYNOPSIS

**gitgres-backend** _command_ _connection_string_ _repo_name_ [_path_]

# DESCRIPTION

**gitgres** 将 Git 对象和引用作为行存储在 **PostgreSQL** 表中。一个基于 **libgit2** 的小型后端（**gitgres-backend**）将标准 Git 协议操作（如 **push** 和 **clone**）转换为 SQL，使现有 Git 客户端可以直接面向数据库而非文件系统工作。

项目的既定目标是让 Git 托管平台（如 **Forgejo**、**Gitea**）完全抛弃文件系统存储，改由数据库承载仓库、对象、引用和 reflog。其数据库模式包含仓库、对象、引用和 reflog 相关表，并提供哈希、对象存储以及树与提交解析等辅助功能。

# COMMANDS

**init** _conn_ _repo_
> 创建所需的数据库表（如有必要）并注册名为 _repo_ 的新仓库。

**push** _conn_ _repo_ _path_
> 将位于 _path_ 的磁盘 Git 仓库推送到数据库中，命名为 _repo_。

**clone** _conn_ _repo_ _path_
> 将数据库中的仓库 _repo_ 实体化为位于 _path_ 的普通磁盘 Git 仓库。

**ls-refs** _conn_ _repo_
> 打印数据库中当前为 _repo_ 存储的引用。

# REQUIREMENTS

需要带有 **pgcrypto** 扩展的 **PostgreSQL**。后端链接了 **libgit2**、**libpq** 和 **OpenSSL**。基于 shell 的导入器（_./import/gitgres-import.sh_）只需要一个可用的 **psql** 客户端和一个 Git 检出副本。

# CAVEATS

该项目尚处于研究阶段：将仓库存入 PostgreSQL 会带来不同于文件系统的 I/O 与锁行为。其性能、清理（vacuum）和复制特性与传统 Git 托管不同，在生产使用前应先做基准测试。备份必须包含数据库转储，而不是工作树。

# HISTORY

**gitgres** 由 **Andrew Nesbitt** 创建，旨在探索消除 Git 托管平台对文件系统的依赖，动机是让元数据和 Git 数据共用单一后端存储（PostgreSQL）从而简化运维。

# SEE ALSO

[git](/man/git)(1), [psql](/man/psql)(1)
