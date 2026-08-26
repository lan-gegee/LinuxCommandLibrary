# TAGLINE

管理 Kyma Kubernetes 模块和应用的 CLI 工具

# TLDR

**列出已安装的模块**

```kyma module list```

**查看目录中可用的模块**

```kyma module catalog```

**向集群添加模块**

```kyma module add [module_name]```

**从集群删除模块**

```kyma module delete [module_name]```

**将应用推送到集群**

```kyma app push --name [my-app] --image [image:tag] --container-port [8080]```

**推送并暴露应用**

```kyma app push --name [my-app] --image [image:tag] --expose --container-port [80]```

# SYNOPSIS

**kyma** _command_ [_options_]

# SUBCOMMANDS

**module list**
> 显示已安装的 Kyma 模块。

**module catalog**
> 查看可供安装的模块。

**module add** _name_
> 向集群添加模块。

**module delete** _name_
> 从集群移除模块。

**module manage** _name_
> 将模块设为受管状态。

**module unmanage** _name_
> 将模块设为非受管状态。

**app push**
> 构建应用并将其部署到集群。

**completion** _shell_
> 生成 Shell 补全脚本（bash、zsh、fish、powershell）。

**version**
> 显示 CLI 版本信息。

# DESCRIPTION

**kyma** 是用于管理 Kyma 的命令行界面。Kyma 是一套面向企业级云原生应用的、基于 Kubernetes 且带有一套固定主张的模块化构建组件。该 CLI 简化了 Kubernetes 集群上 Kyma 资源的模块管理、部署和配置工作。

该 CLI 提供发现、安装和移除 Kyma 模块的命令，支持通过 **app push** 部署应用，并且可以直接在命令行上操作 Kyma 的自定义资源。

# CAVEATS

需要能够访问已安装 Kyma 的 Kubernetes 集群。模块的可用性取决于集群配置和 Kyma 版本。v2 CLI 命令已弃用，请改用 v3 命令。

# HISTORY

**kyma** CLI 由 **Kyma 项目**（SAP 生态的一部分）开发，使用 **Go** 编写。v3 版本将工具的定位重新聚焦于以 Kyma 作为 Kubernetes 运行时的应用开发者。

# INSTALL

```aur: yay -S kyma```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [helm](/man/helm)(1)
