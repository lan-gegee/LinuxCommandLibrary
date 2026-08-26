# TAGLINE

在隔离的 Linux 命名空间中运行程序

# TLDR

在新的**网络命名空间**中运行命令

```unshare -n command```

在新的**挂载和 PID** 命名空间中运行命令

```unshare -m --pid --fork command```

在**隔离的网络**命名空间中运行 shell

```unshare -n /bin/bash```

创建带 root 映射的新**用户命名空间**

```unshare -r command```

在所有**新命名空间**中运行

```unshare --mount --uts --ipc --net --pid --fork command```

# SYNOPSIS

**unshare** [_options_] [_program_ [_arguments_]]

# DESCRIPTION

**unshare** 创建新的命名空间，然后在其中执行指定的程序。如果未指定程序，则运行 shell。命名空间为系统资源提供隔离。

# NAMESPACE OPTIONS

**-m, --mount[=file]**
> 创建新的挂载命名空间

**-u, --uts[=file]**
> 创建新的 UTS（主机名）命名空间

**-i, --ipc[=file]**
> 创建新的 IPC 命名空间

**-n, --net[=file]**
> 创建新的网络命名空间

**-p, --pid[=file]**
> 创建新的 PID 命名空间

**-U, --user[=file]**
> 创建新的用户命名空间

**-C, --cgroup[=file]**
> 创建新的 cgroup 命名空间

**-T, --time[=file]**
> 创建新的时间命名空间

# PARAMETERS

**-f, --fork**
> 执行前先 fork（PID 命名空间必需）

**-r, --map-root-user**
> 在用户命名空间中将当前用户映射为 root

**--map-user=UID**
> 在用户命名空间中映射到指定的 UID

**--map-group=GID**
> 在用户命名空间中映射到指定的 GID

**-R, --root=DIR**
> 设置根目录

**-w, --wd=DIR**
> 设置工作目录

**--propagation private|shared|slave|unchanged**
> 设置挂载传播方式

**--mount-proc[=DIR]**
> 在新的挂载命名空间中挂载 /proc

**--kill-child[=signame]**
> 当 unshare 终止时，向 fork 出的子进程发送信号（默认：SIGKILL）。与 --pid 搭配可用于终止整个进程树。

**-c, --map-current-user**
> 在新的用户命名空间中将当前有效用户 ID 和组 ID 映射为其自身。隐含 --setgroups=deny 和 --user。

**-S, --setuid** _uid_
> 在进入的命名空间中设置用户 ID。

**-G, --setgid** _gid_
> 在进入的命名空间中设置组 ID，并放弃补充组。

**--setgroups allow|deny**
> 在用户命名空间中允许或拒绝 setgroups(2)。

**--keep-caps**
> 在子进程中保留用户命名空间内授予的能力（capabilities）。

# CAVEATS

PID 命名空间必须搭配 **--fork** 使用，否则第一个进程会成为 PID 1，可能出现意料之外的行为。用户命名空间需要相应的内核支持，且可能存在安全限制。

# HISTORY

**unshare** 是 **util-linux** 的一部分。它使用 unshare(2) 系统调用创建新命名空间，而命名空间正是 Docker 等容器技术的基础。

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

[nsenter](/man/nsenter)(1), [lsns](/man/lsns)(1), [chroot](/man/chroot)(1), [clone](/man/clone)(2), [namespaces](/man/namespaces)(7), [systemd-nspawn](/man/systemd-nspawn)(1)
