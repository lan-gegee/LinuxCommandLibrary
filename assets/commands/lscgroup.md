# TAGLINE

列出系统中的 cgroup

# TLDR

**列出所有 cgroup**

```lscgroup```

**列出特定控制器**

```lscgroup [cpu]```

**列出特定 cgroup**

```lscgroup [cpu:/mygroup]```

**显示所有控制器**

```lscgroup -a```

**列出一个控制器的 cgroup 层级**

```lscgroup [memory]```

# SYNOPSIS

**lscgroup** [_options_] [_controller_]

# PARAMETERS

_CONTROLLER_
> Cgroup 控制器名称。

**-a**
> 显示所有控制器。

**-g** _GROUP_
> 显示特定的组。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lscgroup** 列出系统中的 cgroup。Cgroup 用于控制进程的资源分配。

该工具显示 cpu、memory、blkio 等控制器的 cgroup 层级结构。

# CAVEATS

属于 cgroups v1 工具，在 cgroups v2 下行为可能不同。是 libcgroup-tools 的一部分。

# HISTORY

lscgroup 属于 **libcgroup** 工具集，用于管理 Linux 控制组以实现资源管理。

# INSTALL

```apt: sudo apt install cgroup-tools```

```apk: sudo apk add cgroup-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cgcreate](/man/cgcreate)(1), [cgexec](/man/cgexec)(1), [cgset](/man/cgset)(1)
