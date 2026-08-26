# TAGLINE

创建新的控制组

# TLDR

创建带特定控制器的 **cgroup**

```cgcreate -g cpu:mygroup```

创建带**多个控制器**的 cgroup

```cgcreate -g cpu,memory:mygroup```

创建带所有已**挂载控制器**的 cgroup

```cgcreate -g *:mygroup```

设置 **tasks 文件**的所有权

```cgcreate -t user:group -g cpu:mygroup```

设置**控制文件**的所有权

```cgcreate -a user:group -g cpu:mygroup```

设置**目录权限**

```cgcreate -d 755 -g cpu:mygroup```

# SYNOPSIS

**cgcreate** [**-h**] [**-t** _tuid_:_tgid_] [**-a** _agid_:_auid_] [**-f** _mode_] [**-d** _mode_] **-g** _controllers_:_path_ [**-g** ...]

# DESCRIPTION

**cgcreate** 创建新的 cgroup（控制组），用于限制、度量并控制进程使用的资源。cgroup 控制器包括 memory、cpu、cpuset、blkio、net_cls 等。

# PARAMETERS

**-g CONTROLLERS:PATH**
> 指定 cgroup 的控制器和路径（必需）。控制器可用逗号分隔，或用 "*" 表示所有已挂载的控制器

**-t TUID:TGID**
> 设置 tasks 文件的所有权（决定谁可以添加进程）

**-a AUID:AGID**
> 设置控制文件的所有权（决定谁可以修改参数）

**-d, --dperm=MODE**
> 以八进制表示法设置目录权限（如 755）

**-f, --fperm=MODE**
> 以八进制表示法设置参数文件权限

**-s, --tperm=MODE**
> 以八进制表示法设置 tasks 文件权限

**-h, --help**
> 显示帮助信息

# CAVEATS

Cgroups v1 和 v2 的层级结构与功能不同。在 cgroups v2 系统上，语法和可用控制器可能有所差异。创建的 cgroup 会一直存在，直到用 cgdelete 删除或系统重启。

# HISTORY

**cgcreate** 是 **libcgroup** 的一部分，后者为管理 Linux 控制组提供用户态工具。控制组在内核 2.6.24 中引入。

# INSTALL

```apt: sudo apt install cgroup-tools```

```apk: sudo apk add cgroup-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cgdelete](/man/cgdelete)(1), [cgexec](/man/cgexec)(1), [cgset](/man/cgset)(1), [cgroups](/man/cgroups)(7)

# RESOURCES

```[Source code](https://github.com/libcgroup/libcgroup)```

<!-- verified: 2026-06-22 -->
