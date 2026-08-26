# TAGLINE

停止一个或多个运行中的 Docker 容器

# TLDR

**优雅地停止容器**（先发 SIGTERM，超时后再发 SIGKILL）

```docker container stop mycontainer```

**停止多个容器**

```docker container stop container1 container2```

**使用自定义超时停止**（发出 SIGKILL 前等待的秒数）

```docker container stop --timeout 30 mycontainer```

**发送指定的停止信号**

```docker container stop --signal SIGINT mycontainer```

# SYNOPSIS

**docker** **container** **stop** [_options_] _container_ [_container_...]

# DESCRIPTION

**docker container stop** 停止一个或多个运行中的容器。它会向容器内的主进程发送 `SIGTERM`（或由 `--signal` 指定的信号，或容器的 `STOPSIGNAL`）。如果进程未在超时时间内退出（Linux 默认 10 秒、Windows 默认 30 秒，除非在创建/运行时通过 `--stop-timeout` 配置），则会发送 `SIGKILL`。

这是干净利落停止容器的首选方式。别名 `docker stop` 与之等价。

# PARAMETERS

**-t**, **--timeout** _seconds_
> 发送停止信号后等待容器停止的秒数，超时则以 `SIGKILL` 强制终止。设为 `-1` 表示无限等待。默认：守护进程默认值（Linux 为 10 秒，Windows 为 30 秒）或容器配置的停止超时。

**-s**, **--signal** _signal_
> 发送给容器的信号（如 `SIGTERM`、`SIGINT`、`SIGKILL` 或数字）。默认为容器配置的停止信号或 `SIGTERM`。

# CAVEATS

如果主进程忽略 SIGTERM，容器可能直到超时触发 SIGKILL 才会停止。已停止的容器仍保留在磁盘上，可以用 `docker start` / `docker container start` 重新启动，或用 `docker rm` 移除。

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

[docker-stop](/man/docker-stop)(1), [docker-start](/man/docker-start)(1), [docker-container-start](/man/docker-container-start)(1), [docker-rm](/man/docker-rm)(1), [docker-ps](/man/docker-ps)(1)

# RESOURCES

```[Documentation](https://docs.docker.com/reference/cli/docker/container/stop/)```

<!-- verified: 2026-07-11 -->
