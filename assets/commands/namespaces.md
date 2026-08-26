# TAGLINE

Linux 内核命名空间资源隔离概述

# TLDR

**列出所有命名空间**

```lsns```

**进入进程的命名空间**

```nsenter -t [PID] -a```

**创建新的挂载命名空间**

```unshare --mount [command]```

**创建新的网络命名空间**

```ip netns add [name]```

**在新的用户命名空间中运行**

```unshare --user --map-root-user [command]```

# SYNOPSIS

**namespaces** - Linux kernel namespace overview

# DESCRIPTION

**命名空间（Namespaces）**是一项 Linux 内核特性，它将全局系统资源封装在一个抽象层中，使命名空间内的进程看起来拥有该资源自己独立的实例。它们是 Docker 和 LXC 等容器技术的基础。

每种命名空间类型隔离系统的不同方面。

# NAMESPACE TYPES

```
mnt    - Mount points
pid    - Process IDs
net    - Network devices, stacks, ports
ipc    - System V IPC, POSIX message queues
uts    - Hostname and NIS domain name
user   - User and group IDs
cgroup - Cgroup root directory
time   - Boot and monotonic clocks
```

# RELATED TOOLS

```
unshare   - Create new namespace
nsenter   - Enter existing namespace
lsns      - List namespaces
ip netns  - Network namespace management
```

# SYSTEM CALLS

```
clone()    - Create process in new namespace
unshare()  - Disassociate from current namespace
setns()    - Join an existing namespace
ioctl()    - Discover namespace relationships
```

# CAVEATS

某些操作需要 root/相应能力。存在命名空间数量限制。用户命名空间有安全隐患。

# HISTORY

命名空间从内核 **2.4.19**（2002 年）的挂载命名空间开始逐步加入 Linux。完整的容器支持大约在内核 **3.8**（2013 年）时成熟。

# SEE ALSO

[unshare](/man/unshare)(1), [nsenter](/man/nsenter)(1), [lsns](/man/lsns)(8), [clone](/man/clone)(2), [ip](/man/ip)(8), [cgroups](/man/cgroups)(7)
