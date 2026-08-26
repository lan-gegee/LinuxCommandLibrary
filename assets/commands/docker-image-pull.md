# TAGLINE

从镜像仓库下载镜像

# TLDR

**拉取一个镜像**

```docker image pull [image]```

**拉取指定标签**

```docker image pull [image]:[tag]```

**拉取所有标签**

```docker image pull -a [image]```

**按摘要拉取**

```docker image pull [image]@[sha256:digest]```

**为特定平台拉取**

```docker image pull --platform [linux/arm64] [image]:[tag]```

**从特定镜像仓库拉取**

```docker image pull [registry.example.com/image]:[tag]```

# SYNOPSIS

**docker** **image** **pull** [_options_] _name[:tag|@digest]_

# PARAMETERS

**-a**, **--all-tags**
> 下载所有带标签的镜像。

**--disable-content-trust**
> 跳过镜像验证。

**--platform** _string_
> 设置平台（例如 linux/amd64）。

**-q**, **--quiet**
> 抑制详细输出。

# DESCRIPTION

**docker image pull** 从镜像仓库（registry）将 Docker 镜像或软件仓库下载到本地 Docker 守护进程。未指定镜像仓库时，默认使用 Docker Hub。如果未提供标签，则假定使用 **latest** 标签。

拉取操作会并行下载镜像层以提高效率。如果某些层已因其他镜像而存在于本地，Docker 会通过其内容寻址存储系统复用这些层，从而最大限度地减少带宽和存储占用。

可以按标签拉取镜像以进行特定版本的部署，也可以按 SHA256 摘要拉取以获得不可变且可验证的镜像引用。**--platform** 选项可用于为跨平台开发和部署场景拉取多架构镜像。

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

[docker-pull](/man/docker-pull)(1), [docker-image](/man/docker-image)(1), [docker-image-ls](/man/docker-image-ls)(1)
