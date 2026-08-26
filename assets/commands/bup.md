# TAGLINE

基于 Git、支持去重的备份系统

# TLDR

**在默认位置（~/.bup）初始化** bup 仓库

```bup init```

**在自定义目录中初始化**仓库

```BUP_DIR=[/path/to/repo] bup init```

**为备份建立文件索引**

```bup index [/path/to/backup]```

**保存**已建立索引的备份并命名

```bup save -n [backup-name] [/path/to/backup]```

**列出**所有备份

```bup ls```

**列出**特定备份中的文件

```bup ls [backup-name]/latest/```

**恢复**文件到目标目录

```bup restore -C [/restore/path] [backup-name/latest/path]```

**检查**仓库完整性

```bup fsck```

# SYNOPSIS

**bup** _command_ [_options_]

# DESCRIPTION

**bup** 是一个基于 git packfile 格式的备份系统。它通过去重提供非常高效的存储：将大文件拆分为数据块，并使用滚动校验和来发现重复数据。

该工具对备份只有少量改动的大文件尤其有效。

# PARAMETERS

**init**
> 初始化 bup 仓库。默认使用 ~/.bup，若设置了 BUP_DIR 则使用它。

**index** _path_
> 为备份建立文件索引。必须在 save 之前运行。

**save** **-n** _name_ _path_
> 将已建立索引的文件保存为命名备份集。

**restore** **-C** _target_ _backup-path_
> 将备份中的文件恢复到目标目录。

**ls** [_backup_]
> 列出备份或某个备份内的文件。

**fsck**
> 检查仓库完整性。

**fuse** _mountpoint_
> 将备份挂载为只读的 FUSE 文件系统。

**damage**
> 故意损坏仓库，用于测试 fsck。

**margin**
> 报告对象之间匹配前缀位的最大数量。

**midx**
> 创建或显示 midx（多索引）文件。

**memtest**
> 测试内存吞吐量。

**web**
> 启动一个 Web 服务器以浏览备份。

# ENVIRONMENT

**BUP_DIR**
> bup 仓库的路径。默认为 ~/.bup。

**BUP_FORCE_TTY**
> 即使不在终端中也强制输出进度信息。

# WORKFLOW

```bash
# Initialize (in ~/.bup by default)
export BUP_DIR=/backup/bup-repo
bup init

# Index files
bup index ~/Documents

# Save backup
bup save -n documents ~/Documents

# List backups
bup ls

# List files in backup
bup ls documents/latest/

# Restore
bup restore -C ~/restored documents/latest/

# Mount as filesystem
mkdir /mnt/bup
bup fuse /mnt/bup

# Remote backup over SSH
bup init -r myserver:
bup save -r myserver: -n documents ~/Documents
```

# DEDUPLICATION

使用滚动校验和识别重复的数据块，即使它们在文件内发生了位移。对以下场景特别高效：
- 虚拟机镜像
- 大型归档
- 数据库备份
- 版本控制仓库

# CAVEATS

默认不加密。缺乏维护时仓库可能变得很大。大量小文件的恢复速度较慢。不如 borg/restic 成熟。文档有时不够完善。不适合海量微小文件。没有内置的旧备份清理功能。

# HISTORY

**bup** 由 Avery Pennarun 在 **2010 年**前后创建，旨在为大型文件提供类似 git 的高效去重备份。

# INSTALL

```apt: sudo apt install bup```

```pacman: sudo pacman -S bup```

```zypper: sudo zypper install bup```

```brew: brew install bup```

```nix: nix profile install nixpkgs#bup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[borg](/man/borg)(1), [restic](/man/restic)(1), [git](/man/git)(1), [rsync](/man/rsync)(1), [tar](/man/tar)(1)
