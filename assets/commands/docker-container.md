# TAGLINE

Docker 容器管理命令

# TLDR

**列出运行中的容器**

```docker container ls```

**列出所有容器，包括已停止的**

```docker container ls -a```

**以交互方式创建并运行容器**

```docker container run -it [image] [command]```

**在后台运行容器**

```docker container run -d -p [host_port]:[container_port] --name [name] [image]```

**启动已停止的容器**

```docker container start [container]```

**停止运行中的容器**

```docker container stop [container]```

**移除已停止的容器**

```docker container rm [container]```

**在运行中的容器内执行命令**

```docker container exec -it [container] [command]```

**查看容器日志**

```docker container logs -f [container]```

# SYNOPSIS

**docker** **container** _command_ [_options_]

# SUBCOMMANDS

**ls**
> 列出容器。

**run**
> 创建并运行容器。

**start**
> 启动已停止的容器。

**stop**
> 停止运行中的容器。

**rm**
> 移除容器。

**exec**
> 在容器内执行命令。

**logs**
> 查看容器日志。

**inspect**
> 显示详细信息。

**cp**
> 在容器与宿主机之间复制文件。

**stats**
> 显示资源使用统计。

**restart**
> 重启一个或多个容器。

**rename**
> 重命名容器。

**prune**
> 移除所有已停止的容器。

**top**
> 显示容器的运行进程。

**attach**
> 附着到运行中容器的 STDIN、STDOUT 和 STDERR。

**wait**
> 阻塞直到容器停止，然后打印退出码。

# DESCRIPTION

**docker container** 管理 Docker 容器。它提供覆盖容器完整生命周期的命令：创建、执行、监控和移除。

这是现代语法；大多数子命令也可以作为直接的 docker 命令使用（例如 **docker ps** = **docker container ls**）。

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

[docker](/man/docker)(1), [docker-run](/man/docker-run)(1), [docker-image](/man/docker-image)(1)
