# TAGLINE

实时显示容器的资源使用统计

# TLDR

**显示所有容器的实时统计**

```docker stats```

**显示指定容器的统计**

```docker stats [container1] [container2]```

**显示一次性快照**

```docker stats --no-stream```

**自定义输出格式**

```docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"```

**包括已停止的容器**

```docker stats -a```

# SYNOPSIS

**docker** **stats** [_options_] [_container..._]

# PARAMETERS

**-a**, **--all**
> 显示所有容器（默认只显示运行中的）。

**--no-stream**
> 禁用流式输出，只显示单次快照。

**--no-trunc**
> 不截断输出。

**--format** _string_
> 使用 Go 模板格式化输出。

# DESCRIPTION

**docker stats** 实时显示容器资源使用统计流，包括 CPU 占用率、内存使用量/上限、网络 I/O 和块设备 I/O。

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

[docker-container-stats](/man/docker-container-stats)(1), [docker-top](/man/docker-top)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
