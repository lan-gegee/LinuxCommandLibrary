# TAGLINE

无需守护进程构建 OCI 和 Docker 容器镜像

# TLDR

从 Containerfile/Dockerfile **构建**容器

```buildah build -t [myimage] [.]```

**创建**工作容器

```buildah from [fedora]```

在容器中**运行**命令

```buildah run [container-id] -- [dnf install -y httpd]```

向容器中**复制**文件

```buildah copy [container-id] [local/path] [/container/path]```

将容器**提交**为镜像

```buildah commit [container-id] [myimage]```

**列出**本地镜像

```buildah images```

将镜像**推送**到仓库（registry）

```buildah push [myimage] [docker://registry.example.com/myimage:tag]```

# SYNOPSIS

**buildah** _command_ [_options_]

# DESCRIPTION

**buildah** 是一个无需守护进程即可构建 OCI 和 Docker 容器镜像的工具。它提供对镜像层的细粒度控制，既可以从 Dockerfile 构建，也可以通过直接操作容器来构建。

与 Docker 不同，buildah 不需要后台守护进程，因此非常适合 CI/CD 流水线和受限环境。它支持无 root 构建，整个构建过程无需提升权限。作为 Podman 生态的一部分，它与 podman 和 skopeo 共享存储和镜像格式，实现工具间的无缝互操作。

# PARAMETERS

**build**（原 **bud**）
> 使用 Containerfile/Dockerfile 构建镜像

**from** _image_
> 创建工作容器

**run** _container_ _cmd_
> 在容器中运行命令

**commit** _container_ _image_
> 将容器保存为镜像

**push** _image_ _destination_
> 将镜像推送到 registry

**pull** _image_
> 从 registry 拉取镜像

**images**
> 列出镜像

**containers**
> 列出工作容器

**copy** _container_ _src_ _dest_
> 向容器中复制文件

**config** [_options_] _container_
> 设置镜像配置（cmd、entrypoint、env、labels 等）

**rm** _container_
> 移除容器

**rmi** _image_
> 移除镜像

**inspect** _container|image_
> 显示详细信息

**mount** _container_
> 挂载容器文件系统

**umount** _container_
> 卸载容器文件系统

# BUILDING IMAGES

**From Containerfile/Dockerfile:**
```bash
buildah build -t myapp:latest .
```

**Script-based:**
```bash
# Create container
ctr=$(buildah from fedora)

# Install packages
buildah run $ctr dnf install -y nginx

# Copy files
buildah copy $ctr ./app /app

# Set config
buildah config --cmd "/app/start.sh" $ctr

# Commit
buildah commit $ctr myapp:latest
```

# FEATURES

- 无守护进程运行
- 无 root 构建
- 兼容 Dockerfile
- 细粒度的层控制
- OCI 镜像格式
- 多种存储后端
- 对脚本友好

# CONFIGURATION

**/etc/containers/registries.conf**
> 仓库配置，包括镜像源、不安全 registry 和搜索顺序。

**/etc/containers/storage.conf**
> 镜像和容器的存储驱动与存储位置设置。

**/etc/containers/policy.json**
> 镜像签名验证策略。

# CAVEATS

工作流与 Docker 不同（有学习成本）。部分 Docker 功能不受支持。无 root 模式受内核和文件系统限制。存储配置很重要。**bud** 子命令已被弃用，应改用 **build**。

# HISTORY

**buildah** 由 Red Hat 于 **2017 年**前后创建，是其容器工具套件的组件之一，专注于无守护进程的镜像构建。

# INSTALL

```apt: sudo apt install buildah```

```dnf: sudo dnf install buildah```

```pacman: sudo pacman -S buildah```

```apk: sudo apk add buildah```

```zypper: sudo zypper install buildah```

```nix: nix profile install nixpkgs#buildah```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [docker](/man/docker)(1), [skopeo](/man/skopeo)(1)
