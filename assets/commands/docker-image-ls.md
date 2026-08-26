# TAGLINE

列出系统上的 Docker 镜像

# TLDR

**列出所有镜像**

```docker image ls```

**列出镜像及其摘要**

```docker image ls --digests```

**仅列出镜像 ID**

```docker image ls -q```

**按引用过滤**

```docker image ls [repository]```

**列出悬空镜像**

```docker image ls -f dangling=true```

# SYNOPSIS

**docker** **image** **ls** [_options_] [_repository[:tag]_]

# PARAMETERS

**-a**, **--all**
> 显示所有镜像（包括中间层镜像）。

**-q**, **--quiet**
> 仅显示镜像 ID。

**--digests**
> 显示摘要。

**-f**, **--filter** _filter_
> 根据条件过滤输出。

**--format** _string_
> 使用 Go 模板格式化输出。

**--no-trunc**
> 不截断输出。

**--tree**
> 以树状结构显示多平台镜像（实验性功能；需要 Docker API 1.47+）。

有效的 **--filter** 键：**dangling**=_true_|_false_、**label**=_key_[=_value_]、**before**=_image_、**since**=_image_、**reference**=_pattern_。

# DESCRIPTION

**docker image ls** 列出存储在本地镜像缓存中的 Docker 镜像，显示的信息包括软件仓库名称、标签、镜像 ID、创建时间和虚拟大小。通过该命令可以了解哪些镜像可用于创建容器，以及它们占用了多少磁盘空间。

默认情况下，构建过程中产生的中间层镜像会被隐藏；使用 **-a** 可以显示它们。悬空镜像（dangling images）是被新构建取代后遗留的无标签层，可以通过过滤器 **dangling=true** 找到它们，是使用 **docker image prune** 清理的候选对象。

该命令支持按软件仓库名称、标签模式以及各种镜像属性进行过滤。使用 Go 模板进行输出格式化可以实现自定义显示和脚本集成。

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

[docker-images](/man/docker-images)(1), [docker-image](/man/docker-image)(1)
