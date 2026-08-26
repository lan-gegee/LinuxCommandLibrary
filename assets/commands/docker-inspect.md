# TAGLINE

返回 Docker 对象的底层信息

# TLDR

**查看一个容器**

```docker inspect [container]```

**查看一个镜像**

```docker inspect [image]```

**获取特定字段**

```docker inspect -f '{{.State.Status}}' [container]```

**获取 IP 地址**

```docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' [container]```

**以 JSON 输出**

```docker inspect --format '{{json .Config}}' [container]```

# SYNOPSIS

**docker** **inspect** [_options_] _name|id_ [_name|id..._]

# PARAMETERS

**-f**, **--format** _string_
> 使用 Go 模板格式化输出。

**-s**, **--size**
> 显示文件总大小（仅限容器）。

**--type** _string_
> 返回指定类型（container 或 image）的 JSON。

# DESCRIPTION

**docker inspect** 返回 Docker 对象的底层信息，包括容器、镜像、卷和网络。输出默认为 JSON，是一个结果对象数组，每个参数对应一个对象。

**--format** 选项接受一个 Go 模板来提取特定字段，在 shell 脚本中可用于捕获 IP 地址、挂载点或退出码等值。**{{json .Field}}** 模板会输出子对象的原始 JSON。当镜像和容器同名时，需要用 **--type** 选项进行区分。

# CAVEATS

当多个对象共享同一名称时，必须使用 **--type** 进行区分。对容器使用 **--size** 会添加 **SizeRw** 和 **SizeRootFs** 字段，但在大型文件系统上开销较大。容器、镜像、网络和卷的输出结构各不相同，因此格式模板不能在不同对象类型之间通用。

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

[docker](/man/docker)(1), [docker-ps](/man/docker-ps)(1), [docker-images](/man/docker-images)(1)
