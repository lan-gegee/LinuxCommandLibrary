# TAGLINE

从镜像仓库下载容器镜像

# TLDR

**拉取一个镜像**

```docker pull [image]```

**拉取指定标签**

```docker pull [image]:[tag]```

**拉取所有标签**

```docker pull -a [image]```

**从私有镜像仓库拉取**

```docker pull [registry.example.com/image]:[tag]```

**按摘要拉取**

```docker pull [image]@sha256:[digest]```

**拉取特定平台的镜像**

```docker pull --platform linux/arm64 [image]```

# SYNOPSIS

**docker** **pull** [_options_] _name[:tag|@digest]_

# PARAMETERS

**-a**, **--all-tags**
> 下载软件仓库中所有带标签的镜像。

**--disable-content-trust**
> 跳过镜像验证。

**--platform** _string_
> 设置平台（例如 linux/amd64、linux/arm64）。

**-q**, **--quiet**
> 抑制详细输出。

# DESCRIPTION

**docker pull** 从镜像仓库下载镜像，默认从 Docker Hub 拉取。未指定标签时拉取 latest 标签。镜像按层下载，Docker 会缓存这些层以优化后续拉取。支持多平台镜像并自动检测平台。

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

[docker-image-pull](/man/docker-image-pull)(1), [docker-run](/man/docker-run)(1), [docker-images](/man/docker-images)(1)
