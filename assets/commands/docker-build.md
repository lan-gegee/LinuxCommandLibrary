# TAGLINE

Docker 镜像构建器

# TLDR

**从 Dockerfile 构建镜像**

```docker build -t [image_name] .```

**使用指定的 Dockerfile 构建**

```docker build -f [Dockerfile.dev] -t [image_name] .```

**带构建参数构建**

```docker build --build-arg [VAR=value] -t [image_name] .```

**不使用缓存构建**

```docker build --no-cache -t [image_name] .```

**为特定平台构建**

```docker build --platform [linux/amd64] -t [image_name] .```

**构建多平台镜像**（buildx）

```docker buildx build --platform [linux/amd64,linux/arm64] -t [image_name] .```

**构建并推送到 registry**

```docker build -t [registry/image:tag] --push .```

# SYNOPSIS

**docker build** [_options_] _path_|_url_

# PARAMETERS

**-t**, **--tag** _name:tag_
> 为镜像命名，可选地打标签。

**-f**, **--file** _path_
> Dockerfile 路径（默认：PATH/Dockerfile）。

**--build-arg** _key=value_
> 构建期变量。

**--no-cache**
> 构建时不使用缓存。

**--pull**
> 始终拉取更新的基础镜像。

**--target** _stage_
> 在多阶段 Dockerfile 中构建指定阶段。

**--platform** _platform_
> 目标平台（linux/amd64、linux/arm64）。

**--progress** _type_
> 进度输出类型：auto、plain、tty。

**--secret** _id=secret_
> 暴露给构建过程的机密。

**--ssh** _socket_
> 要暴露的 SSH agent 套接字。

**-q**, **--quiet**
> 抑制构建输出。

**--push**
> 构建后推送镜像（buildx）。

# DESCRIPTION

**docker build** 基于 Dockerfile 和构建上下文（构建期间可用的文件）创建 Docker 镜像。Dockerfile 中包含逐层组装镜像的指令。

构建上下文会被发送到 Docker 守护进程，由其按顺序处理 Dockerfile 指令。每条指令都会创建一个层；层会被缓存并在未变化时复用，从而加快后续构建。

现代构建使用 **BuildKit**（在近期的 Docker 版本中默认启用），提供更好的性能、更优的缓存，以及 secrets 和 SSH 转发等特性。

# CAVEATS

过大的构建上下文会拖慢构建；请使用 .dockerignore 排除不必要的文件。层缓存依赖于指令顺序；应把经常变化的指令放在最后。多平台构建需要 buildx，可能还需要模拟器或交叉编译环境。

# HISTORY

Docker build 自 **2013 年** Docker 首次发布以来就是核心功能。BuildKit 是具有更好性能和更多特性的新一代构建器，于 **2017 年**推出，并在 Docker **23.0**（2023 年）中成为默认选项。buildx 插件扩展了多平台镜像和高级构建场景的能力。

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

[docker](/man/docker)(1), [docker-run](/man/docker-run)(1), [docker-compose](/man/docker-compose)(1)
