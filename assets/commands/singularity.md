# TAGLINE

无需 root 权限的 HPC 容器运行时

# TLDR

**运行容器**

```singularity run [container.sif]```

**执行命令**

```singularity exec [container.sif] [command]```

进入容器的 shell

```singularity shell [container.sif]```

从定义文件构建

```singularity build [output.sif] [definition.def]```

从镜像仓库拉取

```singularity pull [docker://ubuntu:latest]```

构建沙箱

```singularity build --sandbox [directory] [docker://ubuntu]```

# SYNOPSIS

**singularity** _command_ [_options_] _container_ [_args_]

# PARAMETERS

**run**
> 运行容器。

**exec**
> 执行命令。

**shell**
> 交互式 shell。

**build**
> 构建容器。

**pull**
> 下载镜像。

**--sandbox**
> 可写目录。

**--fakeroot**
> 无 root 构建。

# DESCRIPTION

**Singularity**（现名 **Apptainer**）是为高性能计算（HPC）环境设计的容器运行时，Docker 的 root 特权模型在这种环境中并不实用。容器以调用用户的身份运行，无需守护进程或提升权限，因此可以安全地用于共享的多租户集群。

与 Docker 不同，Singularity 默认与宿主系统紧密集成，共享用户的主目录、网络和其他文件系统。这使得在容器内使用现有数据和工具非常简单。镜像保存为单个 SIF 文件，便于移植，可以从 Docker 镜像或定义文件构建，也可以直接从镜像仓库拉取。

该工具将完整的软件环境打包进不可变的容器中，使其在不同计算系统上产生一致的结果，从而实现可复现的科学研究。

# CAVEATS

运行时不兼容 Docker（无 Docker socket、无守护进程）。传统上构建 SIF 镜像需要 root 或用户命名空间；使用 **--fakeroot** 可以在没有 root 的情况下构建。目前维护着两个分支：**Apptainer**（Linux 基金会）和 **SingularityCE**（Sylabs）。

# HISTORY

**Singularity** 由 **劳伦斯伯克利实验室** 创建，用于在没有特权访问的 HPC 环境中运行容器。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [podman](/man/podman)(1), [apptainer](/man/apptainer)(1)
