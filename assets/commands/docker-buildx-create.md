# TAGLINE

创建新的 Docker Buildx 构建器实例

# TLDR

使用当前 Docker context **创建**构建器

```docker buildx create```

**创建**命名构建器并切换到它

```docker buildx create --name [mybuilder] --use```

在容器中**创建**多平台构建器

```docker buildx create --name [multiarch] --driver docker-container --platform linux/amd64,linux/arm64 --use```

向现有构建器**追加**一个节点

```docker buildx create --name [mybuilder] --append [context_name]```

**创建**带自定义 BuildKit 配置的构建器

```docker buildx create --buildkitd-config [path/to/buildkitd.toml]```

# SYNOPSIS

**docker buildx create** [_options_] [_context_|_endpoint_]

# PARAMETERS

**--append**
> 向现有构建器追加一个节点，而不是新建构建器。需要配合 **--name**。

**--bootstrap**
> 创建后立即启动构建器。

**--buildkitd-config** _file_
> BuildKit 守护进程配置文件。

**--buildkitd-flags** _flags_
> 传给 BuildKit 守护进程的额外标志；会覆盖 **--buildkitd-config** 中的值。

**--driver** _driver_
> 构建器驱动：**docker**（默认）、**docker-container**、**kubernetes** 或 **remote**。

**--driver-opt** _options_
> 驱动专属选项（例如为 **docker-container** 设置 **network=host**）。

**--leave**
> 从构建器中移除一个节点，而不是创建节点。需要配合 **--name** 和 **--node**。

**--name** _name_
> 构建器实例名称。若省略则自动生成。

**--node** _node_
> 要创建或修改的节点名称。默认为构建器名称加数字后缀。

**--platform** _platforms_
> 该节点支持的平台，逗号分隔（例如 **linux/amd64,linux/arm64**）。

**--timeout** _duration_
> 加载构建器状态的超时时间（默认：**20s**）。

**--use**
> 将当前使用的构建器切换为新创建的实例。

# DESCRIPTION

**docker buildx create** 会配置一个新的 Buildx 构建器实例，指向某个 Docker context 或端点。构建器是一个隔离的环境，**docker buildx build** 在其中运行；每个 Docker context 也各自拥有一个默认构建器。

可选的 _context_ 参数是 **docker context ls** 中列出的名称。_endpoint_ 可以是 Docker 套接字地址（即 **DOCKER_HOST** 的值）。两者都未提供时，由当前活动的 Docker 配置决定目标。

驱动决定构建在哪里执行。**docker** 驱动使用守护进程内置的构建器，构建时隐含 **--load**，但无法构建多平台镜像或导出缓存。**docker-container** 会启动一个专用的 BuildKit 容器，支持多平台构建和缓存导出；除非使用 **--load**，镜像不会加载进 **docker images**。**kubernetes** 在 Pod 中运行 BuildKit。**remote** 连接到外部管理的 BuildKit 守护进程。

用 **--append** 可以把另一个节点（context/endpoint）加入现有的命名构建器，让 Buildx 将构建路由到支持所需平台的节点。用 **--leave** 配合 **--name** 和 **--node** 可将节点从构建器上分离。

# CAVEATS

**docker** 驱动不支持多平台镜像构建或缓存导出。**docker-container**、**kubernetes** 和 **remote** 驱动需要通过 **docker buildx build --load** 才能让镜像出现在 **docker images** 中。如果远程或 Kubernetes 构建器的端点在 **--timeout** 内不可达，它们可能显示为非活动状态。

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

[docker-buildx-ls](/man/docker-buildx-ls)(1), [docker-buildx-rm](/man/docker-buildx-rm)(1), [docker-build](/man/docker-build)(1), [docker](/man/docker)(1)
