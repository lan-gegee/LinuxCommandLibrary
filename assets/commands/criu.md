# TAGLINE

在用户态对运行中的进程做检查点与恢复

# TLDR

**检查**内核是否支持 checkpoint/restore

```criu check```

对运行中的进程树**建立检查点**并存入镜像目录

```sudo criu dump -t [pid] -D [path/to/image_dir] --shell-job```

对进程**建立检查点**的同时让它继续运行，包括 TCP 套接字

```sudo criu dump -t [pid] -D [path/to/image_dir] --tcp-established --leave-running```

**从镜像目录恢复**进程树

```sudo criu restore -D [path/to/image_dir] --shell-job```

**以分离方式恢复**（不成为被恢复进程树的父进程）

```sudo criu restore -D [path/to/image_dir] -d```

**通过网络提供内存页**以支持热迁移

```sudo criu page-server -D [path/to/image_dir] --port [1234]```

# SYNOPSIS

**criu** _command_ [_option_ ...]

# PARAMETERS

**-t**, **--tree** _pid_
> 要转储的根任务的 PID。

**-D**, **--images-dir** _dir_
> 存放或读取镜像文件的目录。

**-W**, **--work-dir** _dir_
> 日志与工作文件所在目录（默认为镜像目录）。

**-v**[_n_], **--verbosity**
> 设置日志详细程度（可重复指定）。

**-R**, **--leave-running**
> 转储成功后让任务继续运行。

**-s**, **--leave-stopped**
> 转储后让任务保持停止状态（对热迁移很有用）。

**--tcp-established**
> 对已建立的 TCP 连接做检查点与恢复。

**--shell-job**
> 允许对 shell 作业做检查点/恢复（处理控制终端）。

**--manage-cgroups**
> 随进程一起保存并恢复 cgroup 配置。

**-d**, **--restore-detached**
> 成功后与被恢复的进程树分离。

**--display-stats**
> 完成时打印转储或恢复的统计信息。

# DESCRIPTION

**criu**（Checkpoint and Restore In Userspace，用户态检查点与恢复）会冻结正在运行的 Linux 应用——乃至整个容器——并将其完整状态序列化为一组镜像文件。内存、打开的文件描述符、管道、套接字、命名空间以及 cgroup 归属全部被捕获。之后通过 **criu restore** 可以从这些镜像重建等效的进程，还可以选择在另一台主机上进行，使应用从中断之处继续执行。

大部分工作都在用户态完成。CRIU 通过 **ptrace** 接管进程树，注入一个小型"寄生"代码模块（libcompel）来读取进程的地址空间，然后将所有内容写出到配置好的镜像目录。恢复则逆转这一流程：重建命名空间、重新创建文件描述符、映射内存，最终把控制权交回原来的程序计数器位置。

CRIU 是 **OpenVZ**、**LXC/LXD** 和 **Podman** 中热迁移功能的基石，也被 **runc** 和 **Kubernetes** 用于对容器进行快照和迁移。它还能加快冷启动：先预热应用，再按需从检查点恢复运行。

# CAVEATS

CRIU 仅支持 Linux，且通常需要 **CAP_SYS_ADMIN**（root）。并非每种内核资源都可以做检查点：GPU 上下文、部分 netfilter 状态以及某些外部资源可能需要插件支持或根本不受支持。恢复进程一般要求相同的 PID 可用，这通常意味着要在全新的 PID 命名空间内进行恢复。务必先运行 **criu check**，确认你的内核提供了所需的接口。

# HISTORY

CRIU 由 OpenVZ / Virtuozzo 团队的 **Pavel Emelyanov** 于 **2011 年**发起，**2012 年 7 月**首次公开发布。到 Linux 内核 **3.11**（2013 年 9 月）时，所需的系统调用和接口已合并进主线，CRIU 因此得以在原生内核上运行。如今它由 GitHub 上的 **checkpoint-restore** 社区维护，并持续保持定期发布。

# INSTALL

```apt: sudo apt install criu```

```dnf: sudo dnf install criu```

```pacman: sudo pacman -S criu```

```zypper: sudo zypper install criu```

```nix: nix profile install nixpkgs#criu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runc](/man/runc)(8), [ptrace](/man/ptrace)(2)
