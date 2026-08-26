# TAGLINE

为 HPC 构建、运行和管理应用容器

# TLDR

从 Docker Hub **下载容器**

```apptainer pull [path/to/image.sif] docker://[image]:[tag]```

从 Container Library **下载容器**

```apptainer pull [path/to/image.sif] library://[user/collection/container]:[tag]```

从定义文件**构建容器**

```apptainer build [path/to/image.sif] [path/to/definition.def]```

在容器内启动**交互式 shell**

```apptainer shell [path/to/image.sif]```

在容器内**执行命令**

```apptainer exec [path/to/image.sif] [command]```

**运行容器的默认 runscript**

```apptainer run [path/to/image.sif]```

**检查**容器的元数据

```apptainer inspect [path/to/image.sif]```

# SYNOPSIS

**apptainer** [_global options_] _command_ [_command options_]

# DESCRIPTION

**Apptainer** 是一个面向高性能计算（HPC）、科学计算和 AI/ML 工作负载设计的容器平台。与 Docker 不同，它无需 root 权限即可运行容器，并能与 Slurm、PBS、SGE 等现有 HPC 调度器无缝集成。

容器以单个 **SIF**（Singularity Image Format）文件的形式存储，因此具有极高的可移植性。Apptainer 支持从 Docker Hub、OCI 注册表和 Sylabs Container Library 拉取容器。

主要特性包括 GPU 和 MPI 支持、加密容器签名、用于持久化存储的 overlay 文件系统以及 OCI 运行时兼容性。

# SUBCOMMANDS

**build**
> 从定义文件或基础镜像构建容器

**exec**
> 在容器内执行命令

**run**
> 运行容器的默认 runscript

**shell**
> 在容器中启动交互式 shell

**pull**
> 从注册表下载容器镜像

**push**
> 将容器上传到注册表

**inspect**
> 显示容器元数据

**instance**
> 管理作为后台服务运行的容器

**cache**
> 管理本地镜像缓存

**overlay**
> 管理 EXT3 可写 overlay 镜像

**key**
> 管理用于签名和验证的 OpenPGP 密钥

**sign**
> 对容器进行加密签名

**verify**
> 验证容器的加密签名

# CONFIGURATION

**/etc/apptainer/apptainer.conf**
> 系统级配置，控制安全选项、绑定路径、挂载行为和资源限制。

**~/.apptainer/**
> 每个用户的目录，存放缓存的镜像、密钥和远程端点配置。

# CAVEATS

SIF 文件需要大量磁盘空间，且一旦构建便不可更改。修改需要重新构建或使用 overlay 文件系统。由于用户命名空间和权限处理方式的差异，某些 Docker 容器可能无法完美运行。

# HISTORY

Apptainer 源自 **Singularity**，由 Gregory Kurtzer 于 **2015** 年在劳伦斯伯克利国家实验室创建。**2021** 年，Linux 基金会接管该项目并将其更名为 Apptainer，以确保供应商中立治理。该项目已成为 HPC 环境中容器计算的事实标准。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[singularity](/man/singularity)(1), [docker](/man/docker)(1), [podman](/man/podman)(1), [buildah](/man/buildah)(1)

# RESOURCES

```[Source code](https://github.com/apptainer/apptainer)```

```[Homepage](https://apptainer.org)```

```[Documentation](https://apptainer.org/docs/)```

<!-- verified: 2026-06-11 -->
