# TAGLINE

将容器文件系统导出为 tar 归档

# TLDR

**导出容器文件系统**

```podman export [container] -o [container.tar]```

**导出到 stdout**

```podman export [container] > [container.tar]```

**导出并压缩**

```podman export [container] | gzip > [container.tar.gz]```

# SYNOPSIS

**podman export** [_options_] _container_

# PARAMETERS

**-o**, **--output** _file_
> 写入文件而不是 stdout。

**-h**, **--help**
> 打印用法说明。

# DESCRIPTION

**podman export** 将容器的文件系统导出为 tar 归档，默认写入 stdout。与 podman save 不同，它将容器文件系统导出为扁平的 tar（不包含镜像层历史或元数据）。

结果可用 podman import 导入以创建新镜像。

# EXAMPLES

```bash
# Export to file
podman export mycontainer -o backup.tar

# Export running container
podman export $(podman ps -lq) > latest.tar

# Compress while exporting
podman export webserver | gzip > webserver.tar.gz

# Export and import as new image
podman export mycontainer | podman import - myimage:latest
```

# EXPORT VS SAVE

```
podman export - Container filesystem (flat)
podman save  - Image layers (preserves history)
```

# CAVEATS

会丢失镜像元数据和历史记录。只导出文件系统。要保留完整镜像请使用 podman save。

# HISTORY

podman export 是 **Podman** 的一部分，在无守护进程架构下提供与 Docker 兼容的容器导出功能。

# INSTALL

```apt: sudo apt install podman```

```dnf: sudo dnf install podman```

```pacman: sudo pacman -S podman```

```apk: sudo apk add podman```

```zypper: sudo zypper install podman```

```brew: brew install podman```

```nix: nix profile install nixpkgs#podman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman-import](/man/podman-import)(1), [podman-save](/man/podman-save)(1), [podman-ps](/man/podman-ps)(1)
