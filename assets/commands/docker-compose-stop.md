# TAGLINE

停止 Compose 服务而不移除容器

# TLDR

**停止**所有运行中的服务

```docker compose stop```

停止**指定的**服务

```docker compose stop [service1] [service2]```

以自定义**超时时间**（秒）停止

```docker compose stop -t [30]```

使用指定的 **compose 文件**

```docker compose -f [path/to/compose.yaml] stop```

# SYNOPSIS

**docker** **compose** **stop** [_options_] [_SERVICE_...]

# PARAMETERS

**-t**, **--timeout** _seconds_
> 强制终止容器前等待的关闭超时时间（秒）

# DESCRIPTION

**docker compose stop** 停止 Compose 项目中定义的一个或多个服务的运行容器，但**不移除**它们。已停止的容器会保留其配置和卷，之后可用 **docker compose start** 再次启动。

与 **docker compose down** 不同，此命令不会移除容器、网络或卷。当你想临时停止并保留快速恢复同一批容器的能力时，它很有用。

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

[docker-compose](/man/docker-compose)(1), [docker-compose-up](/man/docker-compose-up)(1), [docker-compose-down](/man/docker-compose-down)(1)

# RESOURCES

```[Documentation](https://docs.docker.com/reference/cli/docker/compose/stop/)```

```[Homepage](https://docs.docker.com/compose/)```

<!-- verified: 2026-07-14 -->
