# TAGLINE

从 tar 归档加载 Docker 镜像

# TLDR

**从 tar 文件加载镜像**

```docker load -i [image.tar]```

**从标准输入加载**

```cat [image.tar] | docker load```

**加载 gzip 压缩的归档**

```docker load -i [image.tar.gz]```

**静默模式加载**

```docker load -q -i [image.tar]```

**通过 curl 从远程 URL 加载**

```curl -sSL [https://example.com/image.tar.gz] | docker load```

# SYNOPSIS

**docker** **load** [_options_]

# PARAMETERS

**-i**, **--input** _file_
> 从 tar 归档文件读取而不是 STDIN。tar 包可以用 gzip、bzip2 或 xz 压缩。

**-q**, **--quiet**
> 抑制加载输出和进度条。

**--platform** _string_
> 从多平台归档中仅加载指定平台的镜像（例如 linux/amd64）。

# DESCRIPTION

**docker load** 从 tar 归档或标准输入加载镜像，可恢复由 **docker save** 保存的镜像及其标签。该命令是 docker save 的对应操作，可在不使用镜像仓库的情况下在系统之间传输镜像。适用于隔离网络环境或离线分发。

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

[docker-image-load](/man/docker-image-load)(1), [docker-save](/man/docker-save)(1), [docker-images](/man/docker-images)(1), [docker-pull](/man/docker-pull)(1), [docker](/man/docker)(1)
