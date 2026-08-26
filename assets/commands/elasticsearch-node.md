# TAGLINE

低层节点恢复与集群操作

# TLDR

在改变节点用途后**清理数据**（移除其当前角色不再使用的数据）

```elasticsearch-node repurpose```

**将节点与其集群分离**，使其可以加入其他集群

```elasticsearch-node detach-cluster```

**覆盖集群状态版本**以允许降级

```elasticsearch-node override-version```

**从集群状态中移除自定义元数据**

```elasticsearch-node remove-customs [customs]```

**从该节点不安全地引导新集群**（可能造成数据丢失）

```elasticsearch-node unsafe-bootstrap```

**从持久化状态中移除集群设置**

```elasticsearch-node remove-settings [settings]```

# SYNOPSIS

**elasticsearch-node** _command_ [_options_]

# SUBCOMMANDS

**repurpose**
> 清理角色已变化、数据不再需要的节点上的数据和索引（例如将数据节点切换为仅主节点）。

**detach-cluster**
> 强制将节点从当前集群分离，使其可以加入新的集群。用于原集群永久丢失的情况。

**override-version**
> 当用比写入数据时更新版本的 Elasticsearch 启动时，覆盖磁盘上集群状态的版本。

**remove-customs** _patterns_
> 从磁盘上的集群状态中移除与给定模式匹配的自定义元数据条目。

**remove-settings** _patterns_
> 移除与给定模式匹配的持久化集群设置。

**unsafe-bootstrap**
> 当原集群无法恢复时，基于该节点的磁盘数据引导一个新的单节点集群。可能导致数据丢失。

# PARAMETERS

**-E** _setting=value_
> 在工具调用期间覆盖某个 Elasticsearch 配置设置。

**-h**, **--help**
> 显示帮助。

**-s**, **--silent**
> 显示最少输出。

**-v**, **--verbose**
> 显示详细输出。

# CAVEATS

这些命令可能导致数据丢失和节点间的状态分歧。只能在已停止的节点上运行，且必须在每个受影响的节点上都执行，并且仅在针对具体恢复场景查阅过 Elasticsearch 官方文档之后才能使用。务必先备份数据目录。

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1)
