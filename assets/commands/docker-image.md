# TAGLINE

管理 Docker 镜像

# TLDR

**列出镜像**

```docker image ls```

**拉取一个镜像**

```docker image pull [image]:[tag]```

**删除一个镜像**

```docker image rm [image]```

**构建一个镜像**

```docker image build -t [name] [path]```

**查看镜像详情**

```docker image inspect [image]```

**查看镜像历史**

```docker image history [image]```

**清理未使用的镜像**

```docker image prune```

# SYNOPSIS

**docker** **image** _command_ [_options_]

# SUBCOMMANDS

**ls**
> 列出镜像。

**pull**
> 从镜像仓库下载镜像。

**push**
> 将镜像上传到镜像仓库。

**rm**
> 删除镜像。

**build**
> 从 Dockerfile 构建镜像。

**inspect**
> 显示详细信息。

**history**
> 查看镜像层。

**tag**
> 创建镜像标签。

**prune**
> 删除未使用的镜像。

**save**
> 将镜像保存为 tar 归档。

**load**
> 从 tar 归档加载镜像。

**import**
> 从 tar 包导入。

# DESCRIPTION

**docker image** 用于管理 Docker 镜像。镜像是用于创建容器的只读模板，包含在隔离环境中运行软件所需的应用程序代码、运行时、库、环境变量和配置文件。

Docker 镜像采用分层构建方式，Dockerfile 中的每条指令都会创建一个新层。这种分层系统通过镜像之间的层共享实现高效存储，并通过缓存加快构建速度。镜像由软件仓库名称、可选标签（默认为 "latest"）以及唯一的 SHA256 摘要来标识。

**docker image** 命令组提供全面的镜像生命周期管理，包括从镜像仓库拉取镜像、通过 Dockerfile 构建自定义镜像、打标签进行组织管理，以及清理占用磁盘空间的未使用镜像。

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

[docker](/man/docker)(1), [docker-image-ls](/man/docker-image-ls)(1), [docker-image-rm](/man/docker-image-rm)(1), [docker-image-pull](/man/docker-image-pull)(1)
