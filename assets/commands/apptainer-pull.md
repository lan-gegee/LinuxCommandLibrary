# TAGLINE

从远程注册表下载容器镜像。

# TLDR

从 **Docker Hub** 拉取容器

```apptainer pull [path/to/image.sif] docker://[image]:[tag]```

从 **Container Library** 拉取容器

```apptainer pull [path/to/image.sif] library://[user/collection/container]:[tag]```

从 **OCI 注册表**拉取容器

```apptainer pull [path/to/image.sif] oras://[registry/namespace/image]:[tag]```

拉取**特定架构**的容器

```apptainer pull --arch [amd64|arm64|ppc64le] [path/to/image.sif] library://[image]:[tag]```

**强制覆盖**已有的镜像文件

```apptainer pull -F [path/to/image.sif] docker://[image]:[tag]```

以**可写沙箱**目录的形式拉取容器

```apptainer pull --sandbox [path/to/directory] docker://[image]:[tag]```

拉取容器时**不使用缓存**

```apptainer pull --disable-cache [path/to/image.sif] docker://[image]:[tag]```

# SYNOPSIS

**apptainer pull** [_options_] [_output_] _URI_

# DESCRIPTION

**apptainer pull** 从远程注册表下载容器镜像并转换为 SIF（Singularity Image Format）。支持的来源包括 Docker Hub（**docker://**）、Sylabs Container Library（**library://**）、OCI 注册表（**oras://**）、Shub（**shub://**）以及 HTTP/HTTPS URL。

下载的镜像会缓存到本地，以加快后续操作。生成的 SIF 文件是可移植的，可以在任何安装了 Apptainer 的系统上运行。

# PARAMETERS

**--arch** _architecture_
> 拉取特定 CPU 架构的镜像。

**--arch-variant** _variant_
> 拉取特定架构变体的镜像（例如 armv6 用 6）。

**-F**, **--force**
> 覆盖已存在的本地镜像文件。

**--sandbox**
> 创建可写目录而不是 SIF 文件。

**--disable-cache**
> 不使用也不更新镜像缓存。

**--no-https**
> 下载时使用 HTTP 而不是 HTTPS。

**--dir** _path_
> 将镜像下载到指定目录。

# CONFIGURATION

**/etc/apptainer/apptainer.conf**
> 主配置文件，控制缓存目录、注册表默认值和下载行为。

# CAVEATS

大型镜像的下载可能耗费大量时间和带宽。Docker 镜像需要即时转换，这会带来额外开销。由于运行时预期的差异，某些 Docker 镜像可能无法完美转换。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-push](/man/apptainer-push)(1), [apptainer-build](/man/apptainer-build)(1)
