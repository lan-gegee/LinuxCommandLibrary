# TAGLINE

移除一个或多个容器

# TLDR

**移除容器**

```podman rm [container]```

**强制移除运行中的容器**

```podman rm -f [container]```

**移除多个容器**

```podman rm [container1] [container2]```

**移除所有容器**

```podman rm -a```

**移除容器及其匿名卷**

```podman rm -v [container]```

**移除匹配过滤器的容器**

```podman rm --filter status=exited```

# SYNOPSIS

**podman rm** [_options_] _container_...

# PARAMETERS

**-a**, **--all**
> 移除所有容器。

**--cidfile** _file_
> 从文件读取容器 ID 并移除该容器。可多次指定。

**--depend**
> 移除选定的容器，并递归移除所有依赖它的容器。

**--filter** _filter_
> 过滤要移除的容器（如 status、label、network、ancestor、name）。

**-f**, **--force**
> 强制移除正在运行和已暂停的容器。

**-i**, **--ignore**
> 当指定的容器不存在于容器存储中时忽略错误。

**-l**, **--latest**
> 使用最后创建的容器，而无需指定名称或 ID。

**-t**, **--time** _seconds_
> 强制停止容器前等待的秒数（需要 --force）。设为 -1 表示无限等待。

**-v**, **--volumes**
> 移除与容器关联的匿名卷。

# DESCRIPTION

**podman rm** 移除一个或多个容器。默认只能移除已停止的容器。使用 --force 可移除运行中的容器。

# EXAMPLES

```bash
# Remove stopped container
podman rm mycontainer

# Force remove running container
podman rm -f webserver

# Remove all containers
podman rm -a

# Remove all containers including running ones
podman rm -af

# Remove with anonymous volumes
podman rm -v database

# Remove containers filtered by status
podman rm --filter status=exited

# Remove latest container
podman rm -l
```

# CAVEATS

没有 --force 无法移除运行中的容器。未指定 -v 时不会移除匿名卷。此命令从不移除命名卷。

# HISTORY

podman rm 是 **Podman** 的一部分，Podman 是 **Red Hat** 开发的无守护进程容器引擎，提供与 Docker 兼容的容器管理。

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

[podman](/man/podman)(1), [podman-rmi](/man/podman-rmi)(1), [podman-ps](/man/podman-ps)(1), [docker-rm](/man/docker-rm)(1)
