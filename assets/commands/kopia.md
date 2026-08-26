# TAGLINE

快速、安全的备份工具，具备加密、去重和压缩功能

# TLDR

**创建本地仓库**

```kopia repository create filesystem --path [/path/to/repo]```

**连接已有仓库**

```kopia repository connect filesystem --path [/path/to/repo]```

**创建备份快照**

```kopia snapshot create [/path/to/backup]```

**列出所有快照**

```kopia snapshot list```

**将快照恢复到目录**

```kopia restore [snapshot_id] [/path/to/restore]```

**将快照挂载为 FUSE 文件系统**

```kopia mount all [/mnt/kopia]```

**显示仓库状态**

```kopia repository status```

**设置保留策略**

```kopia policy set --keep-latest [10] --keep-daily [7] [/path/to/backup]```

# SYNOPSIS

**kopia** _command_ [_options_]

# PARAMETERS

**repository create** _type_
> 创建新仓库（filesystem、s3、b2、gcs、azure、sftp 等）。

**repository connect** _type_
> 连接已有仓库。

**repository status**
> 显示仓库连接状态。

**snapshot create** _path_
> 创建备份快照。

**snapshot list** [_path_]
> 列出快照，可按来源过滤。

**restore** _id_ _target_
> 将快照恢复到目录。

**mount** _snapshots_ _mountpoint_
> 将快照挂载为 FUSE 文件系统。

**policy set** [_options_] [_path_]
> 设置备份与保留策略。

**policy show** [_path_]
> 显示生效的策略。

**maintenance run**
> 运行仓库维护。

**server start**
> 启动 Kopia 服务器（UI 和 API）。

**--password** _pass_
> 仓库密码。

**--config-file** _path_
> 使用备用配置文件。

# DESCRIPTION

**Kopia** 是一款快速、安全的备份工具，具备加密、去重和压缩功能。它支持多种存储后端，包括本地文件系统、云存储（S3、B2、GCS、Azure）和 SFTP 服务器。

备份数据在离开你的机器之前就会用 AES-256-GCM 进行客户端加密。内容定义分块让所有快照之间都能高效去重。压缩则进一步降低存储需求。

快照模型提供时间点备份。每个快照都会连同元数据一起捕获目录状态。增量备份只存储发生变化的数据，但每个快照在逻辑上都是完整的——你可以独立恢复任意一个快照。

策略按目录控制备份行为：压缩、调度、保留（保留多少份快照）以及文件排除规则。策略会从全局级联到具体路径。

可选的服务器组件提供 Web UI，用于浏览快照、监控备份状态和管理策略。它还可以作为多台机器的集中式备份服务器。

挂载功能允许把快照当作文件系统浏览，无需完整恢复即可进行文件级找回。

# CAVEATS

仓库密码一旦丢失无法找回——请妥善备份凭据。首次大型备份耗时较长。FUSE 挂载需要 FUSE 支持。某些存储后端可能产生 API 费用。去重效果取决于数据模式。

# HISTORY

**Kopia** 由 Jarek Kowalski 自 **2019 年**前后开始开发，是一款现代备份方案。其设计强调安全性（强制加密）、性能（Go 实现、并行处理）和灵活性（多种后端）。作为 Restic 和 Borg 的替代品，它凭借 Web UI 和跨平台支持获得了广泛使用。

# INSTALL

```zypper: sudo zypper install kopia```

```brew: brew install kopia```

```nix: nix profile install nixpkgs#kopia```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restic](/man/restic)(1), [borg](/man/borg)(1), [duplicacy](/man/duplicacy)(1), [rclone](/man/rclone)(1)
