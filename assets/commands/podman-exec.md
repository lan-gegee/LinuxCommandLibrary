# TAGLINE

在运行中的容器内执行命令

# TLDR

**在容器中执行命令**

```podman exec [container] [command]```

**交互式 Shell**

```podman exec -it [container] /bin/bash```

**以指定用户运行**

```podman exec -u [root] [container] [command]```

**设置环境变量**

```podman exec -e [VAR=value] [container] [command]```

# SYNOPSIS

**podman exec** [_options_] _container_ _command_ [_args_]

# PARAMETERS

**-i**, **--interactive**
> 保持 stdin 打开。

**-t**, **--tty**
> 分配 TTY。

**-u**, **--user** _user_
> 以指定用户身份运行。

**-e**, **--env** _var=val_
> 设置环境变量。

**-w**, **--workdir** _dir_
> 工作目录。

**-d**, **--detach**
> 在后台运行。打印 exec 会话 ID 并立即退出。

**--detach-keys** _sequence_
> 与容器分离的按键序列（默认：ctrl-p,ctrl-q）。

**--env-file** _file_
> 从以行分隔的文件读取环境变量。

**-l**, **--latest**
> 使用最近创建的容器，而无需指定名称或 ID。

**--preserve-fds** _N_
> 向进程额外传递 N 个文件描述符（stdin/stdout/stderr 之外）。

**--privileged**
> 给予该命令扩展权限。

# DESCRIPTION

**podman exec** 在运行中的容器内执行命令。它是调试、维护以及与容器进程交互的必备工具。

# CAVEATS

容器必须处于运行状态。命令必须存在于容器镜像中。无根模式的 Podman 存在用户命名空间限制。远程客户端不支持 **--latest** 标志。

# HISTORY

podman exec 是 **Podman** 的一部分，Podman 是由 **Red Hat** 开发的无守护进程容器引擎，作为 Docker 的兼容替代品。

# INSTALL

```apt: sudo apt install podman```

```dnf: sudo dnf install podman```

```pacman: sudo pacman -S podman```

```apk: sudo apk add podman```

```zypper: sudo zypper install podman```

```brew: brew install podman```

```nix: nix profile install nixpkgs#podman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman-run](/man/podman-run)(1), [podman](/man/podman)(1), [docker-exec](/man/docker-exec)(1)
