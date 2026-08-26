# TAGLINE

面向 GCR 增强的容器镜像管理工具

# TLDR

**列出 GCR 路径中的仓库和标签**

```gcrane ls [gcr.io/project-id]```

**列出特定镜像的标签**

```gcrane ls [gcr.io/project-id/image]```

**将镜像复制**到另一个位置

```gcrane cp [gcr.io/project-id/image:tag] [gcr.io/other-project/image:tag]```

**递归复制镜像**从一个路径到另一个路径

```gcrane cp -r [gcr.io/project-id/repo] [gcr.io/other-project/repo]```

**查找可垃圾回收的无标签镜像**

```gcrane gc [gcr.io/project-id/repo]```

**删除无标签镜像**（垃圾回收）

```gcrane gc [gcr.io/project-id/repo] | xargs -n1 gcrane delete```

**按摘要删除特定镜像**

```gcrane delete [gcr.io/project-id/image@sha256:digest]```

# SYNOPSIS

**gcrane** _COMMAND_ [_FLAGS_]

# COMMANDS

**ls** _REPOSITORY_
> 列出标签、清单和子仓库。比 crane ls 更详细。

**cp** [**-r**] _SRC_ _DST_
> 复制镜像。使用 -r 可递归复制整个仓库。

**gc** _REPOSITORY_
> 列出可垃圾回收的镜像（无标签镜像）。

**delete** _IMAGE_
> 按引用（标签或摘要）删除镜像。

**digest** _IMAGE_
> 获取镜像的摘要。

**manifest** _IMAGE_
> 获取镜像的清单。

**config** _IMAGE_
> 获取镜像的配置。

# PARAMETERS

**-r**
> 递归复制镜像（用于 cp 命令）。

**--platform** _PLATFORM_
> 为多架构镜像指定平台。

**-v**, **--verbose**
> 启用详细输出。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**gcrane** 是 **crane** 针对 Google Container Registry 的增强变体，为 GCR 和 Artifact Registry 提供了增强功能。它实现了 crane 命令的超集，并增加了 GCR 特有的操作。

相比 crane 的关键增强包括：通过 **-r** 标志进行递归复制（适用于备份、异地复制或批量重命名）、更丰富的 ls 输出以详细探索仓库，以及通过 **gc** 命令识别无标签镜像以便清理。

gcrane 依赖 GCR 的实现细节，这些细节可能与通用的 OCI 镜像仓库规范不一致。

# CAVEATS

依赖 GCR 特有的实现细节，镜像仓库变更时可能出现问题。需要相应的 GCP 身份验证（gcloud auth、服务账号等）。gc 命令只识别删除候选对象；实际删除需要通过管道传给 gcrane delete。

# HISTORY

gcrane 是 Google 开发的 **go-containerregistry** 项目的一部分。它旨在为 Google Container Registry 和 Artifact Registry 用户提供增强的工具，在通用 crane 工具的基础上扩展了 Google 特有的容器镜像大规模管理功能。

# INSTALL

```zypper: sudo zypper install gcrane```

```nix: nix profile install nixpkgs#gcrane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [docker](/man/docker)(1), [skopeo](/man/skopeo)(1), [gcloud](/man/gcloud)(1)
