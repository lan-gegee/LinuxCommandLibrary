# TAGLINE

快速安全的去重备份工具

# TLDR

**初始化仓库**

```restic -r [/path/to/repo] init```

**备份目录**

```restic -r [/path/to/repo] backup [/path/to/data]```

**列出快照**

```restic -r [/path/to/repo] snapshots```

**从最新快照恢复**

```restic -r [/path/to/repo] restore latest --target [/path/to/restore]```

**恢复指定快照**

```restic -r [/path/to/repo] restore [snapshot_id] --target [/path/to/restore]```

**检查仓库完整性**

```restic -r [/path/to/repo] check```

**移除旧快照**（保留最近 7 个每日快照）

```restic -r [/path/to/repo] forget --keep-daily [7] --prune```

**备份到 S3**

```restic -r s3:s3.amazonaws.com/[bucket_name] backup [/path/to/data]```

将快照**挂载**为文件系统

```restic -r [/path/to/repo] mount [/mnt/restic]```

# SYNOPSIS

**restic** [_global options_] _command_ [_options_] [_arguments_]

# DESCRIPTION

**restic** 是一个快速、安全且高效的备份程序。它为你的数据创建加密、去重的快照，可保存到本地或远程仓库，包括本地磁盘、SFTP、S3、Azure、Google Cloud Storage 等。

每次备份都会创建一个包含该时刻文件状态的快照。Restic 使用基于内容的分块进行去重，这意味着相同的数据在所有快照中只存储一次。所有数据都使用 AES-256 加密。

恢复操作可以针对整个快照或特定文件。mount 命令允许将快照作为 FUSE 文件系统浏览。

# PARAMETERS

**-r** _repo_, **--repo** _repo_
> 仓库位置。

**-p** _file_, **--password-file** _file_
> 包含仓库密码的文件。

**--verbose**
> 详细输出。

**init**
> 初始化新仓库。

**backup**
> 创建新快照。

**restore**
> 从快照解压文件。

**snapshots**
> 列出所有快照。

**forget**
> 移除快照（需要 --prune 才能释放空间）。

**prune**
> 移除未引用的数据。

**check**
> 验证仓库完整性。

**mount**
> 将仓库挂载为 FUSE 文件系统。

**--exclude** _pattern_
> 排除匹配模式的文件。

**--keep-last** _n_
> 保留最近 n 个快照。

**--keep-daily** _n_
> 保留 n 个每日快照。

# CAVEATS

仓库密码一旦丢失无法找回。首次备份较慢（由于去重，后续备份很快）。不带 prune 的 forget 不会释放空间。某些后端需要通过环境变量提供凭据。

# HISTORY

**restic** 由 **Alexander Neumann** 于 **2014 年**创建，是针对现有工具不足之处的现代备份解决方案。它使用 Go 编写，设计时以安全、去重和云存储支持为主要目标。该项目凭借简洁性和可靠性广受欢迎，成为 duplicity 等工具的推荐替代品。

# INSTALL

```apt: sudo apt install restic```

```dnf: sudo dnf install restic```

```pacman: sudo pacman -S restic```

```apk: sudo apk add restic```

```zypper: sudo zypper install restic```

```brew: brew install restic```

```nix: nix profile install nixpkgs#restic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[duplicity](/man/duplicity)(1), [borg](/man/borg)(1), [rsync](/man/rsync)(1), [rclone](/man/rclone)(1)
