# TAGLINE

用 Podman 运行多容器应用

# TLDR

**启动服务**

```podman-compose up```

**后台启动**

```podman-compose up -d```

**停止服务**

```podman-compose down```

**查看日志**

```podman-compose logs```

**构建镜像**

```podman-compose build```

**列出容器**

```podman-compose ps```

**在服务中执行命令**

```podman-compose exec [service] [command]```

# SYNOPSIS

**podman-compose** [_options_] _command_ [_args_...]

# SUBCOMMANDS

**up** [_service_...]
> 创建并启动项目的容器、网络和卷。**--build** 强制重新构建，**--force-recreate** 强制重建正在运行的容器。

**down** [**-v**] [**--remove-orphans**]
> 停止并移除容器（可选连同卷 / 孤儿容器一起删除）。

**start** / **stop** / **restart** / **pause** / **unpause** [_service_...]
> 针对已创建服务的生命周期命令。

**build** [_service_...]
> 构建（或重新构建）服务镜像。

**pull** / **push** [_service_...]
> 拉取或推送服务镜像。

**logs** [**-f**] [_service_...]
> 查看 / 跟踪容器日志。

**ps**
> 列出属于该项目的容器。

**exec** [_service_] _command_
> 在运行中的服务内运行命令。

**run** [_service_] _command_
> 以该服务的配置启动一次性容器。

**config**
> 将合并后的 Compose 文件渲染为 YAML 并校验。

**top** / **kill** / **rm** / **port** / **events**
> 对应 **docker compose** 的同名子命令。

# OPTIONS

**-f** _FILE_, **--file** _FILE_
> Compose 文件路径。可重复使用以叠加多个文件。

**-p** _NAME_, **--project-name** _NAME_
> 项目名称（默认：父目录名）。用作容器、网络和卷名称的前缀。

**--profile** _NAME_
> 激活一个 Compose profile。

**--podman-args** _ARGS_
> 向每次 **podman** 调用传递额外参数。

**--podman-run-args** _ARGS_, **--podman-build-args** _ARGS_, **--podman-pull-args** _ARGS_
> 向特定的 Podman 子命令传递额外参数。

**-d**, **--detach**
> 在后台运行（用于 **up**、**run**）。

**--no-cache**
> 禁用构建缓存（用于 **build**）。

**--dry-run**
> 打印将要执行的 Podman 命令而不实际运行。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**podman-compose** 是 **docker compose** 的轻量级 Python 重实现，驱动 **podman** 而非 Docker 守护进程。它读取 **docker-compose.yml** / **compose.yaml** / **podman-compose.yml** 文件（Compose 规范 1.x 和 3.x），并将其转换为一系列 `podman run`、`podman build` 和 `podman network create` 命令，因此可以在无根模式且无守护进程的情况下工作。

现代 Podman（4.0+）还内置了原生 `podman compose`（带空格），它会根据可用情况委派给 **podman-compose** 或 **docker compose** —— 两者最终都调用相同的 Podman API。

# CAVEATS

对 Compose 规范的覆盖良好但并非 100% —— 一些高级特性（例如 `extends`、基于 healthcheck 的 `depends_on.condition`、某些 `deploy.*` 键）表现不同或被静默忽略。Compose 管理的网络使用 podman 的 CNI/Netavark 后端，因此基于 DNS 的服务发现需要 **dnsname** 插件（CNI）或 Aardvark-DNS（Netavark，Podman 4.0 起的默认选择）。

# INSTALL

```dnf: sudo dnf install podman-compose```

```pacman: sudo pacman -S podman-compose```

```apk: sudo apk add podman-compose```

```brew: brew install podman-compose```

```nix: nix profile install nixpkgs#podman-compose```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [docker-compose](/man/docker-compose)(1)
