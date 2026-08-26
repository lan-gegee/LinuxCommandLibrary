# TAGLINE

Amanda 备份管理的管理界面

# TLDR

转储完整的内部**配置**表示

```amadmin [config_name] config```

显示每个磁盘上次转储时间及下一个计划的**级别**

```amadmin [config_name] info [hostname]```

在下次运行时强制对主机进行**全新完整备份**

```amadmin [config_name] force [hostname]```

从配置数据库中**移除**主机或磁盘

```amadmin [config_name] delete [hostname]```

显示备份在各运行日之间如何**均衡**

```amadmin [config_name] balance```

列出配置中的**磁盘**

```amadmin [config_name] disklist```

# SYNOPSIS

**amadmin** _config_ _command_ [_args_]

# DESCRIPTION

**amadmin** 是 Amanda（Advanced Maryland Automatic Network Disk Archiver）的管理界面，Amanda 是一款开源备份解决方案。它对备份配置执行交互式维护：强制完整转储、检查备份数据库以及查询过往转储的存放位置。

第一个参数始终是配置名称，其后是子命令。**amadmin** 操作的是 Amanda 自己的数据库和调度；它本身不运行备份（请用 **amdump**），也不为介质写标签（请用 **amlabel**）。

# PARAMETERS

**config**
> 以文本格式转储配置的完整内部表示

**info** [_host_ [_disk_]]
> 显示 Amanda 为各主机和磁盘记录的当前信息

**disklist** [_host_ [_disk_]]
> 列出 Amanda 将备份的 disklist 条目

**force** _host_ [_disk_]
> 在下次运行时强制对指定主机或磁盘做完整备份

**unforce** _host_ [_disk_]
> 撤销之前的强制请求

**delete** _host_ [_disk_]
> 从 Amanda 数据库中移除主机或磁盘（不会修改 disklist 文件）

**balance** [**--days** _num_]
> 显示完整备份在整个运行周期内如何均衡分布

**find** [_host_ [_disk_]]
> 显示哪些介质保存了给定主机和磁盘的转储数据

# CONFIGURATION

**/etc/amanda/<config>/amanda.conf**
> Amanda 主配置文件，定义备份计划、磁带类型和暂存盘。

**/etc/amanda/<config>/disklist**
> 列出给定配置中要备份的主机和磁盘。

# CAVEATS

需要正确安装和配置 Amanda。某些操作需要适当的权限。更改会影响下一次计划备份运行。

# HISTORY

**Amanda** 自 **1991** 年起由马里兰大学开发。它成为 Unix 系统上使用最广泛的开源备份解决方案之一，amadmin 提供其管理界面。

# INSTALL

```apt: sudo apt install amanda-server```

```dnf: sudo dnf install amanda-server```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amcheck](/man/amcheck)(8), [amdump](/man/amdump)(8), [amrecover](/man/amrecover)(8)

# RESOURCES

```[Source code](https://github.com/zmanda/amanda)```

```[Homepage](https://www.amanda.org/)```

```[Documentation](https://manpages.ubuntu.com/manpages/noble/man8/amadmin.8.html)```

<!-- verified: 2026-06-11 -->
