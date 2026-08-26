# TAGLINE

显示容器的资源使用统计

# TLDR

**实时查看资源使用情况**

```docker container stats```

**查看指定容器的统计信息**

```docker container stats [container1] [container2]```

**显示一次性快照**

```docker container stats --no-stream```

**自定义格式**

```docker container stats --format "{{.Name}}: {{.CPUPerc}}"```

# SYNOPSIS

**docker** **container** **stats** [_options_] [_container..._]

# PARAMETERS

**--no-stream**
> 禁用流式输出，只显示一次快照。

**-a**, **--all**
> 显示所有容器（默认只显示运行中的）。

**--format** _string_
> 使用 Go 模板格式化输出。占位符：**.Container**、**.Name**、**.ID**、**.CPUPerc**、**.MemUsage**、**.MemPerc**、**.NetIO**、**.BlockIO**、**.PIDs**。

**--no-trunc**
> 不截断输出（显示完整容器 ID）。

# DESCRIPTION

**docker container stats** 以实时流的形式显示容器的资源使用统计，让你实时了解运行中容器的 CPU 占用率、内存使用量与上限、网络 I/O 和块设备 I/O。

默认情况下，界面会持续更新所有运行中容器的当前指标。**--no-stream** 选项改为提供单次快照而非持续刷新，适合脚本和自动化场景。

# CAVEATS

在 Linux 上，内存使用量默认包含缓存。网络 I/O 显示的是自容器启动以来的累计值，而不是每秒速率。在某些平台上，使用 **host** 网络模式的容器无法获取统计数据。

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

[docker-stats](/man/docker-stats)(1), [docker-container-top](/man/docker-container-top)(1)
