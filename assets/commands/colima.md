# TAGLINE

macOS 和 Linux 上的容器运行时

# TLDR

**以默认配置启动**

```colima start```

**以自定义资源配置启动**

```colima start --cpu [4] --memory [8] --disk [100]```

**以 containerd 运行时启动**

```colima start --runtime containerd```

**随 Kubernetes 一起启动**

```colima start --kubernetes```

**停止 Colima**

```colima stop```

**删除实例**

```colima delete```

**列出实例**

```colima list```

**SSH 进入虚拟机**

```colima ssh```

# SYNOPSIS

**colima** _command_ [_options_]

# DESCRIPTION

**colima** 以最少的设置和资源需求在 macOS 和 Linux 上提供容器运行时。它利用 Lima（Linux 虚拟机）创建运行 Docker 和 containerd 的环境，是 Docker Desktop 完全免费开源的替代方案。

在 macOS 上，Colima 可以选用 QEMU 或原生 Apple Virtualization 框架（VZ）以在 Apple Silicon 上获得更好性能。在 Linux 上，它提供一致的容器化环境。该工具自动配置 Docker 客户端连接、端口转发和卷挂载，使虚拟机层对用户完全透明。

Colima 支持多个运行时配置档案，可为不同项目创建相互独立的实例。可以启用 Kubernetes 集群用于本地开发。它与现有 Docker 工作流无缝集成，无需修改 docker 命令或 compose 文件。资源分配（CPU、内存、磁盘）可配置，且相比同类工具更加轻量。

# COMMANDS

**start**
> 启动 Colima 虚拟机

**stop**
> 停止 Colima 虚拟机

**delete**
> 删除 Colima 实例

**status**
> 显示状态

**list**
> 列出实例

**ssh**
> SSH 进入虚拟机

**nerdctl**
> 运行 nerdctl（containerd）

**version**
> 显示版本

# START OPTIONS

**--cpu** _n_
> CPU 数量

**--memory** _n_
> 内存大小（GB）

**--disk** _n_
> 磁盘大小（GB）

**--runtime** _type_
> 运行时：docker、containerd

**--kubernetes**
> 启用 Kubernetes

**--arch** _arch_
> 架构：x86_64、aarch64

**--vm-type** _type_
> 虚拟化方式：vz、qemu

**--profile** _name_
> 实例配置档案名称

# DOCKER USAGE

启动之后：
```
docker ps
docker run hello-world
```

# CAVEATS

需要 macOS 10.15+ 或 Linux。在 Apple Silicon 上 vz（Apple 虚拟化）更快。完全免费开源。

# INSTALL

```brew: brew install colima```

```nix: nix profile install nixpkgs#colima```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [nerdctl](/man/nerdctl)(1), [lima](/man/lima)(1)

# RESOURCES

```[Source code](https://github.com/abiosoft/colima)```

<!-- verified: 2026-06-22 -->
