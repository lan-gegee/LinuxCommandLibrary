# TAGLINE

从系统中移除已停止的容器

# TLDR

**删除一个容器**

```docker rm [container]```

**删除多个容器**

```docker rm [container1] [container2]```

**强制删除运行中的容器**

```docker rm -f [container]```

**删除容器及其卷**

```docker rm -v [container]```

**删除所有已停止的容器**

```docker rm $(docker ps -aq)```

# SYNOPSIS

**docker** **rm** [_options_] _container_ [_container..._]

# PARAMETERS

**-f**, **--force**
> 强制删除运行中的容器。

**-l**, **--link**
> 删除指定的链接。

**-v**, **--volumes**
> 删除容器附带的匿名卷。

# DESCRIPTION

**docker rm** 删除一个或多个容器。除非使用 -f，否则容器必须处于停止状态。该命令不会删除镜像；删除镜像请使用 docker rmi。删除容器可以释放磁盘空间，并从 Docker 守护进程清理容器元数据。除非使用 -v 显式删除，命名卷会被保留。

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

[docker-container-rm](/man/docker-container-rm)(1), [docker-rmi](/man/docker-rmi)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
