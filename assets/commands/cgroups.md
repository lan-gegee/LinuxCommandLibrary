# TAGLINE

Linux 内核资源控制与隔离

# TLDR

本页是索引页——创建控制组请见 **cgcreate**

```cgcreate -g [controllers]:[path]```

使用 **cgexec** 在 cgroup 中运行进程

```cgexec -g [controllers]:[path] [command]```

使用 **cgclassify** 移动运行中的进程

```cgclassify -g [controllers]:[path] [pid]```

# DESCRIPTION

**cgroups**（control groups，控制组）是 Linux 内核的一项特性，用于限制、度量和控制进程的资源使用。它不是单个命令，而是一组工具和内核接口的集合。

cgroups 可以限制 CPU、内存、I/O 和网络资源。它是 Docker 等容器技术和 systemd 资源管理的基础。

# RELATED COMMANDS

**cgclassify**
> 将运行中的进程移入 cgroup

**cgcreate**
> 创建新的 cgroup

**cgexec**
> 在 cgroup 中运行命令

**cgget**
> 获取 cgroup 参数

**cgset**
> 设置 cgroup 参数

**cgdelete**
> 删除 cgroup

# CAVEATS

Linux 有两个版本的 cgroups（v1 和 v2），接口不同。现代系统通常使用 cgroups v2 统一层级。libcgroup 工具适用于 v1；systemd 原生管理 v2。

# SEE ALSO

[cgclassify](/man/cgclassify)(1), [cgcreate](/man/cgcreate)(1), [cgexec](/man/cgexec)(1), [systemd-cgtop](/man/systemd-cgtop)(1)

# RESOURCES

```[Documentation](https://man7.org/linux/man-pages/man7/cgroups.7.html)```

<!-- verified: 2026-06-22 -->
