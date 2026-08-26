# TAGLINE

Linkerd 的 CLI，Linkerd 是 Kubernetes 的轻量级服务网格

# TLDR

**检查 CLI 和控制平面版本**

```linkerd version```

**校验集群配置**

```linkerd check```

**安装 Linkerd** 控制平面

```linkerd install | kubectl apply -f -```

向 deployment **注入 sidecar 代理**

```linkerd inject [deployment.yaml] | kubectl apply -f -```

**查看实时流量**统计

```linkerd stat deploy```

**打开 Linkerd 控制面板**

```linkerd viz dashboard```

**按路由查看流量排行**

```linkerd viz top deploy/[name]```

**检查某命名空间的代理状态**

```linkerd diagnostics proxy-metrics -n [namespace] [pod-name]```

**生成 Linkerd 升级清单**

```linkerd upgrade | kubectl apply -f -```

# SYNOPSIS

**linkerd** _command_ [_options_]

# COMMANDS

**install**
> 生成 Linkerd 控制平面的安装清单。

**check**
> 校验安装和集群配置。

**inject**
> 向 Kubernetes 资源添加 Linkerd 代理 sidecar。

**uninject**
> 从资源中移除 Linkerd 代理。

**upgrade**
> 为控制平面生成升级清单。

**uninstall**
> 生成移除 Linkerd 的清单。

**version**
> 显示 CLI 和控制平面版本。

**identity**
> 查看工作负载身份证书。

**diagnostics**
> 故障排查和调试命令。

**completion**
> 生成 shell 补全脚本。

# VIZ EXTENSION COMMANDS

**viz install**
> 安装可观测性扩展。

**viz dashboard**
> 打开 Web 控制面板。

**viz stat**
> 显示流量统计。

**viz top**
> 按路由显示实时流量。

**viz tap**
> 实时流式输出请求。

**viz edges**
> 显示资源之间的连接。

**viz routes**
> 显示按路由划分的指标。

# PARAMETERS

**--context** _name_
> 要使用的 Kubernetes context。

**--kubeconfig** _path_
> kubeconfig 文件的路径。

**--api-addr** _address_
> 覆盖 API 服务器地址。

**--namespace**, **-n** _namespace_
> 目标命名空间。

**--linkerd-namespace** _namespace_
> Linkerd 控制平面所在的命名空间。

**--set** _key=value_
> 覆盖配置值。

**--values** _file_
> 用于配置的 values 文件路径。

**--verbose**
> 启用详细输出。

**--as** _user_
> 模拟某个 Kubernetes 用户。

**-o**, **--output** _format_
> 输出格式：table、json、yaml。

# DESCRIPTION

**linkerd** 是 Linkerd 的 CLI，Linkerd 是 Kubernetes 的轻量级服务网格。它负责管理安装、代理注入，并为微服务流量提供可观测性工具。

**install** 命令生成控制平面的 Kubernetes 清单。将输出通过管道传给 **kubectl apply** 即可部署。使用 **check** 校验前提条件和安装健康状况。

通过 **inject** 注入 sidecar 代理会将 Linkerd 代理加入 pod，从而启用 mTLS、流量指标和负载均衡。注入可以通过命名空间注解实现自动化。

**viz** 扩展提供可观测性功能。**dashboard** 会打开一个 Web UI，展示服务拓扑和指标。**stat**、**top** 和 **tap** 等命令则提供基于 CLI 的流量分析。

Linkerd 默认使用双向 TLS，无需修改应用即可自动加密网格内服务之间的流量。

# CAVEATS

部分命令需要单独安装 viz 扩展。CLI 版本应与控制平面版本一致。代理注入需要重启 pod 才能生效。某些功能需要集群管理员权限。

# HISTORY

Linkerd 最初由 **Buoyant** 于 **2016 年**创建，是最早的服务网格之一。第 2 版于 **2018 年**发布，是用 Rust 和 Go 进行的完全重写，专注于简单性和低资源开销。Linkerd 加入了 CNCF 并于 **2021 年**毕业。相比同类方案，它以轻量占用和运维简单而持续受到欢迎。

# INSTALL

```brew: brew install linkerd```

```nix: nix profile install nixpkgs#linkerd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [istioctl](/man/istioctl)(1), [helm](/man/helm)(1)
