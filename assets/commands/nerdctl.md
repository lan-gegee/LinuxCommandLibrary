# TAGLINE

containerd（工业级标准容器运行时）的 Docker 兼容 CLI

# TLDR

**列出所有容器**（运行中和已停止）

```nerdctl ps -a```

以自定义名称**运行**容器

```nerdctl run --name [container_name] [image]```

**启动或停止**容器

```nerdctl start [container_name]```
```nerdctl stop [container_name]```

从镜像仓库**拉取**镜像

```nerdctl pull [image]```

**列出已下载的镜像**

```nerdctl images```

在容器中**执行**交互式 shell

```nerdctl exec -it [container_name] sh```

**移除**已停止的容器

```nerdctl rm [container1] [container2]```

**查看**容器的日志

```nerdctl logs -f [container_name]```

# SYNOPSIS

**nerdctl** _command_ [_options_] [_arguments_]

# COMMANDS

**run**
> 运行新容器

**ps**
> 列出容器

**start**
> 启动已停止的容器

**stop**
> 停止运行中的容器

**exec**
> 在运行中的容器里执行命令

**pull**
> 从镜像仓库拉取镜像

**push**
> 推送镜像到镜像仓库

**images**
> 列出镜像

**rm**
> 移除容器

**rmi**
> 移除镜像

**build**
> 从 Dockerfile 构建镜像

**logs**
> 获取容器日志

**compose**
> 兼容 Docker Compose 的命令

# PARAMETERS

**-a**, **--all**
> 显示所有容器（默认仅显示运行中的）

**-i**, **--interactive**
> 保持 STDIN 开启

**-t**, **--tty**
> 分配伪终端

**-d**, **--detach**
> 在后台运行容器

**--name** _name_
> 为容器指定名称

**-p**, **--publish** _port_
> 发布容器端口（主机:容器）

**-v**, **--volume** _mount_
> 绑定挂载卷（主机:容器）

**-f**, **--follow**
> 持续跟踪日志输出

**--rm**
> 容器退出后将其移除

**-e**, **--env** _VAR=VALUE_
> 设置环境变量

**--network** _network_
> 连接到指定网络

# DESCRIPTION

**nerdctl** 是 containerd 的 Docker 兼容 CLI，而 containerd 是工业级标准的容器运行时。它提供与 Docker 相同的命令体验，同时利用 containerd 的能力，包括无根（rootless）容器和惰性拉取镜像。

该工具支持 Docker Compose 文件、Dockerfile 构建以及大多数 Docker CLI 语法。它既能处理 Docker 镜像，也能处理 containerd 的镜像和仓库。

# CAVEATS

某些 Docker 功能可能没有完全对应的实现。无根模式需要配置用户命名空间。镜像兼容性取决于容器运行时的配置。

# HISTORY

**nerdctl** 由 **containerd** 维护者作为 containerd 项目的一部分开发。它为 containerd 提供了用户友好的 CLI，而 containerd 被 Kubernetes 和其他容器编排器用作底层运行时。

# INSTALL

```pacman: sudo pacman -S nerdctl```

```apk: sudo apk add nerdctl```

```zypper: sudo zypper install nerdctl```

```brew: brew install nerdctl```

```nix: nix profile install nixpkgs#nerdctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [containerd](/man/containerd)(8), [ctr](/man/ctr)(1), [podman](/man/podman)(1)
