# TAGLINE

将容器镜像保存为 tar 归档

# TLDR

**将镜像保存为 tar**

```podman save -o [image.tar] [image:tag]```

**保存到 stdout**

```podman save [image:tag] > [image.tar]```

**压缩保存**

```podman save [image:tag] | gzip > [image.tar.gz]```

**保存多个镜像**

```podman save -o [images.tar] [image1:tag] [image2:tag]```

# SYNOPSIS

**podman save** [_options_] _image_...

# PARAMETERS

**-o**, **--output** _file_
> 输出文件路径。

**--compress**
> 压缩层。

**--format** _format_
> 输出格式（oci-archive、docker-archive）。

**-q**, **--quiet**
> 抑制输出。

# DESCRIPTION

**podman save** 将一个或多个镜像保存到 tar 归档中。归档保留所有镜像层和元数据，适合在系统之间传输。

使用 podman load 恢复已保存的镜像。

# EXAMPLES

```bash
# Save to file
podman save -o nginx.tar nginx:latest

# Save with compression
podman save myimage:v1 | gzip > myimage.tar.gz

# Save in OCI format
podman save --format oci-archive -o image.tar myimage

# Save multiple images
podman save -o all-images.tar image1:v1 image2:v2

# Transfer to another host
podman save myimage | ssh user@host podman load
```

# FORMATS

```
docker-archive - Docker compatible (default)
oci-archive    - OCI format
oci-dir        - OCI directory layout
```

# CAVEATS

归档可能很大。仅导出文件系统请使用 podman export。

# HISTORY

podman save 是 **Red Hat** 的 **Podman** 的一部分，提供与 Docker 兼容的镜像归档功能。

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

[podman-load](/man/podman-load)(1), [podman-export](/man/podman-export)(1)
