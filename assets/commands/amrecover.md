# TAGLINE

交互式浏览和恢复 Amanda 备份

# TLDR

使用某个配置**启动恢复会话**

```amrecover [config_name]```

**连接到特定的索引服务器**

```amrecover -s [index_server] [config_name]```

**指定磁带服务器和设备**

```amrecover -t [tape_server] -d [/dev/nst0] [config_name]```

**恢复其他主机的文件**

```amrecover -h [hostname] [config_name]```

**常见的交互会话工作流程**

```
sethost [hostname]
setdisk [/home]
setdate [2024-01-15]
cd [path/to/restore]
add [filename]
extract
```

# SYNOPSIS

**amrecover** [**-C** _config_] [**-s** _index-server_] [**-t** _tape-server_] [**-d** _tape-device_] [**-h** _hostname_]

# PARAMETERS

**-C** _config_
> 要使用的 Amanda 配置名称

**-s** _index-server_
> 运行索引守护进程的主机

**-t** _tape-server_
> 运行磁带服务器守护进程的主机

**-d** _tape-device_
> 磁带服务器上要使用的磁带设备

**-h** _hostname_
> 要恢复的主机名；默认为当前系统的主机名

# INTERACTIVE COMMANDS

**sethost** _hostname_
> 设置要浏览和从中恢复的主机

**setdisk** _diskname_
> 设置要浏览的磁盘（文件系统）

**setdate** _YYYY-MM-DD_
> 设置查看备份状态的日期

**cd** _directory_
> 在备份内切换目录

**ls**
> 列出当前备份目录的内容及日期

**add** _pattern_
> 将文件或目录加入恢复列表（支持通配符）

**delete** _pattern_
> 从恢复列表中移除条目

**list**
> 显示当前的恢复列表

**clear**
> 清空恢复列表

**extract**
> 开始提取恢复列表中的文件

**history**
> 显示当前主机和磁盘的备份历史

**lcd** _directory_
> 切换本地工作目录

**lpwd**
> 显示本地工作目录

**quit**
> 退出 amrecover

# DESCRIPTION

**amrecover** 是一个交互式工具，用于浏览 Amanda 备份索引并恢复文件。它提供类似 FTP 的界面，可用于浏览各备份快照、选择要恢复的文件，并从磁带或其他备份介质中提取数据。

该工具连接到 Amanda 索引服务器来浏览备份目录，确定哪些磁带包含所需文件。用户通过浏览目录并将文件加入列表来构建恢复清单，然后启动提取操作，由其联系磁带服务器获取数据。

若要进行原位恢复，请从被备份文件系统的根目录运行 amrecover，或在提取前使用 **lcd** 切换到该目录。否则，会在当前目录下创建一个复刻备份结构的目录树。

在可用时，GNU readline 库会提供命令历史和编辑功能。

# CONFIGURATION

**/etc/amanda/<config>/amanda.conf**
> Amanda 配置文件，定义恢复期间使用的索引服务器和磁带服务器设置。

# CAVEATS

原位恢复需要从适当的目录运行 amrecover。索引服务器和磁带服务器必须可以通过网络访问。对于客户端加密或客户端自定义压缩的备份，请改用 **amrestore**。客户端与服务器之间必须正确配置认证。

# HISTORY

Amanda（Advanced Maryland Automatic Network Disk Archiver）自 **1991** 年起在**马里兰大学**开发。amrecover 工具提供文件级恢复的主要用户界面，旨在让用户无需直接操作磁带即可完成恢复。它已发展为支持传统磁带之外的多种存储后端。

# INSTALL

```apt: sudo apt install amanda-client```

```dnf: sudo dnf install amanda-client```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amcheck](/man/amcheck)(8), [amdump](/man/amdump)(8)
