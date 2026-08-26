# TAGLINE

移除一个或多个容器

# TLDR

**移除容器**

```docker container remove [container]```

# SYNOPSIS

**docker** **container** **remove** [_options_] _container_

# DESCRIPTION

**docker container remove** 是 **docker container rm** 的别名，从 Docker 主机上移除一个或多个容器。除非使用强制选项，否则容器必须先停止才能移除。此命令会清理容器的文件系统层和元数据，但不会影响底层镜像。

移除容器对保持系统整洁和释放磁盘空间非常重要，因为已停止的容器在被显式删除之前会持续占用存储空间。

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

[docker-container-rm](/man/docker-container-rm)(1), [docker-rm](/man/docker-rm)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
