# TAGLINE

列出本地存储的 Docker 镜像

# TLDR

**列出所有镜像**

```docker images```

**列出镜像及其摘要**

```docker images --digests```

**仅列出镜像 ID**

```docker images -q```

**按软件仓库过滤**

```docker images [repository]```

**显示悬空镜像**

```docker images -f dangling=true```

# SYNOPSIS

**docker** **images** [_options_] [_repository[:tag]_]

# PARAMETERS

**-a**, **--all**
> 显示所有镜像（包括中间层）。

**-q**, **--quiet**
> 仅显示镜像 ID。

**--digests**
> 显示摘要。

**-f**, **--filter** _filter_
> 过滤输出。

**--format** _string_
> 使用自定义模板格式化输出：table、table TEMPLATE、json 或 Go 模板字符串。

**--no-trunc**
> 不截断输出。

# DESCRIPTION

**docker images** 列出存储在本地系统上的镜像，是 docker image ls 的简写形式。显示软件仓库、标签、镜像 ID、创建时间和大小。镜像是创建容器的模板，包含运行应用程序所需的文件系统和配置。

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

[docker-image-ls](/man/docker-image-ls)(1), [docker-rmi](/man/docker-rmi)(1), [docker-pull](/man/docker-pull)(1)
