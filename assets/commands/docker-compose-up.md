# TAGLINE

启动 Compose 服务

# TLDR

**启动服务**

```docker compose up```

**以后台模式启动**

```docker compose up -d```

**启动前先构建镜像**

```docker compose up --build```

**启动指定服务**

```docker compose up [service1] [service2]```

**强制重建容器**

```docker compose up --force-recreate```

**扩缩某个服务**

```docker compose up --scale [service]=[3]```

**移除孤儿容器**

```docker compose up --remove-orphans```

# SYNOPSIS

**docker** **compose** **up** [_options_] [_service..._]

# PARAMETERS

**-d**, **--detach**
> 在后台运行容器并打印容器名。

**--build**
> 在启动容器之前构建镜像。

**--no-build**
> 即使镜像缺失也不构建。

**--pull** _policy_
> 运行前拉取镜像：_always_、_missing_（默认）或 _never_。

**--force-recreate**
> 即使配置和镜像未变化也重建容器。

**--no-recreate**
> 不重建已存在的容器。

**--always-recreate-deps**
> 重建依赖的容器。与 **--no-recreate** 不兼容。

**-V**, **--renew-anon-volumes**
> 重新创建匿名卷，而不是从之前的容器中取回数据。

**--no-deps**
> 不启动关联（依赖）的服务。

**--scale** _service=num_
> 将指定服务扩展为 _num_ 个实例（覆盖 deploy.replicas）。

**--remove-orphans**
> 移除未在 Compose 文件中定义的服务的容器。

**--wait**
> 等待服务进入 _running_ 或 _healthy_ 状态。隐含 **--detach**。

**--wait-timeout** _seconds_
> 使用 **--wait** 时等待服务的最长时间。

**--abort-on-container-exit**
> 任一容器停止时停止所有容器。与 **-d** 不兼容。

**--abort-on-container-failure**
> 任一容器以非零状态退出时停止所有容器。

**--attach** _service_
> 将日志输出限制到指定的服务。

**--no-attach** _service_
> 不附着（流式输出日志）到指定的服务。

**-t**, **--timeout** _seconds_
> 停止所附着的容器时的关闭超时时间（秒）。

**--timestamps**
> 在容器日志中显示时间戳。

**--quiet-pull**
> 拉取镜像时不打印进度信息。

**--no-start**
> 创建服务后不启动它们。

# DESCRIPTION

**docker compose up** 为 _compose.yaml_ / _docker-compose.yml_ 中定义的服务构建、（重新）创建、启动并附着到容器。它还会创建文件中声明的网络和卷。

不带 **-d** 运行时，它会流式输出所有附着容器的聚合日志，并在按下 Ctrl+C 时停止这些容器。使用 **--wait** 或 **-d** 时，命令会在服务就绪后立即返回（配合 **--wait** 则是健康检查通过）。

# CAVEATS

如果 Compose 文件有变化，容器会被重建，除非设置了 **--no-recreate**。将 **--force-recreate** 与 **-V** 一起使用会丢弃被重建服务的匿名卷中的全部现有数据。

# INSTALL

```apt: sudo apt install docker-compose```

```dnf: sudo dnf install docker-compose```

```pacman: sudo pacman -S docker-compose```

```apk: sudo apk add docker-cli-compose```

```zypper: sudo zypper install docker-compose```

```brew: brew install docker-compose```

```nix: nix profile install nixpkgs#docker-compose```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-compose](/man/docker-compose)(1), [docker-compose-down](/man/docker-compose-down)(1)
