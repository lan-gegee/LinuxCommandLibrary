# TAGLINE

管理 Podman 中的容器镜像

# TLDR

**列出镜像**

```podman image list```

**移除镜像**

```podman image rm [image]```

**拉取镜像**

```podman image pull [image:tag]```

**查看镜像详情**

```podman image inspect [image]```

**构建镜像**

```podman image build -t [name] [path]```

**清理未使用的镜像**

```podman image prune```

# SYNOPSIS

**podman** **image** _command_ [_options_]

# PARAMETERS

**list**
> 列出镜像。

**rm** _image_
> 移除镜像。

**pull** _image_
> 从 registry 拉取镜像。

**push** _image_
> 将镜像推送到 registry。

**build**
> 从 Dockerfile 构建镜像。

**inspect** _image_
> 显示镜像详情。

**prune**
> 移除未使用的镜像。

**tag** _src_ _dest_
> 为镜像打标签。

# DESCRIPTION

**podman image** 管理容器镜像。它是 Podman 镜像操作的子命令。支持拉取、构建、打标签和移除镜像。兼容 OCI 和 Docker 镜像格式。

# INSTALL

```apt: sudo apt install podman```

```dnf: sudo dnf install podman```

```pacman: sudo pacman -S podman```

```apk: sudo apk add podman```

```zypper: sudo zypper install podman```

```brew: brew install podman```

```nix: nix profile install nixpkgs#podman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [podman-pull](/man/podman-pull)(1)
