# TAGLINE

无需 Docker 即可与容器镜像仓库交互

# TLDR

**拉取镜像**

```crane pull [registry/image:tag] [output.tar]```

**推送镜像**

```crane push [image.tar] [registry/image:tag]```

**在镜像仓库之间复制镜像**

```crane copy [src/image:tag] [dst/image:tag]```

**列出镜像的标签**

```crane ls [registry/image]```

**获取镜像摘要**

```crane digest [registry/image:tag]```

**获取镜像清单**

```crane manifest [registry/image:tag]```

**获取镜像配置**

```crane config [registry/image:tag]```

**向镜像仓库进行身份验证**

```crane auth login [registry] -u [user] -p [password]```

# SYNOPSIS

**crane** _command_ [_options_] [_arguments_]

# DESCRIPTION

**crane** 是一个用于与容器镜像仓库交互的工具。它可以在不依赖 Docker 等容器运行时的情况下拉取、推送、复制和检查容器镜像。属于 go-containerregistry 项目。

# COMMANDS

**pull**
> 将镜像下载为 tar 包

**push**
> 将 tar 包上传为镜像

**copy**
> 在镜像仓库之间复制镜像

**ls**
> 列出仓库的标签

**digest**
> 获取镜像摘要

**manifest**
> 获取镜像清单

**config**
> 获取镜像配置

**catalog**
> 列出镜像仓库中的仓库

**auth**
> 管理镜像仓库身份验证

**append**
> 向镜像追加层

**flatten**
> 压平镜像的层

**mutate**
> 修改镜像元数据

**validate**
> 校验镜像

**export**
> 从镜像导出文件系统

# PARAMETERS

**--platform** _os/arch_
> 目标平台（例如 linux/amd64）

**--insecure**
> 允许不安全的镜像仓库连接

**-v**, **--verbose**
> 详细输出

# CONFIGURATION

**~/.docker/config.json**
> 存储镜像仓库凭据的 Docker 配置文件，crane 用它进行身份验证。

# ENVIRONMENT

**DOCKER_CONFIG**
> 用于凭据的 Docker 配置路径

# CAVEATS

不需要 Docker 守护进程。直接使用 OCI 镜像仓库 API。默认从 Docker 配置读取凭据。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [skopeo](/man/skopeo)(1), [cosign](/man/cosign)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md)```

<!-- verified: 2026-06-26 -->
