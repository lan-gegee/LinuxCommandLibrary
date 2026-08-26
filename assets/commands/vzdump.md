# TAGLINE

Proxmox VE 虚拟机备份工具

# TLDR

**备份**单个虚拟机

```vzdump [vm_id]```

备份**多个**虚拟机

```vzdump [101] [102] [103]```

以指定**模式**备份（snapshot、stop 或 suspend）

```vzdump [vm_id] --mode [snapshot|stop|suspend]```

备份**所有**虚拟机并发送邮件通知

```vzdump --all --mode snapshot --mailto [root@example.com]```

带 **zstd 压缩**备份到指定目录

```vzdump [vm_id] --dumpdir [/mnt/backup] --mode snapshot --compress zstd```

备份所有虚拟机但**排除**指定的若干台

```vzdump --all --exclude [101,102]```

按**保留策略**备份

```vzdump [vm_id] --mode snapshot --prune-backups keep-last=5,keep-daily=7```

# SYNOPSIS

**vzdump** [_OPTIONS_] _VMID_...

# PARAMETERS

**--mode** _MODE_
> 备份模式：snapshot（默认，停机时间最短）、stop（一致性最高，虚拟机会停止）或 suspend（兼容模式）。

**--dumpdir** _DIR_
> 将生成的备份文件存放到 DIR，而不是默认位置。

**--storage** _STORAGE_ID_
> 将生成的备份文件存到指定的 Proxmox 存储。

**--mailto** _EMAIL_
> 向该地址发送通知邮件。已被通知系统取代，不建议使用。

**--all**
> 备份主机上所有已知的客户机系统。

**--exclude** _VMIDS_
> 排除指定的虚拟机 ID（需配合 --all）。

**--pool** _POOL_
> 备份指定资源池中的所有客户机系统。

**--compress** _TYPE_
> 压缩类型：0（不压缩，默认）、gzip、lzo 或 zstd。

**--zstd** _N_
> Zstandard 线程数（默认：1）。0 表示使用可用核心的一半。

**--pigz** _N_
> 使用并行 gzip。N=1 使用可用核心的一半；N>1 使用 N 个线程。

**--prune-backups** _RETENTION_
> 保留策略（例如 keep-last=N,keep-daily=N,keep-weekly=N,keep-monthly=N,keep-yearly=N）。默认：keep-all=1。

**--maxfiles** _N_
> 已弃用。每个虚拟机的最大备份文件数量。请改用 --prune-backups。

**--protected**
> 将备份标记为受保护，防止被自动删除。

**--bwlimit** _KiB/s_
> 以 KiB/s 为单位限制 I/O 带宽（默认：0，不限制）。

**--ionice** _N_
> 使用 BFQ 调度器时设置 IO 优先级（0-8）（默认：7）。

**--tmpdir** _DIR_
> 将临时文件存放在 DIR 中。

**--lockwait** _MIN_
> 等待全局锁的最长分钟数（默认：180）。

**--stopwait** _MIN_
> 等待客户机系统停止的最长分钟数（默认：10）。

**--script** _FILE_
> 在备份过程中执行钩子脚本。

**--notes-template** _TEMPLATE_
> 备份备注的模板。变量：{{vmid}}、{{guestname}}、{{node}}、{{cluster}}。

**--quiet**
> 不输出详细信息。

**--stdexcludes**
> 排除临时文件和日志（默认：启用）。

# DESCRIPTION

**vzdump** 是 Proxmox VE 虚拟机（KVM）和容器（LXC）的备份工具。它创建一致性备份，之后可以用 **qmrestore**（虚拟机）或 **pct restore**（容器）恢复。

有三种备份模式可用：**snapshot**（默认，借助 LVM/ZFS/QEMU 快照实现最短停机）、**stop**（一致性最高，备份期间停止客户机）和 **suspend**（旧式兼容模式）。备份默认存放在 /var/lib/vz/dump/，或存到已配置的 Proxmox 存储中。

# CAVEATS

仅适用于 Proxmox VE。大型虚拟机需要大量备份存储空间。快照模式要求支持 LVM、ZFS 或 QEMU 快照。--maxfiles 选项已被弃用，请改用 --prune-backups。全局配置可在 /etc/vzdump.conf 中设置。

# SEE ALSO

[qmrestore](/man/qmrestore)(1), [pct](/man/pct)(1), [qm](/man/qm)(1), [pvesm](/man/pvesm)(1)
