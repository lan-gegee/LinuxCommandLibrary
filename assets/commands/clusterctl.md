# TAGLINE

Kubernetes Cluster API 管理 CLI

# TLDR

**初始化管理集群**

```clusterctl init --infrastructure [aws]```

**以指定版本初始化**

```clusterctl init --infrastructure [aws:v2.0.0]```

**生成集群模板**

```clusterctl generate cluster [mycluster] --kubernetes-version [v1.28.0]```

**获取工作负载集群的 kubeconfig**

```clusterctl get kubeconfig [mycluster]```

**升级提供商**

```clusterctl upgrade apply --contract [v1beta1]```

**在集群之间移动资源**

```clusterctl move --to-kubeconfig [target.kubeconfig]```

**删除提供商**

```clusterctl delete --infrastructure [aws]```

# SYNOPSIS

**clusterctl** _command_ [_options_]

# DESCRIPTION

**clusterctl** 是用于管理 Kubernetes Cluster API（CAPI）管理集群的命令行工具。它负责集群基础设施提供商的完整生命周期，从初始安装到升级和删除。

该工具可以通过安装基础设施提供商（AWS、Azure、vSphere 等）、引导提供商和控制平面提供商，将一个 Kubernetes 集群初始化为 CAPI 管理集群。初始化完成后，它会生成用于创建工作负载集群的集群模板，并获取它们的 kubeconfig。

clusterctl 还支持在管理集群之间移动 Cluster API 资源，这对升级场景和灾难恢复至关重要。upgrade 命令可帮助保持提供商与最新版本及 API 契约版本同步。

# COMMANDS

**init**
> 安装 Cluster API 组件

**generate cluster**
> 生成集群模板

**generate yaml**
> 处理 YAML 模板

**get kubeconfig**
> 获取工作负载集群的 kubeconfig

**upgrade plan**
> 显示升级建议

**upgrade apply**
> 应用提供商升级

**move**
> 在集群之间移动资源

**delete**
> 删除提供商

**describe cluster**
> 描述集群资源

**config**
> 显示 clusterctl 的配置详情。

**version**
> 打印 clusterctl 版本信息。

**completion**
> 输出 Shell 自动补全代码（bash、zsh、fish、powershell）。

**alpha rollout**
> 管理 Cluster API 资源的发布。

# INIT OPTIONS

**--infrastructure** _provider_
> 基础设施提供商（aws、azure、vsphere 等）

**--bootstrap** _provider_
> 引导提供商

**--control-plane** _provider_
> 控制平面提供商

**--target-namespace** _ns_
> 提供商的目标命名空间

**--core** _provider_
> 核心提供商版本

# CONFIGURATION

**~/.cluster-api/clusterctl.yaml**
> 用于提供商、变量和镜像覆盖的主配置文件。

# CAVEATS

设置 GITHUB_TOKEN 以避免 API 速率限制。需要为目标集群配置好 kubectl。使用 go proxy 进行版本检测。

# INSTALL

```zypper: sudo zypper install clusterctl```

```brew: brew install clusterctl```

```nix: nix profile install nixpkgs#clusterctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kind](/man/kind)(1), [kubeadm](/man/kubeadm)(1)
