# TAGLINE

运行 Amanda 备份

# TLDR

使用某个配置**运行完整备份**

```amdump [config_name]```

仅**备份特定主机**

```amdump [config_name] [host1] [host2]```

**备份某台主机上的特定磁盘**

```amdump [config_name] [hostname] [/path/to/disk]```

**仅备份到暂存盘**（不写磁带）

```amdump --no-taper [config_name]```

**覆盖某个配置选项**

```amdump -o [runtapes=2] [config_name]```

**使用精确的主机/磁盘匹配**

```amdump --exact-match [config_name] [hostname] [diskname]```

# SYNOPSIS

**amdump** [**--no-taper**] [**--exact-match**] [**-o** _configoption_...] _config_ [_host_ [_disk_]...]

# PARAMETERS

**--no-taper**
> 仅转储到暂存盘而不写入磁带；立即进入降级模式

**--exact-match**
> 将主机和磁盘参数解析为精确值而非表达式

**-o** _name=value_
> 覆盖 amanda.conf 中的某个配置选项

_config_
> 定义备份作业的 Amanda 配置名称

_host_
> 要备份的特定客户端主机名

_disk_
> 指定主机上要备份的特定磁盘或文件系统

# DESCRIPTION

**amdump** 是运行 Amanda 备份的主要命令。它会加载指定的配置，备份 disklist 文件中列出的所有磁盘；如果在命令行上指定了具体的主机和磁盘，则只备份其中的子集。

该命令通常通过 cron 执行以进行定期的夜间备份。它协调整个备份过程：联系客户端主机、将数据传输到暂存盘，然后写入磁带或其他存储介质。Amanda 的调度算法根据配置的转储周期决定哪些文件系统做全量备份、哪些做增量备份。

如果配置目录中存在名为 **hold** 的文件，amdump 会每分钟检查一次，直到该文件被删除后才开始备份。这让管理员可以在磁带设备被其他任务占用时推迟计划备份。

出现问题时，amdump 可能进入"降级模式"，此时备份继续写入暂存盘，但跳过磁带写入。**--no-taper** 选项可以有意强制进入此模式。

# CONFIGURATION

**/etc/amanda/<config>/amanda.conf**
> Amanda 服务器配置，定义磁带设备、暂存盘、转储类型和调度参数。

**/etc/amanda/<config>/disklist**
> 要备份的客户端主机和文件系统列表。

# CAVEATS

对于给定的配置，同一时间只能运行一个 amdump 或 amflush。如果上一次运行被中断，必须先执行 **amcleanup**，amdump 才能启动。备份操作期间，该进程需要足够的暂存盘空间用于中间存储。

# EXIT CODES

退出代码表示备份状态：**0** = 成功，**1** = 错误，**2** = 某个 DLE 返回了异常消息，**4** = 某 DLE 失败，**8** = 某 DLE 状态未知。多种情况同时发生时，各代码按位或组合。

# HISTORY

Amanda（Advanced Maryland Automatic Network Disk Archiver）自 **1991** 年起在**马里兰大学**开发。它开创了以暂存盘作为中间存储以及在备份周期内智能调度的理念。该项目成为企业 Unix 备份策略的基石，目前在开源社区治理下继续发展。

# INSTALL

```apt: sudo apt install amanda-server```

```dnf: sudo dnf install amanda-server```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amcheck](/man/amcheck)(8), [amrecover](/man/amrecover)(8)
