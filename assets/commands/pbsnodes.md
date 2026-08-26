# TAGLINE

查询和管理 PBS 集群中的计算节点

# TLDR

**列出所有节点**

```pbsnodes -a```

**显示特定节点**

```pbsnodes [node_name]```

**显示空闲节点**

```pbsnodes -l free```

**将节点标记为离线**

```pbsnodes -o [node_name]```

**清除离线状态**

```pbsnodes -c [node_name]```

**设置节点备注**

```pbsnodes -N "[comment]" [node_name]```

# SYNOPSIS

**pbsnodes** [_options_] [_nodes_...]

# PARAMETERS

**-a**
> 显示所有节点。

**-l** _state_
> 列出处于指定状态的节点。

**-o**
> 标记为离线。

**-c**
> 清除离线状态。

**-N** _note_
> 设置备注/注释。

**-x**
> 以 XML 格式输出。

**-s** _server_
> 指定 PBS 服务器。

# DESCRIPTION

**pbsnodes** 用于查询和管理 PBS（Portable Batch System）集群中的计算节点。管理员借助它检查节点状态、在维护时将节点标记为离线以及查看资源可用情况。

# NODE STATES

```
free          - Available for jobs
job-exclusive - Running exclusive job
job-sharing   - Running shared jobs
down          - Unavailable
offline       - Admin disabled
```

# EXAMPLE OUTPUT

```
node01
     state = free
     np = 32
     properties = gpu
     status = ...
```

# CAVEATS

需要安装 PBS。修改操作需要管理员权限。配置因集群而异。

# HISTORY

PBS 由 **NASA Ames** 于 20 世纪 90 年代初开发，用于集群作业调度，后来演化为 OpenPBS 和 PBS Professional。

# SEE ALSO

[qstat](/man/qstat)(1), [qsub](/man/qsub)(1), [qdel](/man/qdel)(1)
