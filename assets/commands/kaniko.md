# TAGLINE

在容器或 Kubernetes 中从 Dockerfile 构建容器镜像

# TLDR

**构建并推送镜像**到镜像仓库

```/kaniko/executor --dockerfile=[Dockerfile] --context=[dir://workspace] --destination=[gcr.io/project/image:tag]```

**只构建不推送**

```/kaniko/executor --dockerfile=[Dockerfile] --context=[.] --no-push```

**启用缓存构建**

```/kaniko/executor --dockerfile=[Dockerfile] --destination=[registry/image] --cache=true```

**将镜像保存为 tar 包**

```/kaniko/executor --dockerfile=[Dockerfile] --context=[.] --tar-path=[image.tar] --no-push```

**构建指定的目标阶段**

```/kaniko/executor --dockerfile=[Dockerfile] --destination=[registry/image] --target=[build-stage]```

**使用构建参数构建**

```/kaniko/executor --dockerfile=[Dockerfile] --destination=[registry/image] --build-arg=[VERSION=1.0]```

# SYNOPSIS

**/kaniko/executor** [_options_]

# PARAMETERS

**--dockerfile** _path_
> Dockerfile 路径。默认：Dockerfile。

**--context** _uri_
> 构建上下文：dir://、git://、s3://、gs:// 或本地路径。

**--destination** _registry/image:tag_
> 推送镜像的目标仓库。除非指定 --no-push，否则必需。

**--no-push**
> 构建镜像但不推送到仓库。

**--tar-path** _path_
> 将镜像保存为 tar 包而不推送。

**--cache**
> 启用层缓存。

**--cache-repo** _repository_
> 存储缓存层的仓库。

**--cache-ttl** _duration_
> 缓存过期时间。

**--target** _stage_
> 只构建到 Dockerfile 的指定阶段。

**--build-arg** _KEY=value_
> 设置构建时变量。可重复使用。

**--ignore-var-run**
> 拍摄镜像快照时忽略 /var/run。默认：true。

**--ignore-path** _path_
> 拍摄镜像快照时忽略指定路径。可重复使用。

**--snapshot-mode** _mode_
> 快照模式：full 或 redo（默认：redo）。

**--single-snapshot**
> 只在结束时拍一次快照，而不是每层都拍。

**--reproducible**
> 去除时间戳以实现可重现构建。

**--registry-mirror** _mirror_
> 使用镜像仓库 mirror 作为拉取缓存。

**--insecure**
> 推送到不安全的（HTTP）镜像仓库。

**--skip-tls-verify**
> 跳过 TLS 证书验证。

**--insecure-pull**
> 从不安全的（HTTP）镜像仓库拉取。

**--skip-tls-verify-pull**
> 拉取时跳过 TLS 证书验证。

**--kaniko-dir** _path_
> Kaniko 工作目录（默认：/kaniko）。

**--image-fs-extract-retry** _count_
> 提取镜像文件系统的重试次数。默认：0。

**--image-download-retry** _count_
> 以指数退避方式下载远程镜像的重试次数。默认：0。

**--label** _KEY=value_
> 设置镜像标签元数据。可重复使用。

**--verbosity** _level_
> 日志级别：panic、fatal、error、warn、info、debug、trace。

# DESCRIPTION

**kaniko** 在容器或 Kubernetes 集群内部从 Dockerfile 构建容器镜像，不需要特权访问或 Docker 守护进程。它在用户空间中执行每条 Dockerfile 命令并对文件系统做快照。

执行器本身以容器镜像（**gcr.io/kaniko-project/executor**）运行，因此非常适合 Kubernetes 中的 CI/CD 管道——在这些场景下 Docker-in-Docker 不可用，或出于安全原因不宜使用。

上下文来源包括本地目录（**dir://**）、Git 仓库（**git://**）、Google Cloud Storage（**gs://**）、Amazon S3（**s3://**）和 Azure Blob Storage。身份验证通过挂载的凭据或环境变量处理。

配合 **--cache** 使用层缓存可以显著加快构建速度，它会复用未变化的层。缓存的层存储在 **--cache-repo** 指定的仓库或由 **--destination** 推导出的仓库中。

调试镜像（**gcr.io/kaniko-project/executor:debug**）包含 busybox，便于排障。

# CAVEATS

Kaniko 在容器内部运行，不适合直接在宿主机上执行。某些 Dockerfile 特性的行为可能与 Docker 守护进程不同。**redo** 快照模式可能遗漏仅元数据的变更；必要时请使用 **full** 模式。**--reproducible** 标志会在构建结束时只拍一次快照，因此基础镜像上只会追加一层。

# HISTORY

Kaniko 由 **Google** 开发，于 **2018** 年作为 Google Container Tools 的一部分发布。它旨在让 Kubernetes 环境中的安全容器构建成为可能——在这些环境中运行 Docker 守护进程既不现实也被禁止。该项目由开源社区维护，广泛应用于云原生 CI/CD 管道。

# INSTALL

```nix: nix profile install nixpkgs#kaniko```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [buildah](/man/buildah)(1), [podman](/man/podman)(1)
