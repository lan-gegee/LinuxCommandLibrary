# TAGLINE

查看 Compose 服务的日志

# TLDR

**查看所有服务**的日志

```docker compose logs```

**跟踪日志输出**

```docker compose logs -f```

**查看指定服务**的日志

```docker compose logs [service_name]```

**显示时间戳**

```docker compose logs -t```

**限制输出行数**

```docker compose logs --tail [100]```

**从指定时间起显示**

```docker compose logs --since [1h]```

# SYNOPSIS

**docker** **compose** **logs** [_options_] [_service..._]

# PARAMETERS

**-f**, **--follow**
> 跟踪日志输出。

**-t**, **--timestamps**
> 显示时间戳。

**--tail** _n_
> 从末尾算起的行数。

**--since** _time_
> 显示自某时间戳或相对时间之后的日志。

**--until** _time_
> 显示在某时间戳或相对时间之前的日志。

**--no-color**
> 输出单色内容。

# DESCRIPTION

**docker compose logs** 显示 Compose 文件中定义的服务的日志输出。它会汇总每个服务的所有容器的日志。

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

[docker-compose](/man/docker-compose)(1), [docker-logs](/man/docker-logs)(1)

# RESOURCES

```[Source code](https://github.com/docker/compose)```

```[Documentation](https://docs.docker.com/reference/cli/docker/compose/)```

<!-- verified: 2026-07-11 -->
