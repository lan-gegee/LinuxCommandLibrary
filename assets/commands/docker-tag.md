# TAGLINE

为 Docker 镜像创建标签

# TLDR

**为一个镜像打标签**

```docker tag [source_image] [target_image]:[tag]```

**为私有镜像仓库打标签**

```docker tag [image] [registry.example.com/image]:[tag]```

**按镜像 ID 打标签**

```docker tag [image_id] [repository]:[tag]```

**添加 latest 标签**

```docker tag [image]:[version] [image]:latest```

# SYNOPSIS

**docker** **tag** _source_image[:tag]_ _target_image[:tag]_

# DESCRIPTION

**docker tag** 创建一个引用现有镜像的标签。一个镜像可以有多个标签。标签用于对镜像进行版本管理，并为其推送到镜像仓库做准备。

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

[docker-image-tag](/man/docker-image-tag)(1)
