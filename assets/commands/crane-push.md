# TAGLINE

将 tar 包上传为容器镜像

# TLDR

**推送 tar 包**为镜像

```crane push [image.tar] [registry/repo:tag]```

**推送**并写出结果镜像的摘要

```crane push [image.tar] [registry/repo:tag] --image-refs [refs.txt]```

**以特定的平台索引推送**

```crane push [image.tar] [registry/repo:tag] --index```

# SYNOPSIS

**crane** **push** [_options_] _tarball_ _image_

# PARAMETERS

**--image-refs** _file_
> 用于写出完整镜像引用（含摘要，按标签）的文件路径。

**--index**
> 将一组镜像作为单个索引（manifest list）推送。

**--platform** _os/arch_
> 推送多平台 tar 包时指定平台。

# DESCRIPTION

**crane push** 将 tar 包作为容器镜像上传到镜像仓库。tar 包应为 OCI 或 Docker 镜像格式（即 **crane pull**、**docker save** 或 **crane export** 生成的格式）。

该命令从 tar 包中读取镜像层并推送到目标仓库，然后上传清单。身份验证使用 **~/.docker/config.json** 中配置的同一套 Docker 凭据。

# CAVEATS

要求镜像仓库可达且用户具有推送权限。多平台镜像请使用 **--index**。大型 tar 包会从磁盘流式读取，因此需要足够的带宽。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-pull](/man/crane-pull)(1), [docker](/man/docker)(1), [skopeo](/man/skopeo)(1)
