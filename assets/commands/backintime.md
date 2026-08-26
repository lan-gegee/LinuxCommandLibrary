# TAGLINE

基于 rsync 和硬链接快照的增量备份

# TLDR

为当前配置档**创建备份**

```backintime backup```

为指定配置档**创建备份**

```backintime --profile [NAME] backup```

**列出备份 ID**

```backintime show```

**显示最近一次备份**及其磁盘占用

```backintime show --last --usage```

**列出已配置的配置档**

```backintime show --profiles```

从最新备份**恢复文件**到原路径

```backintime restore [/path/to/file]```

从指定备份 ID **恢复文件**到新位置

```backintime restore [/path/to/file] [/path/to/dest] [BACKUP_ID]```

确认后**删除备份**

```backintime remove [BACKUP_ID]```

**应用 Remove & Retention 策略**

```backintime prune```

**校验配置**并安装 crontab 条目

```backintime check-config```

# SYNOPSIS

**backintime** [_global options_] _command_ [_args_]

# DESCRIPTION

**backintime** 是 **Back In Time** 的命令行客户端；后者是一款使用 **rsync**(1) 和文件系统硬链接的 Linux 备份工具。每次运行都会呈现所有选中文件的完整树结构，但只复制发生变化的文件；未变化的文件通过硬链接指向上一次备份，因此备份看起来像完整副本，实际占用的是增量空间。

配置档可以将备份存储在**本地**、通过 **SSH** 存储，或使用 **gocryptfs** 加密存储（本地或 SSH）。定时任务由 **cron**(1) 完成；**check-config** 会写入 crontab 条目。Qt 图形界面为 **backintime-qt**。恢复操作可通过本 CLI、GUI 或浏览按日期组织的备份目录的文件管理器完成。

术语**snapshot**（快照）一直使用到 1.6.0 版本；从 1.6.0 起，项目改用**backup**（备份），以免与卷镜像混淆。

# PARAMETERS

**-h**, **--help**
> 显示帮助。

**-p** _NAME_|_ID_, **--profile** _NAME_|_ID_
> 按名称或数字 ID 选择配置档。

**--config** _PATH_
> 从 _PATH_ 读取配置（默认 **$XDG_CONFIG_HOME/backintime/config**）。

**--quiet**
> 抑制标准输出上的状态消息。

**--debug**
> 打印调试消息。

**-v**, **--version**
> 打印版本号。

**--license**
> 打印许可证信息。

**--diagnostics**
> 打印用于 bug 报告的诊断信息。

**backup**
> 创建新备份。前台运行总是执行一次备份。**--background** 使其转入后台且**不会**强制运行，因此当配置档未到期或机器使用电池供电时，计划任务可能会跳过。**--checksum** 通过校验和而不是大小和修改时间来比较文件。

**show**
> 列出备份 ID（使用 **--path** 时列出路径）。**--last** 将列表限制为最新一次备份。**--profiles** 列出配置档。**--usage** 报告逻辑大小、真实磁盘占用以及硬链接节省的空间。

**restore** [_WHAT_] [_WHERE_] [_BACKUP_ID_]
> 恢复文件或目录。_WHERE_ 为空则恢复到原位置。_BACKUP_ID_ 是 ID 或索引（**0** = 最近一次备份，**-1** = 最老一次）。**--delete** 会删除目标位置中不在备份内的文件（作用于 **/** 时非常危险）。**--local-backup** / **--no-local-backup** 控制 **FILE.backup.YYYYMMDD** 安全副本的创建。**--only-new** 使用 rsync 的 **--update**。

**remove** [_BACKUP_ID_ ...]
> 删除一个或多个备份。**--skip-confirmation** 跳过确认提示。

**prune**
> 根据配置档的 Remove & Retention 策略删除备份。

**unmount**
> 卸载当前配置档。

**shutdown**
> 在正在运行的备份完成后关机。

**check-config**
> 校验配置、创建备份目标路径并安装 crontab 条目。**--no-crontab** 跳过对 crontab 的修改。

**pw-cache** [_start_|_stop_|_restart_|_reload_|_status_]
> 控制供非交互式 cron 任务使用的密码缓存守护进程。

# CONFIGURATION

每用户配置文件位于 **~/.config/backintime/config**（即 `$XDG_CONFIG_HOME/backintime/config`）。行格式为 **keyword=value**，值不加引号。配置档按数字编号（**profile1**、**profile2** 等）。全局的 **/etc/backintime/config** 已不再支持。

典型键：

```
profile1.snapshots.mode=local
profile1.snapshots.path=/mnt/backup
profile1.schedule.mode=20
profile1.schedule.time=200
```

**profile\<N\>.snapshots.mode** 可为 **local**、**ssh** 或加密的 gocryptfs 模式。**profile\<N\>.snapshots.path** 是本地目标路径，其中必须包含 **backintime/\<HOST\>/\<USER\>/\<PROFILE_ID\>** 目录树。**profile\<N\>.schedule.mode** 选择 crontab 计划（**0** = 禁用，**20** = 每天，**30** = 每周等）。编辑后请运行 **backintime check-config** 来校验文件、创建目标路径并刷新 crontab。示例配置文件位于 **/usr/share/doc/backintime-common/examples/** 下。

# CAVEATS

这是文件级备份工具，不是全系统镜像工具；系统还原请使用 **timeshift** 或磁盘克隆类工具。不是真正文件系统或 SSH 目标的云盘无法使用。EncFS 模式已在 2.0 中移除；加载配置时会剥离残留的 EncFS 配置档（同时保留该文件的备份）。目标文件系统应支持 Unix 硬链接；NTFS 和许多 Samba 共享并不合适。**restore --delete** 若指向 **/** 可能摧毁整个系统。即使只有部分文件失败（例如悬空的符号链接），rsync 退出码 23 也会被报告为错误。

# HISTORY

**Back In Time** 由 **Oprea Dan** 于 **2008** 年创建，灵感来自 **FlyBack**。**Germar Reitze** 从约 **2012** 年维护到 **2019** 年，期间增加了 SSH 目标、EncFS 加密和统一的 **backintime-qt** GUI。经过一段沉寂后，**Christian Buhtz**、**Jürgen Altfeld** 和 **Michael Büker** 于 **2022** 年重启了开发。版本 **2.0**（候选发布版 **2026**）弃用 EncFS，改用 **gocryptfs**。

# INSTALL

```apt: sudo apt install backintime-common```

```dnf: sudo dnf install backintime-common```

```aur: yay -S backintime```

```zypper: sudo zypper install backintime```

```nix: nix profile install nixpkgs#backintime```

<!-- packages: 2026-08-15 -->

# SEE ALSO

[rsync](/man/rsync)(1), [cron](/man/cron)(8), [timeshift](/man/timeshift)(1), [restic](/man/restic)(1), [borg](/man/borg)(1), [duplicity](/man/duplicity)(1), [gocryptfs](/man/gocryptfs)(1), [ssh](/man/ssh)(1)

# RESOURCES

```[Source code](https://github.com/bit-team/backintime)```

```[Documentation](https://backintime.readthedocs.io)```

<!-- verified: 2026-08-16 -->
