# TAGLINE

从镜像创建并启动容器

# TLDR

**运行容器**

```podman run [image]```

**交互式运行**

```podman run -it [image] [/bin/bash]```

**后台运行**

```podman run -d [image]```

**带端口映射运行**

```podman run -p [8080:80] [image]```

**带卷挂载运行**

```podman run -v [/host/path:/container/path] [image]```

**指定名称运行**

```podman run --name [mycontainer] [image]```

**带环境变量运行**

```podman run -e [VAR=value] [image]```

**运行并在退出后自动移除**

```podman run --rm -it [image] [command]```

**使用自定义网络运行**

```podman run --network [network_name] [image]```

# SYNOPSIS

**podman run** [_options_] _image_ [_command_]

# PARAMETERS

_IMAGE_
> 容器镜像。

**-it**
> 交互式终端。

**-d**, **--detach**
> 在后台运行。

**-p**, **--publish** _PORT_
> 端口映射。

**-v**, **--volume** _MOUNT_
> 卷挂载。

**--name** _NAME_
> 容器名称。

**-e**, **--env** _VAR_
> 环境变量。

**--rm**
> 退出后移除容器。

**--network** _MODE_
> 设置网络模式（bridge、host、none 或自定义网络名称）。

**--restart** _POLICY_
> 重启策略（no、on-failure[:max]、always、unless-stopped）。

**-w**, **--workdir** _DIR_
> 容器内的工作目录。

**--user** _USER_
> 以指定用户身份运行（名称或 UID[:GID]）。

**--cap-add** _CAP_
> 添加 Linux 能力。

**--cap-drop** _CAP_
> 移除 Linux 能力。

**--entrypoint** _CMD_
> 覆盖镜像的入口点。

**--label** _KEY=VALUE_
> 在容器上设置元数据标签。

# DESCRIPTION

**podman run** 从指定镜像创建并启动新容器。它是启动容器的主要命令，支持交互式会话（**-it**）、后台执行（**-d**）、端口映射（**-p**）、卷挂载（**-v**）和环境变量（**-e**）。

**--rm** 标志在容器退出时自动将其移除。**--name** 选项为容器指定一个人类可读的名称。默认情况下，Podman 以无根模式运行容器且不需要守护进程，使其可以直接替代 docker run。

# CAVEATS

默认以无根模式运行且无需守护进程。大多数 Docker CLI 标志都兼容。某些功能（例如特定网络模式）在无根模式下可能表现不同。

# HISTORY

**podman run** 作为 Red Hat Podman 项目的一部分推出，提供无守护进程且与 Docker 兼容的容器运行时。

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

[podman](/man/podman)(1), [podman-exec](/man/podman-exec)(1), [docker-run](/man/docker-run)(1)
