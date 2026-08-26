# TAGLINE

获取或设置进程资源限制

# TLDR

显示当前进程的**所有限制**

```prlimit```

显示**特定进程**的限制

```prlimit -p [pid]```

以**自定义文件数限制**运行命令

```prlimit -n [1024] [command]```

# SYNOPSIS

**prlimit** [**-p** _pid_] [_limit_=_value_] [_command_]

# PARAMETERS

**-p, --pid _pid_**
> 要查询或修改的进程 ID

**-n, --nofile _limit_**
> 可打开文件的最大数量

**-u, --nproc _limit_**
> 最大进程数量

**-s, --stack _limit_**
> 最大栈大小

**-v, --as _limit_**
> 最大虚拟内存大小

**-m, --rss _limit_**
> 最大常驻内存集大小

# DESCRIPTION

**prlimit** 获取或设置进程资源限制。它可以查询运行中进程的限制，也可以用指定的限制运行新命令。限制可以按 soft:hard 形式设置，也可以只用单个值同时应用于两者。

该工具比 ulimit 提供更精细的控制，允许修改其他进程的限制，并同时设置软限制和硬限制。

# CAVEATS

修改其他进程需要相应权限。硬限制只能由 root 提升。某些限制在所有系统上可能都不可调整。

# HISTORY

**prlimit** 是 **util-linux** 的一部分，为 prlimit 系统调用提供了现代接口。它比 shell 内建的 ulimit 命令更灵活。

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

[ulimit](/man/ulimit)(1), [getrlimit](/man/getrlimit)(2)
