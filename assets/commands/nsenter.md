# TAGLINE

在其他进程的名称空间中运行程序

# TLDR

在进程的**全部名称空间**中运行命令

```nsenter -t 1234 -a command```

进入进程的**挂载名称空间**

```nsenter -t 1234 --mount command```

进入进程的**网络名称空间**

```nsenter -t 1234 --net command```

进入进程的 **PID 名称空间**

```nsenter -t 1234 --pid command```

进入**多个名称空间**（UTS、time、IPC）

```nsenter -t 1234 -u -T -i -- command```

通过 **procfs 引用**进入名称空间

```nsenter --net=/proc/1234/ns/net command```

# SYNOPSIS

**nsenter** [_options_] [_program_ [_arguments_]]

# DESCRIPTION

**nsenter** 在另一个进程的名称空间中运行程序。它特别适合用于进入 Docker 容器、调试位于不同名称空间中的进程，或在 chroot 监狱中工作。如果未指定程序，则运行默认 shell。

# PARAMETERS

**-t, --target pid**
> 指定作为名称空间上下文来源的进程

**-a, --all**
> 进入目标进程的所有名称空间

**-m, --mount[=file]**
> 进入挂载名称空间

**-u, --uts[=file]**
> 进入 UTS（主机名/域名）名称空间

**-i, --ipc[=file]**
> 进入 IPC 名称空间

**-n, --net[=file]**
> 进入网络名称空间

**-p, --pid[=file]**
> 进入 PID 名称空间

**-U, --user[=file]**
> 进入用户名称空间

**-C, --cgroup[=file]**
> 进入 cgroup 名称空间

**-T, --time[=file]**
> 进入 time 名称空间

**-S, --setuid uid**
> 在进入的名称空间中设置用户 ID

**-G, --setgid gid**
> 在进入的名称空间中设置组 ID

**-F, --no-fork**
> 执行程序前不 fork

**-w, --wd[=directory]**
> 设置工作目录

**-r, --root[=directory]**
> 设置根目录

# CAVEATS

进入 PID 名称空间时，nsenter 默认会 fork。使用 **--no-fork** 可禁用此行为。进入其他用户的名称空间需要相应的权限。

# HISTORY

**nsenter** 是 **util-linux** 软件包的一部分。它使用 Linux 3.0 引入的 setns(2) 系统调用来进入已存在的名称空间。

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

[unshare](/man/unshare)(1), [clone](/man/clone)(2), [namespaces](/man/namespaces)(7)
