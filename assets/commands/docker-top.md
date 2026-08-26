# TAGLINE

显示容器中正在运行的进程

# TLDR

**显示容器中运行的进程**

```docker top [container]```

**使用 BSD 风格的 ps 选项显示（完整信息）**

```docker top [container] aux```

**显示指定的列**

```docker top [container] -o pid,user,comm```

**使用容器 ID 代替名称**

```docker top [container_id]```

# SYNOPSIS

**docker top** _CONTAINER_ [_ps OPTIONS_]

# PARAMETERS

_CONTAINER_
> 运行中容器的名称或 ID。

_ps OPTIONS_
> 可选的 **ps**(1) 标志，转发给主机的 ps 用于格式化输出（例如 `aux`、`-eo pid,comm`）。

# DESCRIPTION

**docker top** 通过查询主机的进程列表并筛选出属于该容器命名空间的进程，来显示容器内正在运行的进程。概念上等同于 **docker container top**，并接受任意 **ps**(1) 选项来控制输出格式。

容器必须处于运行状态；已停止的容器无法用该命令查看。输出反映的是主机视角的进程（主机 PID），而不是容器内的 PID。

# CAVEATS

显示的进程 ID 是主机的 PID，而不是从容器内部看到的 PID。可用的 **ps** 选项取决于主机的 ps 实现（Linux 上为 procps）。对 Windows 容器的行为有所不同。

# INSTALL

```apt: sudo apt install docker-cli```

```dnf: sudo dnf install docker-cli```

```pacman: sudo pacman -S docker```

```apk: sudo apk add docker-cli```

```zypper: sudo zypper install docker```

```brew: brew install docker```

```nix: nix profile install nixpkgs#docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [docker-container-top](/man/docker-container-top)(1), [docker-ps](/man/docker-ps)(1), [docker-stats](/man/docker-stats)(1), [ps](/man/ps)(1), [top](/man/top)(1)
