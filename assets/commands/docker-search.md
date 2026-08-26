# TAGLINE

在 Docker Hub 中搜索容器镜像

# TLDR

**搜索 Docker Hub**

```docker search [term]```

**限制搜索结果数量**

```docker search --limit [25] [term]```

**过滤官方镜像**

```docker search -f is-official=true [term]```

**过滤自动构建镜像**

```docker search -f is-automated=true [term]```

**按星标数过滤**

```docker search -f stars=[100] [term]```

# SYNOPSIS

**docker** **search** [_options_] _term_

# PARAMETERS

**-f**, **--filter** _filter_
> 根据条件过滤输出。

**--format** _string_
> 使用 Go 模板格式化输出。

**--limit** _int_
> 结果数量上限（默认 25）。

**--no-trunc**
> 不截断输出。

# DESCRIPTION

**docker search** 在 Docker Hub 中搜索镜像，返回镜像名称、描述、星标数以及官方/自动构建状态。该命令查询公共的 Docker Hub 镜像仓库，帮助发现可用镜像。结果可按官方状态、自动化程度或热门程度进行过滤，以便找到可信的镜像。

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

[docker-pull](/man/docker-pull)(1), [docker-images](/man/docker-images)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
