# TAGLINE

提供对 Python 进程的远程调试访问

# TLDR

**连接到进程**

```manhole [pid]```

**连接到 Unix 套接字**

```manhole [/var/run/manhole.sock]```

**带超时连接**

```manhole -t [30] [pid]```

**详细模式连接**

```manhole -v [pid]```

# SYNOPSIS

**manhole** [_options_] _target_

# PARAMETERS

_TARGET_
> 进程 ID 或套接字路径。

**-t** _SECONDS_
> 连接超时时间。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**manhole** 提供对 Python 进程的远程调试访问。它会打开一个交互式 Python shell。

该工具连接到运行 manhole 库的进程。适用于调试正在运行的应用程序。

# CAVEATS

目标进程必须使用 manhole 库。在生产环境中使用需考虑安全问题。仅限 Python。

# HISTORY

manhole 的创建目的是在不重启的情况下为 **Python** 应用程序提供运行时调试访问。

# SEE ALSO

[gdb](/man/gdb)(1), [strace](/man/strace)(1), [python](/man/python)(1)
