# TAGLINE

查看容器的日志

# TLDR

**查看容器日志**

```docker container logs [container]```

**跟踪日志输出**

```docker container logs -f [container]```

**显示时间戳**

```docker container logs -t [container]```

**显示最后 n 行**

```docker container logs --tail [100] [container]```

**显示自某个相对时间或时间戳以来的日志**

```docker container logs --since [1h30m] [container]```

**显示指定时间之前的日志**

```docker container logs --until [2024-01-01T00:00:00Z] [container]```

**显示日志驱动提供的额外属性**

```docker container logs --details [container]```

# SYNOPSIS

**docker** **container** **logs** [_options_] _container_

# PARAMETERS

**--details**
> 显示创建容器时提供给 `--log-opt` 的额外属性。

**-f**, **--follow**
> 跟踪日志输出。

**-n**, **--tail** _n_
> 从日志末尾开始显示的行数。默认为 `all`。

**--since** _time_
> 显示自某时间戳（如 `2024-01-01T00:00:00Z`）或相对时间（如 `42m`、`1h30m`）之后的日志。

**-t**, **--timestamps**
> 显示 RFC3339Nano 时间戳。

**--until** _time_
> 显示在某时间戳或相对时间之前的日志。

# DESCRIPTION

**docker container logs** 获取容器主进程的日志，同时显示标准输出和标准错误流。此命令是调试和监控容器化应用的关键工具，既可以查看历史日志，也可以实时跟踪输出。

日志从容器配置的日志驱动中收集，默认会捕获容器 PID 1 进程的 stdout 和 stderr。基于时间的过滤和 tail 选项让处理大量日志更加高效。`--since` 和 `--until` 选项接受 Unix 时间戳、RFC 3339 日期/时间字符串，或相对于客户端机器时间的 Go duration 字符串。

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

[docker-logs](/man/docker-logs)(1), [docker-container](/man/docker-container)(1)
