# TAGLINE

读取 cgroup 参数

# TLDR

**显示某个 cgroup 的全部参数**

```cgget -a [path/to/cgroup]```

**显示某个 cgroup 的特定参数**

```cgget -r [cpu.shares] [path/to/cgroup]```

**显示多个参数**

```cgget -r [cpuset.cpus] -r [cpuset.mems] [path/to/cgroup]```

**显示特定控制器的参数**

```cgget -g [cpu]:[path/to/cgroup]```

**只显示值而不显示参数名**

```cgget -v -r [memory.limit_in_bytes] [path/to/cgroup]```

**显示时不带组标题**

```cgget -n -g [cpu] /```

**显示当前 cgroups 设置模式**

```cgget -m```

# SYNOPSIS

**cgget** [**-n**] [**-v**] [**-b**] [**-m**] [**-r** _name_] [**-g** _controller_] [**-a**] _path..._

**cgget** [**-n**] [**-v**] [**-b**] [**-m**] [**-r** _name_] **-g** _controller_**:**_path..._

# DESCRIPTION

**cgget** 打印 Linux 控制组（cgroups）的参数。cgroups 是一种内核机制，用于组织进程和管理资源分配，包括 CPU、内存和 I/O。

如果未指定控制器或变量，将显示所有可用参数的值。该命令同时支持 cgroup v1（旧式）和 v2（统一）层级。

# PARAMETERS

**-a, --all**
> 打印给定 cgroup 中所有控制器的变量

**-g** _controller_[**:**_path_]
> 指定要显示的控制器，可选路径

**-r, --variable** _name_
> 显示特定参数（可多次使用）

**-n**
> 不打印组名标题

**-v, --values-only**
> 只打印值，不打印参数名

**-m**
> 显示当前的 cgroups 设置模式（legacy、unified 或 hybrid）

**-b**
> 忽略默认的 systemd 委派层级路径；改为相对根层级构造路径

**-c**
> 显示控制器及其版本（可与 -m 组合）

**-h, --help**
> 显示帮助并退出

# CAVEATS

**CGROUP_LOGLEVEL** 环境变量控制日志详细程度（DEBUG、INFO、WARNING、ERROR）。

读取 cgroup 参数需要相应权限。某些参数可能只有 root 才能访问。

# INSTALL

```apt: sudo apt install cgroup-tools```

```apk: sudo apk add cgroup-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cgset](/man/cgset)(1), [cgcreate](/man/cgcreate)(1), [cgdelete](/man/cgdelete)(1), [cgexec](/man/cgexec)(1), [cgclassify](/man/cgclassify)(1), [lscgroup](/man/lscgroup)(1), [cgroups](/man/cgroups)(7)
