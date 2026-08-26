# TAGLINE

带文件历史的反向差异备份

# TLDR

将本地目录**备份**到本地目标

```rdiff-backup [source/] [backup/]```

通过 SSH 将本地目录**备份**到**远程**主机

```rdiff-backup [source/] [user@host::backup/]```

从备份中**恢复**最新版本

```rdiff-backup -r now [backup/] [restore/]```

**恢复****指定时间前**的文件

```rdiff-backup -r [3D] [backup/] [restore/]```

**列出**所有备份增量及其日期

```rdiff-backup --list-increments [backup/]```

**移除****早于**给定时段的备份增量

```rdiff-backup --remove-older-than [2W] [backup/]```

**验证**备份仓库的完整性

```rdiff-backup --verify [backup/]```

**备份**时排除特定模式

```rdiff-backup --exclude '[**/*.tmp]' [source/] [backup/]```

# SYNOPSIS

**rdiff-backup** [_-r time_] [_options_] _source_ _destination_

# PARAMETERS

**-r**, **--restore-as-of** _TIME_
> 从指定时间恢复。

**--list-increments**
> 显示备份历史。

**--remove-older-than** _TIME_
> 删除旧的增量。

**--verify**
> 验证备份完整性。

**--include** _PATTERN_
> 包含文件。

**--exclude** _PATTERN_
> 排除文件。

**-v**, **--verbosity** _N_
> 详细程度。

**--force**
> 强制执行操作，即使目标目录非空或增量已损坏。

**--print-statistics**
> 备份后打印文件传输统计信息。

# TIME FORMATS

**now** - 当前时间
**3D** - 3 天前
**2W** - 2 周前
**1M** - 1 个月前
**2025-01-15** - 具体日期
**2025-01-15T14:30:00** - 具体日期和时间

# DESCRIPTION

**rdiff-backup** 使用反向差异创建增量备份。目标端镜像当前状态，同时保存历史。

每次备份只存储与上一次的差异。适合频繁备份，节省空间。

可以从历史中的任意时点恢复。应用差异即可重建旧状态。

远程备份通过 SSH 进行。无需特殊的服务器，只要两端都装有 rdiff-backup 即可。

保留策略会移除旧增量。可在历史深度与存储空间之间权衡。

# CAVEATS

远程备份要求本地和远程机器都安装 rdiff-backup。首次完整备份可能很大且耗时。元数据变化（权限、所有者）即使文件内容不变也会触发增量更新。

# HISTORY

**rdiff-backup** 将 rsync 风格的镜像与反向差异版本管理结合在一起。它在提供省空间的增量备份的同时保持了恢复的便捷性。

# INSTALL

```apt: sudo apt install rdiff-backup```

```dnf: sudo dnf install rdiff-backup```

```apk: sudo apk add rdiff-backup```

```zypper: sudo zypper install rdiff-backup```

```brew: brew install rdiff-backup```

```nix: nix profile install nixpkgs#rdiff-backup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [borgbackup](/man/borgbackup)(1), [duplicity](/man/duplicity)(1), [restic](/man/restic)(1), [tar](/man/tar)(1)
