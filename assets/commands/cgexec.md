# TAGLINE

在控制组中运行命令

# TLDR

在 **cpu cgroup** 中运行命令

```cgexec -g cpu:mygroup [command]```

在单个 cgroup 中使用**多个控制器**运行

```cgexec -g cpu,memory:mygroup [command]```

为不同控制器使用**独立的 cgroup** 运行

```cgexec -g cpu:mygroup -g memory:memgroup [command]```

带 **sticky** 标志运行以防止 cgred 重新分类

```cgexec --sticky -g cpu:mygroup [command]```

# SYNOPSIS

**cgexec** [_OPTIONS_] -g _controller:cgroup_ _command_ [_args_]

# DESCRIPTION

**cgexec** 在指定的控制组（cgroup）内执行进程。与移动已在运行的进程的 cgclassify 不同，cgexec 从一开始就将新进程直接启动在目标 cgroup 中。

cgroup 允许对进程的 CPU、内存、I/O 等资源使用进行限制、度量和控制。通过 cgexec 启动进程时，该 cgroup 定义的所有资源约束从进程启动起立即生效，包括其派生的所有子进程。

cgexec 属于 libcgroup-tools 软件包，适用于 cgroups v1。在 cgroups v2 系统上，systemd-run 提供类似功能。

# PARAMETERS

**-g** _controllers:path_
> 指定控制器和 cgroup 路径。多个控制器可用逗号分隔。可多次使用。

**--sticky**
> 防止 cgrulesengd (cgred) 对该进程或其子进程进行重新分类。

**-b**
> 忽略默认的 systemd 委派层级路径，改为相对根层级构造 cgroup 路径。

**-h**
> 显示帮助信息。

Controllers include:
> **cpu** - CPU 时间分配
> **memory** - 内存使用限制
> **blkio** - 块设备 I/O 限制
> **cpuset** - CPU 和内存节点分配
> **devices** - 设备访问控制

# CAVEATS

使用 cgexec 前 cgroup 必须已存在（用 cgcreate 创建）。多个控制器可在单个 -g 选项中以逗号分隔，也可用多个 -g 选项指定。需要相应权限或 root 权限。若未指定 -g，cgexec 会根据 /etc/cgrules.conf 分配任务。

# HISTORY

**cgexec** 是 **libcgroup** 的一部分，后者为 Linux 上的资源控制提供 cgroup 管理工具。

# INSTALL

```apt: sudo apt install cgroup-tools```

```apk: sudo apk add cgroup-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cgcreate](/man/cgcreate)(1), [cgclassify](/man/cgclassify)(1), [cgdelete](/man/cgdelete)(1), [systemd-run](/man/systemd-run)(1)
