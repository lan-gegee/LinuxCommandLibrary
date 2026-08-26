# TAGLINE

将运行中的进程移入 cgroup

# TLDR

将进程移入 **CPU cgroup** "student"

```cgclassify -g [cpu:student] [1234]```

根据 **/etc/cgrules.conf** 移动进程

```cgclassify [1234]```

以 **sticky** 模式移入 cgroup

```cgclassify --sticky -g [cpu:/student] [1234]```

# SYNOPSIS

**cgclassify** [_options_] _pid_...

# DESCRIPTION

**cgclassify** 将运行中的进程移动到控制组（cgroups）。这样可以在不重启进程的情况下，改变已在运行的进程的资源限制和统计。

不带 -g 选项使用时，进程会按照 **/etc/cgrules.conf** 中的规则进行分类。

# PARAMETERS

**-g** _controllers:path_
> 将进程移入指定的 cgroup 层级

**--sticky**
> 阻止 cgred 守护进程重新分类该进程

**--cancel-sticky**
> 允许 cgred 再次管理该进程

# CONFIGURATION

**/etc/cgrules.conf**
> 未指定 -g 时用于自动 cgroup 分类的规则。

**/etc/cgconfig.conf**
> cgroup 层级与控制器配置。

# CAVEATS

需要 cgroups v1 工具（libcgroup）。cgroups v2 请使用其他工具。在 cgroup 之间移动进程可能立即影响其对资源的访问。

# INSTALL

```apt: sudo apt install cgroup-tools```

```apk: sudo apk add cgroup-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cgcreate](/man/cgcreate)(1), [cgexec](/man/cgexec)(1), [cgroups](/man/cgroups)(7)

# RESOURCES

```[Source code](https://github.com/libcgroup/libcgroup)```

<!-- verified: 2026-06-22 -->
