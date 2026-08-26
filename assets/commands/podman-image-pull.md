# TAGLINE

从 registry 下载容器镜像

# TLDR

**从 Docker Hub 拉取镜像**

```podman image pull [nginx]```

**拉取镜像的特定标签**

```podman image pull [nginx]:[1.25]```

**从特定 registry 拉取**

```podman image pull [quay.io/podman/hello]```

**拉取镜像的所有标签**

```podman image pull --all-tags [alpine]```

**不校验 TLS 拉取**（不安全）

```podman image pull --tls-verify=false [registry.local:5000/myimage]```

**带身份验证拉取**

```podman image pull --creds [user]:[password] [registry.example.com/image]```

**拉取并指定架构**

```podman image pull --arch [arm64] [nginx]```

# SYNOPSIS

**podman image pull** [_options_] _image_

# PARAMETERS

**--all-tags**
> 拉取仓库中所有带标签的镜像

**--arch** _ARCH_
> 覆盖要拉取镜像的架构

**--authfile** _path_
> 身份验证文件的路径

**--creds** _[username[:password]]_
> 用于 registry 身份验证的凭据

**--disable-content-trust**
> 跳过镜像验证（默认：true）

**--os** _OS_
> 覆盖要拉取镜像的操作系统

**--platform** _PLATFORM_
> 指定要拉取的平台（os/arch）

**--quiet**, **-q**
> 抑制输出信息

**--tls-verify**
> 要求 HTTPS 并校验证书（默认：true）

**--variant** _VARIANT_
> 覆盖镜像的变体

# DESCRIPTION

**podman image pull** 从 registry 将容器镜像下载到本地存储。它支持多种 registry，包括 Docker Hub、Quay.io 和私有 registry。镜像存储在本地，可用于创建容器。

默认情况下，Podman 会搜索 registries.conf 中定义的 registry。使用完整限定镜像名（含 registry）可跳过 registry 搜索。该命令支持按标签、摘要拉取，或一次获取所有标签。

# CAVEATS

大镜像可能需要大量时间和带宽下载。从不安全的 registry 拉取需要显式指定 --tls-verify=false 标志。命令行上的身份验证凭据可能在进程列表中可见；为了更好的安全性请使用 --authfile。

# HISTORY

**Podman** 由 **Red Hat** 开发，是一个无守护进程的容器引擎，首次发布于 **2018 年**。其镜像拉取命令与 Docker 功能一致，同时增加了无根容器支持。Podman 已成为 RHEL/Fedora 生态系统中的标准容器工具。

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

[podman](/man/podman)(1), [podman-pull](/man/podman-pull)(1), [podman-images](/man/podman-images)(1), [podman-run](/man/podman-run)(1), [docker-pull](/man/docker-pull)(1)
