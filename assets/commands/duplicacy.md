# TAGLINE

无锁的去重云备份工具

# TLDR

**初始化仓库**并使用本地存储

```duplicacy init [snapshot_id] [/path/to/storage]```

**使用云存储初始化**（S3、B2 等）

```duplicacy init [snapshot_id] [s3://bucket/path]```

**创建备份**

```duplicacy backup```

**列出所有快照**

```duplicacy list```

**从最新快照恢复文件**

```duplicacy restore```

**从指定版本恢复**

```duplicacy restore -r [revision_number]```

**清理旧快照**，保留最近 N 个

```duplicacy prune -keep [0:365] -keep [7:30] -keep [1:7]```

**检查仓库完整性**

```duplicacy check```

# SYNOPSIS

**duplicacy** _command_ [_options_] [_arguments_]

# PARAMETERS

**init** _snapshot_id storage_
> 用指定的快照 ID 和存储位置初始化新仓库。

**backup** [_-stats_] [_-threads n_] [_-hash_] [_-t tag_]
> 创建新的备份快照。

**restore** [_-r revision_] [_-overwrite_] [_-delete_]
> 从快照恢复文件。

**list** [_-all_] [_-id snapshot_id_] [_-files_]
> 列出可用快照。

**prune** [_-keep spec_] [_-id snapshot_id_]
> 按保留策略删除旧快照。

**check** [_-files_] [_-stats_]
> 校验仓库完整性。

**diff** [_-r revision_]
> 显示快照之间的差异。

**cat** _file_ [_-r revision_]
> 打印快照中某个文件的内容。

**-encrypt**
> 为仓库启用加密。

**-threads** _n_
> 并发线程数。

**-stats**
> 显示详细统计信息。

**-verbose**
> 启用详细输出。

**-d**
> 启用调试日志。

# DESCRIPTION

**Duplicacy** 是一款跨平台备份工具，以无锁去重为核心特性。它采用变长分块把文件切分成块，并在所有备份之间去重，显著降低了相似数据的存储需求。

它的独特之处在于无锁设计：多台计算机可以同时向同一存储备份而无需协调。每个客户端独立运行，因此 Duplicacy 非常适合把多台机器备份到共享的云存储。

该工具支持众多存储后端，包括本地磁盘、SFTP、WebDAV 和各类云服务（AWS S3、Backblaze B2、Google Cloud、Azure、Wasabi 等）。客户端加密保证了即使存储不可信，数据隐私也不受影响。

Duplicacy 采用双仓库模型：工作目录（源）和存储（目的地）。多个工作目录可以共享同一个存储，从而受益于跨机器去重。prune 命令通过分层 keep 规则实现灵活的保留策略。

# CAVEATS

免费 CLI 版本功能受限；部分特性需要许可证。去重效果因数据类型而异。大数据集的首次备份耗时较长。恢复速度取决于 chunk 在存储中的分布情况。某些云存储操作会产生 API 费用。

# HISTORY

**Duplicacy** 由 Gilbert Chen 于 **2016 年**前后创建，是一个专注于去重和云存储的现代备份方案。无锁设计正是针对 Duplicity 之类工具的局限——并发备份需要协调——做出的回应。它同时提供 CLI（开源）和 GUI（商业）两个版本。

# INSTALL

```nix: nix profile install nixpkgs#duplicacy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restic](/man/restic)(1), [borg](/man/borg)(1), [rclone](/man/rclone)(1), [duplicity](/man/duplicity)(1)
