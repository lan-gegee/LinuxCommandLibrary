# TAGLINE

创建并启动新容器

# TLDR

**运行容器**

```docker container run [image]```

**交互式运行**

```docker container run -it [image] /bin/bash```

**在后台运行**

```docker container run -d [image]```

**带端口映射运行**

```docker container run -p [8080:80] [image]```

**带卷挂载运行**

```docker container run -v [/host/path:/container/path] [image]```

**以指定名称运行**

```docker container run --name [mycontainer] [image]```

**退出后即移除地运行**

```docker container run --rm [image]```

**带环境变量运行**

```docker container run -e [VAR=value] [image]```

# SYNOPSIS

**docker** **container** **run** [_options_] _image_ [_command_] [_args..._]

# PARAMETERS

**-d**, **--detach**
> 在后台运行。

**-i**, **--interactive**
> 保持 STDIN 打开。

**-t**, **--tty**
> 分配伪终端。

**-p**, **--publish** _hostPort:containerPort_
> 发布端口。

**-v**, **--volume** _src:dest_
> 绑定挂载卷。

**-e**, **--env** _var=value_
> 设置环境变量。

**--name** _name_
> 指定容器名称。

**--rm**
> 容器退出时将其移除。

**--network** _network_
> 连接到指定的网络（bridge、host、none 或用户自定义网络）。

**-w**, **--workdir** _dir_
> 容器内的工作目录。

**-u**, **--user** _user_[_:group_]
> 运行时使用的用户名/UID（可选组名/GID）。

**--entrypoint** _cmd_
> 覆盖镜像默认的 **ENTRYPOINT**。

**--restart** _policy_
> 重启策略：**no**、**on-failure**[**:**_N_]、**always** 或 **unless-stopped**。

**--pull** _policy_
> 运行前的拉取策略：**always**、**missing**（默认）或 **never**。

**-m**, **--memory** _bytes_
> 硬内存限制（如 _512m_、_2g_）。

**--cpus** _n_
> 容器可使用的 CPU 数量（如 **1.5**）。

**--hostname** _name_
> 分配给容器内部的主机名。

**--privileged**
> 为容器授予扩展权限。

**--read-only**
> 以只读方式挂载容器的根文件系统。

**--platform** _os/arch_
> 设置镜像的平台（如 **linux/amd64**）。

# DESCRIPTION

**docker container run** 从指定镜像创建并启动一个新容器，把 **docker container create** 和 **docker container start** 的功能合并为一条命令。这是 Docker 中启动容器最常用的方式。

执行时，如果本地没有该镜像，Docker 会先拉取，然后按指定配置创建并启动容器。此命令提供大量配置选项，涵盖网络、存储、资源限制和运行时行为。使用 **--rm** 可确保临时容器被自动清理，而 **-d** 则启用守护模式，适合后台服务。

此命令等价于旧式的 **docker run** 命令。

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

[docker-run](/man/docker-run)(1), [docker-container](/man/docker-container)(1)
