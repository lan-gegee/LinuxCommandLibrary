# TAGLINE

ext2/ext3/ext4 文件系统备份工具

# TLDR

**备份文件系统到文件**

```dump -0uf [/backup/root.dump] [/dev/sda1]```

**带压缩备份**

```dump -0uf - [/] | gzip > [backup.dump.gz]```

**增量备份（级别 1）**

```dump -1uf [/backup/root.1.dump] [/]```

**备份到磁带设备**

```dump -0uf [/dev/st0] [/home]```

**列出 dump 归档中的文件**（借助 restore）

```restore -tf [backup.dump]```

# SYNOPSIS

**dump** [_options_] _filesystem_

# PARAMETERS

**-0** 至 **-9**
> 备份级别；0 为全量，1-9 为增量。

**-u**
> 备份成功后更新 /etc/dumpdates。

**-f** _file_
> 输出文件或设备。

**-a**
> 自动测长；跳过磁带长度计算。

**-h** _level_
> 对高于此级别的备份遵循 nodump 标志。

**-L** _label_
> dump 卷的标签。

**-z** _level_
> 用 zlib 压缩输出。

**-M**
> 多卷模式；提示更换磁带。

# CONFIGURATION

**/etc/dumpdates**
> 记录备份历史，跟踪备份级别和时间戳，用于增量备份管理。

**/etc/fstab**
> 定义文件系统挂载点，dump 借此按名称而非设备识别文件系统。

# DESCRIPTION

**dump** 用于创建 ext2/ext3/ext4 文件系统的备份。它在文件系统层面工作，直接读取磁盘块，因此能提供包含文件元数据和特殊文件的完整备份。

Dump 通过 0-9 级别支持增量备份。级别 0 是全量备份；更高级别只备份自上一个较低级别备份以来发生变化的文件。/etc/dumpdates 文件负责跟踪备份历史。

# DUMP LEVELS

```
Level 0: Full backup (all files)
Level 1: Files changed since level 0
Level 2: Files changed since level 1
...and so on
```

常见策略：每周做一次级别 0，每天做一次级别 1。

# CAVEATS

仅适用于特定文件系统；支持 ext2/3/4，但不支持 XFS 或 Btrfs。并非在所有情况下都能可靠地备份已挂载的文件系统。请使用 **restore** 命令恢复文件。现代替代方案如 rsync 或 borg 可能更受青睐。

# HISTORY

dump 的历史可追溯到 **20 世纪 70 年代** **贝尔实验室**的早期 Unix。它是最早的备份工具之一，为磁带备份而设计。Linux 版本（dump/restore）改编自 4.4BSD，延续了传统接口，同时支持现代 ext 文件系统。

# INSTALL

```apt: sudo apt install dump```

```dnf: sudo dnf install dump```

```zypper: sudo zypper install dump```

```nix: nix profile install nixpkgs#dump```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [rsync](/man/rsync)(1), [dd](/man/dd)(1)
