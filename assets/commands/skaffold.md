# TAGLINE

自动化 Kubernetes 开发工作流

# TLDR

**初始化 skaffold**

```skaffold init```

**开发模式**

```skaffold dev```

**构建镜像**

```skaffold build```

**部署到集群**

```skaffold deploy```

**运行一次**

```skaffold run```

**删除部署**

```skaffold delete```

**调试模式**

```skaffold debug```

**渲染清单**

```skaffold render```

# SYNOPSIS

**skaffold** _command_ [_-f config_] [_options_]

# PARAMETERS

**init**
> 创建配置。

**dev**
> 持续开发。

**build**
> 构建镜像。

**deploy**
> 部署到集群。

**run**
> 构建并部署一次。

**delete**
> 移除部署。

**debug**
> 调试模式。

**-f**, **--filename** _FILE_
> 配置文件。

**-p**, **--profile** _NAME_
> 使用指定 profile。

**-n**, **--namespace** _NS_
> Kubernetes 命名空间。

**--default-repo** _REPO_
> 默认镜像仓库（覆盖全局配置）。

**--kube-context** _CTX_
> 部署到指定的 Kubernetes 上下文。

**--tail**
> 流式输出已部署对象的日志（dev 模式下默认为 true）。

**--port-forward**
> 将 Pod 内暴露的容器端口进行端口转发。

**--trigger** _MODE_
> 变更检测触发方式：polling、notify 或 manual（默认：notify）。

# COMMANDS

**verify**
> 对部署运行验证测试。

**test**
> 对构建好的应用镜像运行测试。

**apply**
> 将渲染后的清单应用到集群。

**diagnose**
> 对 Skaffold 配置运行诊断。

**fix**
> 将旧配置升级到更新的 schema 版本。

# DESCRIPTION

**Skaffold** 通过自动处理容器化应用的构建、推送和部署循环来简化 Kubernetes 开发工作流。**dev** 命令会监视源文件的变化，每次保存时自动重新构建镜像并重新部署到集群，提供快速的内层开发迭代。

该工具集成了多种构建系统，包括 Docker、Jib 和 Cloud Native Buildpacks，并支持通过 kubectl、Helm 和 kustomize 进行部署。Profile 允许针对不同环境（如开发、预发布、生产）自定义流水线，每个环境可以使用不同的镜像仓库、构建配置和部署目标。

端口转发会自动将已部署的服务暴露在 localhost 上，**debug** 命令可为受支持的语言配置远程调试。

# CAVEATS

需要 Kubernetes 集群。需要 Docker 或其他构建器。配置有一定学习成本。

# HISTORY

**Skaffold** 由 **Google** 为 Kubernetes 开发而创建。它简化了容器化应用的内层开发循环。

# INSTALL

```pacman: sudo pacman -S skaffold```

```zypper: sudo zypper install skaffold```

```brew: brew install skaffold```

```nix: nix profile install nixpkgs#skaffold```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [docker](/man/docker)(1), [helm](/man/helm)(1), [devspace](/man/devspace)(1)
