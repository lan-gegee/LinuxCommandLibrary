# TAGLINE

可靠的 PostgreSQL 备份与恢复工具

# TLDR

为 PostgreSQL 集群**初始化新的 stanza**

```pgbackrest --stanza=[name] stanza-create```

**校验**数据库与归档配置是否正确

```pgbackrest --stanza=[name] check```

**创建全量备份**

```pgbackrest --stanza=[name] --type=full backup```

**创建增量备份**

```pgbackrest --stanza=[name] --type=incr backup```

将最新备份**恢复到 PGDATA**

```pgbackrest --stanza=[name] restore```

**恢复到特定时间点**

```pgbackrest --stanza=[name] --type=time --target="[2026-04-27 12:00:00]" restore```

**显示仓库中备份的信息**

```pgbackrest --stanza=[name] info```

按照保留策略使旧备份和归档 WAL **过期**

```pgbackrest --stanza=[name] expire```

# SYNOPSIS

**pgbackrest** [_options_] _command_

# PARAMETERS

**backup**
> 为 PostgreSQL 集群创建全量、差异或增量备份。

**restore**
> 恢复备份，可选恢复到特定时间、名称、xid、LSN 或命名恢复目标。

**archive-push**
> 将一个 WAL 段推送到仓库（由 PostgreSQL 的 **archive_command** 调用）。

**archive-get**
> 在恢复期间从仓库获取 WAL 段（由 **restore_command** 调用）。

**stanza-create**
> 初始化新 stanza，为集群创建仓库布局。

**stanza-upgrade**
> 在 PostgreSQL 大版本升级之后更新 stanza 元数据。

**stanza-delete**
> 移除 stanza 及其全部备份和 WAL。

**check**
> 校验配置、归档命令以及仓库的可访问性。

**info**
> 显示单个或全部 stanza 的备份与归档信息。

**verify**
> 校验仓库中备份与 WAL 的完整性。

**expire**
> 应用保留策略，移除过期备份和已归档 WAL。

**repo-ls**, **repo-get**
> 直接列出或获取仓库中的文件。

**server**, **server-ping**, **start**, **stop**
> 管理 pgBackRest 服务器（用于基于 TLS 的远程仓库）。

**annotate**
> 为备份添加、修改或删除自由格式的注解。

**--stanza** _name_
> 要操作的 stanza（PostgreSQL 集群）。

**--type** _full|diff|incr|time|name|xid|lsn|immediate|default|standby_
> 备份类型（full/diff/incr）或恢复的恢复目标类型。

**--target** _value_
> **--type=time/name/xid/lsn** 恢复的目标值。

**--config** _file_
> 替代 pgbackrest.conf 的路径。

**--config-path** _dir_
> 配置文件的基础目录。

**--repo** _N_
> 配置了多个仓库时选择特定仓库。

**--process-max** _N_
> 压缩与传输的最大并行进程数。

**--compress-type** _none|gz|lz4|zst|bz2_
> 备份和 WAL 使用的压缩算法。

**--log-level-console** _off|error|warn|info|detail|debug|trace_
> 控制台日志的详细程度。

**--delta**
> 只恢复与备份不同的文件（让重复恢复更快）。

# DESCRIPTION

**pgBackRest** 是一款面向大规模可靠性设计的 PostgreSQL 备份与恢复方案。它支持全量、差异和增量备份、并行处理、硬件加速压缩（gz、lz4、zstd）、本地与远程仓库，以及包括文件系统、S3、Azure Blob 和 Google Cloud Storage 在内的存储后端。备份可以端到端校验，并可借助 PostgreSQL 的恢复设施还原到某个时间点。

其操作围绕 **stanza** 组织，一个 stanza 代表一个 PostgreSQL 集群及其备份仓库。执行 **stanza-create** 之后，需将 **postgresql.conf** 中的 **archive_command** 设为 **pgbackrest --stanza=name archive-push %p**，这样每个 WAL 段都会被传送到仓库。随后 **backup** 捕获数据目录，并与归档的 WAL 相配对，从而通过 **restore** 实现时间点恢复。

pgBackRest 以 C 语言实现，历史上带有一层小型 Perl 辅助代码；现代版本已是纯 C 实现。它被广泛部署于 PostgreSQL operator 技术栈（Crunchy Data、CloudNativePG、Zalando），也常见于 pg_basebackup 无法满足需求的生产数据库环境。

# CAVEATS

**stanza** 名称必须与 **archive_command** 中使用的值以及每个访问仓库的主机上使用的值一致。PostgreSQL 大版本升级后忘记运行 **stanza-upgrade** 会导致 stanza 与新集群不一致。恢复操作具有破坏性：默认会覆盖 **PGDATA**，拿不准时应使用 **--delta** 或恢复到空目录。如果使用了仓库加密密钥，必须将其另行备份——丢失密钥会使备份无法读取。

# CONFIGURATION

**/etc/pgbackrest/pgbackrest.conf**（或 **/etc/pgbackrest.conf**）
> 默认配置文件。定义 stanza、仓库位置、保留策略、加密、压缩以及 PostgreSQL 连接信息。

**[global]** 区段
> 进程级默认值：**repo1-path**、**repo1-cipher-type**、**process-max**、**log-level-***、**compress-type**。

**[stanza-name]** 区段
> 每个 stanza 的设置：**pg1-path**、**pg1-host**、**pg1-port**、**pg1-user**，以及 **repo1-retention-full** 等保留策略覆盖项。

# HISTORY

**pgBackRest** 由 **Crunchy Data** 的 **David Steele** 创建，首次发布于 **2013 年**，旨在成为比基于 **pg_basebackup** 的备份工作流更具扩展性的替代方案。最初用 Perl 编写，后来出于性能考虑逐步用 **C** 重写，到 **2.0** 版本时迁移已基本完成。它已成为生产环境 PostgreSQL 备份的事实标准，并被主要的 PostgreSQL Kubernetes operator 内置支持。

# INSTALL

```apt: sudo apt install pgbackrest```

```pacman: sudo pacman -S pgbackrest```

```apk: sudo apk add pgbackrest```

```zypper: sudo zypper install pgbackrest```

```brew: brew install pgbackrest```

```nix: nix profile install nixpkgs#pgbackrest```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_basebackup](/man/pg_basebackup)(1), [pg_dump](/man/pg_dump)(1), [postgres](/man/postgres)(1)
