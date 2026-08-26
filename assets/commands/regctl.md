# TAGLINE

管理容器镜像仓库中的镜像和标签

# TLDR

**列出镜像的标签**

```regctl tag ls [registry/image]```

**不拉取直接检查镜像**

```regctl image inspect [registry/image:tag]```

**在镜像仓库之间复制镜像**

```regctl image copy [source/image:tag] [dest/image:tag]```

**获取镜像摘要**

```regctl image digest [registry/image:tag]```

**从仓库删除标签**

```regctl tag rm [registry/image:tag]```

**将镜像导出为 OCI 布局**

```regctl image export [registry/image:tag] [output.tar]```

**列出**镜像仓库中的**仓库**

```regctl repo ls [registry]```

**检查 Docker Hub 速率限制**

```regctl registry ratelimit docker.io```

# SYNOPSIS

**regctl** _command_ [_subcommand_] [_options_] [_arguments_]

# PARAMETERS

**image inspect** _ref_
> 显示镜像配置和元数据

**image copy** _src_ _dest_
> 在镜像仓库之间复制镜像（高效复用层）

**image digest** _ref_
> 获取镜像摘要

**image export** _ref_ _file_
> 将镜像导出为 tar 文件（OCI 或 Docker 格式）

**image import** _ref_ _file_
> 从 tar 文件导入镜像

**tag ls** _repository_
> 列出仓库中的标签

**tag rm** _ref_
> 从镜像仓库删除标签

**repo ls** _registry_
> 列出镜像仓库中的仓库

**manifest get** _ref_
> 获取原始 manifest 内容

**manifest put** _ref_
> 将 manifest 上传到镜像仓库

**blob get** _ref_
> 下载 blob 内容

**registry login** _registry_
> 向镜像仓库进行身份验证

**registry ratelimit** _registry_
> 检查镜像仓库的速率限制状态

**--platform** _os/arch_
> 按平台筛选（如 linux/amd64、linux/arm64）

**--format** _template_
> 输出格式（Go 模板）

**-v**, **--verbosity** _level_
> 设置日志详细程度

# DESCRIPTION

**regctl** 是一款与符合 OCI 规范的容器镜像仓库交互的 CLI 工具，无需容器运行时或特权访问。它直接调用镜像仓库 API，提供高效的镜像操作。

该工具擅长在镜像仓库之间复制镜像，只传输目标位置不存在的层。这使其非常适合镜像同步、跨环境提升镜像或在物理隔离系统之间同步。

Regctl 支持多平台镜像和 OCI 工件，并可将 OCI Layout 目录作为本地镜像仓库的等价物使用。它会自动从 Docker CLI 配置导入凭据。

常见工作流包括检查远程镜像、在镜像仓库之间复制、管理标签、检查速率限制以及导出/导入镜像以便离线传输。

# CONFIGURATION

**~/.regctl/config.json**
> 主配置文件，存储镜像仓库凭据、默认设置和特定于镜像仓库的选项。

**~/.docker/config.json**
> Docker CLI 凭据存储，regctl 会自动导入用于镜像仓库身份验证。

# CAVEATS

删除操作要求镜像仓库支持删除 API，某些仓库（如免费账户的 Docker Hub）可能加以限制。

默认情况下，认证信息继承自 Docker CLI 配置。如需单独管理凭据，请使用 **regctl registry login**。

当操作无法处理 manifest 列表时（如某些导出场景），多平台镜像需要用 **--platform** 选择特定架构。

Docker Hub 和其他镜像仓库有速率限制。批量操作前请使用 **regctl registry ratelimit** 检查当前状态。

# INSTALL

```nix: nix profile install nixpkgs#regctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [skopeo](/man/skopeo)(1), [crane](/man/crane)(1), [podman](/man/podman)(1)
