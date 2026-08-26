# TAGLINE

获取容器镜像的配置

# TLDR

**获取镜像配置**

```crane config [image]```

**以 JSON 形式获取配置**

```crane config [image] | jq .```

# SYNOPSIS

**crane** **config** [_options_] _image_

# PARAMETERS

_image_
> 容器镜像引用（例如 `ubuntu:latest`、`ghcr.io/org/image:tag`）。

**--platform** _os/arch_
> 为多架构镜像指定平台（例如 `linux/amd64`）。

# DESCRIPTION

**crane config** 获取容器镜像的配置 blob。其中包括环境变量、入口点（entrypoint）、命令、工作目录、标签、暴露端口以及 OCI 镜像规范中定义的其他镜像元数据。

输出为 JSON 格式，便于通过管道传给 **jq** 提取字段。

# CAVEATS

需要能够访问容器镜像仓库的网络。私有镜像仓库需要先通过 `crane auth login` 进行身份验证。多架构镜像默认返回主机平台对应的配置，除非指定了 `--platform`。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-manifest](/man/crane-manifest)(1)
