# TAGLINE

支持压缩和加密的去重备份工具

# TLDR

**初始化**仓库

```borg init --encryption=[repokey] [/path/to/repo]```

**创建**备份

```borg create [/path/to/repo::backup-{now}] [/path/to/data]```

**列出**归档

```borg list [/path/to/repo]```

**解压**备份

```borg extract [/path/to/repo::backup-name]```

**检查**仓库

```borg check [/path/to/repo]```

**修剪**旧备份

```borg prune --keep-daily [7] --keep-weekly [4] [/path/to/repo]```

**压缩整理**仓库以真正释放被修剪的空间

```borg compact [/path/to/repo]```

**挂载**归档以便像文件系统一样浏览

```borg mount [/path/to/repo::backup-name] [/mnt/point]```

# SYNOPSIS

**borg** _command_ [_options_]

# DESCRIPTION

**borg**（BorgBackup）是一款带压缩和认证加密的去重备份程序。它通过共享相同的数据块来高效存储多个备份，非常适合对大型数据集进行频繁备份。

该工具为本地和远程备份提供安全性、效率和可靠性。

# PARAMETERS

**init**
> 初始化仓库。

**create**
> 创建新归档。

**extract**
> 解压归档内容。

**list**
> 列出归档或内容。

**diff**
> 比较归档。

**delete**
> 删除归档。

**prune**
> 按保留策略删除旧归档。

**compact**
> 释放由 prune 或 delete 腾出的仓库空间（在修剪之后运行）。

**info**
> 显示归档/仓库信息。

**mount**
> 将归档挂载为文件系统。

**check**
> 验证仓库一致性。

# ENCRYPTION MODES

**repokey**
> 密钥存储在仓库中。

**keyfile**
> 密钥存储在本地。

**none**
> 不加密。

**authenticated**
> 仅认证（不加密）。

# WORKFLOW

```bash
# Initialize repository
borg init --encryption=repokey /backup/repo

# Create first backup
borg create /backup/repo::monday /home/user

# Create incremental backup (automatic deduplication)
borg create /backup/repo::tuesday /home/user

# List backups
borg list /backup/repo

# Restore
borg extract /backup/repo::monday

# Mount for browsing
borg mount /backup/repo::monday /mnt/backup

# Prune old backups
borg prune --keep-daily=7 --keep-weekly=4 /backup/repo

# Reclaim the space freed by prune
borg compact /backup/repo
```

# FEATURES

**去重**
> 块级去重可在多个归档之间共享相同数据。

**压缩**
> 支持 lz4、zstd、zlib 和 lzma。

**加密**
> 基于 repokey 或 keyfile 模式的认证 AES 加密。

**远程备份**
> 通过 SSH 将备份推送到远程仓库。

**其他**
> 稀疏文件支持、基于 FUSE 的归档挂载、数据验证和高效存储。

# CAVEATS

仓库损坏可能导致所有备份丢失（请保留异地副本）。加密密钥丢失意味着数据永久丢失。大型仓库需要大量内存用于缓存。远程仓库需要 SSH 连接。检查操作可能较慢。

# HISTORY

**BorgBackup** 由 Thomas Waldmann 于 **2015 年**作为 Attic 备份的分支创建，专注于性能、安全性和可靠性。

# INSTALL

```apt: sudo apt install borgbackup```

```dnf: sudo dnf install borgbackup```

```pacman: sudo pacman -S borg```

```apk: sudo apk add borgbackup```

```zypper: sudo zypper install borgbackup```

```brew: brew install borgbackup```

```nix: nix profile install nixpkgs#borgbackup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restic](/man/restic)(1), [duplicity](/man/duplicity)(1), [rsync](/man/rsync)(1)

# RESOURCES

```[Source code](https://github.com/borgbackup/borg)```

```[Homepage](https://www.borgbackup.org)```

```[Documentation](https://borgbackup.readthedocs.io)```

<!-- verified: 2026-06-19 -->
