# TAGLINE

Istio 的 CLI，Istio 是提供流量管理的服务网格

# TLDR

使用默认 profile **安装 Istio**

```istioctl install```

**使用指定 profile 安装**

```istioctl install --set profile=[demo]```

**检查代理同步状态**

```istioctl proxy-status```

**分析配置**中的问题

```istioctl analyze```

**查看某个 pod 的 Envoy 代理配置**

```istioctl proxy-config cluster [pod-name].[namespace]```

**打开 Kiali 控制台**

```istioctl dashboard kiali```

**生成安装清单**

```istioctl manifest generate```

**卸载 Istio**

```istioctl uninstall --purge```

# SYNOPSIS

**istioctl** _command_ [_options_]

# COMMANDS

**install**
> 安装 Istio 控制平面。

**uninstall**
> 从集群中移除 Istio。

**manifest** generate|diff|install
> 生成、比较或应用清单。

**profile** list|dump|diff
> 管理安装 profile。

**analyze**
> 分析配置中潜在的问题。

**proxy-status**
> 显示 Envoy 代理的同步状态。

**proxy-config** _type_ _pod_
> 获取 Envoy 配置（cluster、listener、route、endpoint）。

**dashboard** _component_
> 打开 Kiali、Grafana、Jaeger 等组件的 Web UI。

**kube-inject**
> 向 pod spec 注入 Envoy sidecar。

**validate**
> 验证 Istio 策略和规则。

**version**
> 显示客户端和控制平面版本。

**upgrade**
> 升级 Istio 控制平面。

# PARAMETERS

**--set** _key=value_
> 覆盖安装设置。

**--filename**, **-f** _file_
> IstioOperator 自定义资源文件的路径。

**--revision** _name_
> 定位到特定的 Istio revision。

**--context** _name_
> 要使用的 Kubernetes context。

**--kubeconfig** _path_
> kubeconfig 文件的路径。

**--namespace**, **-n** _namespace_
> 目标命名空间。

**--istioNamespace** _namespace_
> Istio 系统命名空间。默认：istio-system。

**--skip-confirmation**, **-y**
> 跳过确认提示。

**--dry-run**
> 只预览而不应用更改。

# PROFILES

**default**
> 包含 istiod 和 ingress gateway 的生产部署。

**demo**
> 面向评估的全功能配置，追踪/日志级别较高。

**minimal**
> 仅包含 istiod 控制平面。

**remote**
> 用于多集群远程配置。

**empty**
> 作为自定义配置的基础。

# DESCRIPTION

**istioctl** 是 Istio 的 CLI。Istio 是一款为微服务提供流量管理、安全性和可观测性的服务网格。它负责管理 Istio 的安装、配置和诊断。

**install** 命令使用打包了配置预设的 profile 来部署 Istio 控制平面。可以使用 **--set** 标志自定义单个设置，或通过 **-f** 提供 IstioOperator YAML 文件。

**analyze** 等诊断命令可检测配置问题，**proxy-status** 显示 Envoy 的同步状态，**proxy-config** 则检查单个代理的配置以便调试。

**dashboard** 命令会打开可观测性工具的 Web 界面，包括 Kiali（服务网格可视化）、Grafana（指标）、Jaeger（追踪）和 Prometheus。

要启用自动 sidecar 注入，可对 pod 清单使用 **kube-inject**，或通过标签启用命名空间级别的注入。

# CAVEATS

istioctl 与控制平面之间的版本兼容性很重要；请使用匹配的版本。部分命令需要集群管理员权限。多集群设置需要额外的配置。卸载时使用 **--purge** 可移除所有资源。

# HISTORY

Istio 于 **2017 年 5 月**发布，是 Google、IBM 和 Lyft 合作的成果。它迅速成为 Kubernetes 上领先的服务网格。该项目于 **2022 年**作为孵化项目加入 CNCF，并于 **2023 年**毕业。istioctl 也在不断演进，简化了安装流程并提供了全面的诊断功能。

# INSTALL

```zypper: sudo zypper install istioctl```

```brew: brew install istioctl```

```nix: nix profile install nixpkgs#istioctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [linkerd](/man/linkerd)(1), [helm](/man/helm)(1)
