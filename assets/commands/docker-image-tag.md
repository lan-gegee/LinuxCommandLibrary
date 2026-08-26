# TAGLINE

为 Docker 镜像打上软件仓库和版本标识

# TLDR

**用名称和版本为本地镜像打标签**

```docker image tag [source_image]:[tag] [target_image]:[version]```

**为私有镜像仓库给镜像打标签**

```docker image tag [image]:[tag] [registry.example.com:5000/image]:[tag]```

**按镜像 ID 打标签**

```docker image tag [image_id] [repository]:[tag]```

**从带版本号的镜像创建 latest 标签**

```docker image tag [image]:[version] [image]:latest```

# SYNOPSIS

**docker** **image** **tag** _SOURCE_IMAGE[:TAG]_ _TARGET_IMAGE[:TAG]_

# DESCRIPTION

**docker image tag** 创建一个指向现有镜像的标签。标签是镜像 ID 的别名，用于对镜像进行版本管理并将其推送到镜像仓库。多个标签可以指向同一个镜像，从而支持不同的版本方案或镜像仓库位置，而无需复制镜像数据。

标签名必须是有效的 ASCII 字符，可以包含大小写字母、数字、下划线、句点和连字符。不能以句点或连字符开头，长度限制为 128 个字符。

如果未指定标签，源和目标默认都使用 **latest**。

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

[docker-tag](/man/docker-tag)(1), [docker-image-ls](/man/docker-image-ls)(1), [docker-image-pull](/man/docker-image-pull)(1), [docker-image-rm](/man/docker-image-rm)(1), [docker-build](/man/docker-build)(1), [docker-pull](/man/docker-pull)(1)
