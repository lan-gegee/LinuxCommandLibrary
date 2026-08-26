# TAGLINE

创建轻量级的无特权沙箱

# TLDR

在**只读环境**中运行程序

```bwrap --ro-bind / / [/bin/bash]```

允许访问**设备、进程信息和 tmpfs**

```bwrap --dev-bind /dev /dev --proc /proc --ro-bind / / --tmpfs /tmp [/bin/bash]```

**在没有网络访问的情况下运行**

```bwrap --unshare-net --ro-bind / / --dev /dev --proc /proc [/bin/bash]```

**运行隔离进程**，父进程退出时随之终止

```bwrap --unshare-all --die-with-parent --ro-bind / / --dev /dev --proc /proc [command]```

# SYNOPSIS

**bwrap** [_options_] _command_ [_arguments_]

# DESCRIPTION

**bwrap**（bubblewrap）使用 Linux 命名空间创建轻量级沙箱。它提供无特权的容器，以受限制的方式运行应用程序，限制其对文件系统、网络和其他系统资源的访问。

Flatpak 和其他沙箱系统常用该工具将应用与宿主系统隔离。

# PARAMETERS

**--ro-bind** _src_ _dest_
> 将源路径以只读方式绑定挂载到目标位置

**--bind** _src_ _dest_
> 将源路径以读写方式绑定挂载到目标位置

**--dev-bind** _src_ _dest_
> 以设备访问权限绑定挂载源路径

**--proc** _dest_
> 在目标位置挂载 procfs

**--tmpfs** _dest_
> 在目标位置挂载 tmpfs

**--unshare-pid**
> 创建新的 PID 命名空间

**--unshare-net**
> 创建新的网络命名空间

**--unshare-user**
> 创建新的用户命名空间

**--unshare-all**
> 隔离所有可用的命名空间

**--unshare-ipc**
> 创建新的 IPC 命名空间

**--unshare-uts**
> 创建新的 UTS 命名空间

**--unshare-cgroup**
> 创建新的 cgroup 命名空间

**--symlink** _SRC_ _DEST_
> 创建符号链接

**--dev** _DEST_
> 在目标位置挂载新的 devtmpfs

**--dir** _DEST_
> 创建目录

**--setenv** _VAR_ _VALUE_
> 设置环境变量

**--unsetenv** _VAR_
> 移除环境变量

**--chdir** _DIR_
> 更改工作目录

**--hostname** _HOSTNAME_
> 设置自定义主机名（需要 --unshare-uts）

**--die-with-parent**
> 父进程死亡时杀死沙箱

**--new-session**
> 通过 setsid() 创建新的终端会话

**--cap-add** _CAP_
> 添加 Linux capability

**--cap-drop** _CAP_
> 移除 Linux capability

**--seccomp** _FD_
> 从文件描述符加载 seccomp 规则

# CAVEATS

需要内核启用用户命名空间。并非完整的安全边界；某些攻击途径可能仍然存在。复杂的沙箱配置需要仔细设置绑定挂载。

# INSTALL

```apt: sudo apt install bubblewrap```

```dnf: sudo dnf install bubblewrap```

```pacman: sudo pacman -S bubblewrap```

```apk: sudo apk add bubblewrap```

```zypper: sudo zypper install bubblewrap```

```brew: brew install bubblewrap```

```nix: nix profile install nixpkgs#bubblewrap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firejail](/man/firejail)(1), [flatpak](/man/flatpak)(1), [unshare](/man/unshare)(1)
