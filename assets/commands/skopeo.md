# TAGLINE

无需容器运行时的容器镜像操作

# TLDR

**在镜像仓库之间复制镜像**

```skopeo copy docker://[source-image] docker://[dest-image]```

**检查镜像**

```skopeo inspect docker://[image:tag]```

**列出标签**

```skopeo list-tags docker://[registry/image]```

**复制到本地目录**

```skopeo copy docker://[image] dir:[local-dir]```

**删除镜像**

```skopeo delete docker://[image:tag]```

**同步仓库**

```skopeo sync --src docker --dest docker [source] [dest]```

# SYNOPSIS

**skopeo** _command_ [_options_]

# DESCRIPTION

**skopeo** 无需容器运行时即可对容器镜像和镜像仓库执行操作。它可以在不同仓库之间复制、检查、删除和签名镜像。

该工具适用于 CI/CD 流水线、镜像仓库管理和镜像检查，且不必拉取完整镜像。

# PARAMETERS

**copy** _src_ _dest_
> 复制镜像。

**inspect** _image_
> 显示镜像元数据。

**list-tags** _repo_
> 列出可用的标签。

**delete** _image_
> 从仓库中删除镜像。

**sync** _args_
> 同步仓库。

**--src-creds** _user:pass_
> 源仓库凭据。

**--dest-creds** _user:pass_
> 目标仓库凭据。

**--authfile** _file_
> 身份验证文件。

**--override-os** _os_
> 覆盖操作系统。

**--override-arch** _arch_
> 覆盖架构。

# CAVEATS

可能需要镜像仓库身份验证。某些操作需要写权限。大镜像耗时较长。删除操作可能不会立即回收空间。

# HISTORY

**skopeo** 由 **Red Hat** 开发，是容器工具项目的一部分，与 podman 和 buildah 同属该项目。它支持无守护进程的容器镜像操作，契合 podman 的理念。

# INSTALL

```apt: sudo apt install skopeo```

```dnf: sudo dnf install skopeo```

```pacman: sudo pacman -S skopeo```

```apk: sudo apk add skopeo```

```zypper: sudo zypper install skopeo```

```brew: brew install skopeo```

```nix: nix profile install nixpkgs#skopeo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [docker](/man/docker)(1), [crane](/man/crane)(1), [buildah](/man/buildah)(1)
