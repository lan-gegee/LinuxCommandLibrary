# TAGLINE

设置或显示 shell 资源限制

# TLDR

**显示所有限制**

```ulimit -a```

**显示文件大小限制**

```ulimit -f```

**设置打开文件数限制**

```ulimit -n [4096]```

**显示栈大小**

```ulimit -s```

**设置无限制的栈**

```ulimit -s unlimited```

**显示硬限制**

```ulimit -Ha```

# SYNOPSIS

**ulimit** [_-a_] [_-f_] [_-n_] [_-s_] [_-H_] [_-S_] [_value_]

# PARAMETERS

**-a**
> 显示当前所有资源限制。

**-c**
> 核心转储文件的最大大小（块）。

**-d**
> 进程数据段的最大大小（KB）。

**-f**
> shell 写入文件的最大大小（块）。

**-l**
> 可锁定到内存中的最大大小（KB）。

**-m**
> 最大常驻内存集大小（KB）。

**-n**
> 打开文件描述符的最大数量。

**-p**
> 管道缓冲区大小（512 字节块）。

**-s**
> 最大栈大小（KB）。

**-t**
> 最大 CPU 时间（秒）。

**-u**
> 单个用户的最大进程数。

**-v**
> 最大虚拟内存量（KB）。

**-H**
> 设置或显示硬限制。

**-S**
> 设置或显示软限制（默认）。

# DESCRIPTION

**ulimit** 是一个 shell 内建命令，用于控制当前 shell 会话及其派生的所有进程的资源限制。它可以对 CPU 时间、内存使用、打开的文件描述符、进程数量、文件大小及其他系统资源设置限制。

每种资源都有一个软限制（用户可将其提高到硬限制为止的有效限制）和一个硬限制（只有 root 才能提高的上限）。不使用 **-H** 或 **-S** 标志时，ulimit 默认显示和设置软限制。

这些限制对于防止失控进程耗尽所有系统资源，以及为需要更高限制的应用程序进行配置非常重要，例如需要更多打开文件描述符的数据库服务器。

# CAVEATS

shell 内建命令——设置仅作用于当前 shell 会话及其子进程。要持久化限制，请配置 **/etc/security/limits.conf** 或 systemd unit 文件。只有 root 能提高硬限制。

# HISTORY

**ulimit** 是标准的 Unix shell 内建命令，用于控制资源限制，在 bash、zsh 及其他 shell 中均可用。

# SEE ALSO

[limits.conf](/man/limits.conf)(5), [sysctl](/man/sysctl)(8), [getrlimit](/man/getrlimit)(2)
