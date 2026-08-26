# TAGLINE

面向 OCI 容器的无守护进程容器引擎

# TLDR

**运行容器**

```podman run [image]```

**列出运行中的容器**

```podman ps```

**列出所有容器**

```podman ps -a```

**拉取镜像**

```podman pull [image]```

**从 Dockerfile 构建**

```podman build -t [tag] [path]```

**停止容器**

```podman stop [container]```

**移除容器**

```podman rm [container]```

# SYNOPSIS

**podman** [_options_] _command_ [_args_]

# PARAMETERS

**run**
> 运行容器。

**ps**
> 列出容器。

**pull**
> 拉取镜像。

**build**
> 从 Containerfile 构建镜像。

**stop**
> 停止容器。

**rm**
> 移除容器。

**images**
> 列出镜像。

**exec**
> 在容器中执行。

**-d**, **--detach**
> 在后台运行。

# DESCRIPTION

**podman** 是一个无守护进程、无根模式的容器引擎，管理符合 OCI 规范的容器和镜像。与 Docker 不同，它不需要后台守护进程，且容器可以完全以非特权用户的身份运行。

其命令行界面设计为可直接替换 Docker，支持熟悉的命令如 **run**、**build**、**pull**、**ps**、**stop** 和 **rm**。Podman 还支持 pod（共享命名空间的容器组），这与 Kubernetes 的 pod 概念一致。它由 Red Hat 开发，使用 Buildah 构建镜像，并使用 crun/runc 作为容器运行时。

# CONFIGURATION

**/etc/containers/registries.conf**
> 全系统的容器 registry 配置，包括搜索 registry 和镜像源。

**/etc/containers/storage.conf**
> 容器镜像和层的存储驱动及路径配置。

**/etc/containers/containers.conf**
> 默认容器运行时设置，包括资源限制、日志和网络配置。

**~/.config/containers/**
> 无根模式 Podman 配置的用户级覆盖。

# CAVEATS

默认无根模式。Docker CLI 兼容。

# HISTORY

Podman 由 **Red Hat** 创建，作为无守护进程的 Docker 替代品。

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

[docker](/man/docker)(1), [buildah](/man/buildah)(1), [skopeo](/man/skopeo)(1)
