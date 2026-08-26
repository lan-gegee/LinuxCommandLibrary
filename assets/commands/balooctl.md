# TAGLINE

控制 KDE Baloo 文件索引

# TLDR

显示索引器**状态**

```balooctl status```

**启用**文件索引器

```balooctl enable```

**禁用**文件索引器

```balooctl disable```

**清空**索引数据库

```balooctl purge```

**挂起**索引进程

```balooctl suspend```

显示占用的**磁盘**空间

```balooctl indexSize```

**检查**未建立索引的文件

```balooctl check```

# SYNOPSIS

**balooctl** [_OPTIONS_] _COMMAND_

# DESCRIPTION

**balooctl** 是 Baloo 的控制工具；Baloo 是 KDE Plasma 中使用的文件索引与搜索框架。它管理为快速桌面文件搜索提供支撑的文件索引守护进程，允许用户启用、禁用、挂起并监视索引过程。

该工具适用于排查搜索问题、回收索引占用的磁盘空间，以及检查哪些文件已被索引。

# PARAMETERS

**status**
> 显示当前索引器状态

**enable**
> 启用文件索引器

**disable**
> 禁用文件索引器

**purge**
> 删除索引数据库

**suspend**
> 暂时挂起索引进程

**resume**
> 恢复已挂起的索引进程

**indexSize**
> 显示索引占用的磁盘空间

**check**
> 查找并为未建立索引的文件建立索引

**index** _file..._
> 手动为指定文件建立索引

**clear** _file..._
> 从索引中移除指定文件

**config**
> 修改 Baloo 配置

**monitor**
> 监视索引器活动

**failed**
> 列出无法建立索引的文件

# CONFIGURATION

**~/.config/baloofilerc**
> 控制要索引哪些目录、排除哪些文件类型以及索引行为。

# CAVEATS

清空索引后需要重新索引所有文件，可能耗时较长。索引器遵循 KDE 设置中关于索引目录的规定。索引期间 CPU 占用较高属于正常现象。

# HISTORY

**balooctl** 是 **Baloo** 的一部分；Baloo 是 KDE Plasma 桌面的文件索引与搜索框架。

# SEE ALSO

[locate](/man/locate)(1)
