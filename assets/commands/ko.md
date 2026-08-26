# TAGLINE

无需 Dockerfile 即可构建并部署 Go 容器镜像

# TLDR

从 Go 导入路径**构建并发布**容器镜像到 _$KO_DOCKER_REPO_

```ko build [./cmd/app]```

改为**构建到本地 Docker 守护进程**而不推送

```ko build --local [./cmd/app]```

**构建多平台镜像**

```ko build --platform=linux/amd64,linux/arm64 [./cmd/app]```

**解析 Kubernetes 清单**，将 _ko://_ 镜像引用替换为构建出的摘要

```ko resolve -f [path/to/manifest.yaml]```

向当前集群**构建、推送并应用**清单

```ko apply -f [path/to/manifest.yaml]```

在集群中将 Go 软件包作为临时 Pod **运行**

```ko run [./cmd/app]```

**登录**容器镜像仓库

```ko login [registry.example.com] -u [username] -p [password]```

**输出版本号**

```ko version```

# SYNOPSIS

**ko**  _command_  [_flags_]  [_import-path_]

# COMMANDS

**ko build** [_import-path_ ...]
> 为一个或多个 Go _main_ 软件包构建 OCI 镜像并推送到 **$KO_DOCKER_REPO**。别名：**publish**。

**ko resolve** **-f** _file_
> 读取 Kubernetes YAML，构建每个 **ko://** 镜像引用并推送，然后输出清单，其中每个引用都被改写为其镜像摘要。

**ko apply** **-f** _file_
> 与 **resolve** 类似，然后将改写后的清单管道传给 **kubectl apply**。

**ko create** **-f** _file_
> 与 **resolve** 类似，然后管道传给 **kubectl create**。

**ko delete** **-f** _file_
> 从集群中删除清单定义的资源。

**ko run** _import-path_
> 构建二进制文件、推送镜像，并在集群中将其作为 Pod 运行。

**ko login** _registry_
> 向容器镜像仓库进行身份验证；凭据存储在标准 Docker 配置文件中。

**ko deps** _import-path_
> 输出将被打包进镜像的 Go 模块依赖树。

**ko version**
> 输出客户端版本。

# PARAMETERS

**-B**, **--base-import-paths**
> 仅以最后一级路径组件（如 _app_）为镜像打标签。

**-P**, **--preserve-import-paths**
> 以完整导入路径为镜像打标签。

**--bare**
> 原样使用 _$KO_DOCKER_REPO_ 作为镜像名，不加后缀。

**--platform** _list_
> 逗号分隔的平台列表（如 _linux/amd64,linux/arm64,linux/arm/v7_）。使用 _all_ 表示基础镜像支持的每个平台。

**-t**, **--tags** _list_
> 应用于已发布镜像的逗号分隔标签列表（默认：_latest_）。

**-L**, **--local**
> 将构建好的镜像加载到本地 Docker 守护进程，而不是推送。

**--image-refs** _file_
> 将已发布的镜像引用写入 _file_，每行一个。

**--sbom** _format_
> 要嵌入的 SBOM 格式：_spdx_（默认）、_cyclonedx_、_go.version-m_ 或 _none_。

**--push** _bool_
> 为 _false_ 时只构建不推送。与 **--tarball** 搭配很有用。

**--tarball** _file_
> 将镜像写入可由 **docker load** 加载的 tar 包。

**--kubeconfig** _file_
> **apply**、**create**、**run**、**delete** 所使用的 kubeconfig 文件路径。

**--selector** _label=value_
> 只应用于匹配标签选择器的资源。

# CONFIGURATION

**ko** 会读取仓库根目录下每个项目各自的 **.ko.yaml**。常见键：

**defaultBaseImage**: _registry/image:tag_
> 用作基础层的 distroless 镜像（默认：_cgr.dev/chainguard/static_）。

**baseImageOverrides**: _map_
> 按导入路径覆盖的基础镜像。

**builds**: _list_
> 按导入路径配置的构建设置（env、flags、ldflags、main、dir）。

**defaultPlatforms**: _list_
> **--platform** 的默认值。

**ko** 还会读取以下环境变量：

**KO_DOCKER_REPO**
> 目标镜像仓库。设为 _ko.local_ 表示写入本地 Docker 守护进程，设为 _kind.local_ 表示加载到 Kind 集群。

**KO_DEFAULTBASEIMAGE**
> 覆盖 **.ko.yaml** 中的 _defaultBaseImage_。

**KOCACHE**
> 用于缓存构建层的目录；可加速增量构建。

**KO_CONFIG_PATH**
> 当 **.ko.yaml** 不在仓库根目录时指定其路径。

# DESCRIPTION

**ko** 是一个专用于 Go 的容器镜像构建器。它用本地 **go** 工具链编译 Go _main_ 软件包，把得到的静态二进制文件叠加到一个精简的 distroless 基础镜像上，生成 OCI 镜像——全程不需要启动 **docker**，也不执行 Dockerfile。由于构建本质上就是 **go build**，交叉编译、可复现构建和 Go 模块缓存都与容器外的工作方式完全一致。

典型工作流是在 Kubernetes 清单中存放一段 YAML，例如 _image: ko://github.com/me/app/cmd/server_。**ko resolve** 会读取该清单，对每个此类引用执行 **ko build**，把生成的镜像推送到 **$KO_DOCKER_REPO**，并输出一份新清单，其中每个 **ko://** 引用都已被改写为不可变摘要。**ko apply** 做同样的事并把输出管道传给 **kubectl apply**，一条命令即可完成 GitOps 风格的部署。

镜像默认包含 SBOM（SPDX），并且可以在不同机器之间复现，因为唯一的输入就是 Go 二进制文件、基础镜像摘要和入口点。多平台镜像会并行构建并组装成 OCI 镜像索引。

# CAVEATS

**ko** 只能交付 Go 二进制文件；不支持 cgo、系统软件包以及任意 RUN 步骤。需要 glibc、系统工具或自定义基础层的项目必须通过 _defaultBaseImage_ 改用其他 distroless 或 **cgr.dev/chainguard/\*** 基础镜像，或者换用其他构建器。

**--local** 选项要求本地有正在运行的 Docker 守护进程；没有它时，**ko** 直接与镜像仓库通信，完全不接触 Docker。

# HISTORY

**ko** 由 **Jason Hall**、**Matt Moore** 等人于 **2018 年**在 **Google** 的 **Knative** 团队中创建，目的是发布他们的 Go 服务而无需编写 Dockerfile。它于 **2021 年**捐赠给 **ko-build** GitHub 组织，并于 **2022 年**被接纳进入 **CNCF Sandbox**。

# INSTALL

```pacman: sudo pacman -S ko```

```brew: brew install ko```

```nix: nix profile install nixpkgs#ko```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [buildah](/man/buildah)(1), [crane](/man/crane)(1), [kubectl](/man/kubectl)(1), [skaffold](/man/skaffold)(1)
