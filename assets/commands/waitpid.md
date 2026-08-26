# TAGLINE

等待任意进程终止

# TLDR

等待**进程**退出

```waitpid [pid1] [pid2]```

带**超时时间**等待

```waitpid -t [n] [pid1] [pid2]```

忽略已**退出**的进程

```waitpid -e [pid1] [pid2]```

等待 **N** 个进程

```waitpid -c [n] [pid1] [pid2]```

显示**帮助**

```waitpid -h```

# SYNOPSIS

**waitpid** [_OPTIONS_] _PID_...

# PARAMETERS

**-t, --timeout** _SECONDS_
> 最长等待时间

**-e, --exited**
> PID 已经退出时不报错

**-c, --count** _N_
> 等待直到 N 个进程已退出

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**waitpid** 按 PID 等待任意进程的终止。与 shell 内建的 wait 不同，它可以等待任何进程，而不只是当前 shell 的子进程。

该命令会阻塞，直到所有指定进程都终止或超时到期。

# CAVEATS

属于 util-linux 的一部分。只能监视当前用户可见的进程。监视进程需要相应权限。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wait](/man/wait)(1), [kill](/man/kill)(1)
