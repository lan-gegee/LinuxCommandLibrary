# TAGLINE

基于 Linux 命名空间的无特权沙箱

# TLDR

在最小沙箱中**运行命令**

```bwrap --ro-bind /usr /usr --symlink usr/lib64 /lib64 --proc /proc --dev /dev --unshare-pid [command]```

**创建隔离的主目录**

```bwrap --ro-bind / / --bind [/tmp/fakehome] /home/user --unshare-all [command]```

**在网络隔离下运行**

```bwrap --ro-bind /usr /usr --unshare-net [command]```

为临时存储**挂载 tmpfs**

```bwrap --ro-bind / / --tmpfs /tmp --unshare-all [command]```

以读写方式**绑定挂载当前目录**

```bwrap --ro-bind / / --bind $(pwd) $(pwd) --chdir $(pwd) [command]```

**以伪 root 运行**（用户命名空间）

```bwrap --ro-bind / / --unshare-user --uid 0 --gid 0 [command]```

# SYNOPSIS

**bwrap** [_options_] [**--**] _command_ [_arguments_]

# DESCRIPTION

**bubblewrap**（bwrap）是一个无特权沙箱工具，使用 Linux 命名空间创建隔离环境。与传统容器不同，它可以借助用户命名空间在无 root 权限的情况下运行。

该工具创建一个新的挂载命名空间，其中仅包含从主机显式指定的绑定挂载。这允许对沙箱内进程可访问的内容进行细粒度控制。它还可以隔离网络、PID、IPC 和用户命名空间。

Bubblewrap 是 Flatpak 沙箱机制的基础，也可直接用于自定义的应用隔离。其设计注重安全与极简。

# PARAMETERS

**--ro-bind** _src_ _dest_
> 将 src 以只读方式绑定挂载到 dest。

**--bind** _src_ _dest_
> 读写方式的绑定挂载。

**--dev-bind** _src_ _dest_
> 带设备访问权限的绑定挂载。

**--tmpfs** _dest_
> 在目标位置挂载 tmpfs。

**--proc** _dest_
> 在目标位置挂载 procfs。

**--dev** _dest_
> 在目标位置创建新的 devtmpfs。

**--symlink** _src_ _dest_
> 创建符号链接。

**--unshare-all**
> 隔离所有可用的命名空间。

**--unshare-user**
> 创建新的用户命名空间。

**--unshare-pid**
> 创建新的 PID 命名空间。

**--unshare-net**
> 创建新的网络命名空间。

**--unshare-ipc**
> 创建新的 IPC 命名空间。

**--uid** _uid_
> 设置沙箱内的用户 ID。

**--gid** _gid_
> 设置沙箱内的组 ID。

**--chdir** _dir_
> 运行前切换到指定目录。

**--die-with-parent**
> 父进程退出时终止沙箱。

**--new-session**
> 创建新的终端会话。

# CAVEATS

需要内核支持用户命名空间（在某些系统上可能被禁用）。没有 seccomp 时并非所有系统调用都能被沙箱化。复杂的设置可能需要仔细安排挂载顺序。某些应用在受限环境中可能无法正常运行。

# HISTORY

**Bubblewrap** 由 **Red Hat** 的 **Alexander Larsson** 于 **2016 年**创建，是一个极简的无特权沙箱工具。它从 Flatpak 项目中抽离出来，提供独立的沙箱解决方案。其设计专注于简单、安全且无需 root 权限即可使用，因此适合桌面应用的隔离场景。

# INSTALL

```dnf: sudo dnf install bubblewrap```

```pacman: sudo pacman -S bubblewrap```

```zypper: sudo zypper install bubblewrap```

```brew: brew install bubblewrap```

```nix: nix profile install nixpkgs#bubblewrap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flatpak](/man/flatpak)(1), [unshare](/man/unshare)(1), [firejail](/man/firejail)(1), [namespaces](/man/namespaces)(7)

# RESOURCES

```[Source code](https://github.com/containers/bubblewrap)```

<!-- verified: 2026-06-22 -->
