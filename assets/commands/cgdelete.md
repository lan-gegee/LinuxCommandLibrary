# TAGLINE

删除控制组

# TLDR

**删除一个 cgroup**

```cgdelete -g [cpu]:[/mygroup]```

**从多个控制器删除 cgroup**

```cgdelete -g [cpu,memory]:[/mygroup]```

**递归删除 cgroup**（包括子组）

```cgdelete -r -g [cpu]:[/mygroup]```

**删除 cgroup 及所有空父组**

```cgdelete -g [memory]:[/parent/child]```

# SYNOPSIS

**cgdelete** [**-r**] [**-g** _controllers_:_path_]...

# DESCRIPTION

**cgdelete** 从 Linux 控制组层级中移除 cgroup。cgroup（控制组）用于限制、统计和隔离进程的资源使用。

该命令从 cgroup 文件系统中移除指定的 cgroup 目录。默认情况下，cgroup 在删除前必须为空（不含进程或子 cgroup）。-r 标志允许递归删除子 cgroup。

cgdelete 属于 libcgroup-tools，后者提供管理 cgroups v1 的用户态工具。注意，cgroups v2 使用统一层级和不同的管理方式。

# PARAMETERS

**-g** _controllers_:_path_
> 指定要删除的控制器和 cgroup 路径。

**-r**
> 递归删除子 cgroup。

**-h**, **--help**
> 显示帮助信息。

# CAVEATS

无法删除包含运行中进程的 cgroup。需要相应权限（通常是 root）。指定的控制器必须已挂载。不适用于 cgroups v2 统一层级（请改用直接文件系统操作或 systemd）。空的父 cgroup 可能被自动移除。

# HISTORY

**cgdelete** 是 **libcgroup** 的一部分，该项目是管理 Linux cgroups 的库和工具集，由 **Red Hat** 于 **2008 年**前后发起，为 cgroups v1 提供用户态工具。随着 Linux 向 cgroups v2 迁移，systemd 成为大多数系统上的主要 cgroup 管理器，不过 libcgroup 工具在 cgroups v1 系统上仍然有用。

# INSTALL

```apt: sudo apt install cgroup-tools```

```apk: sudo apk add cgroup-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cgcreate](/man/cgcreate)(1), [cgset](/man/cgset)(1), [cgget](/man/cgget)(1), [lscgroup](/man/lscgroup)(1)

# RESOURCES

```[Source code](https://github.com/libcgroup/libcgroup)```

<!-- verified: 2026-06-22 -->
