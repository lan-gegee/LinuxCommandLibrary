# TAGLINE

从 STDOUT 和 STDERR 获取容器日志

# TLDR

**显示容器日志**

```docker logs [container]```

**跟踪日志输出**

```docker logs -f [container]```

**显示最后 N 行**

```docker logs --tail [100] [container]```

**显示时间戳**

```docker logs -t [container]```

**显示某个时间之后的日志**

```docker logs --since [2h] [container]```

**显示某个时间之前的日志**

```docker logs --until [1h] [container]```

# SYNOPSIS

**docker** **logs** [_options_] _container_

# PARAMETERS

**-f**, **--follow**
> 跟踪日志输出。

**--tail** _string_
> 从末尾算起的行数（默认 "all"）。

**-t**, **--timestamps**
> 显示时间戳。

**--since** _string_
> 显示指定时间戳或时长之后的日志。

**--until** _string_
> 显示指定时间戳或时长之前的日志。

**--details**
> 显示额外的详细信息。

# DESCRIPTION

**docker logs** 获取容器的日志，显示容器主进程的 STDOUT 和 STDERR 输出。日志由 Docker 的日志驱动程序捕获，可按时间范围或行数进行过滤。是调试容器化应用和监控运行时行为的必备工具。

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

[docker-container-logs](/man/docker-container-logs)(1)
