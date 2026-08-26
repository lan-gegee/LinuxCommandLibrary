# TAGLINE

KubeVela 应用交付 CLI

# TLDR

**从文件部署应用**

```vela up -f [app.yaml]```

**显示应用状态**

```vela status [appname]```

**列出应用**

```vela ls```

**删除应用**

```vela delete [appname]```

**查看应用的日志**

```vela logs [appname]```

**对应用进行端口转发**

```vela port-forward [appname]```

**在应用容器中执行命令**

```vela exec [appname] -- [command]```

**在 Kubernetes 集群上安装 KubeVela**

```vela install```

# SYNOPSIS

**vela** _command_ [_options_] [_args_]

# PARAMETERS

**up**
> 从文件或 URL 创建或更新应用。

**status**
> 显示应用状态和健康状况。

**ls**
> 列出所有应用。

**delete**
> 移除应用。

**logs**
> 查看应用日志。

**exec**
> 在应用容器中执行命令。

**port-forward**
> 将本地端口转发到应用容器或服务。

**install**
> 在 Kubernetes 集群上安装 KubeVela。

**show**
> 显示组件、trait 或工作流类型的参考文档。

**components**
> 列出可用的组件类型。

**workflow**
> 操作应用交付工作流（suspend、resume、restart、rollback）。

**version**
> 打印版本信息。

**-n**, **--namespace** _NAMESPACE_
> 指定请求的命名空间范围。

**-e**, **--env** _ENV_
> 为应用指定环境名称。

**-y**, **--yes**
> 对所有提示自动回答 yes。

# DESCRIPTION

**vela** 是 KubeVela 的命令行客户端。KubeVela 是基于开放应用模型（OAM）构建的应用交付平台。它管理 Kubernetes 上应用的完整生命周期，涵盖部署、扩缩容、监控和回滚。

应用由组件（component）、运维特征（trait）和策略（policy）定义，这些抽象屏蔽了基础设施的复杂性。平台支持多集群部署，可以从单一的应用定义将应用分发到不同的 Kubernetes 集群和云服务商。

# CAVEATS

需要已安装 KubeVela 的运行中 Kubernetes 集群。建议熟悉 Kubernetes 概念和开放应用模型（OAM）。多集群功能需要额外配置。

# HISTORY

**KubeVela** 由阿里云团队创建，于 2021 年被接受为 **CNCF 沙箱项目**，后晋升为孵化级项目。它实现了开放应用模型（OAM）规范，以简化 Kubernetes 上的应用交付。

# SEE ALSO

[kubectl](/man/kubectl)(1), [helm](/man/helm)(1), [argocd](/man/argocd)(1)
