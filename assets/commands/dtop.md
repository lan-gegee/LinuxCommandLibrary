# TAGLINE

用于 Docker 容器监控的终端仪表盘

# TLDR

**启动** Docker 监控仪表盘

```dtop```

**只监控**指定的容器

```dtop [container1] [container2]```

**每 5 秒刷新一次**

```dtop --refresh 5```

**显示**所有容器，包括已停止的

```dtop --all```

# SYNOPSIS

**dtop** [_options_] [_containers_]

# PARAMETERS

**-r, --refresh** _SECONDS_
> 刷新间隔，单位为秒（默认：2）

**-a, --all**
> 显示所有容器，包括已停止的

**--no-trunc**
> 不截断容器名称

**--cpu-only**
> 只显示 CPU 指标

**--memory-only**
> 只显示内存指标

**--network-only**
> 只显示网络指标

**-c, --config** _FILE_
> 配置文件路径

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**dtop** 是一个基于终端的仪表盘，用于实时监控 Docker 容器。它提供了一个专为 Docker 设计的 top/htop 风格界面，显示 CPU 使用率、内存消耗、网络 I/O 和容器状态。

该工具以可排序的表格形式展示容器指标，并用颜色标识健康状态。它会自动刷新以显示当前统计信息，还支持过滤，以便聚焦于特定容器或资源类型。

# KEYBINDINGS

**↑/↓**
> 在容器之间导航

**s**
> 更改排序列

**q**
> 退出

**p**
> 暂停/恢复选定的容器

**r**
> 重启选定的容器

**k**
> 终止选定的容器

**l**
> 显示容器日志

**/ 或 f**
> 过滤/搜索容器

# CAVEATS

需要 Docker 守护进程访问权限和相应的权限。容器统计信息受 Docker API 能力的限制。大量容器可能影响性能。网络统计信息可能因 Docker 驱动而异。

# HISTORY

**dtop** 的创建目的是提供类似 top/htop 对系统进程那样的 Docker 专属监控。它填补了 Docker 内置 stats 命令与更复杂监控方案之间的空白。

# INSTALL

```apt: sudo apt install diod```

```brew: brew install dtop```

```nix: nix profile install nixpkgs#diod```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [docker-stats](/man/docker-stats)(1), [ctop](/man/ctop)(1), [lazydocker](/man/lazydocker)(1)
