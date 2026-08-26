# 备份与镜像

## 备份策略
好的备份遵循 **3-2-1 法则**：为数据保留 **3** 份副本，存放在 **2** 种不同类型的介质上，其中 **1** 份保存在异地。选用哪个工具取决于你要保护的对象。

| 目标 | 可选工具 |
|-----|-------------|
| **将文件同步到另一块磁盘** | `[rsync](/man/rsync)` |
| **带版本、去重的备份** | `[borg](/man/borg)`, `[restic](/man/restic)` |
| **克隆整块磁盘或分区** | `[dd](/man/dd)`, `[partclone](/man/partclone)` |
| **抢救正在故障的硬盘** | `[ddrescue](/man/ddrescue)` |
| **推送到云存储** | `[rclone](/man/rclone)` |
| **对运行中的文件系统做快照** | `[lvm](/man/lvm)`, `[btrfs](/man/btrfs)`, `[zfs](/man/zfs)` |

**定期演练恢复**——从未被恢复过的备份只是一个希望。

## 用 rsync 备份文件
`rsync` 只复制源与目标之间的差异，因此重复备份非常快。`-a`（归档）选项会保留权限、时间戳、符号链接和所有者信息。
```[rsync](/man/rsync) -a /home/user/ /mnt/backup/user/```
```[rsync](/man/rsync) -ah --info=progress2 /data/ /mnt/backup/data/```

加上 `--delete` 可以精确镜像源，把目标中已不存在于源的文件删除掉。
```[rsync](/man/rsync) -a --delete /data/ /mnt/backup/data/```

源路径末尾的斜杠很关键：`src/` 复制 src 的**内容**，而 `src` 复制 src 这个**目录**本身。

| 选项 | 说明 |
|-----|-------------|
| **-a** | 归档模式（保留元数据，递归） |
| **-v** | 详细输出 |
| **-z** | 传输过程中压缩数据 |
| **-h** | 人类可读的大小 |
| **--delete** | 删除目标中多余的文件 |
| **-n / --dry-run** | 显示将会发生什么，不做任何更改 |
| **--exclude** | 跳过匹配的路径 |
| **--progress** | 显示逐文件进度 |

**务必先试运行：**使用 `--delete` 时先加 `--dry-run`，确认不会清掉重要内容。

## 通过 SSH 备份
当 `rsync` 的任一端写成 `user@host:path` 形式时，传输会自动经 SSH 进行，依然只复制变化的部分。链路较慢时加 `-z` 压缩。
```[rsync](/man/rsync) -avz /data/ user@host:/backup/data/```
```[rsync](/man/rsync) -avz user@host:/var/www/ /mnt/backup/www/```

SSH 选项（如非标准端口）通过 `-e` 传入。
```[rsync](/man/rsync) -avz -e "[ssh](/man/ssh) -p 2222" /data/ user@host:/backup/data/```

只想快速一次性复制单个文件时，`scp` 更简单。
```[scp](/man/scp) backup.tar.gz user@host:/backup/```

## 增量快照
借助 `--link-dest`，`rsync` 会把未变化的文件硬链接到上一次备份，于是每个快照看起来都是完整的，却只为发生变化的文件占用额外空间。
```[rsync](/man/rsync) -a --delete --link-dest=/backup/prev /data/ /backup/2026-06-06/```

这样就能以增量备份的存储成本得到可浏览、按日期命名的快照。轮换的办法是让每次新备份指向前一天的目录。**rsnapshot** 用配置文件和保留级别把这套方案完全自动化。

## 归档备份
`tar` 归档把许多文件打包成一个，适合做时间点快照。配合压缩可以节省空间。
```[tar](/man/tar) czf backup-$(date +%F).tar.gz /home/user```
```[tar](/man/tar) xzf backup-2026-06-06.tar.gz```

对大型数据集，`zstd` 在相近甚至更好的压缩比下比 gzip 快得多。
```[tar](/man/tar) --zstd -cf backup.tar.zst /data```

`tar` 支持**增量**归档：`-g` 使用一个快照文件记录两次运行之间发生了什么变化。第一次是完整备份；之后用同一个快照文件运行就只存储变化。
```[tar](/man/tar) czf full.tar.gz -g backup.snar /data```
```[tar](/man/tar) czf incr1.tar.gz -g backup.snar /data```

恢复时先解压完整归档，再按顺序解压各个增量归档。

不用临时文件，直接把归档流式传送到远程主机。
```[tar](/man/tar) czf - /data | [ssh](/man/ssh) user@host "cat > /backup/data.tar.gz"```

`tar`、`gzip`、`xz` 和 `zstd` 的完整选项参见 **压缩与归档**基础页面。

## 快照与去重工具
专用备份程序在普通复制之上增加了去重、加密、压缩和保留策略。每个文件的块只存一次，因此重复执行备份代价很小。

| 工具 | 特点 |
|-----|-------------|
| `[borg](/man/borg)` | 去重、压缩、加密、可挂载的归档 |
| `[restic](/man/restic)` | 简单快速，内置多种云后端 |
| `[duplicity](/man/duplicity)` | 经 GPG 的加密增量备份 |
| `[bup](/man/bup)` | 基于 Git 的去重，擅长处理超大文件 |
| **rsnapshot** | rsync 加硬链接轮换，无需额外格式 |

初始化一个 `borg` 仓库，然后创建压缩且去重的归档。
```[borg](/man/borg) init --encryption=repokey /mnt/backup/repo```
```[borg](/man/borg) create --compression zstd /mnt/backup/repo::{now} /home/user```

`restic` 的用法相同，并且支持本地磁盘、SFTP、S3 等更多后端。
```[restic](/man/restic) -r /mnt/backup/repo init```
```[restic](/man/restic) -r /mnt/backup/repo backup /home/user```

用保留策略清理旧快照，避免备份无限增长。使用 `borg` 时，之后还要运行 `compact` 才能真正释放空间。
```[borg](/man/borg) prune --keep-daily=7 --keep-weekly=4 /mnt/backup/repo```
```[borg](/man/borg) compact /mnt/backup/repo```
```[restic](/man/restic) -r /mnt/backup/repo forget --keep-daily 7 --keep-weekly 4 --prune```

把某个快照解压到临时目录来测试恢复，或者挂载仓库直接浏览。
```[restic](/man/restic) -r /mnt/backup/repo restore latest --target /tmp/restore-test```
```[borg](/man/borg) mount /mnt/backup/repo /mnt/restore```

**仓库若已加密，备份的安全性就取决于密钥和口令。**导出密钥，把它存放在备份之外的地方。

## 数据库与活跃数据
在数据库写入中途直接复制其文件会得到损坏的备份。先转储出一份一致的快照，然后像普通文件一样备份这份转储。
```[mysqldump](/man/mysqldump) --all-databases > mysql-backup.sql```
```[pg_dumpall](/man/pg_dumpall) > postgres-backup.sql```
```[sqlite3](/man/sqlite3) app.db ".backup app-backup.db"```

对其他持续写入的东西（虚拟机磁盘、邮件队列）同理：让写入方停下、做转储，或基于文件系统快照来备份（见下文）。

## 磁盘与分区镜像
`dd` 按块复制数据，生成磁盘或分区的精确镜像。先用 `lsblk` 确认目标设备，再仔细核对。
```[lsblk](/man/lsblk)```
```[dd](/man/dd) if=/dev/sda of=/dev/sdb bs=4M status=progress```

不写入另一块磁盘，而是把分区保存为压缩的镜像文件。
```[dd](/man/dd) if=/dev/sda1 bs=4M status=progress | [gzip](/man/gzip) > sda1.img.gz```

把镜像还原回设备。
```[gunzip](/man/gunzip) -c sda1.img.gz | [dd](/man/dd) of=/dev/sda1 bs=4M status=progress```

**小心：**`dd` 指哪写哪，不做确认。`of=` 写错会立刻毁掉数据。设备名查两遍，然后再查一遍。只对已**卸载**的分区做镜像：对一个正在变化的文件系统做出来的镜像是不一致的。

| 选项 | 说明 |
|-----|-------------|
| **if=** | 输入文件或设备 |
| **of=** | 输出文件或设备 |
| **bs=** | 块大小（4M 是不错的默认值） |
| **status=progress** | 显示传输进度 |
| **conv=noerror,sync** | 遇读取错误继续进行，并填充数据块 |
| **conv=fsync** | 退出前刷写到设备 |
| **count=** | 只复制 N 个块 |

## 将镜像写入 USB
要把安装 ISO 写入 U 盘，用 `dd` 写入整个设备（而不是分区）。`conv=fsync` 确保命令返回前所有数据都已刷写完毕。
```[dd](/man/dd) if=distro.iso of=/dev/sdc bs=4M status=progress conv=fsync```

普通的 `cp` 和 `cat` 也能把镜像流式写入设备。
```[cp](/man/cp) distro.iso /dev/sdc && [sync](/man/sync)```

重新使用设备前，先擦除其上的旧文件系统签名。
```[wipefs](/man/wipefs) -a /dev/sdc```

## 高可靠镜像与恢复
硬盘开始故障时，用 `ddrescue` 替代 `dd`：它会重试坏扇区，先处理容易的区域，并保存映射文件以便日后续传。
```[ddrescue](/man/ddrescue) /dev/sda rescue.img rescue.map```
```[ddrescue](/man/ddrescue) -r3 /dev/sda rescue.img rescue.map```

`partclone` 只对文件系统**已使用**的块做镜像，因此比对近乎空白的分区整块执行 `dd` 更快、产物也更小。用 `-c` 创建镜像，用 `-r` 还原。
```[partclone](/man/partclone).ext4 -c -s /dev/sda1 -o sda1.img```
```[partclone](/man/partclone).ext4 -r -s sda1.img -o /dev/sda1```

`clonezilla` 把这些工具整合成一个带向导的磁盘克隆环境，适合裸机备份。
```[clonezilla](/man/clonezilla)```

修复无法启动的系统、用 `testdisk` 和 `photorec` 找回删除的文件、读取 SMART 健康状况等内容，参见 **系统恢复**基础页面。

## 文件系统级快照
现代文件系统和卷管理器可以对运行中的系统即时创建快照，为你提供稳定一致的备份来源。

| 系统 | 创建快照 |
|-----|-------------|
| **LVM** | `lvcreate -s -n snap -L 5G /dev/vg/lv` |
| **Btrfs** | `btrfs subvolume snapshot / /snap` |
| **ZFS** | `zfs snapshot pool/data@backup` |

创建 LVM 快照，以只读方式挂载，在系统持续运行的同时完成备份。完成后删除快照，让它不再占用空间。
```[lvcreate](/man/lvcreate) -s -n root_snap -L 5G /dev/vg0/root```
```[mount](/man/mount) -o ro /dev/vg0/root_snap /mnt/snap```
```[rsync](/man/rsync) -a /mnt/snap/ /mnt/backup/root/```
```[umount](/man/umount) /mnt/snap && [lvremove](/man/lvremove) /dev/vg0/root_snap```

Btrfs 和 ZFS 快照开销更低；创建为只读（`-r`），这样备份源就不会变化。
```[btrfs](/man/btrfs) subvolume snapshot -r / /.snapshots/2026-06-06```
```[zfs](/man/zfs) snapshot tank/home@2026-06-06```

`snapper` 和 `timeshift` 能按计划自动创建带保留策略的 Btrfs/LVM 快照。
```[snapper](/man/snapper) create --description "before upgrade"```
```[timeshift](/man/timeshift) --create```

**快照就在同一块磁盘上，其本身并不是备份。**要把它们复制到别处。

## 云端与远程同步
经过一次性的 `rclone config` 之后，`rclone` 可以把文件同步到数十家云服务商（S3、Backblaze、Google Drive 等）。
```[rclone](/man/rclone) copy /data remote:backup/data```
```[rclone](/man/rclone) sync /data remote:backup/data --progress```

不实际传输就能预览将要发生的变化、校验已完成的备份，或把远程存储挂载为本地文件夹。
```[rclone](/man/rclone) sync /data remote:backup --dry-run```
```[rclone](/man/rclone) check /data remote:backup/data```
```[rclone](/man/rclone) mount remote:backup /mnt/remote```

**小心：**与 `rsync --delete` 一样，`rclone sync` 会让目标与源完全一致，包括删除操作。只想新增文件时请改用 `copy`。

## 校验与自动化
只有完好无损的备份才算好备份。创建备份时记录校验和，恢复时加以验证。
```[sha256sum](/man/sha256sum) backup.tar.gz > backup.sha256```
```[sha256sum](/man/sha256sum) -c backup.sha256```

给备份排定计划，它们才会真正执行。编辑 crontab，添加一个夜间任务。
```[crontab](/man/crontab) -e```
```0 2 * * * [rsync](/man/rsync) -a --delete /data/ /mnt/backup/data/```

**备份要自动化，但恢复要按计划手动验证。**唯一经过证明的备份，是你成功恢复过的那个。
