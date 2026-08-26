# TAGLINE

快速的加密去重备份工具

# TLDR

**初始化仓库**

```rustic init```

**创建备份**

```rustic backup [path/to/backup]```

**列出快照**

```rustic snapshots```

**恢复快照**

```rustic restore [snapshot_id] [target/]```

**遗忘旧快照**

```rustic forget --keep-daily [7] --keep-weekly [4]```

**清理未使用的数据**

```rustic prune```

**检查仓库**

```rustic check```

**挂载仓库**

```rustic mount [mountpoint/]```

# SYNOPSIS

**rustic** [_-r repository_] [_options_] _command_ [_args_]

# PARAMETERS

**-r**, **--repo** _PATH_
> 仓库位置。

**-p**, **--password** _PASS_
> 仓库密码。

**--password-file** _FILE_
> 密码文件。

**-v**, **--verbose**
> 详细输出。

**--dry-run**
> 仅模拟执行。

# COMMANDS

**init**
> 创建仓库。

**backup**
> 创建备份。

**snapshots**
> 列出快照。

**restore**
> 恢复数据。

**forget**
> 移除快照。

**prune**
> 删除未使用的数据。

**check**
> 校验完整性。

# DESCRIPTION

**rustic** 是一个用 Rust 编写的快速备份工具，与 restic 的仓库格式完全兼容。它提供加密的去重备份，采用带认证标签的 AES-256 加密，确保静态数据的机密性与完整性。

该工具使用基于内容的分块和去重技术，只存储唯一的数据块，显著降低增量备份的存储需求。它支持多种存储后端，包括本地文件系统、S3 兼容对象存储、SFTP 和 REST 服务器。

通过 **forget** 配合保留规则（daily、weekly、monthly）指定的保留策略可以自动清理快照。**prune** 命令通过删除不再被任何快照引用的数据块来回收空间。

# CONFIGURATION

**~/.config/rustic/rustic.toml**
> 主配置文件，定义默认仓库位置、密码来源、备份路径和保留策略。

**RUSTIC_REPOSITORY**
> 指定默认仓库位置的环境变量。

**RUSTIC_PASSWORD**
> 提供仓库密码的环境变量。

# CAVEATS

是 restic 的独立实现。仓库格式兼容。部分功能可能存在差异。

# HISTORY

**Rustic** 作为 **restic** 的 Rust 重写版而诞生，以获得更好的性能。它与 restic 仓库保持兼容。

# INSTALL

```pacman: sudo pacman -S rustic```

```brew: brew install rustic```

```nix: nix profile install nixpkgs#rustic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restic](/man/restic)(1), [borgbackup](/man/borgbackup)(1), [duplicacy](/man/duplicacy)(1)
