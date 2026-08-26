# TAGLINE

停止一个或多个运行中的 Docker 容器（别名）

# TLDR

**停止一个容器**（`docker container stop` 的别名）

```docker stop mycontainer```

**停止多个容器**

```docker stop container1 container2```

**使用自定义超时时间停止**（发出 SIGKILL 前等待的秒数）

```docker stop --timeout 30 mycontainer```

**发送特定的停止信号**

```docker stop --signal SIGINT mycontainer```

# SYNOPSIS

**docker** **stop** [_options_] _container_ [_container_...]

# DESCRIPTION

**docker stop** 是 `docker container stop` 的别名。它通过向一个或多个运行中的容器发送终止信号（默认为 `SIGTERM`，或容器设置的 `STOPSIGNAL` / `--signal`）并等待其优雅关闭来停止容器。如果进程未在超时时间内退出（在 Linux 上默认为 10 秒，除非另行配置），则发送 `SIGKILL`。

完整的选项说明请参考 `docker container stop` 的规范形式文档。

# PARAMETERS

**-t**, **--timeout** _seconds_
> 发送停止信号后、杀死容器前等待的秒数。设为 `-1` 表示无限等待。

**-s**, **--signal** _signal_
> 发送给容器的信号（例如 `SIGTERM`、`SIGINT`）。

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

[docker-container-stop](/man/docker-container-stop)(1), [docker-start](/man/docker-start)(1), [docker-container-start](/man/docker-container-start)(1), [docker-rm](/man/docker-rm)(1), [docker-ps](/man/docker-ps)(1)

# RESOURCES

```[Documentation](https://docs.docker.com/reference/cli/docker/container/stop/)```

<!-- verified: 2026-07-11 -->
