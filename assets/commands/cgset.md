# TAGLINE

设置 cgroup 参数

# TLDR

为 cgroup **设置 CPU 配额**

```cgset -r cpu.cfs_quota_us=[50000] [/mygroup]```

为 cgroup **设置内存限制**

```cgset -r memory.limit_in_bytes=[512M] [/mygroup]```

一次**设置多个参数**

```cgset -r cpu.shares=[512] -r memory.limit_in_bytes=[1G] [/mygroup]```

将一个 cgroup 的**配置复制**到另一个

```cgset --copy-from [/source_group] [/dest_group]```

# SYNOPSIS

**cgset** [**-r** _name=value_]... _cgroup_

**cgset** **--copy-from** _source_ _destination_

# DESCRIPTION

**cgset** 修改已有控制组（cgroups）的参数。它可以为进程组设置 CPU、内存、I/O 及其他子系统的资源限制和控制。

常见参数包括 CPU shares（相对优先级）、CPU 配额（硬限制）、内存限制和 I/O 权重。可用参数取决于挂载了哪些控制器以及 cgroup 版本。

cgset 属于管理 cgroups v1 的 libcgroup-tools。对于 cgroups v2，通常改用 systemd 或直接写文件系统。

# PARAMETERS

**-r** _name=value_
> 将参数设置为指定值。

**--copy-from** _cgroup_
> 从另一个 cgroup 复制参数。

**-h**, **--help**
> 显示帮助信息。

# CAVEATS

需要相应权限（通常是 root）。参数名和取值因控制器而异。无效的值可能被内核拒绝。仅适用于 cgroups v1 层级。某些参数在 cgroup 中仍有进程时无法更改。

# HISTORY

**cgset** 是 **libcgroup** 的一部分，后者由 **Red Hat** 自 **2008 年**前后开发，提供用户态的 cgroup 管理。该工具提供了一种无需直接操作文件系统即可配置资源限制的方式。随着 cgroups v2 和 systemd 的普及，直接使用这些工具进行管理的情况已越来越少。

# INSTALL

```apt: sudo apt install cgroup-tools```

```apk: sudo apk add cgroup-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cgcreate](/man/cgcreate)(1), [cgdelete](/man/cgdelete)(1), [cgget](/man/cgget)(1), [cgexec](/man/cgexec)(1)

# RESOURCES

```[Source code](https://github.com/libcgroup/libcgroup)```

<!-- verified: 2026-06-22 -->
