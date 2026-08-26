# TAGLINE

从 tar 归档加载镜像

# TLDR

**从 tar 归档加载镜像**

```docker image load -i [image.tar]```

**从 stdin 加载镜像**

```cat [image.tar] | docker image load```

**以安静模式加载镜像**

```docker image load -q -i [image.tar]```

**只加载特定平台变体**

```docker image load --platform [linux/amd64] -i [image.tar]```

# SYNOPSIS

**docker** **image** **load** [_options_]

# PARAMETERS

**-i**, **--input** _file_
> 从 tar 归档文件读取而不是 STDIN。

**-q**, **--quiet**
> 抑制加载过程的输出。

**--platform** _value_
> 只加载指定的平台变体，格式为 "os[/arch[/variant]]"（如 linux/amd64）。可多次指定。

# DESCRIPTION

**docker image load** 从由 **docker image save** 创建的 tar 归档（即使经过 gzip、bzip2、xz 或 zstd 压缩）中加载 Docker 镜像，将镜像层和元数据恢复到本地 Docker 守护进程。

tar 归档包含完整重建镜像所需的全部镜像层、配置和 manifest 数据。加载镜像时会原样保留其保存时的仓库标签和摘要。这使 **docker image load** 非常适合物理隔离（air-gapped）环境、备份/恢复工作流，以及通过物理介质或安全文件传输分发镜像的场景。

该命令可以从 **-i** 指定的文件或 stdin 读取输入，便于灵活地与压缩工具和网络传输集成。

# CAVEATS

tar 归档必须由 **docker image save** 或兼容工具创建。加载镜像不会从 registry 拉取缺失的层。镜像只会加载到本地 Docker 守护进程中。

# HISTORY

**docker image load** 是 **docker load** 命令的现代语法，作为 Docker CLI 重构的一部分引入，目的是将命令按管理类别分组。

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

[docker-load](/man/docker-load)(1), [docker-image-save](/man/docker-image-save)(1), [docker-image](/man/docker-image)(1), [docker](/man/docker)(1)
