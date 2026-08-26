# TAGLINE

停止并移除 Compose 资源

# TLDR

**停止并移除容器**

```docker compose down```

**同时移除卷**

```docker compose down -v```

**同时移除镜像**

```docker compose down --rmi all```

**移除孤儿容器**

```docker compose down --remove-orphans```

**设置关闭超时时间**

```docker compose down -t [30]```

# SYNOPSIS

**docker** **compose** **down** [_options_]

# PARAMETERS

**-v**, **--volumes**
> 移除命名卷和匿名卷。

**--rmi** _type_
> 移除镜像：all 或 local。

**--remove-orphans**
> 移除未在 Compose 文件中定义的容器。

**-t**, **--timeout** _seconds_
> 关闭超时时间（默认 10）。

# DESCRIPTION

**docker compose down** 停止并移除由 **docker compose up** 创建的容器和网络。

默认只移除容器和网络。除非指定了 **-v** 或 **--rmi**，否则卷和镜像会被保留。定义为 **external** 的网络和卷永远不会被移除。

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

[docker-compose](/man/docker-compose)(1), [docker-compose-up](/man/docker-compose-up)(1)
