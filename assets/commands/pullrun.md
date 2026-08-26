# TAGLINE

基于单一镜像和二进制文件的容器与虚拟机 OCI 运行时

# TLDR

将 OCI 镜像**拉取**到本地 DAG 存储中

```pullrun pull [image:tag]```

以容器（Linux）或默认后端**运行**

```pullrun run [image:tag] --cmd [command]```

以 **microVM** 方式**运行**

```pullrun run [image:tag] --backend vm --cmd [command] --attach -t```

**列出**工作负载

```pullrun list```

在运行中的工作负载内**执行**命令

```pullrun exec [id] [command]```

**停止**工作负载

```pullrun stop [id]```

从 Dockerfile **构建**镜像

```pullrun build [Dockerfile] [.] -t [name:tag]```

**列出**本地镜像

```pullrun images```

为 AI 智能体**启动** MCP 服务器

```pullrun mcp```

# SYNOPSIS

**pullrun** _command_ [_options_] [_args_]

# DESCRIPTION

**pullrun** 是一个单二进制文件的 OCI 运行时，可以将同一镜像运行为 Linux 容器（runc）、Firecracker microVM 或 Apple Silicon 虚拟机，无需单独构建 VM 镜像。镜像层存储在内容寻址的 **DAG 存储**（零拷贝 mmap 读取、内容哈希校验）中，而非传统的 overlayfs。可选的守护进程支持 P2P 块同步、后台服务和面向集群的工作流；许多 CLI 操作无需重量级的 dockerd 式中央守护进程即可完成。

Go 编写的 CLI 涵盖镜像生命周期（**pull**、**build**、**push**、**save**/**load**、**images**、**rmi**、**gc**）、工作负载生命周期（**run**、**stop**、**exec**、**list**、**logs**、**stats**、**events**、**inspect**、**commit**、**diff**）、网络、加密的机密（secrets）、配置、仓库 **login**/**logout**、策略门控（如 Cosign、SBOM、seccomp），以及用于智能体集成的 **mcp** 子命令。Compose 支持由配套的 **pullrun-compose** 二进制文件提供。更广泛的项目中还包含 Kubernetes CRI shim 和多节点控制平面组件，供集群场景使用。

默认后端取决于平台：macOS Apple Silicon 上为 Apple Virtualization，Linux 上当 **runc** 和 KVM 可用时为容器和/或 Firecracker。可通过项目安装脚本、Homebrew tap 或上游文档记载的软件包进行安装。

# PARAMETERS

**pull** _image_
> 将 OCI 镜像拉取到本地存储。

**run** _image_ [_options_]
> 启动一个工作负载。常用选项：**--cmd**（可重复使用）、**--backend** **vm**|container 路径、**--attach**、**-t**/**--tty**、**--net**、**--secret**、**--config**、**--volume**。

**list**
> 列出工作负载（pending/running/exited）。

**stop** _id_
> 停止工作负载。

**exec** _id_ [_command_]
> 在工作负载中运行命令；**-t** 用于 TTY 重新附加模式。

**build** _Dockerfile_ _context_ **-t** _tag_
> 原生 Dockerfile 构建，带有内容寻址的层缓存（RUN 无需 Docker 守护进程）。

**push** _digest_ _registry/ref_
> 将存储中的内容推送到镜像仓库。

**images**
> 列出本地 DAG 存储中的镜像。

**rmi** _image_|_digest_
> 删除镜像；级联删除不可达的层，同时保留共享引用。

**gc** [**--apply**] [**--force**]
> 垃圾回收不可达的 DAG 节点（默认仅试运行）。

**save** / **load**
> 导出或导入兼容 OCI 的 tar 包，用于离线（air-gapped）环境。

**network** **create** _name_ [_options_]
> 管理用户自定义网络。

**secret** **create**|**ls**|... 
> AES-256-GCM 加密的机密，可挂载到工作负载中。

**mcp** [**--sse** _addr_]
> MCP 服务器（stdio 或 SSE），向 AI 智能体暴露运行时操作。

**events** / **stats** / **inspect** / **diff** / **commit**
> 可观测性与文件系统变更工具。

**login** / **logout**
> 镜像仓库身份验证。

# CAVEATS

项目尚年轻，API 和打包方式可能仍会变化。VM 后端需要平台支持（Linux 上的 **KVM**/Firecracker，Apple Silicon 上的 Apple Virtualization）。容器模式需要主机上有 **runc**（或等效工具）。设计上无根运行（rootless），但完整的网络和 VM 功能可能仍需要主机能力（capabilities）和正确的设备权限。生产环境的 CRI/compose 布局请以官方文档为准。

# SEE ALSO

[docker](/man/docker)(1), [podman](/man/podman)(1), [nerdctl](/man/nerdctl)(1), [runc](/man/runc)(1), [containerd](/man/containerd)(1)

# RESOURCES

```[Source code](https://github.com/pullrun/pullrun)```

```[Homepage](https://pullrun.dev)```

```[Documentation](https://github.com/pullrun/pullrun/blob/main/docs/PULLRUN_GUIDE.md)```

<!-- verified: 2026-07-15 -->
