# TAGLINE

显示 System V IPC 资源的相关信息

# TLDR

显示**所有**活跃的 IPC 设施

```ipcs```

显示活跃的共享**内存**段

```ipcs -m```

显示活跃的消息**队列**

```ipcs -q```

显示活跃的**信号量**

```ipcs -s```

按 ID 显示**特定共享内存**段的详情

```ipcs -m -i [shmid]```

显示系统**限制**

```ipcs -l```

显示当前用量的**摘要**

```ipcs -u```

显示**创建者/所有者**信息

```ipcs -c```

显示**最后访问时间**

```ipcs -t```

# SYNOPSIS

**ipcs** [_options_]

# PARAMETERS

**-m**, **--shmems**
> 显示共享内存段

**-q**, **--queues**
> 显示消息队列

**-s**, **--semaphores**
> 显示信号量集

**-i**, **--id** _ID_
> 显示特定资源的详情

**-l**, **--limits**
> 显示系统限制

**-u**, **--summary**
> 显示用量摘要

**-c**, **--creator**
> 显示创建者和所有者的 UID/PID

**-p**, **--pid**
> 显示最后操作者的 PID

**-t**, **--time**
> 显示最后访问时间

**--human**
> 以人类可读格式显示大小

# DESCRIPTION

**ipcs** 显示 System V IPC 资源的信息：共享内存段、消息队列和信号量数组。它显示资源 ID、键、所有者、权限和大小。

这对于监视 IPC 资源用量以及发现需要用 ipcrm 清理的孤立资源至关重要。

# CAVEATS

只显示 System V IPC，不包括 POSIX IPC 资源。用户只能看到自己有权限访问的资源（root 可见全部）。资源数量异常庞大可能意味着存在泄漏。

# HISTORY

自 **1980 年代**初 System V IPC 引入以来，ipcs 就一直是标准的 Unix 工具。它仍是检查 System V IPC 资源的主要工具。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ipcmk](/man/ipcmk)(1), [ipcrm](/man/ipcrm)(1), [lsipc](/man/lsipc)(1)
