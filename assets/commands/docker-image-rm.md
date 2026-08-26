# TAGLINE

删除一个或多个镜像

# TLDR

**删除一个镜像**

```docker image rm [image]```

**删除多个镜像**

```docker image rm [image1] [image2]```

**强制删除**

```docker image rm -f [image]```

**按镜像 ID 删除**

```docker image rm [image_id]```

# SYNOPSIS

**docker** **image** **rm** [_options_] _image_ [_image..._]

# PARAMETERS

**-f**, **--force**
> 强制删除。

**--no-prune**
> 不删除无标签的父镜像。

# DESCRIPTION

**docker image rm** 从本地 Docker 镜像缓存中删除一个或多个镜像，释放其各层占用的磁盘空间。镜像可以通过 repository:tag 或其唯一的镜像 ID 来指定。

如果有任何容器（无论运行中还是已停止）依赖于某个镜像，则该镜像无法被删除，除非使用 **-f** 强制选项。强制删除容器依赖的镜像可能导致这些容器在重启时出问题，因为它们将无法访问自己的镜像层。

删除镜像时，Docker 还会删除不再被其他镜像引用的无标签父镜像，除非指定 **--no-prune**。这种自动清理有助于保持镜像缓存精简。

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

[docker-rmi](/man/docker-rmi)(1), [docker-image-ls](/man/docker-image-ls)(1)
