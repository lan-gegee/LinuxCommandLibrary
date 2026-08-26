# TAGLINE

支持热重载的 Kubernetes 开发者工具

# TLDR

**初始化项目**

```devspace init```

**部署到 Kubernetes**

```devspace deploy```

**启动开发模式**

```devspace dev```

**在容器中打开终端**

```devspace enter```

**查看日志**

```devspace logs```

**在容器中运行命令**

```devspace run [command]```

**清除部署**

```devspace purge```

# SYNOPSIS

**devspace** _command_ [_options_]

# SUBCOMMANDS

**init**
> 初始化 DevSpace 配置。

**deploy**
> 部署应用。

**dev**
> 启动带热重载的开发模式。

**enter**
> 在容器中打开终端。

**logs**
> 查看容器日志。

**run**
> 运行预定义的命令。

**purge**
> 删除已部署的资源。

**ui**
> 在浏览器中打开 DevSpace UI。

# DESCRIPTION

**devspace** 是一款用于构建、部署和开发应用的 Kubernetes 开发者工具。它在开发过程中提供热重载、日志流和终端访问能力。

该工具通过自动化常见任务来简化 Kubernetes 开发：构建容器镜像、部署清单、同步代码变更等。DevSpace 监视本地文件变化并自动同步到运行中的容器，无需重新构建镜像即可快速迭代。

配置定义在 devspace.yaml 中，声明镜像、部署、dev 配置和自定义命令。该工具支持 Helm chart、kubectl 清单和 Kustomize。

# CONFIGURATION

**devspace.yaml**
> 主配置文件，定义镜像、部署、dev 设置和流水线。

# CAVEATS

需要 kubectl 以及可访问的 Kubernetes 集群。热重载性能取决于文件同步机制。大镜像的初始部署可能较慢。

# INSTALL

```brew: brew install devspace```

```nix: nix profile install nixpkgs#devspace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [skaffold](/man/skaffold)(1)
