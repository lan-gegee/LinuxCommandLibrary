# TAGLINE

创建可细粒度控制资源共享的子进程

# TLDR

**以命名空间隔离克隆进程**（C 语言）

```clone(child_func, stack_top, CLONE_NEWNS | SIGCHLD, arg)```

**创建新的命名空间**（unshare 命令）

```sudo unshare --mount --uts --ipc --net --pid --fork /bin/bash```

**无需 root 创建用户命名空间**

```unshare --user --map-root-user /bin/bash```

**进入进程的现有命名空间**

```sudo nsenter --target [pid] --mount --uts --ipc --net --pid```

# SYNOPSIS

```c
#include <sched.h>

int clone(int (*fn)(void *), void *stack, int flags, void *arg, ...);
```

# PARAMETERS

**CLONE_NEWNS**
> 创建新的挂载命名空间。

**CLONE_NEWUTS**
> 创建新的 UTS 命名空间（主机名/域名）。

**CLONE_NEWIPC**
> 创建新的 IPC 命名空间。

**CLONE_NEWPID**
> 创建新的 PID 命名空间。

**CLONE_NEWNET**
> 创建新的网络命名空间。

**CLONE_NEWUSER**
> 创建新的用户命名空间。

**CLONE_NEWCGROUP**
> 创建新的 cgroup 命名空间。

**CLONE_VM**
> 共享虚拟内存空间（用于线程）。

**CLONE_FILES**
> 共享文件描述符表。

**CLONE_FS**
> 共享文件系统信息（根目录、当前工作目录、umask）。

**CLONE_SIGHAND**
> 共享信号处理函数表。

**CLONE_THREAD**
> 将子进程放入与调用者相同的线程组。

**CLONE_SYSVSEM**
> 共享 System V 信号量的调整值。

**CLONE_CHILD_SETTID**
> 在子进程内存中的某个位置存储子线程 ID。

**CLONE_CHILD_CLEARTID**
> 子进程退出时清除其内存中某位置的子线程 ID。

# DESCRIPTION

**clone()** 是一个 Linux 系统调用，它创建新进程或线程，并可细粒度控制父子之间共享哪些资源。它既是线程创建（通过 pthread）的基础，也是容器隔离（通过命名空间）的基础。

与创建父进程完整副本的 **fork()** 不同，clone() 允许精确指定要共享哪些资源（内存、文件描述符、信号处理函数）或隔离哪些资源（命名空间）。这种灵活性使得线程（最大共享）和容器（最大隔离）都得以实现。

命名空间标志为系统资源创建隔离环境。Docker 等容器使用带命名空间标志的 clone() 来提供进程隔离。**unshare** 和 **nsenter** 命令在用户空间提供了对这些能力的访问。flags 参数的低字节包含子进程退出时发送给父进程的信号编号。

# CAVEATS

创建命名空间通常需要 root 权限，用户命名空间除外。使用不当可能造成资源泄漏或安全问题。该函数接口复杂；栈分配出错很常见。创建线程时应使用 pthread_create() 而非直接调用 clone()。**clone3()** 系统调用（Linux 5.3+）提供了更易扩展的接口。

# HISTORY

**clone()** 系统调用于 Linux **1.3.43** 版本（1995 年）引入，用于支持原生线程实现。自内核 **2.4.19**（2002 年）加入挂载命名空间起，它随命名空间支持的发展而显著演进。用户命名空间在内核 **3.8**（2013 年）中加入，使非特权容器创建成为可能。**clone3()** 于内核 **5.3**（2019 年）加入，是其更易扩展的后继者。

# SEE ALSO

[unshare](/man/unshare)(1), [nsenter](/man/nsenter)(1), [namespaces](/man/namespaces)(7), [docker](/man/docker)(1)
