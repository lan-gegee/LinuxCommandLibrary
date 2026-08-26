# TAGLINE

基于镜像创建并启动容器

# TLDR

**交互式运行一个容器**

```docker run -it [image] [bash]```

**在后台运行容器**

```docker run -d [image]```

**运行时映射端口**

```docker run -p [8080:80] [image]```

**运行时挂载卷**

```docker run -v [/host/path:/container/path] [image]```

**运行时设置环境变量**

```docker run -e [VAR=value] [image]```

**退出时自动删除容器**

```docker run --rm [image]```

**使用自定义名称运行**

```docker run --name [container_name] [image]```

**运行时限制内存**

```docker run -m [512m] [image]```

# SYNOPSIS

**docker run** [_options_] _image_ [_command_] [_args_]

# PARAMETERS

**-d**, **--detach**
> 在后台运行容器。

**-it**
> 交互模式并分配伪终端。

**-p**, **--publish** _host:container_
> 将容器端口发布到主机。

**-v**, **--volume** _host:container_
> 绑定挂载一个卷。

**-e**, **--env** _VAR=value_
> 设置环境变量。

**--name** _name_
> 指定容器名称。

**--rm**
> 容器退出时将其删除。

**-m**, **--memory** _limit_
> 内存限制（例如 512m、1g）。

**--cpus** _n_
> CPU 数量。

**--network** _network_
> 连接到指定网络。

**--restart** _policy_
> 重启策略：no、always、unless-stopped、on-failure。

**-w**, **--workdir** _dir_
> 容器内的工作目录。

**-u**, **--user** _user_
> 用户名或 UID。

**--entrypoint** _cmd_
> 覆盖默认的入口点。

# DESCRIPTION

**docker run** 基于镜像创建并启动一个新容器。它将 **docker create** 和 **docker start** 合并为一条命令，是启动容器的主要方式。

如果本地不存在该镜像，命令会先拉取镜像，然后基于它创建容器并开始执行。各种选项用于控制资源分配、网络、存储和运行时行为。

容器之间相互隔离，但可以通过端口映射、卷挂载和网络配置连接主机资源。**-it** 选项提供交互式终端访问，便于调试和探索。

# CAVEATS

容器默认以 root 身份运行；需要非 root 执行时使用 **-u**。低于 1024 的端口在主机上需要 root 权限。使用相对路径的卷会被创建为 Docker 卷，而不是绑定挂载。如果不使用卷，容器文件系统的更改会丢失。

# HISTORY

docker run 自 **2013 年 Solomon Hykes** 和 dotCloud（即后来的 Docker, Inc.）首次发布 Docker 以来就是其核心命令。该命令的设计借鉴了 Unix 哲学和 LXC 容器理念。其选项已大幅扩展，以支持企业级功能、编排和安全需求。

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

[docker](/man/docker)(1), [docker-build](/man/docker-build)(1), [docker-ps](/man/docker-ps)(1), [docker-exec](/man/docker-exec)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
