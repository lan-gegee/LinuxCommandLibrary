# TAGLINE

列出系统上的容器

# TLDR

**列出运行中的容器**

```docker container ls```

**列出所有容器**

```docker container ls -a```

**以指定格式列出**

```docker container ls --format "{{.Names}}: {{.Status}}"```

**按状态过滤**

```docker container ls -f status=[running|exited|paused]```

**只显示 ID**

```docker container ls -q```

**按名称过滤**

```docker container ls -f name=[container_name]```

**显示最近创建的容器**

```docker container ls --latest```

# SYNOPSIS

**docker** **container** **ls** [_options_]

# PARAMETERS

**-a**, **--all**
> 显示所有容器（默认只显示运行中的）。

**-q**, **--quiet**
> 只显示容器 ID。

**-f**, **--filter** _filter_
> 按条件过滤输出（如 status、name、label、ancestor、network、exited）。

**--format** _string_
> 使用 Go 模板格式化输出。

**-n**, **--last** _n_
> 显示最后创建的 n 个容器（包含所有状态）。

**-l**, **--latest**
> 显示最近创建的容器（包含所有状态）。

**-s**, **--size**
> 显示文件总大小。

**--no-trunc**
> 不截断输出。

# DESCRIPTION

**docker container ls** 列出 Docker 主机上的容器，提供容器 ID、镜像、命令、创建时间、状态、端口和名称等信息。默认只显示运行中的容器，但加上 **-a** 标志可以查看所有状态的容器。

此命令等价于旧式的 **docker ps** 命令，是查看容器清单的主要接口。其过滤和格式化选项使其非常适合脚本和自动化工作流。

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

[docker-ps](/man/docker-ps)(1), [docker-container](/man/docker-container)(1), [docker-container-run](/man/docker-container-run)(1), [docker-container-rm](/man/docker-container-rm)(1)
