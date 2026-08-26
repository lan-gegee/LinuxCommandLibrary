# TAGLINE

资源限制查询与管理接口

# TLDR

**查看资源限制（shell）**

```ulimit -a```

**查看特定限制（打开文件数）**

```ulimit -n```

**显示进程的资源限制**

```prlimit --pid [pid]```

**为某条命令设置打开文件数限制**

```prlimit --nofile=4096 [command]```

# SYNOPSIS

**#include <sys/resource.h>**

**int getrlimit(int** _resource_, **struct rlimit** \*_rlim_**);**

**int setrlimit(int** _resource_, **const struct rlimit** \*_rlim_**);**

# PARAMETERS

_resource_
> 资源类型（RLIMIT_NOFILE、RLIMIT_NPROC 等）。

_rlim_
> 指向包含软/硬限制的 rlimit 结构的指针。

# DESCRIPTION

**getrlimit()** 和 **setrlimit()** 是用于查询和设置调用进程资源限制的系统调用。这些限制控制着各种系统资源的最大值。

**ulimit** shell 内建命令提供了对这些限制的命令行访问方式。每个限制都有软（当前生效）和硬（上限）两种取值。

# RESOURCES

```
RLIMIT_NOFILE  - Maximum open files
RLIMIT_NPROC   - Maximum processes
RLIMIT_AS      - Maximum address space
RLIMIT_CORE    - Maximum core file size
RLIMIT_STACK   - Maximum stack size
RLIMIT_DATA    - Maximum data segment
RLIMIT_FSIZE   - Maximum file size
RLIMIT_CPU     - CPU time limit
RLIMIT_MEMLOCK - Maximum locked memory
```

# SHELL ACCESS

```bash
ulimit -n        # Open files
ulimit -u        # Max processes
ulimit -s        # Stack size
ulimit -a        # All limits
ulimit -n 4096   # Set open files limit
```

# CONFIGURATION

**/etc/security/limits.conf**
> PAM 配置文件，用于按用户或组设置默认资源限制。

**/etc/systemd/system.conf**
> systemd 全局的默认资源限制设置，作用于服务和用户会话。

# CAVEATS

这是系统调用而非命令。非 root 用户不能提高硬限制。某些限制会影响子进程。PAM 可能在登录时设置限制。

# SEE ALSO

[ulimit](/man/ulimit)(1), [prlimit](/man/prlimit)(1), [limits.conf](/man/limits.conf)(5)
