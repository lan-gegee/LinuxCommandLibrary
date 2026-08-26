# TAGLINE

在镜像仓库之间复制容器镜像

# TLDR

**在仓库之间复制镜像**

```gcrane copy [source_image] [dest_image]```

**递归复制仓库**

```gcrane copy -r [source_repo] [dest_repo]```

**按平台过滤复制**

```gcrane copy --platform linux/amd64 [source] [dest]```

**使用并行任务复制**

```gcrane copy --jobs [4] [source] [dest]```

# SYNOPSIS

**gcrane** **copy** [_options_] _src_ _dst_

# PARAMETERS

**-r**, **--recursive**
> 递归复制仓库（复制所有标签和子仓库）。

**--platform** _platform_
> 要复制的平台（例如 linux/amd64）。使用 `all` 复制所有平台。

**--jobs** _num_
> 并行复制作业的数量。

**--allow-nondistributable-artifacts**
> 允许推送不可分发的（外部）层。

**--insecure**
> 允许在不使用 TLS 的情况下获取镜像引用。

# DESCRIPTION

**gcrane copy** 在镜像仓库之间复制容器镜像，既支持单个镜像也支持整仓操作。它支持多架构镜像，并在传输过程中保留所有镜像元数据。

该命令可以复制单个带标签的镜像，也可以使用 **-r** 标志递归复制所有标签和子仓库。平台过滤可以按特定架构选择性复制。并行作业执行可以加快批量复制操作。gcrane copy 常用于备份、跨区域或跨项目的异地复制，以及将镜像从测试环境晋升到生产仓库。

**gcrane** 在 **crane** 的基础上扩展了 Google Container Registry 和 Artifact Registry 特有的功能，例如递归仓库复制。

# INSTALL

```zypper: sudo zypper install gcrane```

```nix: nix profile install nixpkgs#gcrane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcrane](/man/gcrane)(1), [crane-copy](/man/crane-copy)(1)
