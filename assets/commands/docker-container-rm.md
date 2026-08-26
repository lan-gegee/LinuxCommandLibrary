# TAGLINE

移除一个或多个容器

# TLDR

**移除容器**

```docker container rm [container]```

**移除多个容器**

```docker container rm [container1] [container2]```

**强制移除运行中的容器**

```docker container rm -f [container]```

**移除容器及其卷**

```docker container rm -v [container]```

**移除所有已停止的容器**

```docker container rm $(docker container ls -aq -f status=exited)```

# SYNOPSIS

**docker** **container** **rm** [_options_] _container_ [_container..._]

# PARAMETERS

**-f**, **--force**
> 强制移除运行中的容器（使用 SIGKILL）。

**-v**, **--volumes**
> 移除匿名卷。

**-l**, **--link**
> 移除指定的容器间网络链接，而非容器本身。

# DESCRIPTION

**docker container rm** 从 Docker 主机上移除一个或多个容器，释放容器的读写层和元数据占用的磁盘空间。除非使用 **-f** 标志强制移除运行中的容器，否则必须先停止容器才能移除。

**-v** 选项还会移除与容器关联的匿名卷，适合做彻底清理。命名卷默认会被保留，以防误删数据。

简写形式 **docker rm** 等价于 **docker container rm**。

# CAVEATS

用 **-f** 强制移除运行中的容器会发送 SIGKILL，不给进程清理善后的机会。若要一步清理所有已停止的容器，请使用 **docker container prune**。

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

[docker-rm](/man/docker-rm)(1), [docker-container](/man/docker-container)(1)
