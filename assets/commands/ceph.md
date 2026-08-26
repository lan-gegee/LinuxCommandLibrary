# TAGLINE

分布式存储集群管理

# TLDR

检查集群**健康状况**

```ceph status```

查看集群**使用统计**

```ceph df```

获取**归置组（placement group）**统计信息

```ceph pg dump --format [plain]```

**创建**存储池

```ceph osd pool create [pool_name] [pg_num]```

**删除**存储池

```ceph osd pool delete [pool_name]```

**重命名**存储池

```ceph osd pool rename [current_name] [new_name]```

对池存储进行**自修复**

```ceph pg repair [pool_name]```

# SYNOPSIS

**ceph** [_options_] _command_

# DESCRIPTION

**ceph** 是管理 Ceph 分布式存储集群的命令行界面。Ceph 提供统一的对象、块和文件存储，具备自动数据复制、自愈能力，且没有单点故障。

该命令与 Ceph monitor 守护进程通信，执行集群管理任务，包括检查健康状况、管理 OSD（Object Storage Daemon，对象存储守护进程）、配置归置组以及处理认证。它是日常集群运维和故障排查的主要工具。

Ceph 将数据组织到池（pool）中，池包含归置组（placement group），归置组再映射到集群中的各 OSD。`ceph status` 命令提供集群健康的快速概览，而更具体的子命令则允许对单个组件进行细粒度控制。

# SUBCOMMANDS

**status**
> 显示集群健康与状态

**df**
> 显示集群磁盘使用情况

**osd**
> 管理对象存储守护进程（OSD）

**pg**
> 管理归置组

**mon**
> 管理 monitor 守护进程

**mds**
> 管理元数据服务器

**auth**
> 管理认证

# PARAMETERS

**-s, --status**
> 显示集群状态

**--format** _format_
> 输出格式：json、plain

**-c** _file_
> 使用备用配置文件

# CONFIGURATION

**/etc/ceph/ceph.conf**
> 集群主配置文件，包括 monitor 地址、认证设置和 OSD 参数。

**/etc/ceph/ceph.client.admin.keyring**
> 用于访问集群的管理员认证密钥环。

# CAVEATS

需要正确的 Ceph 配置和认证。集群操作可能需要一些时间才能完成。某些命令需要特定权限。

# INSTALL

```apt: sudo apt install ceph-common```

```dnf: sudo dnf install ceph-common```

```apk: sudo apk add ceph18-common```

```zypper: sudo zypper install ceph-common```

```nix: nix profile install nixpkgs#ceph```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cephadm](/man/cephadm)(8)
