# TAGLINE

从本地存储中删除 Docker 镜像

# TLDR

**删除一个镜像**

```docker rmi [image]```

**删除多个镜像**

```docker rmi [image1] [image2]```

**强制删除**

```docker rmi -f [image]```

**删除所有悬空镜像**

```docker rmi $(docker images -f dangling=true -q)```

**按镜像 ID 删除**

```docker rmi [image_id]```

# SYNOPSIS

**docker** **rmi** [_options_] _image_ [_image..._]

# PARAMETERS

**-f**, **--force**
> 强制删除。

**--no-prune**
> 不删除无标签的父镜像。

# DESCRIPTION

**docker rmi** 删除一个或多个镜像。正在被容器使用的镜像除非强制删除否则无法移除。该命令是 docker image rm 的简写形式。删除镜像会删除其所有层，除非这些层与其他镜像共享。悬空镜像是不再被任何带标签镜像引用的无标签镜像。

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

[docker-image-rm](/man/docker-image-rm)(1), [docker-rm](/man/docker-rm)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
