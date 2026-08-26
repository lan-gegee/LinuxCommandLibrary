# TAGLINE

支持压缩和加密的去重备份工具

# TLDR

**初始化新的备份仓库**

```borg init --encryption=repokey [/path/to/repo]```

**创建备份**

```borg create [/path/to/repo]::[archive_name] [/path/to/source]```

**创建带压缩和统计信息的备份**

```borg create --stats --compression lz4 [/path/to/repo]::[archive_name] [/path/to/source]```

**列出仓库中的归档**

```borg list [/path/to/repo]```

**列出归档的内容**

```borg list [/path/to/repo]::[archive_name]```

**解压归档**

```borg extract [/path/to/repo]::[archive_name]```

**显示仓库信息**，包括存储用量和加密细节

```borg info [/path/to/repo]```

**删除旧归档**，保留最近 7 个每日备份和 4 个每周备份

```borg prune --keep-daily=7 --keep-weekly=4 [/path/to/repo]```

**将归档挂载为文件系统**

```borg mount [/path/to/repo]::[archive_name] [/mnt/point]```

# SYNOPSIS

**borg** _command_ [_options_] [_repository_]

# PARAMETERS

**init**
> 初始化新的备份仓库。

**create**
> 创建新的备份归档。

**list**
> 列出仓库内容或归档中的文件。

**extract**
> 从归档中提取文件。

**delete**
> 删除归档。

**prune**
> 根据保留策略删除归档。

**mount** / **umount**
> 将归档挂载/卸载为 FUSE 文件系统。

**info**
> 显示归档或仓库信息。

**check**
> 验证仓库一致性。

**--encryption** _mode_
> 加密模式：none、repokey、keyfile。

**--compression** _algo_
> 压缩算法：none、lz4、zstd、zlib、lzma。

**--exclude** _pattern_
> 排除匹配模式的文件。

**--progress**
> 在操作过程中显示进度。

**-v**, **--verbose**
> 提高输出详细程度。

**--stats**
> 打印所创建归档的统计信息（文件数、大小、去重率）。

**--list**
> 在 create 或 extract 处理过程中输出文件列表。

**--dry-run**
> 执行试运行，不做任何更改（create、prune、delete 支持）。

**--remote-path** _path_
> 设置远程主机上 borg 可执行文件的路径。

# DESCRIPTION

**Borg**（BorgBackup）是一款带压缩和加密功能的去重备份程序。它通过识别并复用重复的数据块来高效存储多个备份，大幅减少增量备份所需的存储空间。

主要特性包括确保只有你能读取数据的**客户端加密**、在每个归档中只存储一次唯一数据块的**高效去重**，以及进一步降低存储需求的**压缩**。

Borg 可以备份到本地目录、通过 SSH 备份到远程主机，或通过 rclone 备份到云存储。归档可以通过 FUSE 挂载，便于浏览和选择性恢复。保留策略会自动修剪旧归档。

# CAVEATS

仓库格式是 Borg 专有的；其他工具无法读取这些归档。加密密钥必须单独备份——丢失密钥意味着无法再访问备份。远程备份需要 SSH 访问权限且两端都安装 Borg。去重在同一个仓库内的所有归档之间进行，而不是跨仓库进行。

# HISTORY

BorgBackup 于 **2015 年**从 **Attic** 分叉而来，当时 Attic 的开发已陷入停滞。"Borg" 这个名字致敬《星际迷航》中以同化和高效组织著称的博格人。分叉后开发加速，陆续加入了认证加密、改进的压缩以及 macOS/Windows 支持等特性。Borg 已成为最受欢迎的开源备份方案之一。

# INSTALL

```apt: sudo apt install borgbackup```

```dnf: sudo dnf install borgbackup```

```zypper: sudo zypper install borgbackup```

```brew: brew install borgbackup```

```nix: nix profile install nixpkgs#borgbackup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restic](/man/restic)(1), [duplicity](/man/duplicity)(1), [rsync](/man/rsync)(1), [rclone](/man/rclone)(1), [rdiff-backup](/man/rdiff-backup)(1), [tar](/man/tar)(1)
