# TAGLINE

Containerd 命令行客户端

# TLDR

**列出**所有容器

```ctr containers list```

**列出**所有镜像

```ctr images list```

**拉取**镜像

```ctr images pull [image]```

为镜像**打标签**

```ctr images tag [source_image]:[source_tag] [target_image]:[target_tag]```

列出 Kubernetes 命名空间中的**镜像**

```ctr -n k8s.io images list```

**运行**容器

```ctr run [docker.io/library/alpine:latest] [my-container]```

# SYNOPSIS

**ctr** [_global options_] _command_ [_arguments_]

# DESCRIPTION

**ctr** 是 containerd 的命令行客户端。containerd 是业界标准的容器运行时，ctr 提供了底层的容器与镜像管理能力。

与 Docker CLI 不同，ctr 面向调试和直接与 containerd 交互而设计，并非面向日常使用。Kubernetes 通常通过 crictl 来使用 containerd。

# SUBCOMMANDS

**containers list**
> 列出所有容器

**containers rm** _id_
> 删除容器

**images list**
> 列出所有镜像

**images pull** _ref_
> 拉取镜像

**images push** _ref_
> 推送镜像

**images tag** _source_ _target_
> 为镜像打标签

**run** _image_ _container_id_
> 运行容器

**tasks list**
> 列出运行中的任务

**tasks kill** _container_id_
> 终止运行中的任务

**snapshots list**
> 列出快照

**namespaces list**
> 列出命名空间

**content fetch** _ref_
> 从远端获取内容

# PARAMETERS

**-n**, **--namespace** _namespace_
> 要使用的命名空间。默认：default。Kubernetes 使用 k8s.io。

**--address** _address_
> containerd GRPC 服务器的地址。

**--connect-timeout** _duration_
> 连接 containerd 的超时时间。

**--debug**
> 在日志中启用调试输出。

# CAVEATS

这是主要用于调试的底层工具。Kubernetes 环境请使用 crictl。想要通用的类 Docker 体验请使用 nerdctl。需要 root 权限或能访问 containerd 套接字。

# HISTORY

**ctr** 是 **containerd** 的一部分。containerd 最初由 Docker Inc. 开发，并于 **2017 年**捐赠给 **云原生计算基金会（CNCF）**。containerd 已成为 CNCF 毕业项目，现在是 Kubernetes 及众多平台的标准容器运行时。

# INSTALL

```apt: sudo apt install containerd```

```dnf: sudo dnf install containerd```

```pacman: sudo pacman -S containerd```

```apk: sudo apk add containerd-ctr```

```zypper: sudo zypper install containerd```

```brew: brew install containerd```

```nix: nix profile install nixpkgs#containerd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[containerd](/man/containerd)(8), [crictl](/man/crictl)(1), [nerdctl](/man/nerdctl)(1)
